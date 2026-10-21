# BG-10 — VÒNG HỌC: BÁO GIÁ NÀO CHỐT ĐƯỢC
Version 1.0 · Cập nhật: 2026-10-21

> Agent chỉ khá lên nếu kết quả thật được ghi lại. Không có file này, mỗi báo giá là một lần đoán mới.

---

## 1. BỐN CHỈ SỐ — không có chỉ số thứ năm

| Chỉ số | Đo gì | Nguồn |
|---|---|---|
| **Tỉ lệ phản hồi** | gửi file → khách nhắn lại | tư vấn viên |
| **Tỉ lệ đặt khám** | gửi file → đặt lịch khám | CRM |
| **Tỉ lệ show-up** | đặt khám → tới thật | lễ tân / ERP |
| **Tỉ lệ chốt** | tới khám → thực hiện dịch vụ | ERP |

⛔ Không tối ưu cho "file đẹp" hay "khách khen". Một tờ báo giá đẹp mà không ai đặt khám là một tờ thất bại.

## 2. BẢNG GHI — mỗi báo giá một dòng

| Mã BG | Ngày | Nhóm KH | Giai đoạn | Dịch vụ | Tổng | Kênh gửi | Phản hồi | Đặt khám | Show-up | Chốt | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(ví dụ)* BG-2026-1021-01 | 21/10 | 1 | CÂN NHẮC | cắt mí 6D | 17,2tr | Zalo | có | có | — | — | khách hỏi thêm về nghỉ làm |

> Bảng này bắt đầu trống. Điền tay sau mỗi ca, hoặc xuất từ CRM rồi dán vào.

## 3. BỐN CÂU HỎI RÀ MỖI THÁNG
1. **Nhóm khách nào chốt tốt nhất?** → ưu tiên mẫu câu của nhóm đó.
2. **Giai đoạn nào gửi báo giá hiệu quả nhất?** (giả thuyết hiện tại: CÂN NHẮC) → nếu dữ liệu nói khác, sửa [[BG-04-chan-dung-khach]] mục 3.
3. **Khối nào khách hay hỏi lại sau khi nhận file?** Khách hỏi lại = khối đó viết chưa đủ.
   - Hỏi lại về tiền → thiếu dòng *đã gồm / chưa gồm*
   - Hỏi lại về nghỉ bao lâu → khối lộ trình yếu
   - Hỏi "có thật không" → thiếu case/ảnh
4. **Báo giá nào bị đem đi so giá?** → thường do gửi quá sớm (giai đoạn NHẬN BIẾT) hoặc mở đầu bằng con số.

## 4. BA GIẢ THUYẾT ĐANG CHỜ KIỂM CHỨNG
| # | Giả thuyết | Đo bằng |
|---|---|---|
| 1 | Gửi **cả PDF + ảnh slide** chốt tốt hơn chỉ gửi một loại | so tỉ lệ phản hồi |
| 2 | Báo giá có **case tương tự kèm ảnh thật** tăng tỉ lệ đặt khám với nhóm 1, 4, 5 | so nhóm có ảnh vs ô ảnh tạm |
| 3 | Khối **"phương án khác"** làm tăng chốt (khách thấy mình được chọn) hay giảm chốt (phân vân) | A/B theo tuần |

Có số rồi thì ghi kết luận vào đây và sửa thẳng vào knowledge tương ứng.

## 5. CÁCH CẬP NHẬT KNOWLEDGE TỪ KẾT QUẢ
```
Thấy mẫu lặp lại ≥ 5 ca
   → viết thành một dòng luật trong file knowledge đúng chủ đề
   → ghi vào doc/CHANGELOG.md (ngày + lý do + dựa trên bao nhiêu ca)
   → nói cho người dùng agent biết luật mới
```
⛔ Không sửa luật vì **một** ca. Một ca là giai thoại, không phải dữ liệu.

Liên quan: [[BG-03-cau-truc-bao-gia]] · [[BG-04-chan-dung-khach]]
