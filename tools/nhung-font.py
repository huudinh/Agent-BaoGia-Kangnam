#!/usr/bin/env python3
"""Tải font chữ về và nhúng thẳng vào CSS dưới dạng data URI.

Vì sao phải nhúng thay vì <link> tới Google Fonts:
  - Máy render có thể không có mạng; font tải chậm làm Chrome chụp ảnh hụt chữ.
  - File gửi khách phải TỰ ĐỨNG MỘT MÌNH — khách mở file sau một tháng,
    không phụ thuộc CDN nào còn sống.
Chạy lại khi muốn đổi font:
    python tools/nhung-font.py                      # font mặc định
    python tools/nhung-font.py --font "Inter" --nang 400 600 700 800
Kết quả: template/font-nhung.css  (render_baogia.py tự chèn vào mọi file xuất ra)
"""
from __future__ import annotations

import argparse
import base64
import re
import sys
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
GOC = Path(__file__).resolve().parent.parent

# UA của Chrome thật: không có nó Google Fonts trả TTF nguyên bản (nặng gấp 5 lần)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

# Bộ ký tự cần: latin cho chữ thường, vietnamese cho dấu. latin-ext không dùng
# tới mà nặng thêm, nên bỏ.
DAU_HIEU_VIET = "U+0102-0103"
DAU_HIEU_LATIN = "U+0000-00FF"


def tai(url: str) -> bytes:
    yc = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(yc, timeout=60) as r:
        return r.read()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--font", default="Be Vietnam Pro",
                    help="tên font trên Google Fonts (mặc định: Be Vietnam Pro)")
    ap.add_argument("--nang", nargs="+", default=["400", "600", "700", "800", "900"],
                    help="các độ đậm cần nhúng")
    a = ap.parse_args()

    ten_url = a.font.replace(" ", "+")
    css_url = (f"https://fonts.googleapis.com/css2?family={ten_url}"
               f":wght@{';'.join(a.nang)}&display=block")
    print(f"Tải mô tả font: {a.font} — độ đậm {', '.join(a.nang)}")
    try:
        css = tai(css_url).decode("utf-8")
    except Exception as e:
        print(f"✗ Không tải được: {e}")
        print("  Font này có thể không có trên Google Fonts, hoặc máy đang không có mạng.")
        return 1

    khoi = re.findall(r"@font-face\s*\{[^}]*\}", css)
    if not khoi:
        print("✗ Google Fonts không trả @font-face nào — kiểm lại tên font.")
        return 1

    # Font VARIABLE (Google Sans là một ví dụ): Google Fonts trả CÙNG MỘT file
    # woff2 cho nhiều độ đậm. Nhúng từng khối một là lặp y nguyên file đó mấy
    # lần. Gom theo URL rồi khai một @font-face với DẢI độ đậm.
    nhom: dict[str, dict] = {}
    bo = 0
    for k in khoi:
        dai = re.search(r"unicode-range:\s*([^;]+);", k)
        pham_vi = dai.group(1) if dai else ""
        if pham_vi and not (pham_vi.startswith(DAU_HIEU_LATIN)
                            or DAU_HIEU_VIET in pham_vi):
            bo += 1
            continue
        u = re.search(r"url\((https://[^)]+\.woff2)\)", k)
        nang = re.search(r"font-weight:\s*(\d+)", k)
        if not u or not nang:
            bo += 1
            continue
        g = nhom.setdefault(u.group(1), {"khoi": k, "nang": [], "viet": DAU_HIEU_VIET in pham_vi})
        g["nang"].append(int(nang.group(1)))

    ra, tong = [], 0
    for url, g in nhom.items():
        b = tai(url)
        tong += len(b)
        uri = "data:font/woff2;base64," + base64.b64encode(b).decode("ascii")
        k = re.sub(r"url\(https://[^)]+\)", f"url({uri})", g["khoi"], count=1)
        lo, hi = min(g["nang"]), max(g["nang"])
        dai_nang = str(lo) if lo == hi else f"{lo} {hi}"
        k = re.sub(r"font-weight:\s*[^;]+;", f"font-weight: {dai_nang};", k, count=1)
        ra.append(k)
        print(f"  nhúng {a.font} {dai_nang}"
              f" · {'việt' if g['viet'] else 'latin'}"
              f" · {len(b) / 1024:.1f} KB"
              + (f"  (một file cho {len(g['nang'])} độ đậm)" if lo != hi else ""))

    if not ra:
        print("✗ Không nhúng được mảnh font nào.")
        return 1

    dich = GOC / "template" / "font-nhung.css"
    dau = (f"/* Font nhúng sẵn — sinh bằng: python tools/nhung-font.py --font \"{a.font}\"\n"
           f"   ⛔ Không sửa tay file này. Nó là {len(ra)} mảnh woff2 đã base64,\n"
           f"   nhúng vào mọi file xuất ra để file gửi khách tự đứng một mình. */\n")
    dich.write_text(dau + "\n".join(ra) + "\n", encoding="utf-8")
    print(f"\nĐã ghi: {dich}  —  {dich.stat().st_size / 1024:.0f} KB"
          f"  (woff2 gốc {tong / 1024:.0f} KB, bỏ {bo} mảnh không dùng)")
    print(f"Font đã nhúng: \"{a.font}\". Nhớ đặt tên này trong khai báo font-family")
    print("của hai template, rồi render lại để kiểm.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
