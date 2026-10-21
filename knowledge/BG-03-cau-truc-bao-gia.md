# BG-03 — CẤU TRÚC MỘT TỜ BÁO GIÁ CÁ NHÂN HOÁ
Version 1.0 · Cập nhật: 2026-10-21

---

## 1. CHÍN KHỐI — thứ tự cố định, không đảo

| # | Khối | Trả lời câu hỏi ngầm của khách | Bắt buộc |
|---|---|---|---|
| 1 | **Đầu trang + mã báo giá** | "Cái này có phải gửi riêng cho mình không?" | ✔ |
| 2 | **Tiêu đề + lời mở cá nhân hoá** | "Họ có nhớ mình nói gì không?" | ✔ |
| 3 | **Điều khách đang gặp** | "Họ hiểu đúng vấn đề của mình chưa?" | ✔ |
| 3b | **Vấn đề → cách xử lý** (từng cặp) | "Cái tôi lo, họ giải quyết kiểu gì?" | ✔ *(hoặc khối 9)* |
| 4 | **Phương án bác sĩ đề xuất** | "Làm gì, vì sao là cái này?" | ✔ |
| 5 | **Chi phí dự tính** | "Bao nhiêu, gồm gì, có phát sinh không?" | ✔ |
| 6 | **Phương án khác để cân nhắc** | "Có lựa chọn nào khác không?" | nên có |
| 7 | **Trường hợp tương tự + ảnh trước–sau** | "Có ai giống mình đã làm chưa?" | nên có |
| 8 | **Lộ trình từng bước** | "Rồi sao nữa? Mất bao lâu?" | ✔ |
| 9 | **Băn khoăn + Bước tiếp theo (CTA)** | "Mình có phải quyết ngay không?" | ✔ |

Chân trang: khối **miễn trừ pháp lý** — luôn in, không bỏ dù file ngắn.

## 1b. MẠCH ĐỌC — mượn cách email bán hàng dẫn dắt, không mượn giọng

Thứ làm một email marketing tốt không phải màu mè, mà là **mạch**: gọi đúng vấn đề người đọc đang có → nói cách xử lý từng vấn đề → rồi mới tới tiền → rồi mới tới bằng chứng. Tờ báo giá đi đúng mạch đó, **nhưng giữ giọng tư vấn y khoa** — điềm tĩnh, không chào mời.

```
Trang 1  Vấn đề   — lời hứa cá nhân hoá · điều khách đang gặp · VẤN ĐỀ → CÁCH XỬ LÝ
Trang 2  Giải pháp — phương án bác sĩ đề xuất · các bước · lưu ý riêng · phương án khác
Trang 3  Chi phí   — bảng chi phí · ưu đãi · tổng · đã gồm/chưa gồm · lộ trình
Trang 4  Bằng chứng — case tương tự + ảnh trước–sau · album · CTA · chữ ký
```

⛔ Thứ **không** mượn từ email marketing: nhãn mục kiểu chào mời (*"Em hiểu đúng chưa ạ"*), giục chốt, khan hiếm giả, emoji. Xem [[BG-01-ho-so-thuong-hieu]] mục 3.

### Khối 3b — vấn đề → cách xử lý
Mỗi cặp một dòng: bên trái là **vấn đề bằng chữ của khách**, bên phải là **cách bên em xử lý đúng vấn đề đó**.

```json
"van_de_giai_phap": [
  {"van_de": "Sợ lộ sẹo mỗi khi trang điểm.",
   "giai_phap": "Đường mổ đặt đúng nếp mí nên khi mở mắt bị nếp che. Mức độ mờ sẹo tuỳ cơ địa mỗi người."}
]
```

| Luật | |
|---|---|
| Số cặp | **3–4**. Nhiều hơn là đang liệt kê, không phải tư vấn |
| Nguồn vấn đề | **chữ khách đã nói**, không phải nỗi lo chung của ngành |
| Mỗi giải pháp | nói **cơ chế thật** + **giới hạn trung thực** ([[BG-05-noi-so-phan-doi]] khuôn 3 nhịp) |
| ⛔ Trùng lặp | Khối 3b và khối 9 **không nói cùng một nỗi lo**. Có 3b rồi thì khối 9 chỉ giữ câu hỏi còn lại, hoặc bỏ hẳn |

Cổng dữ liệu đòi **ít nhất một trong hai**: `van_de_giai_phap` hoặc `giai_toa`. Có cả hai mà nói cùng một nỗi lo thì vừa loãng vừa đội thêm một trang giấy.

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
5. Đã gồm / chưa gồm

⛔ **Không có dòng trả góp** — Kangnam không có chính sách đó ([[BG-02-bang-gia]] mục 7). Khách lo tiền thì đưa phương án vừa ngân sách ở khối 6, không hứa cách thanh toán không tồn tại.

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
| PDF A4 | **4 trang**, mỗi trang một mạch | ~900–1.100 chữ. Quá 4 trang là đang viết brochure, không phải báo giá |
| JPG slide | **3 ảnh** 1080×1920 | mỗi ảnh ≤ 170 chữ. Tràn khung → tool tự thu nhỏ và cảnh báo |

Tool đếm số trang PDF và cảnh báo khi vượt 4. Ba chỗ cắt được nhiều nhất: số cặp vấn đề→giải pháp (3 là đủ) · lời mở (giữ đúng 3 câu) · số bước trong `giai_phap.gom`.

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
