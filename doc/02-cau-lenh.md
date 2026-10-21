# 02 — TÁM LỆNH CỦA AGENT

| Lệnh | Việc agent làm | Input tối thiểu | Output |
|---|---|---|---|
| `/baogia` | **Lệnh chính** — từ thông tin khách ra báo giá | tên + nhu cầu + cơ sở | 6 mục A→F, có `du-lieu.json` + lệnh render |
| `/banggia` | **Bảng giá một nhóm dịch vụ** ra HTML — 9 nhóm, gõ `mũi` hay `nâng mũi` đều khớp | tên nhóm | 1 file HTML (hoặc PDF) |
| `/wizard` | Hỏi dẫn 3 vòng × 3 câu | **chỉ cần tên dịch vụ** | THÔNG TIN ĐÃ KHOÁ → chạy tiếp `/baogia` |
| `/tinnhan` | Tin nhắn Zalo/Messenger gửi kèm file | mã báo giá hoặc mô tả khách | 1–2 phiên bản ≤ 60 chữ |
| `/doichieu` | Soi báo giá có sẵn với `bang-gia.json` | nội dung báo giá cũ | bảng khớp/lệch + chỗ thiếu chứng từ |
| `/kiemtra` | Chạy cổng pháp lý trên chữ đã viết | đoạn văn bất kỳ | danh sách CHẶN/CẢNH/NHẮC + bản viết lại |
| `/lo` | Làm hàng loạt | danh sách khách | mỗi khách một `du-lieu.json` |
| `/hoc` | Ghi kết quả vào vòng học | kết quả từng mã BG | bảng `BG-10` được cập nhật |

Không gọi lệnh → agent tự suy và **nói rõ đã chọn lệnh nào**: có thông tin khách → `/baogia` · chỉ có tên dịch vụ → `/wizard` · có file báo giá cũ → `/doichieu` · xin *"bảng giá nhóm X"* → `/banggia`.

---

## 1b. `/banggia` — khi khách mới hỏi giá

```bash
python tools/render_banggia.py --liet-ke                 # xem có những nhóm nào
python tools/render_banggia.py "nâng mũi" --xung-ho chị  # ra HTML
python tools/render_banggia.py mũi --dinh-dang html pdf  # ra cả PDF
```

Tool lấy **đủ** dịch vụ trong nhóm từ `bang-gia.json`, in giá ưu đãi kèm giá niêm yết gạch ngang, tự thêm khối nhắc đại phẫu phải ở tuyến bệnh viện, hotline và ba câu miễn trừ.

> ⚠️ **Bảng giá cả nhóm là bước lùi so với báo giá cá nhân hoá.** Khách cầm bảng giá chung rất dễ đem đi so giá. Agent luôn kèm một câu nhắc chuyển sang `/baogia` khi đã có thông tin khách.

Mẫu prompt nói thường: [`prompts/prompt-bang-gia.md`](../prompts/prompt-bang-gia.md).

---

## 1. `/baogia` — output 6 mục

```
A. ĐỌC KHÁCH        nhóm · giai đoạn · nỗi lo        (3 dòng, để bạn xác nhận)
B. PHƯƠNG ÁN        tên + 2 câu vì sao hợp
C. BẢNG CHI PHÍ     có mã dịch vụ, tổng, ưu đãi
D. du-lieu.json     khối JSON dán được vào file
E. LỆNH RENDER      python tools/render_baogia.py out/<ma>/du-lieu.json
F. CẦN NGƯỜI THẬT   [CHỜ XÁC NHẬN] · ảnh cần xin · ưu đãi cần chứng từ
```

**Mục F là mục quan trọng nhất.** Nó liệt kê những gì agent **không được phép** tự quyết. Không đọc mục F mà gửi file đi là bỏ qua toàn bộ lớp bảo vệ.

Mẫu prompt cho 6 nhóm dịch vụ: [`prompts/prompt-bao-gia.md`](../prompts/prompt-bao-gia.md).

## 2. `/wizard` — khi chưa có gì trong tay

Ba vòng, mỗi vòng tối đa 3 câu, có phương án chọn sẵn:

| Vòng | Khoá | Ba câu |
|---|---|---|
| 1 | Người đọc | khách là ai · nhóm 1–6 · giai đoạn |
| 2 | Nội dung | tình trạng & mong muốn · nỗi lo · ngân sách + thời điểm |
| 3 | Vật liệu | cơ sở · đã khám/bác sĩ chưa · ảnh case đã có consent chưa |

Gõ *"đủ rồi, cứ làm"* bất cứ lúc nào → agent giả định các ô còn lại **trừ giá và trường pháp lý**.

Cách dùng tốt nhất: **dán nguyên đoạn chat với khách** cho agent tự rút thông tin. Xem [`prompts/prompt-wizard.md`](../prompts/prompt-wizard.md).

## 3. `/tinnhan` — đừng bỏ qua lệnh này
File báo giá không tự bán được. Tin nhắn gửi kèm quyết định khách có mở file hay không.
Luật: ≤ 60 chữ · cấu trúc *nhắc điều khách quan tâm → nói trong file có gì → một câu hỏi mở* · ⛔ không giục chốt, không khan hiếm giả.
Mẫu cho cả 6 nhóm khách: [`prompts/prompt-tin-nhan.md`](../prompts/prompt-tin-nhan.md).

## 4. `/doichieu` — bắt lỗi báo giá làm tay
Dán báo giá nhân viên đã gửi khách → agent chỉ ra dòng nào lệch bảng giá, dòng nào không có trong danh mục, "ưu đãi riêng" nào không có chứng từ.
Đây là cách rẻ nhất để biết đội tư vấn đang báo giá sai ở đâu.

## 5. `/kiemtra` — cổng pháp lý trên chữ
Dùng trước khi gửi bất cứ nội dung nào, kể cả tin nhắn.
Chạy trên dữ liệu thật bằng tool:
```
python tools/cong_phap_ly.py out/<ma>/du-lieu.json
```

## 6. `/lo` — hàng loạt, nhưng không giống nhau
Agent vẫn đổi giọng theo nhóm khách. Hai file giống hệt nhau trừ cái tên là làm sai — đó là bảng giá chung, không phải báo giá cá nhân hoá.

## 7. `/hoc` — bước duy nhất làm agent khá lên
Sau mỗi tuần, đưa kết quả thật: phản hồi · đặt khám · show-up · chốt. Agent cập nhật `BG-10` và chỉ ra mẫu lặp lại.
⛔ Không sửa luật vì **một** ca. Một ca là giai thoại, ≥ 5 ca mới là dữ liệu.

---

## 8. Lệnh render (chạy trên máy, không phải trong chat)

```bash
python tools/render_baogia.py out/<ma>/du-lieu.json                  # PDF + 6 ảnh
python tools/render_baogia.py out/<ma>/du-lieu.json --dinh-dang jpg  # chỉ ảnh Zalo
python tools/render_baogia.py out/<ma>/du-lieu.json --dinh-dang pdf  # chỉ PDF
python tools/render_baogia.py out/<ma>/du-lieu.json --chi-html       # chỉ HTML
python tools/render_baogia.py out/<ma>/du-lieu.json --nhap           # bản nháp có dấu NHÁP
python tools/render_baogia.py out/<ma>/du-lieu.json --ra D:\gui-khach   # đổi thư mục xuất
python tools/cong_phap_ly.py  out/<ma>/du-lieu.json                  # chỉ chạy cổng pháp lý
```

**Ba cổng chạy trước khi xuất, fail là không xuất file:**
```
CỔNG DỮ LIỆU   thiếu trường bắt buộc
CỔNG BẢNG GIÁ  mã sai · giá lệch không khai lý do · dịch vụ "liên hệ" bị tự đặt số
CỔNG PHÁP LÝ   từ cấm · mốc hồi phục cứng · bác sĩ sai trạng thái · ảnh thiếu consent · …
```
Bị chặn mà vẫn muốn xem bố cục → thêm `--nhap`, file ra sẽ đóng dấu **NHÁP** và **không được gửi khách**.
