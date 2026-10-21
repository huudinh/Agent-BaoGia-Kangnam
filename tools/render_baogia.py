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

SO_TRANG_CHUAN = 4   # PDF A4 chuẩn 4 trang, một mạch mỗi trang (BG-03 mục 8):
                     # vấn đề -> phương án -> chi phí -> bằng chứng & bước tiếp.

# Trường phải điền đủ thì báo giá mới ra hồn. Cổng dữ liệu nay siết chặt hơn
# phần "ai đã duyệt" — thà bắt người lập điền đủ còn hơn chặn vì thiếu con dấu.
TRUONG_BAT_BUOC = [
    ("meta.ma_bao_gia", "mã báo giá"),
    ("meta.ngay", "ngày lập"),
    ("meta.co_so", "cơ sở thực hiện — quyết định dịch vụ đại phẫu có được mời hay không"),
    ("meta.nguoi_lap", "người lập — in lên file, ai gửi thì chịu trách nhiệm bản đó"),
    ("khach.ten_hien_thi", "tên khách"),
    ("khach.mo_ta_ngan", "mô tả tình trạng khách bằng CHỮ CỦA KHÁCH — thiếu là mất cá nhân hoá"),
    ("khach.mong_muon", "điều khách mong muốn (2-4 ý)"),
    ("mo_dau.tieu_de", "tiêu đề lời hứa"),
    ("mo_dau.loi_mo", "lời mở 3 câu"),
    ("giai_phap.ten_phuong_an", "tên phương án"),
    ("giai_phap.vi_sao_hop", "VÌ SAO phương án này hợp với khách NÀY — phần đắt giá nhất"),
    ("chi_phi.dong", "dòng chi phí"),
    ("chi_phi.ghi_chu_gia", "dòng đã gồm / chưa gồm — khách sợ phát sinh chứ không sợ đắt"),
    ("lo_trinh", "lộ trình từng bước"),
    ("cta.buoc_tiep", "bước tiếp theo"),
    ("cta.dia_chi", "địa chỉ cơ sở khách tới khám"),
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
    for t, vi_sao in TRUONG_BAT_BUOC:
        if not _that(lay(d, t)):
            loi.append(f"{t}  —  {vi_sao}")
    if not (d.get("chi_phi") or {}).get("dong"):
        loi.append("chi_phi.dong  —  báo giá phải có ít nhất 1 dòng chi phí")
    # Nỗi lo của khách phải được xử lý ở ÍT NHẤT MỘT trong hai khối. Có cả hai mà
    # nói cùng một nỗi lo là lặp — vừa loãng vừa đội thêm một trang giấy.
    # Kangnam KHÔNG có chính sách trả góp. Nêu ra là nói sai sự thật về một
    # chính sách thanh toán — khách tin rồi tới viện mới biết không có.
    if (d.get("chi_phi") or {}).get("tra_gop"):
        loi.append("chi_phi.tra_gop  —  Kangnam KHÔNG có chính sách trả góp. "
                   "Bỏ trường này; muốn hạ áp lực chi phí thì đưa phương án vừa "
                   "ngân sách ở khối phuong_an_khac")
    if not _that(d.get("van_de_giai_phap")) and not _that(d.get("giai_toa")):
        loi.append("van_de_giai_phap HOẶC giai_toa  —  phải có một khối xử lý nỗi lo "
                   "của khách: cặp vấn đề→cách xử lý, hoặc khối băn khoăn")
    return loi


def can_nhac_truoc_khi_gui(d: dict, loi_pl: list[dict]) -> list[str]:
    """Vài thứ tool không tự biết được — người gửi liếc qua rồi gửi.

    ⛔ KHÔNG phải quy trình phê duyệt. Đây là báo giá tham khảo gửi một khách,
    không phải ấn phẩm phát hành, nên không có "bộ phận có thẩm quyền" nào ở đây.
    """
    o = []
    if (d.get("chi_phi") or {}).get("uu_dai"):
        o.append("Ưu đãi đang ghi còn hiệu lực không?")
    if d.get("_co_dai_phau"):
        o.append("Có dịch vụ ĐẠI PHẪU — khách đã biết phẫu thuật thực hiện tại tuyến bệnh viện chưa?")
    o.append("Đọc lại mục chi phí: đã gồm / chưa gồm đã nói đủ chưa?")
    o.append("Che tên khách đi, file này còn gửi được cho khách khác không? Còn = chưa cá nhân hoá.")
    for l in loi_pl:
        if l["muc"] == "CANH":
            o.append("[%s] %s → %s" % (l["ma"], l["trich"], l["thay_bang"]))
    return o


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


def dung_ngu_canh(d: dict, bang: dict, nhap: bool, goc_anh: Path) -> dict:
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

    for pa in d.get("phuong_an_khac") or []:
        pa["gia_ht"] = tien(pa.get("gia"))

    # Album nào dùng cho case chưa có ảnh: ưu tiên khai riêng ở case, không có
    # thì lấy chính album đã khai để gửi kèm khách.
    album_chung = lay(d, "case_album.album") or lay(d, "case_album.link") or ""

    for c in d.get("case_tuong_tu") or []:
        # Chưa dán link ảnh mà có album -> TỰ GỌI API lấy, khỏi bắt người lập
        # báo giá chạy anh_album.py rồi dán tay. Ảnh album vốn đã ghép sẵn
        # trước–sau nên nhãn mặc định là "Ca 1/2/3", không phải "Trước"/"Sau".
        if not (c.get("anh_truoc") or c.get("anh_sau") or c.get("anh_them")):
            ngn = c.get("album") or album_chung
            if ngn:
                try:
                    import anh_album
                    lay_ve = anh_album.lay_anh(ngn, int(c.get("so_anh") or 3))
                except Exception:
                    lay_ve = []
                if lay_ve:
                    for o, u in zip(("anh_truoc", "anh_sau", "anh_them"), lay_ve):
                        c[o] = u
                    for k, v in zip(("chu_thich_truoc", "chu_thich_sau", "chu_thich_them"),
                                    ("Ca 1", "Ca 2", "Ca 3")):
                        c.setdefault(k, v)
                    print(f"  ảnh       : lấy {len(lay_ve)} ảnh từ album \"{ngn}\"")
                else:
                    print(f"  ! Không lấy được ảnh từ album \"{ngn}\" — thiếu khoá API "
                          f"(KN_ALBUM_KEY / template/album-key.local.json) hoặc album rỗng.")

        # ảnh có thể là link album, URL bất kỳ, hay file trên máy — nhúng hết vào
        # file để bản gửi khách tự đứng một mình, không phụ thuộc album còn sống
        for o in ("anh_truoc", "anh_sau", "anh_them"):
            if c.get(o):
                c[o] = nhung_anh(c[o], goc_anh)
        c["co_anh"] = bool(c.get("anh_truoc") or c.get("anh_sau") or c.get("anh_them"))
        # ảnh thứ ba chỉ hiện khi có ảnh thật — không dựng ô ảnh tạm cho nó,
        # hai ô trước–sau đã đủ để nhắc đi xin ảnh
        c["co_anh_them"] = bool(c.get("anh_them"))
        # Nhãn dưới mỗi ô ảnh đặt lại được: ảnh trong Album Kangnam thường ĐÃ LÀ
        # ảnh ghép trước–sau, lúc đó nhãn "Trước"/"Sau" là sai — ghi "Ca 1, 2, 3"
        # hoặc tên kỹ thuật thì đúng hơn.
        c.setdefault("chu_thich_truoc", "Trước")
        c.setdefault("chu_thich_sau", c.get("moc_chup") or "Sau")
        c.setdefault("chu_thich_them", "Góc khác")
        # case kể bằng chữ (không định dùng ảnh) thì không dựng ô ảnh tạm;
        # khai can_anh = true khi case SẼ có ảnh nhưng đang chờ xin
        c["hien_anh"] = c["co_anh"] or bool(c.get("can_anh"))

    # hotline: nguồn duy nhất là template/thong-tin-lien-he.json,
    # chỉ ghi đè khi báo giá khai số riêng của chi nhánh
    # agent lỡ ghi [CHỜ XÁC NHẬN] vào hotline -> coi như bỏ trống, điền số thật
    _ht = str(d["meta"].get("hotline") or "")
    if "CHỜ" in _ht.upper() or _ht.strip().startswith("["):
        print("  ! meta.hotline đang là placeholder — hotline CÓ nguồn, tool tự điền số thật.")
        d["meta"]["hotline"] = ""
    if not d["meta"].get("hotline"):
        lh = GOC / "template" / "thong-tin-lien-he.json"
        if lh.exists():
            d["meta"]["hotline"] = json.loads(lh.read_text(encoding="utf-8")).get("hotline", "")
        if not d["meta"].get("hotline"):
            print("  ! Không có hotline: thiếu template/thong-tin-lien-he.json "
                  "và du-lieu.json cũng không khai meta.hotline.")

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
    d["co_van_de"] = bool(d.get("van_de_giai_phap"))
    d["co_mong_muon"] = bool(kh.get("mong_muon") or kh.get("noi_so"))
    # Font nhúng sẵn (data URI) — sinh bằng tools/nhung-font.py. Thiếu file thì
    # không sao: khai báo font-family còn font hệ thống đứng sau đỡ.
    fo = GOC / "template" / "font-nhung.css"
    d["font_nhung"] = fo.read_text(encoding="utf-8") if fo.exists() else ""
    if not d["font_nhung"]:
        print("  ! Thiếu template/font-nhung.css — file xuất ra dùng font hệ thống. "
              "Chạy: python tools/nhung-font.py")

    # logo thật nhúng thẳng vào file (data URI) để HTML/PDF xuất ra tự đứng một mình
    d["logo"] = lay_logo()
    d["co_logo"] = bool(d["logo"])

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


def chay_chrome(chrome: str, them: list[str], url: str) -> str:
    with tempfile.TemporaryDirectory() as hs:
        lenh = [chrome, "--headless=new", "--disable-gpu", "--no-first-run",
                "--no-default-browser-check", "--hide-scrollbars",
                f"--user-data-dir={hs}", "--virtual-time-budget=4000"] + them + [url]
        # encoding tường minh: --dump-dom trả HTML tiếng Việt, để Python tự đoán
        # thì trên Windows nó dùng cp1252, luồng đọc chết và stdout thành None
        kq = subprocess.run(lenh, capture_output=True, text=True, timeout=180,
                            encoding="utf-8", errors="replace")
        if kq.returncode != 0:
            print(kq.stderr[-1500:], file=sys.stderr)
            raise RuntimeError(f"Chrome trả mã {kq.returncode}")
        return kq.stdout


def slide_bi_tran(chrome: str, html: Path) -> list[int]:
    """Slide nào thu nhỏ hết cỡ mà vẫn tràn 1920px thì script gắn data-tran.

    Ảnh chụp ra trông vẫn "đẹp" vì overflow:hidden cắt gọn phần thừa — nên phải
    đọc lại DOM mới biết, không thể nhìn ảnh mà đoán.
    """
    try:
        dom = chay_chrome(chrome, ["--dump-dom"], html.as_uri())
    except Exception:
        return []
    ra = []
    for i, the in enumerate(re.findall(r'<div class="slide[^>]*>', dom), start=1):
        if "data-tran" in the:
            ra.append(i)
    return ra


LOGO_URL = ("https://benhvienthammykangnam.com.vn/wp-content/themes/SCI_Theme_v3/"
            "Module/Home/header_kn_3_0_0/images/top.png")


def lay_logo() -> str:
    """Trả data URI của logo. Thiếu file trên máy thì tải lại từ web Kangnam.

    File xuất ra hay mất logo vì `template/logo-kangnam.png` không nằm cùng chỗ
    với tool — hay gặp nhất khi kéo file thẳng từ cửa sổ xem ZIP. Có mạng thì tự
    lấy lại rồi lưu luôn, lần sau khỏi tải.
    """
    import base64
    f = GOC / "template" / "logo-kangnam.png"
    if f.exists():
        return "data:image/png;base64," + base64.b64encode(f.read_bytes()).decode()

    print("  ! Thiếu template/logo-kangnam.png — thử tải lại từ web Kangnam…")
    try:
        import urllib.request
        yc = urllib.request.Request(LOGO_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(yc, timeout=25) as r:
            b = r.read()
    except Exception as e:
        print(f"    ✗ không tải được ({e}). Dùng chữ thay logo — KHÔNG gửi khách bản này.")
        return ""
    try:
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(b)
        print(f"    lấy được {len(b) / 1024:.0f} KB, đã lưu lại {f}")
    except OSError:
        print(f"    lấy được {len(b) / 1024:.0f} KB (không lưu được, lần sau tải lại)")
    return "data:image/png;base64," + base64.b64encode(b).decode()


def nhung_anh(nguon: str, goc: Path) -> str:
    """Biến link ảnh thành data URI để file gửi khách tự đứng một mình.

    Nhận: URL http(s) (vd link từ Album Kangnam) · đường dẫn tương đối cạnh
    du-lieu.json · hoặc data URI sẵn. Lấy không được thì trả "" để template
    dựng ô ảnh tạm, kèm cảnh báo — không bao giờ để <img> trỏ vào link chết.
    """
    import base64
    import mimetypes

    nguon = (nguon or "").strip()
    if not nguon or nguon.startswith("data:"):
        return nguon

    try:
        if nguon.startswith(("http://", "https://")):
            import urllib.request
            req = urllib.request.Request(nguon, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                loai = r.headers.get_content_type()
        else:
            f = (goc / nguon) if not Path(nguon).is_absolute() else Path(nguon)
            raw = f.read_bytes()
            loai = mimetypes.guess_type(f.name)[0] or "image/jpeg"
    except Exception as e:
        print(f"  ! Không lấy được ảnh {nguon[:70]} — {e}")
        print("    Dùng ô ảnh tạm thay thế. Kiểm lại link, hoặc tải ảnh về cạnh du-lieu.json.")
        return ""

    if not loai.startswith("image/"):
        print(f"  ! {nguon[:70]} trả về {loai}, không phải ảnh. Dùng ô ảnh tạm.")
        return ""
    print(f"  ảnh       : nhúng {round(len(raw) / 1024)} KB từ {nguon[:62]}")
    return "data:%s;base64,%s" % (loai, base64.b64encode(raw).decode())


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
    ap.add_argument("--khoa", help="khoá API Album Kangnam, để tự lấy ảnh khách thật "
                                   "(hoặc đặt biến môi trường KN_ALBUM_KEY)")
    a = ap.parse_args(argv)
    if a.khoa:
        import os
        os.environ["KN_ALBUM_KEY"] = a.khoa

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
    d = dung_ngu_canh(d, bang, a.nhap, f.parent)

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
        chuan = SO_TRANG_CHUAN
        print(f"  => PDF    : {pdf}  ({so_trang} trang)")
        if so_trang > chuan:
            print(f"  ! Báo giá dài {so_trang} trang, chuẩn là {chuan}. "
                  f"Rút gọn lời mở, số cặp vấn đề→giải pháp, hoặc bước phương án (BG-03 mục 8).")

    if "jpg" in a.dinh_dang and html_slide:
        so_slide = len(re.findall(r'class="slide[ "]', html_slide.read_text(encoding="utf-8")))
        for i in range(1, so_slide + 1):
            png = ra / f"{ten}-{i:02d}.png"
            chay_chrome(chrome, [f"--screenshot={png}", "--window-size=1080,1920",
                                 "--force-device-scale-factor=1"],
                        html_slide.as_uri() + f"?s={i}")
            ket = png_sang_jpg(png, ra / f"{ten}-{i:02d}.jpg")
            print(f"  => ảnh {i} : {ket}")
        tran = slide_bi_tran(chrome, html_slide)
        if tran:
            print(f"  ! Slide {', '.join(map(str, tran))} TRÀN KHUNG — nội dung bị cắt "
                  f"ở mép dưới. Rút gọn cặp vấn đề→giải pháp hoặc câu 'vì sao hợp'.")

    # Gợi ý ảnh thật: khách tin ảnh hơn tin chữ
    co_anh = any(c.get("anh_truoc") or c.get("anh_sau") or c.get("anh_them")
                 for c in d.get("case_tuong_tu") or [])
    if not co_anh:
        lh = GOC / "template" / "thong-tin-lien-he.json"
        album = ""
        if lh.exists():
            album = json.loads(lh.read_text(encoding="utf-8")).get("album_anh_khach", "")
        print("\n  GỢI Ý — báo giá này chưa có ảnh khách thật.")
        print("  Ảnh trước–sau là thứ khách xem trước cả giá. Cách nhanh nhất:")
        print('      khai "case_album": {"album": "<id>"} trong du-lieu.json')
        print("      — tool TỰ gọi API lấy ảnh. Danh mục: template/album-index.json")
        print("  Hoặc chọn tay:")
        print("      python tools/anh_album.py --album \"<tên album>\" --lay 3")
        if album:
            print("      hoặc tự chọn trong %s" % album)
        print("  rồi dán link vào case_tuong_tu[].anh_truoc / anh_sau / anh_them — tool tự tải về")
        print("  nhúng vào file, bản gửi khách vẫn tự đứng một mình.")

    print("\n" + "=" * 68)
    print("  LIẾC QUA TRƯỚC KHI GỬI — vài thứ tool không tự biết được")
    print("=" * 68)
    for i, o in enumerate(can_nhac_truoc_khi_gui(d, loi_pl), 1):
        print("  %d. %s" % (i, o))
    print("\n  Đây là báo giá tham khảo gửi riêng một khách — đọc xong rồi gửi.")

    if a.nhap:
        print("\n! BẢN NHÁP — đã đóng dấu NHÁP, KHÔNG gửi khách hàng.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
