# PROMPT MẪU — `/wizard` (hỏi dẫn khi chưa có gì trong tay)

Dùng khi bạn chỉ biết **tên dịch vụ** hoặc có một đoạn chat lộn xộn.
Agent hỏi **theo vòng, tối đa 3 câu mỗi vòng**, mỗi câu kèm phương án chọn sẵn và lựa chọn *"để agent chọn"*. Sau mỗi vòng nó chốt lại một dòng rồi mới hỏi tiếp.

---

## 1. Khởi động ngắn nhất
```
/wizard cắt mí
```
```
/wizard nâng mũi cho khách Gen Z
```

## 2. Khởi động từ đoạn chat thật (cách tốt nhất)
```
/wizard

Đây là đoạn chat với khách, bạn tự rút thông tin ra:

Khách: cho e hỏi cắt mí bao nhiêu tiền ạ
Em: dạ chị cho em xin ảnh mắt để bác sĩ xem giúp mình ạ
Khách: [ảnh] mắt e 1 mí, da hơi sụp xuống. e sợ đau lắm
Em: dạ bên em có gây tê ạ, chị nghỉ được mấy ngày ạ
Khách: e nghỉ đc 3-4 ngày thôi, mà e sợ lộ sẹo lúc makeup
Khách: tầm 15tr đổ lại thì có làm đc k ạ
```

## 3. Ba vòng hỏi của agent

| Vòng | Khoá cái gì | Ba câu |
|---|---|---|
| **1** | Người đọc | khách là ai (tuổi, nghề, khu vực) · nhóm 1–6 · giai đoạn |
| **2** | Nội dung báo giá | tình trạng & mong muốn (chữ của khách) · nỗi lo · ngân sách + thời điểm |
| **3** | Vật liệu & ràng buộc | cơ sở thực hiện · đã khám/đã có bác sĩ chưa · có ảnh case đủ consent chưa |

Đủ 9 ô → agent in **THÔNG TIN ĐÃ KHOÁ** rồi hỏi đúng một câu: *"Chạy `/baogia` luôn chứ?"*

## 4. Agent dừng giữa chừng trong ba trường hợp
1. Dịch vụ **đại phẫu** mà cơ sở khai không phải tuyến bệnh viện → dừng ở vòng 3, nêu hai cách xử lý rào R3.
2. Bạn khai tên bác sĩ **không có trong `bac-si-duyet.json`** hoặc đang `xung_dot` → không ghi tên đó, nói rõ lý do.
3. Bạn dán **CCCD · bệnh án · ảnh khách chưa có consent** → agent từ chối nhận và nói rõ không ghi vào file.

## 5. Thoát sớm
Gõ bất cứ lúc nào:
```
đủ rồi, cứ làm
```
→ agent dừng hỏi, giả định các ô còn lại **trừ trường pháp lý và giá**, in khối **GIẢ ĐỊNH** rồi chạy tiếp. Giá, ưu đãi, tên bác sĩ, ảnh vẫn để `[CHỜ XÁC NHẬN]`.

## 6. Khi khách mới chỉ hỏi "bao nhiêu tiền"
```
/wizard khách mới nhắn hỏi giá cắt mí, chưa nói gì thêm
```
Agent sẽ cảnh báo đây là giai đoạn **NHẬN BIẾT**, gửi báo giá đầy đủ lúc này dễ bị đem đi so giá, và đề xuất:
- hoặc trả lời khoảng chi phí + mời khám (không xuất file),
- hoặc làm **bản rút gọn**: phương án + khoảng chi phí + 1 case.

Bạn chọn một trong hai, agent làm tiếp.
