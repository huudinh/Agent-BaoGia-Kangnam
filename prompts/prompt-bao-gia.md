# PROMPT MẪU — `/baogia`

Copy một mẫu, thay phần trong `[...]` bằng thông tin thật. Càng nhiều **chữ nguyên văn của khách** càng cá nhân hoá được sâu.

---

## 0. Khung chung (dùng được cho mọi dịch vụ)

```
/baogia

Khách: [tên khách tự xưng], [tuổi], [khu vực], nhắn qua [Zalo/Messenger/điện thoại]
Nhóm: [1 công sở · 2 doanh nhân · 3 KOC-GenZ · 4 sinh viên · 5 khách sửa lại · 6 trung niên] (chưa rõ thì để agent đoán)
Giai đoạn: [NHẬN BIẾT / TÌM HIỂU / CÂN NHẮC / THỰC HIỆN]

Khách nói nguyên văn:
"[dán đúng chữ khách nhắn]"

Mong muốn: [3 ý ngắn]
Lo lắng: [2-3 nỗi lo khách đã nói]
Ngân sách khách nói: [khoảng tiền, hoặc "chưa nói"]
Thời điểm mong muốn: [...]
Đã tư vấn tới đâu: [đã gửi ảnh / đã khám / bác sĩ nào đã xem]
Cơ sở dự kiến: [tên bệnh viện/viện]
Người lập: [tên tư vấn viên] · Hotline: 1900 6466
```

---

## 1. Mắt — cắt mí (nhóm 1, công sở)
```
/baogia
Khách: Chị Thu Hà, 32 tuổi, Hà Nội, nhắn Zalo. Nhóm 1, giai đoạn CÂN NHẮC.
Khách nói: "Mắt chị một mí, nhìn lúc nào cũng buồn ngủ. Chị muốn mắt mở hơn
nhưng phải tự nhiên, đừng ai nhận ra. Chị nghỉ làm được ít ngày thôi."
Mong muốn: tự nhiên không lộ dấu · nghỉ ít ngày · khoảng 15 triệu
Lo lắng: sợ đau · sợ lộ sẹo khi trang điểm · sợ nghỉ làm dài
Cơ sở: Bệnh viện thẩm mỹ Kangnam Hà Nội. Người lập: Ngọc Anh — CSKH.
```

## 1b. Mắt — sửa mí bằng dao Plasma (chân dung B1, nhóm 5)
```
/baogia
Khách: Chị Vân, 35 tuổi, Hà Nội, nhắn Zalo. Nhóm 5, giai đoạn CÂN NHẮC.
Khách nói: "Chị cắt mí hơn 2 năm trước rồi, giờ nếp mờ dần, da lại che nếp,
mắt nặng như cũ. Chị muốn biết vì sao nó không giữ được, chứ làm lại
mà vẫn thế thì thôi."
Mong muốn: biết rõ nguyên nhân · nếp giữ được lâu hơn · không làm đi làm lại
Lo lắng: sợ sửa xong vẫn tái sụp · lo tốn thêm chi phí · mất niềm tin sau lần trước
Cơ sở: Bệnh viện thẩm mỹ Kangnam Hà Nội. Người lập: Ngọc Anh — CSKH.
Gửi kèm link album ảnh khách cắt mí.
```
→ Agent phải: nhận ra **chân dung B1** (`BG-11`), mở bằng **bước khám đánh giá lại**,
tách **phí sửa mí** thành dòng riêng, ghi **cả giá niêm yết 10tr và ưu đãi 8tr**,
và ⛔ không bình luận nơi khách từng làm.
Kết quả mẫu đã chạy: [`template/du-lieu.mau-sua-mi.json`](../template/du-lieu.mau-sua-mi.json).

## 1c. Mắt — chín chân dung cắt mí (tra nhanh)
Khi khách hỏi cắt mí, nói rõ chân dung để agent viết đúng khối 3–4:

| Mã | Khách mô tả thế nào | Agent phải nhớ |
|---|---|---|
| A1 | một mí, phải dán kích mí mỗi ngày | sợ làm xong "giả" |
| A2 | mắt nhỏ, khe mắt hẹp | ⛔ không hứa mắt to hơn — phải khám mới biết do da hay do cơ |
| A3 | da chùng, nhiều mỡ mí, nhìn mệt mỏi | sợ trợn, sợ sẹo |
| A4 | một bên có mí một bên không | ⛔ không hứa cân đối tuyệt đối |
| B1 | làm rồi, nếp mờ dần | muốn biết **nguyên nhân** |
| B2 | làm rồi, mí trợn, nếp quá cao | sợ sửa nữa vẫn không đẹp |
| B3 | nhiều nếp, mí lộn xộn | lo mô sẹo, dính mô |
| B4 | hai bên lệch sau phẫu thuật | sợ sửa làm ảnh hưởng thêm |
| B5 | sẹo, nếp cứng, lộ dấu | muốn biết **khả năng** cải thiện |

## 2. Mũi — nâng cấu trúc (nhóm 3, Gen Z)
```
/baogia
Khách: Bạn Linh, 24 tuổi, TP.HCM, nhắn Messenger. Nhóm 3, giai đoạn TÌM HIỂU.
Khách nói: "Em làm content nên lên hình nhiều, mũi em thấp với đầu mũi hơi to.
Em sợ làm xong cứng đơ nhìn giả. Em quay lại được sau bao lâu ạ?"
Mong muốn: dáng mũi tự nhiên lên hình đẹp · hồi phục kịp lịch quay tháng sau
Lo lắng: sợ mũi giả · sợ lộ sóng · sợ phải nghỉ quay lâu
Cơ sở: Bệnh viện thẩm mỹ Kangnam TP.HCM. Người lập: Mai — CSKH.
→ Lưu ý: khách chưa khám, cần biết độ dày da đầu mũi mới chọn được chất liệu.
```

## 3. Hàm mặt — đại phẫu (kiểm cổng R3)
```
/baogia
Khách: Chị Hương, 29 tuổi, Đà Nẵng. Nhóm 1, giai đoạn CÂN NHẮC.
Khách nói: "Chị bị hô, cười ra lợi nhiều, muốn chỉnh hàm. Chị ở Đà Nẵng,
có làm ở chỗ gần nhà được không?"
Mong muốn: khuôn mặt hài hoà · làm một lần dứt điểm
Lo lắng: sợ đại phẫu · lo chi phí · sợ phải đi xa
Cơ sở dự kiến: khách hỏi viện Kangnam Đà Nẵng.
→ Agent phải xử lý đúng rào R3: đại phẫu chỉ ở tuyến bệnh viện.
```

## 4. Ngực (nhóm 2, riêng tư)
```
/baogia
Khách: Chị M., 38 tuổi, Hà Nội, chủ doanh nghiệp. Nhóm 2, giai đoạn THỰC HIỆN.
Khách nói: "Chị muốn làm nhưng cần kín đáo, không muốn ai biết. Chị bận,
sắp xếp được 1 tuần thôi. Chị muốn bác sĩ giỏi nhất, giá không phải vấn đề."
Mong muốn: tự nhiên như thật · riêng tư tuyệt đối · bác sĩ đích danh
Lo lắng: lộ thông tin · thời gian · chất lượng
Cơ sở: Bệnh viện thẩm mỹ Kangnam Hà Nội. Người lập: Trang — CSKH VIP.
→ Lưu ý: ⛔ không nhấn khuyến mãi với nhóm này. ⛔ "giỏi nhất" không được in ra file.
```

## 5. Khách sửa lại (nhóm 5 — nhạy cảm nhất)
```
/baogia
Khách: Chị Vân, 35 tuổi. Nhóm 5, giai đoạn CÂN NHẮC.
Khách nói: "Chị làm mũi ở chỗ khác 2 năm trước, giờ bị bóng đỏ đầu mũi,
nhìn lệch. Chị sợ lắm rồi, không biết tin ai nữa."
Mong muốn: xử lý dứt điểm · được nghe thật · không bị bán thêm
Lo lắng: sợ hỏng lần nữa · sợ tốn tiền vô ích · mất niềm tin
Cơ sở: Bệnh viện thẩm mỹ Kangnam Hà Nội.
→ ⛔ Tuyệt đối không bình luận nơi cũ (rào R6). Tách riêng bước khám đánh giá lại.
```

## 6. Da liễu / trẻ hoá theo liệu trình (nhóm 6)
```
/baogia
Khách: Cô Lan, 48 tuổi, Hà Nội. Nhóm 6, giai đoạn TÌM HIỂU.
Khách nói: "Mặt cô nám hai bên gò má, da chùng xuống. Cô sợ làm xong mặt đơ,
nhìn giả tạo. Cô muốn làm từ từ thôi."
Mong muốn: trẻ hơn nhưng tự nhiên · làm theo giai đoạn
Lo lắng: sợ mặt đơ · sợ ảnh hưởng sức khoẻ · ngại làm nhiều lần
Cơ sở: Bệnh viện thẩm mỹ Kangnam Hà Nội.
→ Lưu ý: nám là điều trị theo liệu trình, giá theo lần — phải nói rõ số lần dự kiến.
```

---

## 7. Biến thể hay dùng

| Muốn gì | Thêm dòng này vào cuối prompt |
|---|---|
| Chỉ ảnh Zalo, không cần PDF | `Chỉ xuất bản slide JPG.` |
| Bản rút gọn cho khách mới hỏi | `Khách mới hỏi lần đầu — làm bản rút gọn, chỉ khoảng chi phí.` |
| Có ảnh case sẵn | `Ảnh case: anh/truoc-01.jpg và anh/sau-01.jpg, chụp sau 1 tháng, đã có consent.` |
| Đang có ưu đãi | `Ưu đãi tháng 10 đã duyệt: giảm 2 triệu khi đặt khám trước 04/11. (CV số ...)` |
| Khách nói ngân sách thấp hơn phương án | `Ngân sách khách chỉ 8 triệu — đưa phương án trong tầm và nói rõ khác biệt.` |
| Không chắc nhóm khách | `Chưa rõ nhóm khách — agent tự đoán và nói rõ đoán theo dấu hiệu nào.` |

## 8. Câu kiểm tra agent đã cài đúng
> Gõ: *"/baogia — khách muốn nâng ngực ở viện Kangnam Cần Thơ, ngân sách 50 triệu."*
>
> Agent **phải dừng lại** và nói nâng ngực là đại phẫu, chỉ thực hiện ở tuyến bệnh viện, phải ghi rõ *tư vấn/đặt khám tại viện — phẫu thuật tại bệnh viện*.
> Nếu nó vui vẻ dựng báo giá → knowledge chưa nạp hoặc instructions dán thiếu.
