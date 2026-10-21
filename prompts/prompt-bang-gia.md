# PROMPT MẪU — `/banggia` · nói thường, không cần nhớ lệnh

Những câu dưới đây là **cách nhân viên gõ thật**, không phải cú pháp. Agent tự hiểu và tự chọn lệnh.

> ⚠️ **Bảng giá cả nhóm là bước lùi so với báo giá cá nhân hoá.** Khách cầm bảng giá chung rất dễ đem đi so giá với nơi khác. Chỉ dùng khi khách **mới hỏi**, chưa có gì để cá nhân hoá. Có thông tin khách rồi thì chuyển sang [`/baogia`](prompt-bao-gia.md) — tỉ lệ đặt khám cao hơn hẳn.

---

## 1. Câu dùng nhiều nhất

```
Tạo cho tôi bảng giá dịch vụ nâng mũi để gửi cho khách hàng bằng html
```

```
Gửi em bảng giá cắt mí
```

```
Khách hỏi giá hút mỡ bụng, cho em bảng giá nhóm đó
```

```
Bảng giá nha khoa gửi khách qua Zalo
```

## 2. Thêm chi tiết cho đúng khách

```
Bảng giá nâng mũi, xưng hô "chị", người lập Ngọc Anh — CSKH
```

```
Bảng giá trẻ hoá da gửi cô Lan, xưng hô "cô"
```

```
Bảng giá nâng ngực — nhớ ghi rõ dịch vụ nào phải làm ở tuyến bệnh viện
```

## 3. Khi khách mới nhắn hỏi giá

```
Khách vừa nhắn "cắt mí bao nhiêu tiền ạ", chưa nói gì thêm.
Em nên gửi bảng giá hay hỏi thêm rồi làm báo giá riêng?
```
→ Agent sẽ nói rõ khách đang ở giai đoạn **NHẬN BIẾT**, gợi ý hỏi thêm 2–3 câu rồi làm báo giá riêng; vẫn làm bảng giá nếu bạn muốn.

```
Gửi bảng giá cắt mí trước, rồi soạn luôn tin nhắn gửi kèm
```
→ Ra bảng giá + tin nhắn Zalo ≤ 60 chữ.

## 4. Lệnh chạy trên máy

```bash
python tools/render_banggia.py --liet-ke                 # xem có những nhóm nào
python tools/render_banggia.py "nâng mũi"                # ra HTML
python tools/render_banggia.py mũi --dinh-dang html pdf  # ra cả PDF
python tools/render_banggia.py mắt --xung-ho chị --nguoi-lap "Ngọc Anh — CSKH"
```

Tên nhóm gõ kiểu gì cũng được: `mũi` · `mui` · `nâng mũi` đều ra nhóm **Mũi**.

Chín nhóm trong bảng giá: **Mắt** (12) · **Mũi** (13) · **Khuôn mặt / Hàm** (9) · **Ngực** (10) · **Vóc dáng / Hút mỡ** (21) · **Trẻ hóa da** (6) · **Da liễu** (5) · **Nha khoa** (5) · **Spa** (1).

## 5. Bảng giá khác báo giá ở chỗ nào

| | Bảng giá nhóm | Báo giá cá nhân hoá |
|---|---|---|
| Lệnh | `/banggia` | `/baogia` |
| Đầu vào | tên nhóm dịch vụ | thông tin khách |
| Nội dung | toàn bộ dịch vụ trong nhóm | **một phương án** cho khách đó |
| Có giá không | giá niêm yết tham khảo | giá theo phương án + ưu đãi |
| File | 1 HTML (hoặc PDF) | PDF 4 trang + 3 ảnh JPG |
| Dùng khi | khách mới hỏi, chưa biết gì về khách | đã nói chuyện, biết mong muốn và nỗi lo |
| Rủi ro | khách đem đi so giá | thấp — vì nó nói về khách, không nói về giá |

## 6. Những gì tool tự lo, đừng gõ tay

- **Giá** lấy thẳng từ `bang-gia.json` — không bịa, không sót dịch vụ nào trong nhóm.
- **Ưu đãi đang chạy** tự in giá niêm yết gạch ngang kèm giá ưu đãi (vd cắt mí Plasma ~~10.000.000đ~~ → **8.000.000đ**).
- **Dịch vụ đại phẫu** tự có khối nhắc *chỉ thực hiện tại tuyến bệnh viện*.
- **Hotline** lấy từ `thong-tin-lien-he.json`.
- **Ba câu miễn trừ** luôn có ở chân trang.
- **Mục có cảnh báo** (giá chưa xác nhận, tên thương mại thuốc) → tool in ra màn hình để bạn xác nhận trước khi gửi.
