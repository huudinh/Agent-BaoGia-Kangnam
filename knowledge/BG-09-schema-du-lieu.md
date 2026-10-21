# BG-09 — SCHEMA DỮ LIỆU: ĐẦU VÀO & ĐẦU RA
Version 1.0 · Cập nhật: 2026-10-21
File mẫu: `template/khach-hang.mau.json` (đầu vào) · `template/du-lieu.mau.json` (ca cắt mí lần đầu) · `template/du-lieu.mau-sua-mi.json` (ca sửa mí — có giá ưu đãi, phí sửa mí tách dòng, link album)

---

## 1. LUỒNG

```
Thông tin khách hàng  →  [AGENT]  →  du-lieu.json  →  render_baogia.py  →  PDF + JPG
 (chat / JSON / CSV)      viết        dữ liệu có         3 cổng chặn         gửi khách
                        cá nhân hoá    cấu trúc
```

Agent **chỉ sinh ra `du-lieu.json`** và câu lệnh render. Agent **không tự vẽ PDF**, không tự bịa số.

## 2. ĐẦU VÀO — thông tin khách hàng

| Trường | Bắt buộc | Ghi chú |
|---|---|---|
| `ten_hien_thi` | ✔ | Tên khách tự xưng. ⛔ Không dùng tên trên giấy tờ nếu không cần |
| `xung_ho` | ✔ | `chị` / `anh` / `mình`. Chưa rõ giới tính → `mình` |
| `nhu_cau` | ✔ | Mô tả tình trạng + mong muốn, bằng **chữ của khách** |
| `mong_muon` | ✔ | 2–4 gạch đầu dòng ngắn — in thành chip trên báo giá |
| `noi_so` | nên | 2–3 nỗi lo khách đã nói → quyết định khối "băn khoăn" |
| `nhom_kh` | nên | 1–6 theo [[BG-04-chan-dung-khach]] → quyết định giọng |
| `giai_doan` | nên | NHẬN BIẾT / TÌM HIỂU / CÂN NHẮC / THỰC HIỆN / HẬU PHẪU / GẮN BÓ |
| `ngan_sach` | nên | `{tu, den}` — để chọn phương án, ⛔ không in lên file gửi khách |
| `co_so_du_kien` | ✔ | Quyết định cổng R3 (đại phẫu phải tuyến bệnh viện) |
| `thoi_diem_mong_muon` | nên | Ảnh hưởng lộ trình và hiệu lực báo giá |
| `da_tu_van` | nên | Đã khám chưa, bác sĩ nào đã xem — tránh nói quá |
| `nguoi_lap` | ✔ | In lên file |
| `hotline` | — | Bỏ trống thì lấy `template/thong-tin-lien-he.json`. Chỉ khai khi chi nhánh có số riêng |

⛔ **Không nhập:** CCCD/CMND · số bảo hiểm · bệnh án · ảnh khách chưa có consent · tình trạng bệnh lý chi tiết.

### `[CHỜ XÁC NHẬN]` dùng đúng chỗ

| Thứ | Có nguồn chưa | Ghi gì |
|---|---|---|
| **Hotline** | ✅ `template/thong-tin-lien-he.json` | Để trống `meta.hotline`, tool điền. ⛔ **Không bao giờ** `[CHỜ XÁC NHẬN]` |
| **Giá dịch vụ** | ✅ `template/bang-gia.json` | Mã không có trong bảng mới ghi `[CHỜ XÁC NHẬN]` |
| **Tên bác sĩ** | ✅ `template/bac-si-duyet.json` | Trạng thái không phải `duyet` thì gỡ tên, không ghi placeholder |
| **Ưu đãi** | ❌ cần chứng từ | `[CHỜ XÁC NHẬN]` đúng chỗ |
| **Địa chỉ chi nhánh** | ❌ chưa có trong repo | `[CHỜ XÁC NHẬN]` đúng chỗ |

Thấy `[CHỜ XÁC NHẬN]` ở ba dòng đầu nghĩa là **quên nạp file dữ liệu cứng vào Knowledge**, không phải thiếu dữ liệu thật. Tool render tự thay placeholder của hotline bằng số thật và in cảnh báo.

Thiếu trường bắt buộc → agent chạy `/wizard` hỏi dẫn, tối đa 3 câu một lượt.

## 3. ĐẦU RA — `du-lieu.json`

```jsonc
{
  "meta": {
    "ma_bao_gia": "BG-2026-1021-01",   // bắt buộc, duy nhất
    "ngay": "21/10/2026",              // bắt buộc
    "hieu_luc_den": "04/11/2026",      // nên có — 7-14 ngày
    "co_so": "Bệnh viện thẩm mỹ Kangnam Hà Nội",  // bắt buộc, quyết định cổng R3
    "nguoi_lap": "Ngọc Anh — CSKH",    // bắt buộc
    "sdt_tu_van": "", "kenh_gui": "Zalo"
    // hotline: bỏ trống -> lấy template/thong-tin-lien-he.json
  },

  "khach": {
    "ten_hien_thi": "Chị Thu Hà",      // bắt buộc
    "xung_ho": "chị",
    "mo_ta_ngan": "...",               // 2-3 câu, nhắc lại đúng chữ khách nói
    "mong_muon": ["...", "..."],       // in thành chip xanh
    "noi_so": ["...", "..."]           // in thành chip cam
  },

  "mo_dau": { "tieu_de": "...", "loi_mo": "..." },   // bắt buộc, xem BG-03 mục 3

  "van_de_giai_phap": [            // 3-4 cặp. Xương sống của mạch đọc (BG-03 mục 1b)
    { "van_de": "nỗi lo bằng CHỮ CỦA KHÁCH",
      "giai_phap": "cách bên em xử lý đúng vấn đề đó + giới hạn trung thực" }
  ],                               // bắt buộc có cái này HOẶC giai_toa, ⛔ không nói trùng nhau

  "giai_phap": {
    "ten_phuong_an": "...",            // bắt buộc
    "vi_sao_hop": "...",               // phần đắt giá nhất — nối vào tình trạng khách
    "gom": [ {"buoc": "...", "noi_dung": "..."} ],
    "diem_can_luu_y": ["..."]          // điều bác sĩ cần xác nhận khi khám
  },

  "chi_phi": {
    "dong": [                          // bắt buộc, ít nhất 1 dòng
      { "ma": "mat.cat-mi-6d",         // BẮT BUỘC trỏ về bang-gia.json
        "gia": 12800000,
        "so_luong": 1,
        "dien_giai": "...",
        "ly_do_lech": "..."            // chỉ khi giá khác bảng niêm yết
      }
    ],
    "uu_dai": [ {"ten": "...", "gia_tri": 2000000, "dieu_kien": "...", "han": "..."} ],
    "ghi_chu_gia": "đã gồm ... chưa gồm ..."       // nên có
  },                               // ⛔ KHÔNG có trường tra_gop — Kangnam không có
                                   //    chính sách trả góp, cổng dữ liệu CHẶN (BG-02 mục 7)

  "phuong_an_khac": [ {"ten": "...", "gia": 8000000, "khac_biet": "..."} ],

  "case_tuong_tu": [
    { "ma_case": "CM-0423", "mo_ta": "...", "bac_si": "Henry Nguyen",
      "moc_chup": "sau 1 tháng",       // BẮT BUỘC nếu có ảnh
      "ket_qua": "...",
      "nhom": "mat",                   // body/lipo/giảm cân → chặn ảnh (R12)
      "consent": "ok",                 // BẮT BUỘC nếu có ảnh
      "can_anh": true,                 // case SẼ có ảnh nhưng đang chờ xin → dựng ô ảnh tạm
      "anh_truoc": "anh/truoc-01.jpg",
      "anh_sau": "anh/sau-01.jpg",
      "anh_them": "anh/them-01.jpg",   // ô ảnh THỨ BA — lưới tự chuyển 3 cột
      "chu_thich_truoc": "Trước",      // ba nhãn đều đặt lại được. Ảnh album Kangnam
      "chu_thich_sau": "sau 1 tháng",  // thường ĐÃ ghép sẵn trước–sau → lúc đó đặt
      "chu_thich_them": "Góc khác" }   // "Ca 1 · Ca 2 · Ca 3" (BG-08 mục 5)
  ],

  "case_album": {                      // link album đã duyệt gửi khách (BG-06 mục 3b)
    "link": "https://hcigroup.vn/app/albumkn/?album=theme-1792573778761",
    "nhan": "Hình ảnh khách hàng đã cắt mí tại Kangnam"
  },

  "lo_trinh": [ {"moc": "Bước 1 — Đặt lịch khám", "viec": "..."} ],
  "giai_toa": [ {"noi_so": "...", "tra_loi": "..."} ],

  "cta": { "buoc_tiep": "...", "mo_ta": "...", "nut": "...", "dia_chi": "..." },

  "phap_ly": {
    "gxnndqc": false,
    "ghi_chu": "Báo giá cá nhân gửi 1-1 theo yêu cầu khách hàng."
    // "mien_tru": [...]  — để trống thì tool tự điền 3 câu chuẩn
  }
}
```

## 4. TRƯỜNG TOOL TỰ TÍNH — agent không cần ghi
`chi_phi.tong_tam_tinh` · `tong_ht` · `sau_uu_dai` · `sau_uu_dai_ht` · `*_ht` (chuỗi tiền) · `gia_niem_yet_ht` (tự in khi `gia` = `uu_dai_hien_hanh` của bảng giá) · `co_van_de` · `co_case` · `co_album` · `co_bang_chung` · `co_anh_bat_ky` · `hien_anh` · `co_anh_them` · `chu_thich_*` · `co_lo_trinh` · `co_giai_toa` · `co_phuong_an_khac` · `co_luu_y` · `_co_dai_phau` · `phap_ly.mien_tru` (nếu để trống) · `font_nhung` (nội dung `template/font-nhung.css`).

Muốn ghi đè tổng (vd giá gói đã duyệt) thì khai thẳng `chi_phi.sau_uu_dai`.

## 5. QUY ƯỚC ĐẶT TÊN & THƯ MỤC
```
out/<ma_bao_gia>/
├── du-lieu.json          dữ liệu agent sinh ra
├── anh/                  ảnh case (nếu có)
├── BG-....html           bản A4 dựng ra
├── BG-....pdf            gửi email / in
├── BG-....-slide.html
└── BG-....-01..05.jpg    gửi Zalo
```
Mã báo giá: `BG-<năm>-<ngàytháng>-<số thứ tự trong ngày>`.

## 6. BA CỔNG CHẶN CỦA TOOL
| Cổng | Chặn khi |
|---|---|
| **Dữ liệu** | thiếu trường bắt buộc, `chi_phi.dong` rỗng |
| **Bảng giá** | mã không có trong `bang-gia.json` · giá lệch mà không khai `ly_do_lech` · dịch vụ `lien_he` mà tự đặt số |
| **Pháp lý** | từ cấm · mốc hồi phục cứng · bác sĩ sai trạng thái · ảnh thiếu consent/mốc chụp · ảnh cơ thể · thiếu câu miễn trừ · đại phẫu sai tuyến |

Liên quan: [[BG-02-bang-gia]] · [[BG-07-cong-phap-ly]] · [[BG-08-design-system]]
