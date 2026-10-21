# 03 — OUTPUT MẪU (ca thật đã chạy qua tool)

Ca mẫu: **chị Thu Hà, 32 tuổi, nhóm 1 (công sở), giai đoạn CÂN NHẮC, cắt mí.**
Dữ liệu đầy đủ: [`template/du-lieu.mau.json`](../template/du-lieu.mau.json) — chạy thử được ngay.

---

## Phần 1 — Agent trả lời trong chat

### A. ĐỌC KHÁCH
```
NHÓM     : 1 — công sở & tích góp. Dấu hiệu: 32 tuổi, đi làm, nhắc "nghỉ ít ngày",
           tự đặt trần ngân sách 15 triệu.
GIAI ĐOẠN: CÂN NHẮC — đã qua bước hỏi giá, đang hỏi đau/sẹo/nghỉ làm.
           Đây là lúc gửi báo giá đầy đủ hiệu quả nhất.
NỖI LO   : sợ đau (L6.5) · sợ lộ sẹo khi trang điểm (L6.5) · sợ nghỉ làm dài (L6.4)
```

### B. PHƯƠNG ÁN
**Cắt mí 6D + lấy mỡ nội soi mí trên.**
Mí một nếp kèm da dư nhẹ: chỉ tạo nếp thì nếp dễ bị che và mất độ mở. Lấy bớt mỡ mí trên làm vùng mí gọn lại, nếp ăn sâu đều hơn và tự nhiên theo khuôn mặt tròn của khách.

### C. BẢNG CHI PHÍ
| Mã | Hạng mục | Giá | Nguồn |
|---|---|---|---|
| `mat.cat-mi-6d` | Cắt mí 6D | 12.800.000đ | khớp bảng |
| `mat.lay-mo-noi-soi-mi` | Lấy mỡ nội soi mí | 6.400.000đ | khớp bảng |
| | **Tạm tính** | **19.200.000đ** | |
| | Ưu đãi đặt khám trong tuần | − 2.000.000đ | ⚠️ cần chứng từ |
| | **Sau ưu đãi** | **17.200.000đ** | |

### D. `du-lieu.json`
→ xem [`template/du-lieu.mau.json`](../template/du-lieu.mau.json).

### E. LỆNH RENDER
```bash
python tools/render_baogia.py out/BG-2026-1021-01/du-lieu.json
```

### F. CẦN NGƯỜI THẬT
```
[CHỜ XÁC NHẬN] Ưu đãi 2.000.000đ — cần số công văn/thông báo nội bộ còn hiệu lực
[ẢNH] Case CM-0423 đang để ô ảnh tạm — cần xin ảnh trong Album Kangnam
       + xác nhận văn bản đồng ý còn hiệu lực trước khi gửi khách
[NHẮC]   File này là báo giá cá nhân gửi 1-1. Nếu đem đăng công khai thì phải
       qua quy trình duyệt quảng cáo + GXNNDQC (R9)

Đo gì: tỉ lệ phản hồi · đặt khám · show-up · chốt. Ghi lại bằng /hoc sau 7 ngày.
```

---

## Phần 2 — Tool chạy trên máy

```
BÁO GIÁ BG-2026-1021-01 — Chị Thu Hà
  cổng dữ liệu  : PASS
  cổng bảng giá : PASS

[NHẮC — kiểm bằng mắt] 1 mục
  - R9    phap_ly.gxnndqc
      thấy : chưa xác nhận giấy xác nhận nội dung quảng cáo
      sửa  : báo giá cá nhân gửi 1-1 thường không phải quảng cáo đại chúng;
             nếu dùng lại làm ấn phẩm phát hành thì phải xin GXNNDQC

  HTML A4   : out\BG-2026-1021-01\BG-2026-1021-01.html
  HTML slide: out\BG-2026-1021-01\BG-2026-1021-01-slide.html  (3 slide)
  trình duyệt: C:\Program Files\Google\Chrome\Application\chrome.exe
  => PDF    : out\BG-2026-1021-01\BG-2026-1021-01.pdf  (4 trang)
  => ảnh 1..5 : out\BG-2026-1021-01\BG-2026-1021-01-0X.jpg

! Còn 1 cảnh báo cần người thật xử lý trước khi gửi khách.
```

**File ra:** 1 PDF 4 trang + 3 ảnh JPG 1080×1920 (~220–280 KB/ảnh, gửi Zalo thoải mái).

Tool đếm số trang PDF sau khi render. Vượt 4 trang → in thêm dòng:
```
! Báo giá dài 5 trang, chuẩn là 4. Rút gọn lời mở, cặp vấn đề→giải pháp hoặc bước phương án.
```
Nội dung dài **không bị cắt** — trang tự dãn. Nhưng 5 trang nghĩa là đang viết brochure chứ không phải báo giá.

---

## Phần 3 — Khi cổng chặn, output trông thế nào

Thử sửa `du-lieu.json` thành *"cam kết mắt đẹp tự nhiên 100%, bảo hành trọn đời"*, *"chị yên tâm, không đau đâu ạ"*, *"3 ngày là chị đi làm được bình thường"*, gán bác sĩ đã gỡ khỏi danh sách và gắn ảnh case chưa khai consent. Output thật:

```
[CHẶN — không xuất file] 7 mục
  - R1    giai_phap.vi_sao_hop        thấy: cam kết mắt đẹp
  - R1    giai_phap.vi_sao_hop        thấy: đẹp tự nhiên 100%
  - R1    giai_phap.vi_sao_hop        thấy: trọn đời
  - R1    giai_toa[0].tra_loi         thấy: không đau
  - KN-①  giai_phap.diem_can_luu_y[1] thấy: 3 ngày là chị đi làm
  - R4    (toàn văn)                  thấy: Jolie Huynh
                                      → không còn trên web 16/10/2026, gỡ tên khỏi báo giá
  - R5    case_tuong_tu[CM-0423]      thấy: ảnh case không khai consent

=> KHÔNG XUẤT FILE. Sửa các mục CHẶN rồi chạy lại.
```
(Output đầy đủ còn in kèm câu thay thế đúng luật cho từng mục.)

Đây là **tính năng, không phải lỗi**. Cổng chặn tồn tại vì một câu cam kết sai trong file gửi khách là rủi ro pháp lý của bệnh viện, không phải lỗi đánh máy.

---

## Phần 4 — Bản slide trông thế nào

| Ảnh | Nội dung |
|---|---|
| 1 | Bìa navy — *Gửi Chị Thu Hà* · "Đôi mắt mở hơn — mà vẫn là mắt của chị" · từng cặp **vấn đề → cách xử lý** · mã + hiệu lực |
| 2 | Card phương án + bảng chi phí + **17.200.000đ** (số lớn nhất) + đã gồm/chưa gồm |
| 3 | Case tương tự + **3 ô ảnh thật** + album + khối CTA cam + thông tin liên hệ |

Luôn đúng **3 ảnh**. Thiếu case thì ảnh 3 chỉ còn phần CTA, báo giá vẫn hợp lệ.
