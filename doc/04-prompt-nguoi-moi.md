# 04 — DÀNH CHO NGƯỜI CHƯA DÙNG AGENT BAO GIỜ

Không cần biết lập trình. Bạn chỉ cần biết **copy** và **dán**.

---

## Việc này giải quyết nỗi đau gì của bạn

| Trước | Sau |
|---|---|
| Mỗi khách hỏi giá, bạn gõ lại từ đầu, mất 20–30 phút | Dán đoạn chat vào, 2 phút có file |
| Mỗi bạn tư vấn báo một kiểu, có người báo sai giá | Mọi con số truy về một bảng giá duy nhất |
| Lỡ hứa "không đau", "3 ngày đi làm được" | Tool chặn, không cho xuất file |
| Gửi khách một bảng giá chung ai cũng như ai | File nhắc lại đúng điều khách đã nói |

---

## Ba bước đầu tiên

### Bước 1 — Mở agent
Nhờ người cài giúp theo [`01-cai-dat.md`](01-cai-dat.md), hoặc mở Claude Project đã có sẵn trong đội.

### Bước 2 — Dán đoạn chat với khách
Không cần viết gì hoa mỹ. Dán nguyên văn:

```
/wizard

Đoạn chat với khách:
Khách: cho e hỏi cắt mí bao nhiêu tiền ạ
Em: dạ chị cho em xin ảnh mắt để bác sĩ xem ạ
Khách: [ảnh] mắt e 1 mí, da hơi sụp. e sợ đau lắm
Khách: e nghỉ đc 3-4 ngày thôi, sợ lộ sẹo lúc makeup
Khách: tầm 15tr đổ lại có làm đc k ạ
```

Agent sẽ hỏi lại vài câu (tối đa 3 câu một lượt). Trả lời ngắn gọn là được. Không biết thì gõ **"để agent chọn"**.

### Bước 3 — Nhận file
Agent đưa bạn một khối JSON và một dòng lệnh. Người kỹ thuật trong đội chạy dòng lệnh đó (hoặc agent tự chạy nếu dùng trong Claude Code), ra:
- **1 file PDF** — gửi email, in, đưa khách bàn với người nhà
- **6 ảnh JPG** — gửi thẳng Zalo/Messenger

---

## Năm câu hỏi người mới hay hỏi

**1. Agent có tự bịa giá không?**
Không. Mọi dòng chi phí phải trỏ về một mã trong bảng giá. Không có mã thì nó ghi `[CHỜ XÁC NHẬN]` chứ không đoán. Nếu nó cố ghi giá lệch bảng, tool sẽ chặn không cho xuất file.

**2. Tôi lỡ gõ sai thông tin khách thì sao?**
Mục **A. ĐỌC KHÁCH** ở đầu output là để bạn kiểm. Sai thì nói *"nhóm 2 chứ không phải nhóm 1"*, agent làm lại.

**3. Agent có thay bác sĩ chẩn đoán không?**
Không, và không được phép. Mọi phương án đều ghi rõ là **đề xuất để mang tới buổi khám**, chi phí cuối do bác sĩ quyết sau khi khám.

**4. Khách đòi giá ngay trong tin nhắn đầu tiên thì sao?**
Agent sẽ cảnh báo khách đang ở giai đoạn NHẬN BIẾT — gửi báo giá đầy đủ lúc này dễ bị đem đi so giá với nơi khác. Nó đề xuất bản rút gọn. Bạn quyết định.

**5. Tôi có được sửa file sau khi agent làm xong không?**
Được, nhưng sửa xong **phải chạy lại cổng pháp lý**:
```
python tools/cong_phap_ly.py out/<ma>/du-lieu.json
```
Sửa tay rồi gửi thẳng là bỏ qua lớp bảo vệ duy nhất.

---

## Ba điều tuyệt đối không làm

1. ⛔ **Không dán CCCD, bệnh án, ảnh khách chưa xin phép** vào agent. Agent sẽ từ chối, nhưng đừng thử.
2. ⛔ **Không gửi file còn chữ NHÁP hoặc còn ô ảnh gạch chéo** cho khách.
3. ⛔ **Không đem file báo giá đi đăng Fanpage.** Lúc đó nó thành nội dung quảng cáo dịch vụ khám chữa bệnh và phải qua quy trình duyệt riêng.

---

## Bảng tra nhanh

| Bạn muốn | Gõ |
|---|---|
| Làm báo giá, đã có thông tin khách | `/baogia` + thông tin |
| Chỉ có tên dịch vụ, chưa có gì | `/wizard cắt mí` |
| Dán đoạn chat cho agent tự đọc | `/wizard` + đoạn chat |
| Viết tin nhắn gửi kèm file | `/tinnhan` |
| Kiểm một đoạn chữ có vi phạm không | `/kiemtra` + đoạn chữ |
| Soi báo giá đồng nghiệp làm tay | `/doichieu` + nội dung |
| Làm cho cả danh sách khách | `/lo` + danh sách |
| Báo kết quả tuần này | `/hoc` + kết quả từng mã |

Mẫu prompt đầy đủ: [`prompts/`](../prompts/).
