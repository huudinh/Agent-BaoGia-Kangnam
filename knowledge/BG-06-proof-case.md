# BG-06 — CASE TƯƠNG TỰ & ẢNH TRƯỚC – SAU
Version 1.0 · Nguồn: `Agent-LDP-Kangnam/knowledge/KF-14-proof-bank.md` mục 4–5
Cập nhật: 2026-10-21

---

## 1. NGUỒN ĐƯỢC PHÉP DÙNG

| Nguồn | Trạng thái | Dùng thế nào |
|---|---|---|
| `benhvienthammykangnam.com.vn/case-thuc-te/` | ⚠️ trang công khai **đang trống** (kiểm 16/10/2026) | Ca nào đã publish ở đây thì ưu tiên — khách tự kiểm chứng được |
| `/hinh-anh-khach-hang/` (menu *Ảnh Trước – Sau*) | 9 nhóm dịch vụ | Lấy đúng nhóm dịch vụ, giữ nguyên mốc chụp |
| **Album Kangnam** `hcigroup.vn/app/albumkn/` | **nguồn chính thức, đã duyệt để gửi khách** | Khai id album vào `du-lieu.json` — **tool tự gọi API lấy ảnh** |

## 2. LẤY ẢNH TỪ ALBUM — khai một dòng, tool làm phần còn lại

Album Kangnam là kho ảnh **đã được duyệt để gửi khách**. Không phải xin phép lại từng tấm, không phải chạy lệnh rồi dán link tay. Khai album vào `du-lieu.json`:

```json
"case_album": {
  "album": "theme-1792573778761",
  "link": "https://hcigroup.vn/app/albumkn/?album=theme-1792573778761",
  "nhan": "Hình ảnh khách hàng đã thực hiện tại Kangnam"
}
```

Case nào chưa có `anh_truoc`/`anh_sau`/`anh_them` thì tool **tự gọi API lấy 3 ảnh đầu** của album đó, tải về, nhúng data URI vào file. Muốn lấy từ album khác cho riêng một case thì khai `"album"` ngay trong case đó.

**Chọn album nào:** `template/album-index.json` liệt kê **29 album · 179 ảnh**, kèm id và số ảnh. Vài album hay dùng:

| Dịch vụ | Album | Ảnh |
|---|---|---|
| Cắt mí | `theme-1792573778761` *Cắt mí thành công* · `theme-1789556882622` *Case Cắt Mí* | 13 · 12 |
| Mũi | `theme-1789727113902` *Dịch vụ Mũi* · `theme-1789556976926` *Case Mũi* | 35 · 6 |
| Ngực | `theme-1789557067505` *Case Ngực* | 9 |
| Hàm mặt | `theme-1791294350815` *Gọt hàm Vline* · `theme-1789554992892` *Case Hàm Mặt* | 7 · 5 |
| Mắt (chung) | `theme-1789467261265` *Thẩm Mỹ Mắt* | 10 |

⛔ **Không từ chối đưa ảnh vì "chưa xác minh được consent".** Album đã là nguồn duyệt sẵn. Dịch vụ nào không có album phù hợp thì nói đúng điều đó — *"album chưa có ca nào đúng tình trạng của chị"* — chứ không viết một câu thủ tục.

Cập nhật danh mục khi album đổi: `python tools/anh_album.py --ghi-muc-luc`.

## 3. LUẬT KHI ĐƯA ẢNH VÀO BÁO GIÁ
1. **Ảnh album thường ĐÃ ghép sẵn trước–sau** → nhãn mặc định khi lấy tự động là *Ca 1 · Ca 2 · Ca 3*. Có ảnh trước và sau rời thì đặt lại `chu_thich_truoc` / `chu_thich_sau`.
2. Chọn ảnh **gần chân dung khách nhất** (tình trạng ban đầu giống), không chọn ảnh kết quả ấn tượng nhất.
3. Luôn kèm câu miễn trừ, **chép đúng**:
   > *"Hình ảnh được khách hàng đồng ý chia sẻ và ghi rõ thời điểm chụp. Kết quả thẩm mỹ phụ thuộc cơ địa từng người."*
4. ⛔ **Không tạo ảnh kết quả giả**, không ảnh stock/AI mô phỏng kết quả trình bày như case thật.
5. ⛔ Không ảnh cận cảnh thao tác phẫu thuật, máu, vết mổ.
6. ⛔ **Giảm cân / Lipo 360 / body:** không dùng ảnh so sánh **cơ thể** (rào R12). Thay bằng câu chuyện khách hàng. Tool chặn nếu `case_tuong_tu[].nhom` thuộc nhóm body.

## 3a. LẤY ẢNH THẬT BẰNG CÔNG CỤ — `tools/anh_album.py`

Album có **API công khai**, nên agent lấy được danh sách ảnh. Khoá API chỉ cần để *liệt kê*; **tải ảnh thì không cần khoá**.

```bash
python tools/anh_album.py                            # 29 album trong kho
python tools/anh_album.py --album "cắt mí"            # ảnh trong album, kèm tag
python tools/anh_album.py --album "cắt mí" --lay 3    # in sẵn khối JSON 3 ảnh để dán
```

Dán link vào `case_tuong_tu[].anh_truoc` / `anh_sau` / `anh_them` → **tool tự tải ảnh về nhúng vào file** dưới dạng data URI. Ba ô ảnh, không phải hai — xem [[BG-08-design-system]] mục 5 về cách đặt nhãn khi ảnh album vốn đã ghép sẵn trước–sau. Bản gửi khách vì thế **tự đứng một mình**: album đổi hay link chết thì file đã gửi vẫn nguyên.

Khoá API để ở `template/album-key.local.json` hoặc biến môi trường `KN_ALBUM_KEY`.
⛔ **Không commit khoá** — repo là public; `.gitignore` chặn `*.local.json`. Lỡ lộ thì vào app xoay khoá mới.

> ⚠️ **API trả ảnh, không trả giấy phép.** Hiện **chưa ảnh nào gắn tag**, nên tool không tự biết ảnh nào đã có consent. Người lập báo giá tự kiểm — tool in câu hỏi đó trong bảng **Cân nhắc trước khi gửi**.

Ảnh trước–sau nằm ở **trang 4** cùng case và CTA — không đội thêm trang so với chuẩn 4 trang.

## 3b. LINK ALBUM GỬI KÈM BÁO GIÁ
Một số dịch vụ có **album chia sẻ** đã được duyệt để gửi khách. Khai vào `du-lieu.json`:

```json
"case_album": {"link": "https://...", "nhan": "Hình ảnh khách hàng đã cắt mí tại Kangnam"}
```

| Luật | |
|---|---|
| Album đang có | **Cắt mí:** `https://hcigroup.vn/app/albumkn/?album=theme-1792573778761` ([[BG-11-noi-dau-cat-mi]] mục 5) |
| Gửi Zalo/Messenger | dán link vào **tin nhắn** — link in trên ảnh JPG không bấm được |
| Trước mỗi đợt | kiểm link còn sống và còn đúng album |
| ⛔ | Link album **không thay thế** consent của từng ảnh khi bạn lấy ảnh ra chèn vào file. Gửi link là một việc, chèn ảnh vào ấn phẩm là việc khác |
| ⛔ | Không gửi link album nội bộ chưa được duyệt chia sẻ cho khách |

## 4. CHƯA CÓ ẢNH ĐỦ ĐIỀU KIỆN → Ô ẢNH TẠM
Template dựng ô ảnh tạm khi case khai `"can_anh": true` mà `anh_truoc`/`anh_sau` còn trống: khung gạch chéo ghi rõ **cần ảnh gì, case nào**. Bản gửi khách **không được còn ô ảnh tạm** — đó là tín hiệu cho người lập báo giá đi xin ảnh, không phải để gửi đi.

Case **kể bằng chữ, không định dùng ảnh** → bỏ `can_anh`, template không dựng ô ảnh tạm. Đây là cách làm sạch khi chưa kịp xin consent (xem mục dưới).

Hai cách xử lý khi không kịp có ảnh:
- **Bỏ ảnh, giữ case bằng chữ** — mô tả tình trạng ban đầu, phương pháp, kết quả (không ảnh thì không vướng R5).
- **Bỏ cả khối 7** — báo giá vẫn hợp lệ, nhưng mất một trụ niềm tin với nhóm khách 1, 4, 5.

## 5. CHỌN CASE — thứ tự ưu tiên khi khớp
```
1. Tình trạng ban đầu giống  (da dư / sụp mí do cơ / mũi đã can thiệp...)
2. Độ tuổi & nghề nghiệp     (ảnh hưởng tới kỳ vọng "tự nhiên" và lịch nghỉ)
3. Ràng buộc giống nhau      (nghỉ ít ngày, ngân sách, sắp có sự kiện)
4. Cùng cơ sở / cùng bác sĩ  (khách kiểm chứng được)
```

## 6. CÁCH VIẾT MÔ TẢ CASE — 3 dòng
```
Ai      "Khách nữ 30 tuổi, mí một nếp kèm da dư nhẹ, làm văn phòng"
Làm gì  "Cắt mí 6D kết hợp lấy mỡ mí trên — BS [tên đã duyệt]"
Kết quả "Nếp mí nhỏ, mở mắt tự nhiên; khách đi làm lại theo lịch đã sắp xếp với bác sĩ."
```
⛔ Không viết *"khách hài lòng 100%"*, không gán cảm xúc không có nguồn, không bịa lời khách.

## 7. 🔶 CÒN THIẾU — cần người thật bổ sung
- Bảng kê **ảnh ↔ mã case ↔ ngày consent ↔ hạn consent**. Đề xuất: dùng quy ước tag trong Album Kangnam (`consent-ok` · `consent-cho` · `consent-het-han` · `phap-che-duyet`) — khi đó bộ lọc tag chính là bảng kê.
- Bộ case chuẩn theo từng nhóm dịch vụ để agent chọn nhanh thay vì hỏi lại mỗi lần.

Liên quan: [[BG-07-cong-phap-ly]] · [[BG-03-cau-truc-bao-gia]] · [[BG-09-schema-du-lieu]]
