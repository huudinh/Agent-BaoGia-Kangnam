#!/usr/bin/env python3
"""Gộp tri thức + dữ liệu cứng thành HAI file để upload lên agent.

Vì sao cần: Gemini Gems chỉ cho **tối đa 10 file** tri thức, ChatGPT Custom GPT
cho 20 nhưng upload 15 file một lượt rất hay lỗi. Bộ gốc có 11 file knowledge +
3 file JSON + 1 file mẫu = 15. Gộp lại còn hai:

    goi/KANGNAM-tri-thuc.md       11 file knowledge, giữ nguyên văn
    goi/KANGNAM-du-lieu-cung.json bảng giá + bác sĩ duyệt + liên hệ + mẫu JSON

⛔ KHÔNG sửa tay hai file trong goi/ — sửa ở knowledge/ hoặc template/ rồi chạy:
    python tools/build-goi.py
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
GOC = Path(__file__).resolve().parent.parent
RA = GOC / "goi"

# Thứ tự đọc, quan trọng nhất lên trước — agent đọc từ trên xuống khi phải cắt.
TRI_THUC = [
    ("BG-07-cong-phap-ly", "Cổng pháp lý", "Rào R0–R12 + bảng từ cấm. Fail = không xuất file", True),
    ("BG-02-bang-gia", "Luật nói về tiền", "Nguồn giá duy nhất · ưu đãi · giá lệch · đã gồm/chưa gồm", True),
    ("BG-03-cau-truc-bao-gia", "Cấu trúc 9 khối", "Xương sống của tờ báo giá — thứ tự không đảo", True),
    ("BG-04-chan-dung-khach", "Chân dung khách", "6 nhóm · 6 giai đoạn · khi nào CHƯA nên gửi báo giá", True),
    ("BG-11-noi-dau-cat-mi", "Nỗi đau khách cắt mí", "9 chân dung · 10 nỗi lo · giải pháp Plasma · chính sách giá", True),
    ("BG-05-noi-so-phan-doi", "Nỗi sợ & phản đối", "Khuôn trả lời 3 nhịp cho khối băn khoăn", False),
    ("BG-06-proof-case", "Case & ảnh trước–sau", "4 điều kiện dùng một case · link album · ô ảnh tạm", False),
    ("BG-01-ho-so-thuong-hieu", "Hồ sơ thương hiệu", "Giọng viết · cơ sở & tuyến · bác sĩ · giới hạn phát ngôn", False),
    ("BG-08-design-system", "Design system", "Token màu · 4 trang A4 · 3 ảnh slide · font nhúng", False),
    ("BG-09-schema-du-lieu", "Schema dữ liệu", "Cấu trúc du-lieu.json — đầu vào/đầu ra của tool", False),
    ("BG-10-vong-hoc", "Vòng học", "4 chỉ số thật — hiện đang trống, chờ dữ liệu", False),
]

DU_LIEU = [
    ("bang_gia", "template/bang-gia.json", "NGUỒN GIÁ DUY NHẤT. Mọi dòng chi phí phải có mã trỏ về đây."),
    ("album_index", "template/album-index.json", "29 album ảnh khách thật. Khai id vào case_album.album -> tool tự gọi API lấy ảnh."),
    ("lien_he", "template/thong-tin-lien-he.json", "Hotline in lên báo giá. ⛔ Không bao giờ ghi [CHỜ XÁC NHẬN] cho hotline."),
    ("du_lieu_mau", "template/du-lieu.mau.json", "Mẫu du-lieu.json đầy đủ — sinh JSON theo đúng cấu trúc này."),
]


def gop_tri_thuc() -> Path:
    ngay = date.today().isoformat()
    d = [
        "# KANGNAM — TRI THỨC AGENT BÁO GIÁ",
        f"> Gộp {len(TRI_THUC)} file trong `knowledge/` thành một. Sinh tự động ngày {ngay} "
        "bằng `python tools/build-goi.py`.",
        "> ⛔ **Không sửa file này** — sửa ở `knowledge/BG-xx-*.md` rồi chạy lại lệnh trên.",
        "",
        "**Cách đọc:** mỗi mục `# BG-xx` dưới đây nguyên là **một file tri thức riêng**. "
        "Tham chiếu dạng `[[BG-07-cong-phap-ly]]` nằm trong văn bản trỏ tới **mục cùng tên "
        "ngay trong file này**, không phải file bên ngoài.",
        "",
        "## MỤC LỤC",
        "",
        "| Mã | Nội dung | Đọc khi |",
        "|---|---|---|",
    ]
    for slug, ten, mo_ta, quan_trong in TRI_THUC:
        ma = slug.split("-")[0] + "-" + slug.split("-")[1]
        d.append(f"| **{ma}**{' ⚠️' if quan_trong else ''} | {ten} | {mo_ta} |")
    d += ["", "⚠️ = đọc mọi lần lập báo giá. Còn lại đọc khi chạm tới việc đó.", ""]

    tong = 0
    for slug, ten, _, _ in TRI_THUC:
        f = GOC / "knowledge" / f"{slug}.md"
        noi = f.read_text(encoding="utf-8").strip()
        tong += len(noi)
        d += ["", "<!-- " + "=" * 72 + " -->",
              f"<!-- NGUỒN: knowledge/{slug}.md -->",
              "<!-- " + "=" * 72 + " -->", "", noi, ""]
        print(f"  gộp {slug}.md  ·  {len(noi) / 1024:.1f} KB")

    dich = RA / "KANGNAM-tri-thuc.md"
    dich.write_text("\n".join(d) + "\n", encoding="utf-8")
    print(f"=> {dich.name}  —  {dich.stat().st_size / 1024:.0f} KB "
          f"(nội dung gốc {tong / 1024:.0f} KB)")
    return dich


def gop_du_lieu() -> Path:
    goi = {
        "_doc": ("Gộp 4 file dữ liệu cứng của Agent-BaoGia-Kangnam. Sinh tự động bằng "
                 "tools/build-goi.py — KHÔNG sửa tay, sửa ở template/ rồi chạy lại."),
        "_sinh_ngay": date.today().isoformat(),
        "_cach_dung": {},
    }
    for khoa, duong_dan, vi_sao in DU_LIEU:
        f = GOC / duong_dan
        goi[khoa] = json.loads(f.read_text(encoding="utf-8"))
        goi["_cach_dung"][khoa] = f"{vi_sao}  (nguồn: {duong_dan})"
        print(f"  gộp {duong_dan}  ·  {f.stat().st_size / 1024:.1f} KB")

    dich = RA / "KANGNAM-du-lieu-cung.json"
    dich.write_text(json.dumps(goi, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"=> {dich.name}  —  {dich.stat().st_size / 1024:.0f} KB")
    return dich


def main() -> int:
    RA.mkdir(exist_ok=True)
    print("TRI THỨC")
    a = gop_tri_thuc()
    print("\nDỮ LIỆU CỨNG")
    b = gop_du_lieu()
    print(f"\nUpload lên agent: {a.name} + {b.name}  =  **2 file** "
          f"(trước đây {len(TRI_THUC) + len(DU_LIEU)} file).")
    print("Muốn agent tự dựng PDF/ảnh ở ChatGPT thì thêm tools/baogia-1file.py — tổng 3 file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
