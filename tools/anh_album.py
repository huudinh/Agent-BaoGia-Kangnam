# -*- coding: utf-8 -*-
"""Duyệt Album Kangnam để lấy link ảnh khách hàng thật, dán vào báo giá.

    python tools/anh_album.py                          # liệt kê các album
    python tools/anh_album.py --album "cắt mí"          # liệt kê ảnh trong album
    python tools/anh_album.py --album "cắt mí" --lay 3  # in sẵn JSON 3 ảnh đầu

KHOÁ API — chỉ cần để *liệt kê*; tải ảnh thì không cần. Lấy theo thứ tự:
    1. tham số --khoa
    2. biến môi trường KN_ALBUM_KEY
    3. file template/album-key.local.json  →  {"khoa": "akn_..."}

⛔ File khoá KHÔNG commit lên GitHub (repo công khai). `.gitignore` đã chặn
`*.local.json`. Lỡ lộ khoá thì vào app xoay khoá mới.

⚠️ Ảnh nằm trong album KHÔNG đồng nghĩa đã có văn bản đồng ý của khách.
Kho là chỗ lưu ảnh, không phải chỗ cấp phép — người lập báo giá tự kiểm.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
API = "https://hcigroup.vn/app/albumkn/api/public"

for _l in (sys.stdout, sys.stderr):
    if hasattr(_l, "reconfigure"):
        _l.reconfigure(encoding="utf-8", errors="replace")


def bo_dau(s: str) -> str:
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()


def lay_khoa(tu_tham_so: str | None) -> str:
    if tu_tham_so:
        return tu_tham_so
    if os.environ.get("KN_ALBUM_KEY"):
        return os.environ["KN_ALBUM_KEY"]
    f = GOC / "template" / "album-key.local.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8")).get("khoa", "")
    return ""


def goi(duong: str, khoa: str) -> dict:
    req = urllib.request.Request(API + duong, headers={"X-API-Key": khoa})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))


def tim_album(themes: list, tu_khoa: str) -> dict | None:
    tk = bo_dau(tu_khoa).strip()
    for t in themes:
        if t["id"] == tu_khoa:
            return t
    for t in themes:
        if tk and tk in bo_dau(t.get("title", "")):
            return t
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description="Duyệt Album Kangnam lấy link ảnh thật")
    ap.add_argument("--album", help="tên hoặc id album, vd: \"cắt mí\"")
    ap.add_argument("--lay", type=int, metavar="N",
                    help="in sẵn khối JSON case_tuong_tu với N ảnh đầu (nên dùng 3)")
    ap.add_argument("--khoa", help="khoá API (ưu tiên hơn env và file local)")
    a = ap.parse_args(argv)

    khoa = lay_khoa(a.khoa)
    if not khoa:
        print("Chưa có khoá API. Đặt một trong ba cách:")
        print("  set KN_ALBUM_KEY=akn_...")
        print("  tạo template/album-key.local.json  ->  {\"khoa\": \"akn_...\"}")
        print("  hoặc chạy kèm --khoa akn_...")
        return 2

    try:
        themes = goi("/themes", khoa)["items"]
    except urllib.error.HTTPError as e:
        print("Album trả lỗi HTTP %s — khoá sai hoặc đã xoay khoá." % e.code)
        return 3
    except Exception as e:
        print("Không gọi được album:", e)
        return 3

    if not a.album:
        print("%d album trong kho:\n" % len(themes))
        for t in themes:
            print("  %-26s %s" % (t["id"], t.get("title", "")))
            if t.get("description"):
                print("  %-26s %s" % ("", t["description"]))
        print("\nXem ảnh trong một album:  python tools/anh_album.py --album \"<tên>\"")
        return 0

    t = tim_album(themes, a.album)
    if not t:
        print("Không có album nào khớp '%s'. Chạy không tham số để xem danh sách." % a.album)
        return 2

    anh = goi("/photos?themeId=%s&limit=200" % t["id"], khoa)["items"]
    print("ALBUM: %s  (%s)  — %d ảnh\n" % (t.get("title", ""), t["id"], len(anh)))

    for i, it in enumerate(anh, 1):
        tag = (" · tag: " + ", ".join(it["tags"])) if it.get("tags") else ""
        print("%2d. %s%s" % (i, it["imageUrl"], tag))
        if it.get("description"):
            print("    %s" % it["description"])

    if not any(it.get("tags") for it in anh):
        print("\n⚠️  Chưa ảnh nào gắn tag. Ảnh nằm trong kho KHÔNG đồng nghĩa đã có")
        print("    văn bản đồng ý của khách — người lập báo giá tự kiểm trước khi gửi.")
        print("    Nên dùng quy ước tag: consent-ok · consent-cho · consent-het-han")

    if a.lay:
        lay = anh[:a.lay]
        mau = {
            "case_tuong_tu": [{
                "ma_case": t["id"],
                "mo_ta": "[mô tả tình trạng ban đầu của khách trong ảnh]",
                "bac_si": "",
                "moc_chup": "[vd: sau 1 tháng]",
                "ket_qua": "[kết quả, viết theo đúng luật — không cam kết]",
                "nhom": "mat",
                "consent": "",
                "anh_truoc": lay[0]["imageUrl"] if len(lay) > 0 else "",
                "anh_sau": lay[1]["imageUrl"] if len(lay) > 1 else "",
                "anh_them": lay[2]["imageUrl"] if len(lay) > 2 else "",
                "chu_thich_them": "Góc khác" if len(lay) > 2 else "",
            }]
        }
        print("\nDán khối này vào du-lieu.json (nhớ sửa phần trong ngoặc vuông):\n")
        print(json.dumps(mau, ensure_ascii=False, indent=2))
        print("\nTool render sẽ TẢI ảnh về và nhúng thẳng vào file, nên file gửi khách")
        print("vẫn tự đứng một mình — không phụ thuộc album còn sống hay không.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
