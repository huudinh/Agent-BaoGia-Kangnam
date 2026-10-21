# -*- coding: utf-8 -*-
"""Xuất BẢNG GIÁ MỘT NHÓM DỊCH VỤ ra HTML (và PDF) để gửi khách.

    python tools/render_banggia.py mũi
    python tools/render_banggia.py mắt --xung-ho chị --nguoi-lap "Ngọc Anh — CSKH"
    python tools/render_banggia.py mũi --dinh-dang pdf
    python tools/render_banggia.py --liet-ke          # xem có những nhóm nào

Mọi con số lấy thẳng từ template/bang-gia.json — tool KHÔNG tự đặt giá, không
bỏ sót dịch vụ nào trong nhóm. Hotline lấy từ template/thong-tin-lien-he.json.

⚠️ Bảng giá cả nhóm là **bước lùi** so với báo giá cá nhân hoá: khách cầm bảng
giá chung rất dễ đem đi so giá. Chỉ dùng khi khách mới hỏi và chưa có thông tin
gì để cá nhân hoá; kèm luôn lời mời khám để chuyển sang /baogia.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(GOC / "tools"))
import render_baogia as rb  # noqa: E402  — dùng lại engine template, tiền tệ, Chrome

for _l in (sys.stdout, sys.stderr):
    if hasattr(_l, "reconfigure"):
        _l.reconfigure(encoding="utf-8", errors="replace")

# Tên nhóm hiển thị cho khách — nhóm trong bảng giá viết theo kiểu nội bộ
TEN_KHACH = {
    "Mắt": "cắt mí & vùng mắt",
    "Mũi": "nâng mũi",
    "Khuôn mặt / Hàm": "khuôn mặt & hàm",
    "Ngực": "nâng ngực & tạo hình vòng 1",
    "Vóc dáng / Hút mỡ": "vóc dáng & hút mỡ",
    "Trẻ hóa da": "trẻ hoá da",
    "Da liễu": "điều trị da",
    "Nha khoa": "nha khoa thẩm mỹ",
    "Spa": "chăm sóc da & spa",
}


def bo_dau(s: str) -> str:
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()


def tim_nhom(bang: dict, tu_khoa: str) -> str | None:
    """Khớp tên nhóm kiểu dễ dãi: 'mui', 'nâng mũi', 'Mũi' đều ra nhóm Mũi."""
    nhom = []
    for s in bang["dich_vu"]:
        if s["nhom"] not in nhom:
            nhom.append(s["nhom"])
    tk = bo_dau(tu_khoa).strip()
    for n in nhom:                                   # khớp đúng trước
        if bo_dau(n) == tk:
            return n
    for n in nhom:                                   # rồi mới khớp chứa
        if tk in bo_dau(n) or bo_dau(n) in tk:
            return n
    for n, ten in TEN_KHACH.items():                 # khớp theo tên gọi của khách
        if tk in bo_dau(ten) or bo_dau(ten) in tk:
            return n
    return None


def gia_hien_thi(sv: dict) -> tuple[str, str, str | None]:
    """Trả (chuỗi giá, lớp css, giá niêm yết gạch ngang nếu đang có ưu đãi)."""
    kieu = sv["kieu"]
    uu = sv.get("uu_dai_hien_hanh")
    if kieu == "lien_he":
        return "Liên hệ", "lienhe", None
    if uu is not None:
        return rb.tien(uu), "uudai", rb.tien(sv["gia_min"])
    if kieu == "co_dinh":
        return rb.tien(sv["gia_min"]), "", None
    if kieu == "khoang":
        return "%s – %s" % (rb.tien(sv["gia_min"]), rb.tien(sv["gia_max"])), "", None
    if kieu == "tu_":
        return "từ " + rb.tien(sv["gia_min"]), "", None
    return "Liên hệ", "lienhe", None


def main(argv=None):
    ap = argparse.ArgumentParser(description="Xuất bảng giá một nhóm dịch vụ")
    ap.add_argument("nhom", nargs="?", help="tên nhóm: mũi · mắt · ngực · hàm · hút mỡ · da · nha khoa")
    ap.add_argument("--liet-ke", action="store_true", help="in danh sách nhóm rồi thoát")
    ap.add_argument("--xung-ho", default="mình", help="chị / anh / mình (mặc định: mình)")
    ap.add_argument("--nguoi-lap", default="", help="tên tư vấn viên in ở khối liên hệ")
    ap.add_argument("--dinh-dang", nargs="+", default=["html"], choices=["html", "pdf"])
    ap.add_argument("--ra", help="thư mục xuất (mặc định: out/)")
    a = ap.parse_args(argv)

    bang = json.loads((GOC / "template" / "bang-gia.json").read_text(encoding="utf-8"))

    if a.liet_ke or not a.nhom:
        print("Các nhóm trong bảng giá:")
        seen = []
        for s in bang["dich_vu"]:
            if s["nhom"] not in seen:
                seen.append(s["nhom"])
        for n in seen:
            sl = sum(1 for s in bang["dich_vu"] if s["nhom"] == n)
            print("  %-22s %2d dịch vụ   (khách gọi: %s)" % (n, sl, TEN_KHACH.get(n, n)))
        return 0 if a.liet_ke else 2

    nhom = tim_nhom(bang, a.nhom)
    if not nhom:
        print("Không có nhóm nào khớp '%s'. Chạy --liet-ke để xem danh sách." % a.nhom)
        return 2

    dich_vu = []
    co_dai_phau = False
    for sv in bang["dich_vu"]:
        if sv["nhom"] != nhom:
            continue
        gia, lop, niem_yet = gia_hien_thi(sv)
        if sv.get("dai_phau"):
            co_dai_phau = True
        ghi = []
        if sv.get("dai_phau"):
            ghi.append("thực hiện tại tuyến bệnh viện")
        if sv.get("don_vi") and sv["don_vi"] not in ("ca", ""):
            ghi.append("tính theo %s" % sv["don_vi"])
        dich_vu.append({
            "ten": sv["ten"], "gia_ht": gia, "lop_gia": lop,
            "gia_niem_yet_ht": niem_yet, "ghi_chu_dong": " · ".join(ghi),
            "_canh_bao": sv.get("canh_bao", ""),
        })

    ten_khach = TEN_KHACH.get(nhom, nhom.lower())
    lh = GOC / "template" / "thong-tin-lien-he.json"
    hotline = json.loads(lh.read_text(encoding="utf-8"))["hotline"] if lh.exists() else ""

    ctx = {
        "nhom": nhom,
        "tieu_de": "Bảng giá dịch vụ %s" % ten_khach,
        "loi_mo": ("Em gửi %s bảng giá tham khảo các dịch vụ %s đang áp dụng tại Kangnam. "
                   "Mỗi người một tình trạng khác nhau nên bác sĩ sẽ chốt chi phí chính xác "
                   "sau khi khám trực tiếp." % (a.xung_ho, ten_khach)),
        "dich_vu": dich_vu,
        "co_dai_phau": co_dai_phau,
        "xung_ho": a.xung_ho,
        "cap_nhat": bang.get("cap_nhat", date.today().isoformat()),
        "hotline": hotline,
        "nguoi_lap": a.nguoi_lap,
        "cta_tieu_de": "Muốn biết đúng chi phí của %s?" % a.xung_ho,
        "cta_mo_ta": ("Bác sĩ khám trực tiếp rồi bên em gửi %s một bản báo giá riêng, "
                      "ghi rõ phương án và từng khoản chi phí. Sau khi khám %s vẫn toàn quyền "
                      "quyết định." % (a.xung_ho, a.xung_ho)),
        "cta_nut": "Nhắn giờ %s tiện — em giữ lịch khám" % a.xung_ho,
    }

    logo = GOC / "template" / "logo-kangnam.png"
    if logo.exists():
        import base64
        ctx["logo"] = "data:image/png;base64," + base64.b64encode(logo.read_bytes()).decode()
        ctx["co_logo"] = True
    else:
        ctx["co_logo"] = False
        print("  ! Thiếu template/logo-kangnam.png — dùng chữ thay logo.")

    ra = Path(a.ra).resolve() if a.ra else (GOC / "out")
    ra.mkdir(parents=True, exist_ok=True)
    ten_file = "banggia-" + re.sub(r"[^a-z0-9]+", "-", bo_dau(nhom)).strip("-")

    mau = (GOC / "template" / "banggia.html").read_text(encoding="utf-8")
    html = ra / (ten_file + ".html")
    html.write_text(rb.render(mau, ctx), encoding="utf-8")
    print("BẢNG GIÁ %s — %d dịch vụ" % (nhom, len(dich_vu)))
    print("  HTML : %s" % html)

    canh = [d for d in dich_vu if d["_canh_bao"]]
    if canh:
        print("\n  ! %d mục có cảnh báo, xác nhận trước khi gửi khách:" % len(canh))
        for d in canh:
            print("    - %s: %s" % (d["ten"], d["_canh_bao"]))

    if "pdf" in a.dinh_dang:
        chrome = rb.tim_chrome()
        if not chrome:
            print("\n  ! Không tìm thấy Chrome — mở file HTML rồi Ctrl+P để ra PDF.")
            return 3
        pdf = ra / (ten_file + ".pdf")
        rb.chay_chrome(chrome, ["--print-to-pdf=%s" % pdf, "--no-pdf-header-footer",
                                "--print-to-pdf-no-header"], html.as_uri())
        print("  PDF  : %s  (%d trang)" % (pdf, rb.dem_trang_pdf(pdf)))

    print("\n  Nhắc: bảng giá cả nhóm dễ bị đem đi so giá. Có thông tin khách rồi thì")
    print("  chuyển sang báo giá cá nhân hoá (/baogia) — tỉ lệ đặt khám cao hơn hẳn.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
