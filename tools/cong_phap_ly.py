# -*- coding: utf-8 -*-
"""Cổng pháp lý cho ấn phẩm BÁO GIÁ Kangnam.

Quét toàn bộ chuỗi trong file dữ liệu báo giá và chặn trước khi render.
Nguồn luật: Agent-LDP-Kangnam/knowledge/KF-11-cong-phap-ly.md (rào R0-R12, bảng từ cấm)
            + knowledge/BG-07-cong-phap-ly.md của chính agent này.

Ba mức:
  CHAN   — fail là KHÔNG XUẤT file, không có ngoại lệ.
  CANH   — phải sửa hoặc phải có người duyệt, render vẫn chạy nhưng in cảnh báo.
  NHAC   — nhắc kiểm tra bằng mắt.

Dùng độc lập:   python tools/cong_phap_ly.py out/KH-xxx/du-lieu.json
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent

for _luong in (sys.stdout, sys.stderr):
    if hasattr(_luong, "reconfigure"):
        _luong.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------- từ cấm (R1)
# (mẫu regex, mức, mã rào, thay bằng)
TU_CAM = [
    # cho phép vài chữ chen giữa: "cam kết mắt đẹp", "đẹp tự nhiên 100%"
    (r"cam\s*k[eế]t[^.;]{0,25}?(k[eế]t\s*qu[aả]|đ[eẹ]p|100\s*%|nh[uư]\s*[yý]|hi[eệ]u\s*qu[aả])", "CHAN", "R1",
     "kết quả tuỳ cơ địa, bác sĩ đánh giá riêng từng trường hợp*"),
    (r"(đ[eẹ]p|an\s*to[aà]n|th[aà]nh\s*c[oô]ng|kh[oỏ]i|hi[eệ]u\s*qu[aả])[^.;]{0,25}?(tuy[eệ]t\s*đ[oố]i|100\s*%)",
     "CHAN", "R1", "tỷ lệ cải thiện cao khi thực hiện đúng chỉ định*"),
    (r"ho[aà]n\s*h[aả]o\s*100", "CHAN", "R1", "kết quả hài hoà với gương mặt*"),
    (r"v[iĩ]nh\s*vi[eễ]n", "CHAN", "R1", "duy trì lâu dài, có chế độ bảo hành minh bạch"),
    (r"tr[oọ]n\s*đ[oờ]i", "CHAN", "R1",
     "chế độ theo dõi và chỉnh sửa theo chính sách bảo hành (ghi rõ thời hạn)"),
    (r"kh[oô]ng\s*bi[eế]n\s*ch[uứ]ng", "CHAN", "R1",
     "quy trình chuẩn y khoa, môi trường vô khuẩn, hội đồng chuyên môn giám sát"),
    (r"kh[oô]ng\s*đau(?!\s*6D)", "CHAN", "R1",
     "giảm đau theo phác đồ, gây tê/gây mê do bác sĩ chỉ định"),
    (r"kh[oô]ng\s*(đ[eể]\s*l[aạ]i\s*)?s[eẹ]o", "CHAN", "R1",
     "vị trí đường mổ được chọn để hạn chế sẹo, chăm sóc theo hướng dẫn*"),
    (r"(t[oố]t\s*nh[aấ]t|duy\s*nh[aấ]t|h[aà]ng\s*đ[aầ]u|gi[oỏ]i\s*nh[aấ]t|đ[iỉ]nh\s*cao\s*nh[aấ]t)", "CHAN", "R1",
     "bỏ, hoặc nêu USP đo được: giấy phép, chứng chỉ, chính sách bảo hành"),
    # "số 1" hay dính địa chỉ (số 1 Trường Chinh) nên chỉ CẢNH, người đọc tự phân biệt
    (r"s[oố]\s*1\b", "CANH", "R1",
     "nếu là tự xưng số 1 thì bỏ; nếu là địa chỉ thì bỏ qua cảnh báo này"),
    (r"r[eẻ]\s*nh[aấ]t", "CHAN", "R1", "chi phí minh bạch, công khai tại bảng giá"),
    (r"nh[uư]\s*h[iì]nh|gi[oố]ng\s*(h[eệ]t\s*)?[aả]nh", "CHAN", "R1",
     "kết quả tuỳ cơ địa, bác sĩ đánh giá riêng từng trường hợp*"),
    (r"ho[aà]n\s*ti[eề]n\s*(100|n[eế]u)", "CHAN", "R1", "nêu đúng chính sách đang có hiệu lực"),
    (r"ch[ií]nh\s*h[aã]ng", "CANH", "R7",
     "nêu đúng tên vật liệu/thiết bị có trong hồ sơ, hoặc bỏ"),
    (r"botox|filler|restylane|juvederm|profhilo|radiesse|sculptra", "CANH", "R7",
     "dùng tên kỹ thuật theo DMKT; tên thương mại phải được Pháp chế duyệt"),
    (r"(b[eệ]nh\s*vi[eệ]n|th[aẩ]m\s*m[yỹ])\s*(kh[aá]c|x)\s*(l[aà]m\s*)?h[oỏ]ng", "CHAN", "R6",
     "không phán xét nơi cũ; đưa bộ tiêu chí khách quan để khách tự đánh giá"),
]

# mốc hồi phục cứng (luật riêng ① của gói Kangnam)
HOI_PHUC_CUNG = re.compile(
    r"\b(\d+)\s*(ng[aà]y|tu[aầ]n|th[aá]ng)[^.;]{0,25}?"
    r"(đi\s*l[aà]m|đi\s*h[oọ]c|h[eế]t\s*s[uư]ng|l[aà]nh\s*h[aẳ]n|h[oồ]i\s*ph[uụ]c|"
    r"b[iì]nh\s*th[uư][oờ]ng|đ[eẹ]p)",
    re.IGNORECASE)
CO_TUY_CO_DIA = re.compile(r"t[uù]y\s*c[oơ]\s*đ[iị]a|ph[uụ]\s*thu[oộ]c\s*c[oơ]\s*đ[iị]a", re.IGNORECASE)

# dữ liệu cá nhân không được đưa vào ấn phẩm / công cụ
DU_LIEU_CAM = [
    (r"\b\d{9}(\d{3})?\b(?!\s*(đ|vnđ|vnd))", "CANH", "PDPA",
     "nghi là CCCD/CMND — không in số định danh lên báo giá"),
    (r"b[eệ]nh\s*[aá]n|ti[eề]n\s*s[uử]\s*b[eệ]nh|HIV|ti[eể]u\s*đ[uư][oờ]ng|huy[eế]t\s*[aá]p", "CANH", "PDPA",
     "không in tình trạng sức khoẻ lên ấn phẩm gửi qua kênh chat"),
]

MIEN_TRU_BAT_BUOC = "Kết quả thẩm mỹ phụ thuộc cơ địa từng người"


def _bo_dau(s: str) -> str:
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode()


def _duyet_chuoi(obj, duong_dan="", ra=None):
    """Trả về list (đường_dẫn, chuỗi) của mọi chuỗi trong cấu trúc."""
    if ra is None:
        ra = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            _duyet_chuoi(v, f"{duong_dan}.{k}" if duong_dan else k, ra)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _duyet_chuoi(v, f"{duong_dan}[{i}]", ra)
    elif isinstance(obj, str):
        ra.append((duong_dan, obj))
    return ra


def _tai_bac_si():
    p = GOC / "template" / "bac-si-duyet.json"
    if not p.exists():
        return {}
    data = json.loads(p.read_text(encoding="utf-8"))
    return {_bo_dau(b["ten"]).lower(): b for b in data["bac_si"]}


def kiem_tra(du_lieu: dict) -> list[dict]:
    """Trả về danh sách lỗi: {muc, ma, duong_dan, trich, thay_bang}."""
    loi = []
    chuoi = _duyet_chuoi(du_lieu)

    # --- 1. bảng từ cấm
    for duong_dan, s in chuoi:
        if duong_dan.startswith("phap_ly."):   # khối miễn trừ được phép chứa từ nhạy cảm
            continue
        for mau, muc, ma, thay in TU_CAM:
            m = re.search(mau, s, re.IGNORECASE)
            if m:
                loi.append({"muc": muc, "ma": ma, "duong_dan": duong_dan,
                            "trich": m.group(0), "thay_bang": thay})

    # --- 2. mốc hồi phục cứng
    for duong_dan, s in chuoi:
        m = HOI_PHUC_CUNG.search(s)
        if m and not CO_TUY_CO_DIA.search(s):
            loi.append({"muc": "CHAN", "ma": "KN-①", "duong_dan": duong_dan,
                        "trich": m.group(0),
                        "thay_bang": "mốc dạng khoảng (vd 7-14 ngày) + cụm tùy cơ địa mỗi người"})

    # --- 3. dữ liệu cá nhân nhạy cảm
    for duong_dan, s in chuoi:
        for mau, muc, ma, thay in DU_LIEU_CAM:
            m = re.search(mau, s, re.IGNORECASE)
            if m:
                loi.append({"muc": muc, "ma": ma, "duong_dan": duong_dan,
                            "trich": m.group(0), "thay_bang": thay})

    # --- 4. bác sĩ (R4)
    bs = _tai_bac_si()
    noi_dung = " ".join(s for _, s in chuoi)
    noi_dung_kd = _bo_dau(noi_dung).lower()
    for khoa, b in bs.items():
        if khoa and khoa in noi_dung_kd:
            tt = b.get("trang_thai")
            if tt == "ngung_dung":
                loi.append({"muc": "CHAN", "ma": "R4", "duong_dan": "(toàn văn)",
                            "trich": b["ten"],
                            "thay_bang": f"{b.get('ghi_chu', '')} — gỡ tên này khỏi báo giá"})
            elif tt == "xung_dot":
                loi.append({"muc": "CHAN", "ma": "R4", "duong_dan": "(toàn văn)",
                            "trich": b["ten"],
                            "thay_bang": "web và KF-02 lệch nhau — DỪNG, hỏi Pháp chế trước khi gửi"})
            elif tt == "can_xac_minh":
                loi.append({"muc": "CANH", "ma": "R4", "duong_dan": "(toàn văn)",
                            "trich": b["ten"],
                            "thay_bang": "cần Chuyên môn xác nhận hồ sơ trước khi in tên"})

    # --- 5. ảnh case phải có consent (R5)
    for case in du_lieu.get("case_tuong_tu") or []:
        co_anh = bool(case.get("anh_truoc") or case.get("anh_sau"))
        if co_anh and not case.get("consent"):
            loi.append({"muc": "CHAN", "ma": "R5", "duong_dan": f"case_tuong_tu[{case.get('ma_case', '?')}]",
                        "trich": "ảnh case không khai consent",
                        "thay_bang": 'đặt "consent": "ok" khi đã có văn bản đồng ý còn hiệu lực, hoặc bỏ ảnh và dùng ô ảnh tạm'})
        if co_anh and not case.get("moc_chup"):
            loi.append({"muc": "CHAN", "ma": "R5", "duong_dan": f"case_tuong_tu[{case.get('ma_case', '?')}]",
                        "trich": "thiếu mốc thời gian chụp",
                        "thay_bang": 'ghi đúng mốc, vd "sau 1 tháng" — bỏ mốc là làm sai lệch bằng chứng'})
        if co_anh and (case.get("nhom") or "").lower() in ("body", "giam can", "giảm cân", "lipo"):
            loi.append({"muc": "CHAN", "ma": "R12", "duong_dan": f"case_tuong_tu[{case.get('ma_case', '?')}]",
                        "trich": "ảnh so sánh cơ thể",
                        "thay_bang": "thay bằng câu chuyện khách hàng thật, không dùng ảnh before/after cơ thể"})

    # --- 6. khối miễn trừ bắt buộc
    # chưa khai mien_tru thì render_baogia.py sẽ tự điền 3 câu chuẩn -> không báo lỗi;
    # khai rồi mà thiếu câu cơ địa thì chặn, vì người viết đã chủ động ghi đè
    toan_van = _bo_dau(noi_dung).lower()
    da_khai_mien_tru = bool((du_lieu.get("phap_ly") or {}).get("mien_tru"))
    if da_khai_mien_tru and _bo_dau(MIEN_TRU_BAT_BUOC).lower() not in toan_van:
        loi.append({"muc": "CHAN", "ma": "R1", "duong_dan": "phap_ly.mien_tru",
                    "trich": "thiếu câu miễn trừ",
                    "thay_bang": f'thêm nguyên văn: "{MIEN_TRU_BAT_BUOC}."'})

    # --- 7. GXNNDQC (R9)
    if not (du_lieu.get("phap_ly") or {}).get("gxnndqc"):
        loi.append({"muc": "NHAC", "ma": "R9", "duong_dan": "phap_ly.gxnndqc",
                    "trich": "chưa xác nhận giấy xác nhận nội dung quảng cáo",
                    "thay_bang": "báo giá cá nhân gửi 1-1 thường không phải quảng cáo đại chúng; nếu dùng lại làm ấn phẩm phát hành thì phải xin GXNNDQC"})

    # --- 8. đại phẫu phải đúng tuyến (R3)
    co_so = (du_lieu.get("meta") or {}).get("co_so", "")
    co_so_kd = _bo_dau(co_so).lower()
    if du_lieu.get("_co_dai_phau") and "benh vien" not in co_so_kd:
        loi.append({"muc": "CHAN", "ma": "R3", "duong_dan": "meta.co_so",
                    "trich": co_so or "(trống)",
                    "thay_bang": "dịch vụ đại phẫu chỉ được mời tại tuyến BỆNH VIỆN; viện tỉnh phải ghi rõ: tư vấn/đặt khám tại [viện], phẫu thuật tại [bệnh viện]"})

    return loi


def in_bao_cao(loi: list[dict]) -> None:
    if not loi:
        print("CỔNG PHÁP LÝ: PASS — không phát hiện vi phạm tự động.")
        print("  (Vẫn phải người thật rà: consent còn hiệu lực, DMKT, đúng pháp nhân.)")
        return
    for muc, nhan in (("CHAN", "CHẶN — không xuất file"),
                      ("CANH", "CẢNH BÁO — cần sửa hoặc cần người duyệt"),
                      ("NHAC", "NHẮC — kiểm bằng mắt")):
        nhom = [l for l in loi if l["muc"] == muc]
        if not nhom:
            continue
        print(f"\n[{nhan}] {len(nhom)} mục")
        for l in nhom:
            print(f"  - {l['ma']:5s} {l['duong_dan']}")
            print(f"      thấy : {l['trich']}")
            print(f"      sửa  : {l['thay_bang']}")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    du_lieu = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    loi = kiem_tra(du_lieu)
    in_bao_cao(loi)
    return 1 if any(l["muc"] == "CHAN" for l in loi) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
