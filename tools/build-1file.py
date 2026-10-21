#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gói cả bộ render thành MỘT file Python chạy được ở nơi không có repo.

Chạy:    python tools/build-1file.py
Kết quả: tools/baogia-1file.py  — upload đúng file này lên ChatGPT / Gemini,
         không phải tải cả ZIP repo lên mỗi lần.

Cách gói: nhúng NGUYÊN VĂN các file nguồn dưới dạng base64 rồi lúc chạy thì
bung ra thư mục tạm và gọi chính tools/render_baogia.py. Không chép lại logic,
nên bản một-file không bao giờ lệch với repo — sửa template xong chạy lại
script này là xong.
"""
import base64
import io
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "baogia-1file.py")

for _l in (sys.stdout, sys.stderr):
    if hasattr(_l, "reconfigure"):
        _l.reconfigure(encoding="utf-8", errors="replace")

# Đúng những gì render_baogia.py cần để chạy, không hơn.
NGUON = [
    "tools/render_baogia.py",
    "tools/cong_phap_ly.py",
    "tools/render_banggia.py",
    "tools/anh_album.py",
    "template/baogia-a4.html",
    "template/baogia-slide.html",
    "template/banggia.html",
    "template/bang-gia.json",
    "template/album-index.json",
    "template/thong-tin-lien-he.json",
    "template/logo-kangnam.png",
    "template/font-nhung.css",
]

KHUNG = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BÁO GIÁ KANGNAM — bản MỘT FILE, chạy được ở nơi không có repo.

    python baogia-1file.py du-lieu.json              # HTML + PDF + 5 ảnh (cần Chrome)
    python baogia-1file.py du-lieu.json --chi-html   # chỉ HTML (chạy được ở ChatGPT)
    python baogia-1file.py --banggia "nâng mũi"      # bảng giá cả nhóm dịch vụ
    python baogia-1file.py du-lieu.json --khoa akn_...   # tự lấy ảnh khách từ album
    python baogia-1file.py --album "cắt mí" --lay 3      # xem link ảnh (cần khoá API)

File xuất ra nằm cạnh du-lieu.json. HTML tự đứng một mình: logo nhúng sẵn,
không tham chiếu file ngoài — mở bằng trình duyệt rồi Ctrl+P là ra PDF.

⛔ FILE NÀY LÀ BẢN SINH RA, KHÔNG SỬA TAY.
   Sửa ở repo rồi chạy: python tools/build-1file.py
   Nguồn: github.com/huudinh/Agent-BaoGia-Kangnam  ·  gói ngày @@NGAY@@
"""
import base64
import pathlib
import shutil
import subprocess
import sys
import tempfile

for _l in (sys.stdout, sys.stderr):
    if hasattr(_l, "reconfigure"):
        _l.reconfigure(encoding="utf-8", errors="replace")

FILES = @@FILES@@


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2

    if argv[1] == "--album":
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="album-"))
        try:
            for rel, b64 in FILES.items():
                f = tmp / rel
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_bytes(base64.b64decode(b64))
            return subprocess.run(
                [sys.executable, str(tmp / "tools" / "anh_album.py")] + argv[1:]).returncode
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    if argv[1] == "--banggia":
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="banggia-"))
        try:
            for rel, b64 in FILES.items():
                f = tmp / rel
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_bytes(base64.b64decode(b64))
            ra = pathlib.Path.cwd()
            kq = subprocess.run(
                [sys.executable, str(tmp / "tools" / "render_banggia.py")]
                + argv[2:] + ["--ra", str(ra)])
            return kq.returncode
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    dulieu = pathlib.Path(argv[1]).resolve()
    if not dulieu.exists():
        print("Không thấy file:", dulieu)
        return 2

    tmp = pathlib.Path(tempfile.mkdtemp(prefix="baogia-"))
    try:
        for rel, b64 in FILES.items():
            f = tmp / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(base64.b64decode(b64))

        ra = tmp / "out" / "KH"
        ra.mkdir(parents=True, exist_ok=True)
        shutil.copy(dulieu, ra / "du-lieu.json")

        kq = subprocess.run(
            [sys.executable, str(tmp / "tools" / "render_baogia.py"),
             str(ra / "du-lieu.json")] + argv[2:])

        dich = dulieu.parent
        lay = [f for f in sorted(ra.iterdir()) if f.name != "du-lieu.json"]
        for f in lay:
            shutil.copy(f, dich / f.name)
        if lay:
            print()
            print("File đã chép ra cạnh du-lieu.json:", dich)
            for f in lay:
                print("   ", f.name)
        return kq.returncode
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
'''


def main():
    from datetime import date
    goi = {}
    for rel in NGUON:
        p = os.path.join(REPO, rel)
        if not os.path.exists(p):
            sys.exit("Thieu file nguon: " + rel)
        with open(p, "rb") as f:
            goi[rel] = base64.b64encode(f.read()).decode("ascii")

    # in dict dạng nhiều dòng cho dễ nhìn diff, mỗi chuỗi base64 cắt 96 ký tự
    dong = ["{"]
    for rel, b64 in goi.items():
        dong.append('    %r:' % rel)
        for i in range(0, len(b64), 96):
            dong.append('        "%s"' % b64[i:i + 96])
        dong.append("        ,")
    dong.append("}")
    files_src = "\n".join(dong)

    html = KHUNG.replace("@@FILES@@", files_src).replace("@@NGAY@@", date.today().isoformat())
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)

    kb = os.path.getsize(OUT) / 1024
    print("Đã ghi:", OUT, "-", round(kb), "KB")
    for rel in NGUON:
        print("   nhúng", rel, "-", round(os.path.getsize(os.path.join(REPO, rel)) / 1024, 1), "KB")


if __name__ == "__main__":
    main()
