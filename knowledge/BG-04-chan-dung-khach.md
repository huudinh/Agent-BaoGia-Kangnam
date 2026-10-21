# BG-04 — CHÂN DUNG KHÁCH & GIAI ĐOẠN — ĐIỀU CHỈNH BÁO GIÁ THEO AI ĐỌC
Version 1.0 · Nguồn: `Kangnam-Agent-Factory/knowledge/K2-khach-hang.md` · `K3-hanh-vi-trang-thai.md`
Cập nhật: 2026-10-21

---

## 1. INSIGHT GỐC — bắt đầu mọi báo giá từ đây
> *"Tôi muốn thay đổi ngoại hình để tự tin hơn, nhưng chỉ sẵn sàng thực hiện khi thật sự tin tưởng vào bác sĩ, quy trình và kết quả."*

Thứ tự bất biến: **giải quyết nỗi đau → tăng niềm tin → rồi mới CTA.** Báo giá đi ngược thứ tự này sẽ bị đọc như tờ rơi.

**Ba câu hỏi ngầm phải trả lời đúng cái lo thật:**
| Khách hỏi | Thật ra đang hỏi | Trong báo giá phải có |
|---|---|---|
| "Có đau không?" | *Tôi có chịu nổi không?* | Phác đồ giảm đau, mô tả cảm giác thật |
| "Bao lâu thì đẹp?" | *Khi nào tôi đi làm lại được?* | Mốc hồi phục dạng khoảng + xếp lịch theo công việc khách |
| "Bao nhiêu tiền?" | *Có đáng với số tiền đó không?* | Giá đứng sau phần giải thích giá trị |

## 2. SÁU NHÓM KHÁCH — chỉnh gì trong báo giá

| # | Nhóm | Tuổi | Nỗi đau chính | Báo giá phải nhấn | ⛔ Tránh |
|---|---|---|---|---|---|
| 1 | Công sở & tích góp | 25–45 | Tích góp mới làm được; sợ rủi ro; sợ ảnh hưởng công việc | An toàn, bảo hành rõ, không phát sinh, chia lộ trình theo giai đoạn | Giục chốt, giá "sốc" |
| 2 | Doanh nhân / thu nhập cao | 35–55 | Sợ lộ dấu phẫu thuật; cần riêng tư | Bác sĩ đích danh, lịch riêng, cá nhân hoá tối đa, câu chữ tinh gọn | Khuyến mãi, so sánh giá |
| 3 | KOC/KOL, Gen Z | 20–30 | Sợ lỗi trend, xấu khi lên hình, hồi phục lâu | Kết quả lên hình, lịch hồi phục khớp lịch quay, mô phỏng trước | Giọng già, dài dòng |
| 4 | Sinh viên / mới đi làm | 18–25 | Thu nhập thấp; sợ mua hớ; sợ đau | Minh bạch từng khoản, phương án vừa túi, feedback thật | Đẩy gói cao, gây FOMO |
| 5 | Khách sửa lại (hỏng nơi khác) | 28–50 | Ám ảnh thất bại; kiệt niềm tin | Bước **khám đánh giá lại** đứng riêng, chi phí xử lý phần hỏng tách dòng, giọng lắng nghe | ⛔ Phán xét nơi cũ (rào R6) |
| 6 | Trung niên trẻ hoá | 40–55+ | Lão hóa lộ rõ; sợ mặt đơ, sợ rủi ro sức khỏe | Tự nhiên, kín đáo, lộ trình nhiều mốc, chi phí theo giai đoạn | Ngôn ngữ trẻ hoá quá đà |

> Nhóm 4 có thể là **vị thành niên** → giữ nội dung phù hợp lứa tuổi, hướng có người giám hộ, **không nạp tuổi/DOB thật vào công cụ**.

## 3. SÁU GIAI ĐOẠN — quyết định báo giá có nên gửi chưa

| Giai đoạn | Nhiệt | Tín hiệu | Báo giá nên là gì |
|---|---|---|---|
| **NHẬN BIẾT** | Cold | Hỏi chung, hỏi giá ngay câu đầu | ⚠️ **Chưa gửi báo giá đầy đủ.** Trả lời câu hỏi + mời khám. Gửi sớm = bị đem đi so giá |
| **TÌM HIỂU** | Warm | Hỏi phương pháp, bác sĩ, before-after | Bản rút gọn: phương án + khoảng chi phí + 1 case |
| **CÂN NHẮC & NỖI SỢ** | Warm→Hot | Hỏi đau/rủi ro/bảo hành/"để hỏi người nhà" | ✅ **Đúng lúc nhất.** Bản đầy đủ, khối băn khoăn làm nặng |
| **THỰC HIỆN** | Hot | Hỏi lịch, địa chỉ, cho SĐT | Bản đầy đủ + lộ trình + khung giờ khám cụ thể |
| **HẬU PHẪU** | Existing | Sau làm, hỏi chăm sóc | Không báo giá; chuyển hướng dẫn hậu phẫu |
| **GẮN BÓ** | LTV | Quay lại, giới thiệu người quen | Báo giá cross-sell, nhắc lịch sử đã làm (⛔ không in tình trạng sức khoẻ) |

**Luật:** khách ở **NHẬN BIẾT** mà đòi báo giá → agent vẫn làm được bản rút gọn, nhưng phải nói rõ trong lời mở rằng đây là khoảng tham khảo và chỉ chốt được sau khám. Ghi trạng thái này vào `khach.giai_doan` để người vận hành biết.

## 4. RÀO CẢN → MÃ L6 (nối với CRM)
Thiếu tự tin · sợ đau **L6.5** · sợ biến chứng/kết quả không tự nhiên **L6.5** · không biết chọn cơ sở uy tín **L6.2** · lo chi phí **L6.3** · chưa sắp xếp thời gian **L6.4** · cần hỏi người thân **L6.6** · chưa thấy minh chứng.

Mỗi rào cản có cách xử lý riêng trong [[BG-05-noi-so-phan-doi]]. Báo giá chỉ nên gỡ **đúng 2–3 rào cản khách thật sự nêu** — gỡ hết mọi rào cản là tự tạo nỗi lo khách chưa có.

## 5. CROSS-SELL (chỉ với khách Existing/LTV)
Cắt mí → trẻ hoá da / nâng mũi · Nâng mũi → cắt mí / độn cằm / trẻ hoá · Điều trị da → tiêm trẻ hoá / căng da / chăm sóc định kỳ.
⛔ Không nhét cross-sell vào báo giá của khách lần đầu — làm loãng quyết định chính.

Liên quan: [[BG-05-noi-so-phan-doi]] · [[BG-03-cau-truc-bao-gia]] · [[BG-02-bang-gia]]
