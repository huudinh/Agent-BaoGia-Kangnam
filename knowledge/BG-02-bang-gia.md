# BG-02 — BẢNG GIÁ & LUẬT NÓI VỀ TIỀN
Version 1.1 · Nguồn số: `template/bang-gia.json` — **đã đối chiếu trực tiếp với web `/bang-gia/` ngày 2026-10-21**
Cập nhật: 2026-10-21

---

## 1. MỘT NGUỒN GIÁ DUY NHẤT

```
template/bang-gia.json   ← nguồn đúng duy nhất cho mọi con số trong báo giá
```

**Luật tối thượng: agent không được tự tạo dịch vụ, không được tự đặt giá.**
Mỗi dòng chi phí trong `du-lieu.json` phải có trường `ma` trỏ về một mục trong bảng. Tool `render_baogia.py` chạy **CỔNG BẢNG GIÁ** trước khi xuất file: mã không có trong bảng → **không xuất**.

Khách hỏi dịch vụ không có trong bảng → trả lời *"Mục này em cần xác nhận lại chi phí với bệnh viện rồi gửi chị ngay"*, **không đoán**.

## 2. BỐN KIỂU GIÁ TRONG BẢNG

| `kieu` | Nghĩa | Cách ghi trong báo giá |
|---|---|---|
| `co_dinh` | Giá niêm yết một mức | Ghi đúng số đó |
| `khoang` | Có dải (vd nám 4,4–5,6tr/lần) | Ghi dải, nói rõ yếu tố quyết định nằm ở đâu trong dải |
| `tu_` | "Từ X" (implant, răng sứ…) | Ghi *từ X*, ⛔ không ghi thành giá chốt |
| `lien_he` | Web ghi Liên hệ (spa) | ⛔ Không tự đặt số. Ghi *liên hệ để được báo giá* |

## 2b. ƯU ĐÃI ĐANG HIỆU LỰC — trường `uu_dai_hien_hanh`
Một số dịch vụ có **giá niêm yết** và **giá ưu đãi đang chạy**, cả hai đều nằm trong bảng:

```json
{"ma": "mat.cat-mi-plasma", "gia_min": 10000000, "uu_dai_hien_hanh": 8000000,
 "nguon_uu_dai": "Chính sách giá cắt mí Plasma, cập nhật 2026-10-21"}
```

| Luật | |
|---|---|
| Báo theo giá ưu đãi | hợp lệ, **không cần** khai `ly_do_lech` — cổng bảng giá chấp nhận cả hai mức |
| In ra báo giá | **ghi cả hai số**: niêm yết gạch ngang + ưu đãi. Tool tự in khi `gia` = `uu_dai_hien_hanh` |
| Hết hạn ưu đãi | sửa `bang-gia.json` (gỡ `uu_dai_hien_hanh`), không sửa lẻ từng báo giá |
| Số thứ ba | ⛔ không có. Giá nào khác hai số này phải khai `ly_do_lech` |

**Đang áp dụng:** cắt mí Plasma — niêm yết **10.000.000đ**, ưu đãi **8.000.000đ**. Khách sửa mí cộng thêm `mat.phi-sua-mi` (niêm yết 3.000.000đ, giảm 40–50% tuỳ khu vực → thực thu 1.500.000–1.800.000đ, tổng dự kiến **9,5–9,8 triệu**). Chi tiết và cách viết: [[BG-11-noi-dau-cat-mi]] mục 4.

## 3. GIÁ LỆCH BẢNG — khi nào được phép
Giá trong báo giá khác giá niêm yết **chỉ khi** có lý do thật và được ghi ra:

```json
{"ma": "mat.cat-mi-6d", "gia": 10800000, "ly_do_lech": "Ưu đãi tháng 10 đã duyệt — CV số ..."}
```

Không khai `ly_do_lech` → cổng bảng giá chặn. Ba lý do hợp lệ:
1. **Ưu đãi có văn bản** của tháng (nguồn: K7 chiến dịch tháng / thông báo nội bộ).
2. **Giá gói combo** đã được duyệt riêng.
3. **Bệnh viện cập nhật bảng giá mới** → lúc đó phải cập nhật `bang-gia.json` trước, không sửa lẻ từng báo giá.

⛔ Tuyệt đối không "giảm giá cho chị vì chị dễ thương" — giảm giá không nguồn là rủi ro vận hành, không phải kỹ năng bán hàng.

## 4. CẢNH BÁO ĐANG CÓ TRONG BẢNG (phải hỏi lại trước khi báo)
- **Cắt mí Plasma — lệch nguồn.** Web `/bang-gia/` niêm yết **8.000.000đ**; chính sách nội bộ 21/10/2026 ghi niêm yết **10.000.000đ** + ưu đãi **8.000.000đ**. Khách trả 8.000.000đ ở cả hai cách hiểu, nhưng **chỉ in giá gạch ngang 10.000.000đ khi Vận hành xác nhận** mức niêm yết đó — in một mức giảm giá không có thật là rủi ro.
- **Phí sửa mí** — mức giảm 40–50% **tuỳ khu vực**. Xác nhận với cơ sở thực hiện trước khi chốt con số; chưa xác nhận thì ghi khoảng 1.500.000–1.800.000đ kèm `[CHỜ XÁC NHẬN]`.
- **Lipo mini nhiều vùng 18.000.000đ** rẻ hơn **mini 1 vùng 34.000.000đ** — nghi lệch dữ liệu.

> ✅ Đã đóng: nghi vấn giá cắt mí Plasma **7.200.000đ** (meta website cũ) — web `/bang-gia/` ngày 21/10/2026 ghi 8.000.000đ, không còn con số 7,2tr.

Ba mục trên mang cờ `canh_bao` trong JSON; cổng sẽ nhắc. Báo giá cho khách → **xác nhận với bệnh viện trước**.

## 5. GIÁ ĐÃ GỒM / CHƯA GỒM — luôn phải ghi
Khách không sợ đắt, khách sợ **phát sinh**. Mỗi báo giá phải có một dòng dạng:

> *Chi phí đã gồm khám, phòng mổ, vật tư và các lần tái khám theo lịch. Chưa gồm xét nghiệm tiền phẫu nếu bác sĩ chỉ định thêm.*

Chưa chắc hạng mục nào nằm trong giá → ghi **"cần xác nhận"**, không im lặng, cũng không hứa gồm.

## 6. BA CÂU BẮT BUỘC CỦA MỌI BÁO GIÁ
1. *"Giá niêm yết tham khảo tại thời điểm lập báo giá."*
2. *"Chi phí cuối cùng do bác sĩ quyết định sau khi thăm khám trực tiếp."*
3. *"Kết quả thẩm mỹ phụ thuộc cơ địa từng người."*

Template đã in sẵn; nếu sửa `phap_ly.mien_tru` thì vẫn phải giữ đủ ba ý — cổng pháp lý kiểm câu 3.

## 7. ⛔ KANGNAM KHÔNG CÓ TRẢ GÓP

**Kangnam không có chính sách trả góp.** Không nêu trả góp, không "chia nhỏ theo tháng", không "trả theo kỳ", không gợi ý thẻ tín dụng trả dần — dưới mọi cách diễn đạt.

Hứa một cách thanh toán không tồn tại là thứ khách phát hiện ra **sau khi đã tới viện**: lúc đó mất cả niềm tin lẫn ca khách. Đó là sai thông tin, không phải cách nói hay.

Hai tầng chặn: cổng dữ liệu bắt trường `chi_phi.tra_gop`, cổng pháp lý bắt chữ *trả góp / chia nhỏ nhiều kỳ / trả theo tháng* trong văn bản (rào `KN-②`). Cả hai đều **CHẶN**, không xuất file.

**Khách lo chi phí thì làm gì?** Ba cách thật, không cần chính sách nào:
1. **Ghi rõ từng khoản** — khách sợ phát sinh hơn sợ đắt (mục 5).
2. **Đưa phương án vừa ngân sách** ở khối *Phương án khác*, nói thẳng khác biệt.
3. **Chia lộ trình theo giai đoạn điều trị** — làm phần ảnh hưởng nhiều nhất trước. Đây là chia **việc**, không phải chia **tiền**.

## 8. CÁCH NÓI VỀ TIỀN THEO NHÓM KHÁCH (chi tiết ở [[BG-04-chan-dung-khach]])
| Nhóm | Neo giá trị vào đâu |
|---|---|
| 1 · công sở, tích góp | An toàn · bảo hành · không phát sinh · chia lộ trình theo giai đoạn |
| 2 · doanh nhân | Riêng tư · bác sĩ đích danh · thời gian được tôn trọng. ⛔ không nhấn khuyến mãi |
| 3 · KOC/Gen Z | Kết quả lên hình · lịch hồi phục khớp lịch quay |
| 4 · sinh viên, mới đi làm | Minh bạch từng khoản · phương án vừa túi · ⛔ không đẩy gói cao |
| 5 · khách sửa lại | Chi phí xử lý phần hỏng nằm riêng một dòng, không gộp để che |
| 6 · trung niên trẻ hoá | Lộ trình nhiều mốc · chi phí theo giai đoạn thay vì một cục |

## 9. CẬP NHẬT BẢNG GIÁ

**Đối chiếu với web trước, đừng sửa tay:**
```bash
python tools/doi_chieu_gia_web.py          # tải https://benhvienthammykangnam.com.vn/bang-gia/ rồi so
python tools/doi_chieu_gia_web.py --ghi    # lấy giá web ghi đè các mục LỆCH GIÁ
```
Tool khớp tên theo **độ trùng từ** (ghép cặp tốt nhất toàn cục), nên web đổi cách viết tên vẫn nhận ra. Tên web khác hẳn thì khai `ten_web` trong JSON để lần sau khớp tuyệt đối.
⛔ Không có `--ghi` thì tool **không tự sửa giá** — giá là thứ đi thẳng vào túi khách, không để máy đổi sau lưng người.

**Kết quả lần đối chiếu 2026-10-21:** 86 dòng trên web · **85 khớp · 0 lệch giá** · 1 mục lệch nguồn (cắt mí Plasma, xem mục 4) · `mat.phi-sua-mi` là chính sách nội bộ, web không đăng.

Khi bệnh viện đổi giá:
1. Sửa `template/bang-gia.json` (mục `cap_nhat` ghi ngày mới).
2. Ghi lại thay đổi vào `doc/CHANGELOG.md`.
3. Các báo giá **đã gửi** vẫn giữ nguyên giá trong hiệu lực đã ghi — không gửi lại báo giá sửa giá ngầm.

Liên quan: [[BG-07-cong-phap-ly]] · [[BG-09-schema-du-lieu]] · [[BG-03-cau-truc-bao-gia]]
