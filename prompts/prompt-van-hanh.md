# PROMPT MẪU — `/doichieu` · `/kiemtra` · `/lo` · `/hoc`

Bốn lệnh vận hành, dùng sau khi đã quen `/baogia`.

---

## 1. `/doichieu` — soi một báo giá có sẵn với bảng giá chuẩn

Dùng khi: tư vấn viên đã tự làm báo giá bằng tay, hoặc bạn nhận một file cũ và muốn biết có lệch gì không.

```
/doichieu

Báo giá nhân viên gửi khách hôm qua:
- Cắt mí 6D: 12.800.000
- Lấy mỡ mí: 5.000.000
- Nâng cung chân mày: 8.800.000
- Tổng: 26.600.000, giảm còn 23.000.000 "ưu đãi riêng cho chị"
```

Agent trả về: dòng nào khớp bảng · dòng nào lệch và lệch bao nhiêu · dòng nào không có mã trong bảng · phần "ưu đãi riêng" có chứng từ không. Đây là cách bắt lỗi báo giá tay nhanh nhất.

## 2. `/kiemtra` — chạy cổng pháp lý trên nội dung đã viết

```
/kiemtra

"Cam kết mắt đẹp tự nhiên 100%, không đau, không để lại sẹo.
Bảo hành trọn đời. 3 ngày là chị đi làm được bình thường.
Bác sĩ Jolie Huynh trực tiếp thực hiện."
```

Agent phải chỉ ra **năm lỗi CHẶN**: cam kết 100% (R1) · không đau (R1) · không để lại sẹo (R1) · bảo hành trọn đời (R1) · mốc hồi phục cứng (luật ① Kangnam) — và bác sĩ `ngung_dung` (R4). Kèm bản viết lại đúng luật.

> Đây cũng là **câu kiểm tra agent đã cài đúng chưa**. Agent bỏ sót bất kỳ lỗi nào trong số này → knowledge chưa nạp đủ.

Chạy bằng tool trên dữ liệu thật:
```
python tools/cong_phap_ly.py out/BG-2026-1021-01/du-lieu.json
```

## 3. `/lo` — làm hàng loạt

Dùng khi có danh sách khách cùng một dịch vụ (vd sau một chiến dịch quảng cáo).

```
/lo

Danh sách khách quan tâm cắt mí tuần này, tất cả ở Hà Nội,
cơ sở: Bệnh viện thẩm mỹ Kangnam Hà Nội, người lập: Ngọc Anh:

1. Chị Hà, 32t, nhóm 1, CÂN NHẮC — "mắt một mí, sợ đau, nghỉ ít ngày", NS 15tr
2. Chị Mai, 27t, nhóm 1, TÌM HIỂU — "mí lót, muốn mắt to", NS 10tr
3. Bạn Ly, 22t, nhóm 4, NHẬN BIẾT — "hỏi giá, chưa nói gì thêm"
```

Agent trả về **một `du-lieu.json` cho mỗi khách**, đánh mã lần lượt, và nói rõ khách số 3 đang ở NHẬN BIẾT nên chỉ nên gửi bản rút gọn.

Render cả loạt:
```
for /d %d in (out\BG-2026-1021-*) do python tools\render_baogia.py %d\du-lieu.json
```
(PowerShell: `Get-ChildItem out -Directory | ForEach-Object { python tools/render_baogia.py "$($_.FullName)/du-lieu.json" }`)

⛔ Hàng loạt **không có nghĩa là giống nhau**. Agent vẫn phải đổi giọng theo nhóm khách; hai file giống hệt nhau trừ cái tên là làm sai.

## 4. `/hoc` — ghi kết quả vào vòng học

```
/hoc

BG-2026-1021-01 (chị Hà, nhóm 1, cắt mí 17,2tr, Zalo): phản hồi có,
đặt khám có, tới khám có, chốt KHÔNG — khách nói để qua Tết.

BG-2026-1021-02 (chị Mai, nhóm 1, cắt mí 12,8tr): không phản hồi.

BG-2026-1021-03 (bạn Ly, nhóm 4): phản hồi, hỏi thêm về trả góp, chưa đặt khám.
```

Agent cập nhật bảng trong `BG-10-vong-hoc.md` và chỉ ra mẫu lặp lại nếu có (≥ 5 ca mới được rút thành luật — một ca là giai thoại).

## 5. Lệnh render — nhắc nhanh

```
python tools/render_baogia.py out/<ma>/du-lieu.json                  # PDF + 5 ảnh JPG
python tools/render_baogia.py out/<ma>/du-lieu.json --dinh-dang jpg  # chỉ ảnh Zalo
python tools/render_baogia.py out/<ma>/du-lieu.json --dinh-dang pdf  # chỉ PDF
python tools/render_baogia.py out/<ma>/du-lieu.json --chi-html       # chỉ dựng HTML để xem
python tools/render_baogia.py out/<ma>/du-lieu.json --nhap           # bản nháp đóng dấu NHÁP
```

Không có Chrome trong máy → đặt biến môi trường `KN_CHROME` trỏ tới `chrome.exe`, hoặc mở file HTML rồi Ctrl+P → Save as PDF.
