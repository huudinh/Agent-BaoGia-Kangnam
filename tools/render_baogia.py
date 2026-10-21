# -*- coding: utf-8 -*-
"""Render BÁO GIÁ CÁ NHÂN HOÁ KANGNAM: du-lieu.json  ->  HTML -> PDF (A4) + JPG (slide 1080x1920).

Không cần cài thư viện ngoài: dùng Chrome/Edge đã có sẵn trên máy ở chế độ headless.
Pillow (nếu có) dùng để đổi PNG -> JPG; không có Pillow thì giữ PNG.

    python tools/render_baogia.py out/KH-2026-1021-01/du-lieu.json
    python tools/render_baogia.py <du-lieu.json> --dinh-dang pdf jpg
    python tools/render_baogia.py <du-lieu.json> --nhap        # bản nháp nội bộ, đóng dấu NHÁP
    python tools/render_baogia.py <du-lieu.json> --chi-html    # chỉ dựng HTML, không gọi Chrome

Ba cổng chạy trước khi xuất file, fail là KHÔNG XUẤT:
    1. CỔNG DỮ LIỆU   — thiếu trường bắt buộc
    2. CỔNG BẢNG GIÁ  — mã dịch vụ và giá phải khớp template/bang-gia.json
    3. CỔNG PHÁP LÝ   — tools/cong_phap_ly.py (rào R0-R12 + bảng từ cấm)
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(GOC / "tools"))
import cong_phap_ly  # noqa: E402

# cửa sổ lệnh Windows mặc định cp1252 — ép UTF-8 để in được tiếng Việt
for _luong in (sys.stdout, sys.stderr):
    if hasattr(_luong, "reconfigure"):
        _luong.reconfigure(encoding="utf-8", errors="replace")

SO_TRANG_CHUAN = 3   # PDF A4 chuẩn 3 trang (BG-03 mục 8); dài hơn thì tool cảnh báo

TRUONG_BAT_BUOC = [
    "meta.ma_bao_gia", "meta.ngay", "meta.co_so", "meta.nguoi_lap", "meta.hotline",
    "khach.ten_hien_thi", "mo_dau.tieu_de", "giai_phap.ten_phuong_an", "chi_phi.dong",
]

# ------------------------------------------------------------------ tiện ích


def lay(obj, duong_dan, mac_dinh=None):
    cur = obj
    for phan in duong_dan.split("."):
        if isinstance(cur, dict) and phan in cur:
            cur = cur[phan]
        else:
            return mac_dinh
    return cur


def tien(n) -> str:
    """12800000 -> 12.800.000đ"""
    if n is None or n == "":
        return "Liên hệ"
    if isinstance(n, str):
        return n
    return f"{int(n):,}".replace(",", ".") + "đ"


def thoat_html(s: str) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


# ------------------------------------------------- template engine (mustache-lite)
RE_KHOI = re.compile(r"\{\{([#^])\s*([\w.]+)\s*\}\}(.*?)\{\{/\s*\2\s*\}\}", re.S)
RE_BIEN = re.compile(r"\{\{(\{)?\s*([\w.]+)\s*\}?\}\}")


def _that(v) -> bool:
    return not (v is None or v is False or v == "" or v == [] or v == {})


def render(mau: str, ctx: dict, cha: list | None = None) -> str:
    cha = cha or []

    def tim(ten):
        if ten == ".":
            # phần tử vô hướng trong list được bọc thành {".": giá_trị}
            return ctx.get(".", ctx) if isinstance(ctx, dict) else ctx
        v = lay(ctx, ten, "\0")
        if v != "\0":
            return v
        for c in reversed(cha):
            v = lay(c, ten, "\0")
            if v != "\0":
                return v
        return None

    def thay_khoi(m):
        loai, ten, than = m.group(1), m.group(2), m.group(3)
        v = tim(ten)
        if loai == "^":
            return render(than, ctx, cha) if not _that(v) else ""
        if not _that(v):
            return ""
        if isinstance(v, list):
            return "".join(
                render(than, i if isinstance(i, dict) else {".": i}, cha + [ctx])
                for i in v)
        if isinstance(v, dict):
            return render(than, v, cha + [ctx])
        return render(than, ctx, cha)

    truoc = None
    while truoc != mau:
        truoc = mau
        mau = RE_KHOI.sub(thay_khoi, mau)

    def thay_bien(m):
        raw, ten = m.group(1), m.group(2)
        v = tim(ten)
        if v is None or v is False:
            return ""
        return str(v) if raw else thoat_html(v)

    return RE_BIEN.sub(thay_bien, mau)


# ------------------------------------------------------------------ các cổng


def cong_du_lieu(d: dict) -> list[str]:
    loi = []
    for t in TRUONG_BAT_BUOC:
        if not _that(lay(d, t)):
            loi.append(f"thiếu trường bắt buộc: {t}")
    if not (d.get("chi_phi") or {}).get("dong"):
        loi.append("chi_phi.dong rỗng — báo giá phải có ít nhất 1 dòng chi phí")
    return loi


def cong_bang_gia(d: dict, bang: dict) -> list[str]:
    tra = {s["ma"]: s for s in bang["dich_vu"]}
    loi = []
    co_dai_phau = False
    for i, dong in enumerate(d["chi_phi"]["dong"]):
        ma = dong.get("ma")
        if not ma:
            loi.append(f"chi_phi.dong[{i}] thiếu mã dịch vụ — mọi dòng phải trỏ về bang-gia.json")
            continue
        if ma not in tra:
            loi.append(f"chi_phi.dong[{i}] mã {ma} KHÔNG có trong bảng giá — agent không được tự tạo dịch vụ")
            continue
        sv = tra[ma]
        if sv.get("dai_phau"):
            co_dai_phau = True
        if sv.get("canh_bao"):
            dong.setdefault("_canh_bao", sv["canh_bao"])
        gia = dong.get("gia")
        if sv["kieu"] == "lien_he":
            if gia:
                loi.append(f"chi_phi.dong[{i}] {ma}: bảng giá ghi Liên hệ, không được tự đặt số")
            continue
        if gia is None:
            loi.append(f"chi_phi.dong[{i}] {ma}: thiếu giá")
            continue
        lech = False
        if sv["kieu"] == "co_dinh":
            # giá ưu đãi đang hiệu lực được coi là khớp bảng, không cần khai ly_do_lech
            hop_le = {sv["gia_min"]}
            if sv.get("uu_dai_hien_hanh") is not None:
                hop_le.add(sv["uu_dai_hien_hanh"])
            lech = gia not in hop_le
        elif sv["kieu"] == "khoang":
            lech = not (sv["gia_min"] <= gia <= sv["gia_max"])
        elif sv["kieu"] == "tu_":
            lech = gia < sv["gia_min"]
        if lech and not dong.get("ly_do_lech"):
            loi.append(
                f"chi_phi.dong[{i}] {ma}: giá {tien(gia)} lệch bảng niêm yết "
                f"({tien(sv['gia_min'])}{'' if sv['kieu'] == 'co_dinh' else ' - ' + tien(sv.get('gia_max'))}). "
                f"Khai ly_do_lech (vd: ưu đãi T10 đã duyệt) hoặc sửa lại giá")
    d["_co_dai_phau"] = co_dai_phau
    return loi


# ------------------------------------------------------------- chuẩn bị ngữ cảnh


def dung_ngu_canh(d: dict, bang: dict, nhap: bool) -> dict:
    tra = {s["ma"]: s for s in bang["dich_vu"]}
    cp = d["chi_phi"]
    tong = 0
    for dong in cp["dong"]:
        sv = tra.get(dong.get("ma"), {})
        dong.setdefault("ten", sv.get("ten", ""))
        sl = dong.get("so_luong") or 1
        gia = dong.get("gia")
        tt = (gia or 0) * sl
        dong["so_luong"] = sl
        dong["don_vi"] = dong.get("don_vi") or sv.get("don_vi", "ca")
        dong["gia_ht"] = tien(gia)
        dong["thanh_tien"] = tt
        dong["thanh_tien_ht"] = tien(tt) if gia else "Liên hệ"
        # đang báo theo giá ưu đãi -> in kèm giá niêm yết gạch ngang (BG-11 mục 4.2)
        uu = sv.get("uu_dai_hien_hanh")
        if uu is not None and gia == uu and sv.get("gia_min") not in (None, uu):
            dong["gia_niem_yet_ht"] = tien(sv["gia_min"])
        tong += tt

    cp["tong_tam_tinh"] = cp.get("tong_tam_tinh", tong)
    cp["tong_ht"] = tien(cp["tong_tam_tinh"])

    giam = 0
    for ud in cp.get("uu_dai") or []:
        ud["gia_tri_ht"] = tien(ud.get("gia_tri"))
        if isinstance(ud.get("gia_tri"), (int, float)):
            giam += ud["gia_tri"]
    cp["tong_giam"] = giam
    cp["tong_giam_ht"] = tien(giam) if giam else ""
    cp["sau_uu_dai"] = cp.get("sau_uu_dai", cp["tong_tam_tinh"] - giam)
    cp["sau_uu_dai_ht"] = tien(cp["sau_uu_dai"])
    cp["co_uu_dai"] = bool(cp.get("uu_dai"))

    tg = cp.get("tra_gop")
    if tg and tg.get("so_ky"):
        tg.setdefault("so_tien_moi_ky", round(cp["sau_uu_dai"] / tg["so_ky"] / 1000) * 1000)
        tg["so_tien_moi_ky_ht"] = tien(tg["so_tien_moi_ky"])

    for pa in d.get("phuong_an_khac") or []:
        pa["gia_ht"] = tien(pa.get("gia"))

    for c in d.get("case_tuong_tu") or []:
        c["co_anh"] = bool(c.get("anh_truoc") or c.get("anh_sau"))
        # case kể bằng chữ (không định dùng ảnh) thì không dựng ô ảnh tạm;
        # khai can_anh = true khi case SẼ có ảnh nhưng đang chờ xin
        c["hien_anh"] = c["co_anh"] or bool(c.get("can_anh"))

    d["meta"].setdefault("ngay", date.today().isoformat())
    d["meta"].setdefault("hieu_luc_den", "")
    d["_nhap"] = nhap
    d["_nam"] = date.today().year

    # cờ bật/tắt khối — để template không phải lặp khi chỉ muốn kiểm tra rỗng
    kh = d.setdefault("khach", {})
    kh.setdefault("xung_ho", "chị")
    kh["xung_ho_hoa"] = str(kh["xung_ho"]).upper()
    d["co_case"] = bool(d.get("case_tuong_tu"))
    d["co_lo_trinh"] = bool(d.get("lo_trinh"))
    d["co_giai_toa"] = bool(d.get("giai_toa"))
    d["co_phuong_an_khac"] = bool(d.get("phuong_an_khac"))
    d["co_luu_y"] = bool(lay(d, "giai_phap.diem_can_luu_y"))
    d["co_mong_muon"] = bool(kh.get("mong_muon") or kh.get("noi_so"))
    d["co_album"] = bool(lay(d, "case_album.link"))
    if d["co_album"]:
        d["case_album"].setdefault("nhan", "Xem thêm hình ảnh khách hàng đã thực hiện tại Kangnam")
    d["co_bang_chung"] = d["co_case"] or d["co_album"]
    # câu miễn trừ ảnh chỉ in khi thật sự có ảnh (trong file hoặc trong album)
    d["co_anh_bat_ky"] = d["co_album"] or any(
        c.get("hien_anh") for c in d.get("case_tuong_tu") or [])
    d.setdefault("phap_ly", {})
    d["phap_ly"].setdefault("mien_tru", [
        "Báo giá mang tính tham khảo theo thông tin khách hàng cung cấp. Chi phí cuối cùng do bác sĩ quyết định sau khi thăm khám trực tiếp.",
        "Kết quả thẩm mỹ phụ thuộc cơ địa từng người.",
        "Hình ảnh khách hàng được sử dụng khi có sự đồng ý bằng văn bản và ghi rõ thời điểm chụp.",
    ])
    return d


# ------------------------------------------------------------------ Chrome


def tim_chrome() -> str | None:
    import os
    if os.environ.get("KN_CHROME"):
        return os.environ["KN_CHROME"]
    ung_vien = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ]
    for p in ung_vien:
        if Path(p).exists():
            return p
    for ten in ("chrome", "google-chrome", "chromium", "msedge"):
        p = shutil.which(ten)
        if p:
            return p
    return None


def chay_chrome(chrome: str, them: list[str], url: str) -> None:
    with tempfile.TemporaryDirectory() as hs:
        lenh = [chrome, "--headless=new", "--disable-gpu", "--no-first-run",
                "--no-default-browser-check", "--hide-scrollbars",
                f"--user-data-dir={hs}", "--virtual-time-budget=4000"] + them + [url]
        kq = subprocess.run(lenh, capture_output=True, text=True, timeout=180)
        if kq.returncode != 0:
            print(kq.stderr[-1500:], file=sys.stderr)
            raise RuntimeError(f"Chrome trả mã {kq.returncode}")


def dem_trang_pdf(pdf: Path) -> int:
    """Đếm số trang của PDF Chrome xuất ra, không cần thư viện ngoài."""
    try:
        return len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes())) or 0
    except OSError:
        return 0


def png_sang_jpg(png: Path, jpg: Path) -> Path:
    try:
        from PIL import Image
    except ImportError:
        print("  ! Không có Pillow — giữ nguyên PNG.")
        return png
    with Image.open(png) as im:
        im.convert("RGB").save(jpg, "JPEG", quality=92, optimize=True)
    png.unlink(missing_ok=True)
    return jpg


# ------------------------------------------------------------------- main


def main(argv=None):
    ap = argparse.ArgumentParser(description="Render báo giá cá nhân hoá Kangnam")
    ap.add_argument("du_lieu", help="đường dẫn du-lieu.json")
    ap.add_argument("--dinh-dang", nargs="+", default=["pdf", "jpg"],
                    choices=["pdf", "jpg"], help="định dạng xuất (mặc định cả hai)")
    ap.add_argument("--ra", help="thư mục xuất (mặc định: cạnh file du-lieu.json)")
    ap.add_argument("--nhap", action="store_true", help="bản nháp nội bộ, đóng dấu NHÁP")
    ap.add_argument("--chi-html", action="store_true", help="chỉ dựng HTML")
    a = ap.parse_args(argv)

    f = Path(a.du_lieu).resolve()
    d = json.loads(f.read_text(encoding="utf-8"))
    bang = json.loads((GOC / "template" / "bang-gia.json").read_text(encoding="utf-8"))
    ra = Path(a.ra).resolve() if a.ra else f.parent
    ra.mkdir(parents=True, exist_ok=True)

    print(f"BÁO GIÁ {lay(d, 'meta.ma_bao_gia', '?')} — {lay(d, 'khach.ten_hien_thi', '?')}")

    # --- cổng 1
    loi = cong_du_lieu(d)
    if loi:
        print("\n[CỔNG DỮ LIỆU] CHẶN")
        for l in loi:
            print("  -", l)
        return 1
    print("  cổng dữ liệu  : PASS")

    # --- cổng 2
    loi = cong_bang_gia(d, bang)
    if loi:
        print("\n[CỔNG BẢNG GIÁ] CHẶN")
        for l in loi:
            print("  -", l)
        return 1
    print("  cổng bảng giá : PASS" + ("  (có dịch vụ ĐẠI PHẪU)" if d.get("_co_dai_phau") else ""))

    # chuẩn hoá trước khi soi pháp lý, để cổng đọc đúng văn bản sẽ in ra giấy
    d = dung_ngu_canh(d, bang, a.nhap)

    # --- cổng 3
    loi_pl = cong_phap_ly.kiem_tra(d)
    cong_phap_ly.in_bao_cao(loi_pl)
    if any(l["muc"] == "CHAN" for l in loi_pl) and not a.nhap:
        print("\n=> KHÔNG XUẤT FILE. Sửa các mục CHẶN rồi chạy lại.")
        print("   (Cần xem thử bố cục thì chạy thêm --nhap để ra bản đóng dấu NHÁP, KHÔNG gửi khách.)")
        return 1

    # --- dựng HTML
    ten = re.sub(r"[^\w.-]", "_", lay(d, "meta.ma_bao_gia", "bao-gia"))
    mau_a4 = (GOC / "template" / "baogia-a4.html").read_text(encoding="utf-8")
    html_a4 = ra / f"{ten}.html"
    html_a4.write_text(render(mau_a4, d), encoding="utf-8")
    print(f"\n  HTML A4   : {html_a4}")

    html_slide = None
    if "jpg" in a.dinh_dang:
        mau_sl = (GOC / "template" / "baogia-slide.html").read_text(encoding="utf-8")
        noi_dung_sl = render(mau_sl, d)
        html_slide = ra / f"{ten}-slide.html"
        html_slide.write_text(noi_dung_sl, encoding="utf-8")
        so_slide = len(re.findall(r'class="slide[ "]', noi_dung_sl))
        print(f"  HTML slide: {html_slide}  ({so_slide} slide)")

    if a.chi_html:
        return 0

    chrome = tim_chrome()
    if not chrome:
        print("\n! Không tìm thấy Chrome/Edge. Đặt biến môi trường KN_CHROME trỏ tới chrome.exe,")
        print("  hoặc mở file HTML ở trên rồi Ctrl+P -> Save as PDF.")
        return 3
    print(f"  trình duyệt: {chrome}")

    if "pdf" in a.dinh_dang:
        pdf = ra / f"{ten}.pdf"
        chay_chrome(chrome, [f"--print-to-pdf={pdf}", "--no-pdf-header-footer",
                             "--print-to-pdf-no-header"], html_a4.as_uri())
        so_trang = dem_trang_pdf(pdf)
        print(f"  => PDF    : {pdf}  ({so_trang} trang)")
        if so_trang > SO_TRANG_CHUAN:
            print(f"  ! Báo giá dài {so_trang} trang, chuẩn là {SO_TRANG_CHUAN}. "
                  f"Rút gọn lời mở, bước phương án hoặc khối băn khoăn (BG-03 mục 8).")

    if "jpg" in a.dinh_dang and html_slide:
        so_slide = len(re.findall(r'class="slide[ "]', html_slide.read_text(encoding="utf-8")))
        for i in range(1, so_slide + 1):
            png = ra / f"{ten}-{i:02d}.png"
            chay_chrome(chrome, [f"--screenshot={png}", "--window-size=1080,1920",
                                 "--force-device-scale-factor=1"],
                        html_slide.as_uri() + f"?s={i}")
            ket = png_sang_jpg(png, ra / f"{ten}-{i:02d}.jpg")
            print(f"  => ảnh {i} : {ket}")

    canh = [l for l in loi_pl if l["muc"] in ("CANH", "NHAC")]
    if canh:
        print(f"\n! Còn {len(canh)} cảnh báo cần người thật xử lý trước khi gửi khách (xem ở trên).")
    if a.nhap:
        print("\n! BẢN NHÁP — đã đóng dấu NHÁP, KHÔNG gửi khách hàng.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
