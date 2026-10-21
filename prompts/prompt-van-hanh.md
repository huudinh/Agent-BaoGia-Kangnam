# PROMPT MẪU — `/doichieu` · `/kiemtra` · `/lo` · `/hoc`

Bốn lệnh vận hành, dùng sau khi đã quen `/baogia`.

---

## 1. `/doichieu` — soi một báo giá có sẵn với bảng giá chuẩn

Dùng khi: tư vấn viên đã tự làm báo giá bằng tay, hoặc bạn nhận một file cũ và muốn biết có lệch gì không.

```
/doichieu

Báo giá nhân viên gửi khách hôm qua:
- Cắt mí 6D: 12.800.000
- Lấy mỡ mí: 5.000.000
- Nâng cung chân mày: 8.800.000
- Tổng: 26.600.000, giảm còn 23.000.000 "ưu đãi riêng cho chị"
```

Agent trả về: dòng nào khớp bảng · dòng nào lệch và lệch bao nhiêu · dòng nào không có mã trong bảng · phần "ưu đãi riêng" có chứng từ không. Đây là cách bắt lỗi báo giá tay nhanh nhất.

## 2. `/kiemtra` — chạy cổng pháp lý trên nội dung đã viết

```
/kiemtra

"Cam kết mắt đẹp tự nhiên 100%, không đau, không để lại sẹo.
Bảo hành trọn đời. 3 ngày là chị đi làm được bình thường.
Bác sĩ Jolie Huynh trực tiếp thực hiện."
```

Agent phải chỉ ra **năm lỗi CHẶN**: cam kết 100% (R1) · không đau (R1) · không để lại sẹo (R1) · bảo hành trọn đời (R1) · mốc hồi phục cứng (luật ① Kangnam) — và bác sĩ `ngung_dung` (R4). Kèm bản viết lại đúng luật.

> Đây cũng là **câu kiểm tra agent đã cài đúng chưa**. Agent bỏ sót bất kỳ lỗi nào trong số này → knowledge chưa nạp đủ.

Chạy bằng tool trên dữ liệu thật:
```
python tools/cong_phap_ly.py out/BG-2026-1021-01/du-lieu.json
```

## 3. `/lo` — làm hàng loạt

Dùng khi có danh sách khách cùng một dịch vụ (vd sau một chiến dịch quảng cáo).

```
/lo

Danh sách khách quan tâm cắt mí tuần này, tất cả ở Hà Nội,
cơ sở: Bệnh viện thẩm mỹ Kangnam Hà Nội, người lập: Ngọc Anh:

1. Chị Hà, 32t, nhóm 1, CÂN NHẮC — "mắt một mí, sợ đau, nghỉ ít ngày", NS 15tr
2. Chị Mai, 27t, nhóm 1, TÌM HIỂU — "mí lót, muốn mắt to", NS 10tr
3. Bạn Ly, 22t, nhóm 4, NHẬN BIẾT — "hỏi giá, chưa nói gì thêm"
```

Agent trả về **một `du-lieu.json` cho mỗi khách**, đánh mã lần lượt, và nói rõ khách số 3 đang ở NHẬN BIẾT nên chỉ nên gửi bản rút gọn.

Render cả loạt:
```
for /d %d in (out\BG-2026-1021-*) do python tools\render_baogia.py %d\du-lieu.json
```
(PowerShell: `Get-ChildItem out -Directory | ForEach-Object { python tools/render_baogia.py "$($_.FullName)/du-lieu.json" }`)

⛔ Hàng loạt **không có nghĩa là giống nhau**. Agent vẫn phải đổi giọng theo nhóm khách; hai file giống hệt nhau trừ cái tên là làm sai.

## 4. `/hoc` — ghi kết quả vào vòng học

```
/hoc

BG-2026-1021-01 (chị Hà, nhóm 1, cắt mí 17,2tr, Zalo): phản hồi có,
đặt khám có, tới khám có, chốt KHÔNG — khách nói để qua Tết.

BG-2026-1021-02 (chị Mai, nhóm 1, cắt mí 12,8tr): không phản hồi.

BG-2026-1021-03 (bạn Ly, nhóm 4): phản hồi, hỏi thêm về trả góp, chưa đặt khám.
```

Agent cập nhật bảng trong `BG-10-vong-hoc.md` và chỉ ra mẫu lặp lại nếu có (≥ 5 ca mới được rút thành luật — một ca là giai thoại).

## 4b. Lấy file PDF khi KHÔNG có Python trên máy (ChatGPT · Gemini)

Tool render cần **Python + Chrome**. Sandbox của ChatGPT **không có Chrome**, nên ở đó không dựng thẳng ra PDF được — nhưng dựng được **file HTML tự đứng một mình** (logo đã nhúng sẵn, không tham chiếu file ngoài), mở bằng trình duyệt rồi in ra PDF là xong.

| Máy của bạn | Cách lấy file |
|---|---|
| **Có Python + Chrome** | `render_baogia.py` → PDF 3 trang + 5 ảnh JPG. Đầy đủ nhất |
| **Chỉ có Chrome, không có Python** | Nhờ ChatGPT dựng HTML bằng `baogia-1file.py` → mở bằng Chrome → Ctrl+P ra PDF |
| **Không cài được gì** | Như trên; mở HTML trên điện thoại cũng đọc được, trang tự co |

### Trên ChatGPT — upload **một file duy nhất**, không phải cả ZIP

`tools/baogia-1file.py` (156 KB) gói sẵn **mọi thứ** cần để dựng báo giá: tool render, cổng pháp lý, hai template, bảng giá, danh sách bác sĩ, hotline và logo. Lúc chạy nó tự bung ra thư mục tạm rồi gọi đúng `render_baogia.py` của repo — **không chép lại logic**, nên không bao giờ lệch với bản gốc.

**Chuẩn bị một lần:** bật **Code Interpreter** cho GPT, rồi upload `baogia-1file.py` vào phần **Knowledge**.
Tải riêng file này: `github.com/huudinh/Agent-BaoGia-Kangnam` → `tools/baogia-1file.py` → nút **Download raw file**.

**Mỗi lần làm báo giá, gõ:**

```
Ghi khối JSON dưới đây vào du-lieu.json (UTF-8, giữ nguyên dấu tiếng Việt),
rồi chạy:

    python baogia-1file.py du-lieu.json --chi-html

Dán nguyên phần tool in ra cho em xem, nhất là ba dòng cổng. Có dòng CHẶN thì
dừng lại, đừng đưa file. Không có thì cho em tải hai file HTML.

du-lieu.json:
[dán khối JSON agent vừa sinh ra vào đây]
```

Nếu `baogia-1file.py` không tự có trong sandbox thì kẹp nó vào ngay đoạn chat đó — vẫn chỉ một file.

`--chi-html` là phần quan trọng: nó trả về **trước** bước tìm Chrome nên chạy được ở nơi không có trình duyệt. **Ba cổng chặn vẫn chạy đủ** — không vì đổi cách xuất mà mất lớp bảo vệ.

### Mở HTML rồi in ra PDF — hai thiết lập bắt buộc

Mở file `.html` bằng Chrome hoặc Edge → **Ctrl+P**:

| Thiết lập | Chọn | Không chọn thì sao |
|---|---|---|
| **Lề** (Margins) | **Không** (None) | Lề mặc định đẩy nội dung tràn thành 4–5 trang |
| **Đồ hoạ nền** (Background graphics) | **Bật** | Mất hết khối navy: dải tổng chi phí và khối CTA thành trắng trơn |

Đúng hai thiết lập này thì bản in khớp y hệt bản `render_baogia.py` dựng ra.

### Ảnh JPG gửi Zalo thì sao

Không dựng được ở ChatGPT — ảnh cần Chrome chụp. Hai lối:
- **Có Chrome:** cài thêm Python rồi chạy `python baogia-1file.py du-lieu.json` **thẳng trên máy** — ra đủ PDF + 5 ảnh, vẫn chỉ cần một file, không cần ZIP cũng không cần ChatGPT.
- **Gấp:** mở file `*-slide.html`, chụp màn hình từng slide. Xấu hơn nhưng dùng được.

---

## 4c. Gắn ảnh khách thật vào báo giá

Ảnh trước–sau là thứ khách xem **trước cả giá**. Agent luôn tự đề xuất gắn ảnh khi báo giá chưa có.

```bash
python tools/anh_album.py                          # 29 album trong kho
python tools/anh_album.py --album "cắt mí"          # ảnh trong album, kèm tag
python tools/anh_album.py --album "cắt mí" --lay 2  # in sẵn khối JSON để dán
```

Nói thường với agent cũng được:

```
Gắn 2 ảnh cắt mí thật từ album vào báo giá này
```

```
Album có ảnh nào hợp với ca sửa mí không?
```

Dán link vào `case_tuong_tu[].anh_truoc` / `anh_sau` → **tool tự tải ảnh về nhúng vào file**. Bản gửi khách tự đứng một mình: album đổi hay link chết thì file đã gửi vẫn nguyên. Báo giá có ảnh thật được **thêm một trang** so với chuẩn 3 trang.

**Khoá API** để ở `template/album-key.local.json` hoặc biến môi trường `KN_ALBUM_KEY` — chỉ cần để *liệt kê*, tải ảnh thì không cần.
⛔ **Không commit khoá lên GitHub** (repo công khai). `.gitignore` đã chặn `*.local.json`.

> ⚠️ **API trả ảnh, không trả giấy phép.** Hiện chưa ảnh nào gắn tag consent, nên tool không tự biết ảnh nào đã xin phép khách. Câu hỏi đó nằm trong bảng *Cân nhắc trước khi gửi*, người gửi tự trả lời.

---

## 5. Lệnh render — nhắc nhanh

```
python tools/render_baogia.py out/<ma>/du-lieu.json                  # PDF + 5 ảnh JPG
python tools/render_baogia.py out/<ma>/du-lieu.json --dinh-dang jpg  # chỉ ảnh Zalo
python tools/render_baogia.py out/<ma>/du-lieu.json --dinh-dang pdf  # chỉ PDF
python tools/render_baogia.py out/<ma>/du-lieu.json --chi-html       # chỉ dựng HTML để xem
python tools/render_baogia.py out/<ma>/du-lieu.json --nhap           # bản nháp đóng dấu NHÁP
```

Không có Chrome trong máy → đặt biến môi trường `KN_CHROME` trỏ tới `chrome.exe`, hoặc mở file HTML rồi Ctrl+P → Save as PDF.
