# BG-03 — CẤU TRÚC MỘT TỜ BÁO GIÁ CÁ NHÂN HOÁ
Version 1.0 · Cập nhật: 2026-10-21

---

## 1. CHÍN KHỐI — thứ tự cố định, không đảo

| # | Khối | Trả lời câu hỏi ngầm của khách | Bắt buộc |
|---|---|---|---|
| 1 | **Đầu trang + mã báo giá** | "Cái này có phải gửi riêng cho mình không?" | ✔ |
| 2 | **Tiêu đề + lời mở cá nhân hoá** | "Họ có nhớ mình nói gì không?" | ✔ |
| 3 | **Điều khách đang mong muốn** | "Họ hiểu đúng vấn đề của mình chưa?" | ✔ |
| 4 | **Phương án bác sĩ đề xuất** | "Làm gì, vì sao là cái này?" | ✔ |
| 5 | **Chi phí dự tính** | "Bao nhiêu, gồm gì, có phát sinh không?" | ✔ |
| 6 | **Phương án khác để cân nhắc** | "Có lựa chọn nào khác không?" | nên có |
| 7 | **Trường hợp tương tự + ảnh trước–sau** | "Có ai giống mình đã làm chưa?" | nên có |
| 8 | **Lộ trình từng bước** | "Rồi sao nữa? Mất bao lâu?" | ✔ |
| 9 | **Băn khoăn + Bước tiếp theo (CTA)** | "Mình có phải quyết ngay không?" | ✔ |

Chân trang: khối **miễn trừ pháp lý** — luôn in, không bỏ dù file ngắn.

## 2. LUẬT NỀN — bốn điều

**① Cá nhân hoá nằm ở khối 2–3–4, không nằm ở việc điền tên khách.**
Thay tên vào mẫu chung thì vẫn là bảng giá chung. Cá nhân hoá thật = nhắc lại **đúng chữ khách đã nói** (mong muốn, nỗi lo, ràng buộc về thời gian/ngân sách) rồi gắn phương án vào đó.

**② Giá đứng sau lý do, không bao giờ đứng trước.**
Khối 5 chỉ xuất hiện sau khi khối 4 đã giải thích vì sao phương án này hợp. Tờ báo giá mở đầu bằng con số là tờ báo giá bị so sánh với tờ của nơi khác.

**③ Không chẩn đoán, không chốt giá thay bác sĩ.**
Mọi phương án đều là **đề xuất để mang tới buổi khám**. Chữ dùng: *"bác sĩ sẽ xác nhận sau khi khám"*, không phải *"chị cần làm X"*.

**④ CTA của báo giá là ĐẶT KHÁM, không phải CHỐT CỌC.**
Bước tiếp theo luôn là một việc nhỏ, miễn phí, có thể rút lui: chọn khung giờ khám. Xin cọc qua file báo giá là tự bắn vào chân.

## 2b. BỐN DẤU HIỆU CÁ NHÂN HOÁ — thiếu một là tờ báo giá tụt về bảng giá chung

| # | Dấu hiệu | Ở đâu | Tool/template lo phần nào |
|---|---|---|---|
| 1 | **Lời chào đích danh viết tay** — *"Gửi chị Thu Hà,"* | ngay trên tiêu đề trang 1 và bìa slide | template tự dựng từ `khach.ten_hien_thi` |
| 2 | **Nhắc lại đúng chữ khách nói** | khối 3, và câu *vì sao hợp* ở khối 4 | agent phải viết — không ai viết hộ được |
| 3 | **Lý do phương án này hợp với khách NÀY** | khối 4 | agent viết |
| 4 | **Chữ ký người tư vấn** — *"Đồng hành cùng chị — Ngọc Anh"* | cuối trang 3 | template tự dựng từ `meta.nguoi_lap` |

Dấu hiệu 1 và 4 là **hình thức** — template lo. Dấu hiệu 2 và 3 là **nội dung** — và đó mới là thứ quyết định.
Một tờ báo giá có đủ lời chào đích danh, chữ ký tay, mà phần *vì sao hợp* viết chung chung kiểu *"đây là phương án được nhiều khách lựa chọn"* thì **vẫn là bảng giá chung có điền tên**.

**Phép thử:** che tên khách và ba dòng meta đi. Nếu tờ báo giá vẫn gửi được cho một khách khác cùng dịch vụ mà không phải sửa chữ nào → **chưa cá nhân hoá**, làm lại khối 3 và khối 4.

## 3. KHỐI 2 — lời mở, công thức 3 câu
```
Câu 1  Nhắc lại bối cảnh:   "Em tổng hợp lại những gì chị chia sẻ hôm qua..."
Câu 2  Nói rõ đây là gì:    "...thành một phương án cụ thể kèm chi phí dự tính."
Câu 3  Hạ áp lực:           "Đây là báo giá tham khảo riêng cho trường hợp của chị."
```
⛔ Không mở bằng *"Kangnam là bệnh viện thẩm mỹ hàng đầu..."* — khách không cần profile, khách cần câu trả lời.

## 4. KHỐI 4 — phương án, công thức
```
Tên phương án           ngắn, đọc là hiểu làm gì
Vì sao hợp với khách    nối thẳng vào tình trạng khách đã mô tả — đây là phần đắt giá nhất
2–4 bước thành phần     mỗi bước 1 dòng: làm gì + lợi ích cho khách
Lưu ý riêng             điều bác sĩ cần xác nhận khi khám + mốc hồi phục dạng khoảng
```

## 5. KHỐI 5 — chi phí, thứ tự dòng
1. Hạng mục chính (dịch vụ lõi)
2. Hạng mục đi kèm (làm cùng thì, tiết kiệm cho khách)
3. Ưu đãi — ghi rõ điều kiện và hạn
4. **Chi phí dự tính sau ưu đãi** — số to nhất trên trang
5. Trả góp (nếu có chính sách thật)
6. Đã gồm / chưa gồm

## 6. KHỐI 7 — case tương tự
Chọn case **giống khách**, không phải case đẹp nhất. Tiêu chí khớp, theo thứ tự ưu tiên:
tình trạng ban đầu → độ tuổi/nghề → ràng buộc (thời gian nghỉ, ngân sách) → cơ sở thực hiện.

Chưa có ảnh đủ điều kiện → **để ô ảnh tạm**, không bỏ khối, không dùng ảnh stock/AI. Chi tiết: [[BG-06-proof-case]].

## 7. KHỐI 9 — băn khoăn
Lấy **đúng 2–3 nỗi lo khách đã nói**, không bê nguyên FAQ chung. Mỗi câu trả lời theo khuôn:
> thừa nhận nỗi lo → nói cơ chế xử lý thật → nêu giới hạn trung thực ("tùy cơ địa", "bác sĩ đánh giá khi khám").

Thư viện câu trả lời theo rào cản: [[BG-05-noi-so-phan-doi]].

## 8. ĐỘ DÀI
| Bản | Khổ | Dung lượng chữ |
|---|---|---|
| PDF A4 | 3 trang | ~700–900 chữ. Quá 3 trang là đang viết brochure, không phải báo giá |
| JPG slide | 5 ảnh 1080×1920 | mỗi ảnh ≤ 120 chữ. Tràn khung → tool tự thu nhỏ và cảnh báo |

## 9. TỰ KIỂM TRƯỚC KHI RENDER — 9 ô
```
☐ Khối 3 có ít nhất 2 chi tiết chỉ đúng với khách này
☐ Khối 4 nối thẳng vào tình trạng ở khối 3
☐ Che tên khách đi vẫn KHÔNG gửi được cho khách khác (phép thử mục 2b)
☐ Mọi dòng chi phí có mã trỏ về bang-gia.json
☐ Có dòng đã gồm / chưa gồm
☐ Mốc thời gian đều dạng khoảng + "tùy cơ địa mỗi người"
☐ Tên bác sĩ (nếu có) ở trạng thái duyet
☐ CTA là đặt khám, không phải chuyển cọc
☐ Mỗi trang chỉ có MỘT thứ to nhất (BG-08 mục 1c)
```

Liên quan: [[BG-01-ho-so-thuong-hieu]] · [[BG-02-bang-gia]] · [[BG-09-schema-du-lieu]]
