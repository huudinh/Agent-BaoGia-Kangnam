# -*- coding: utf-8 -*-
"""Đối chiếu template/bang-gia.json với bảng giá đang đăng trên web Kangnam.

    python tools/doi_chieu_gia_web.py              # tải web rồi so
    python tools/doi_chieu_gia_web.py --file x.html  # so với bản đã tải về
    python tools/doi_chieu_gia_web.py --ghi        # ghi giá web vào JSON (có hỏi lại)

Nguồn web: https://benhvienthammykangnam.com.vn/bang-gia/

Bốn nhóm kết quả:
    KHỚP            — giá repo = giá web
    LỆCH GIÁ        — cùng dịch vụ, khác số  ← nguy hiểm nhất, báo giá đang sai
    CHƯA CÓ TRONG REPO — web có, repo thiếu
    KHÔNG THẤY TRÊN WEB — repo có, web không còn (hoặc tên đã đổi)

⚠️ Tool KHÔNG tự sửa giá nếu không có --ghi. Giá là thứ đi thẳng vào túi khách,
không để máy đổi sau lưng người.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
WEB = "https://benhvienthammykangnam.com.vn/bang-gia/"

for _l in (sys.stdout, sys.stderr):
    if hasattr(_l, "reconfigure"):
        _l.reconfigure(encoding="utf-8", errors="replace")


def tu(s: str) -> set:
    """Tập từ đã bỏ dấu. GIỮ phần trong ngoặc — nó là thứ phân biệt
    'chỉnh hàm 1 hàm' với 'chỉnh hàm 1 hàm khó, ghép xương'."""
    s = unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    bo = {"va", "hoac", "cua", "cho", "theo", "the", "rieng", "le"}
    return {w for w in s.split() if w and w not in bo}


def giong(a: set, b: set) -> float:
    """Jaccard — khớp theo độ trùng từ thay vì khớp chuỗi tuyệt đối."""
    return len(a & b) / len(a | b) if (a or b) else 0.0


def doc_gia(t: str) -> dict:
    """'12.800.000đ' · '4.400.000 - 5.600.000đ/lần' · 'Từ 600.000đ' · 'Liên hệ'."""
    t = re.sub(r"\s+", " ", t).strip()
    so = [int(x.replace(".", "")) for x in re.findall(r"\d{1,3}(?:\.\d{3})+", t)]
    if not so:
        return {"kieu": "lien_he", "gia_min": None, "gia_max": None, "goc": t}
    if len(so) >= 2:
        return {"kieu": "khoang", "gia_min": min(so), "gia_max": max(so), "goc": t}
    tu = bool(re.search(r"\bt[uừ]\b", t, re.IGNORECASE))
    return {"kieu": "tu_" if tu else "co_dinh",
            "gia_min": so[0], "gia_max": None if tu else so[0], "goc": t}


def quet_web(raw: str) -> list[dict]:
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    ra = []
    for t in re.findall(r"<table.*?</table>", raw, re.S | re.I):
        for r in re.findall(r"<tr.*?</tr>", t, re.S | re.I):
            o = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip()
                 for c in re.findall(r"<t[dh].*?</t[dh]>", r, re.S | re.I)]
            o = [c for c in o if c]
            if len(o) < 2:
                continue
            ten, gia = o[0], o[-1]
            if "niem" in tu(gia) and "yet" in tu(gia):
                continue           # dòng tiêu đề
            if not re.search(r"\d|li[eê]n h[eệ]", gia, re.IGNORECASE):
                continue
            ra.append({"ten": ten, **doc_gia(gia)})
    return ra


def main(argv=None):
    ap = argparse.ArgumentParser(description="Đối chiếu bảng giá repo với web")
    ap.add_argument("--file", help="dùng file HTML đã tải sẵn thay vì gọi web")
    ap.add_argument("--ghi", action="store_true",
                    help="ghi giá web vào bang-gia.json cho các mục LỆCH GIÁ")
    a = ap.parse_args(argv)

    if a.file:
        raw = Path(a.file).read_text(encoding="utf-8", errors="replace")
    else:
        import urllib.request
        print("Đang tải", WEB)
        req = urllib.request.Request(WEB, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as r:
            raw = r.read().decode("utf-8", "replace")

    web = quet_web(raw)
    print("Web: %d dòng giá\n" % len(web))

    f = GOC / "template" / "bang-gia.json"
    bang = json.loads(f.read_text(encoding="utf-8"))
    repo = [(tu(s["ten"]), s) for s in bang["dich_vu"]]

    # Ghép cặp TỐT NHẤT TOÀN CỤC, không duyệt tuần tự: xếp mọi cặp theo độ giống
    # rồi lấy dần từ cao xuống. Duyệt tuần tự làm dòng đứng trước "giành" mất mục
    # của dòng đứng sau, đẻ ra lệch giá giả.
    NGUONG = 0.45
    cap = []
    for iw, w in enumerate(web):
        tw = tu(w["ten"])
        # tên web riêng khai trong JSON (ten_web) được ưu tiên tuyệt đối
        for tr, sv in repo:
            d = 1.0 if sv.get("ten_web") and tu(sv["ten_web"]) == tw else giong(tw, tr)
            if d >= NGUONG:
                cap.append((d, iw, sv["ma"]))
    cap.sort(key=lambda x: -x[0])

    tra = {s["ma"]: s for _t, s in repo}
    da_web, da_repo, ghep = set(), set(), []
    for d, iw, ma in cap:
        if iw in da_web or ma in da_repo:
            continue
        da_web.add(iw)
        da_repo.add(ma)
        ghep.append((d, iw, ma))

    khop, lech = [], []
    for d, iw, ma in ghep:
        w, s = web[iw], tra[ma]
        w["_diem"] = d
        if s["kieu"] == "lien_he" and w["kieu"] == "lien_he":
            khop.append((s, w))
        elif (s.get("gia_min"), s.get("gia_max")) == (w["gia_min"], w["gia_max"]):
            khop.append((s, w))
        else:
            lech.append((s, w))
    chi_web = [w for i, w in enumerate(web) if i not in da_web]
    da_khop = da_repo
    chi_repo = [sv for _t, sv in repo if sv["ma"] not in da_khop]

    print("KHỚP               : %d" % len(khop))
    print("LỆCH GIÁ           : %d" % len(lech))
    print("CHƯA CÓ TRONG REPO : %d" % len(chi_web))
    print("KHÔNG THẤY TRÊN WEB: %d" % len(chi_repo))

    if lech:
        print("\n--- LỆCH GIÁ (báo giá đang dùng số cũ) ---")
        for s, w in lech:
            print("  %-34s repo %-24s web %-22s (khớp %.0f%%)"
                  % (s["ma"], _ht(s), w["goc"], w.get("_diem", 0) * 100))
            print("  %-34s web : %s" % ("", w["ten"][:70]))
    if chi_web:
        print("\n--- WEB CÓ, REPO THIẾU ---")
        for w in chi_web:
            print("  %-58s %s" % (w["ten"][:58], w["goc"]))
    if chi_repo:
        print("\n--- REPO CÓ, WEB KHÔNG THẤY (có thể web đổi tên) ---")
        for s in chi_repo:
            print("  %-34s %s" % (s["ma"], s["ten"][:48]))

    if a.ghi and lech:
        for s, w in lech:
            for sv in bang["dich_vu"]:
                if sv["ma"] == s["ma"]:
                    sv["kieu"] = w["kieu"]
                    sv["gia_min"] = w["gia_min"]
                    sv["gia_max"] = w["gia_max"]
                    sv.pop("canh_bao", None)
        from datetime import date
        bang["cap_nhat"] = date.today().isoformat()
        f.write_text(json.dumps(bang, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nĐã ghi %d mục lệch vào bang-gia.json, cập nhật %s" % (len(lech), bang["cap_nhat"]))
        print("⚠️ Xem lại git diff trước khi commit.")
    elif lech:
        print("\nChạy lại kèm --ghi để lấy giá web ghi đè vào repo.")
    return 0


def _ht(s):
    if s["kieu"] == "lien_he":
        return "Liên hệ"
    if s["kieu"] == "khoang":
        return "%s-%s" % (f"{s['gia_min']:,}".replace(",", "."), f"{s['gia_max']:,}".replace(",", "."))
    if s["kieu"] == "tu_":
        return "từ " + f"{s['gia_min']:,}".replace(",", ".")
    return f"{s['gia_min']:,}".replace(",", ".")


if __name__ == "__main__":
    sys.exit(main())
