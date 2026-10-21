# CHANGELOG — Agent-BaoGia-Kangnam

## v1.2 — 2026-10-21 · trang hướng dẫn cài đặt + prompt mẫu

**Trang web hướng dẫn:** <https://claude.ai/artifact/WZuxB6N8YyEH4mQoCboJFj> — nhúng vào `README.md` và `doc/01-cai-dat.md`.
Ba mục theo đúng quy ước của `Agent-LDP-Kangnam`: ① Cài đặt (5 bước · 4 tab nền tảng · 3 thẻ Copy bộ não · 15 thẻ copy file) · ② 25 prompt mẫu lọc theo 5 nhóm · ③ Kiến thức (bảng 11 file · 3 cổng chặn · chính sách giá Plasma · album · việc còn treo).

**Thêm `tools/build-huong-dan.py` + `tools/huong-dan.tpl.html`.** Trang được **sinh từ nội dung thật trong repo**, không chép tay: bộ não, 11 file knowledge, 4 file dữ liệu `template/*.json` và toàn bộ prompt đều đọc trực tiếp từ file nguồn, kèm số ký tự thật. Sửa knowledge hoặc bảng giá → chạy lại script → republish cùng URL là trang khớp ngay.
`tools/huong-dan.html` là bản sinh ra, đã vào `.gitignore` — **không sửa tay**.

> 🔧 Lỗi đã sửa khi dựng: hàm rút khối copy của bộ não dùng regex ``` … ``` nên **cắt cụt ở fence lồng bên trong** (hộp quy trình 4 bước, checklist cổng) — thẻ A chỉ ra 3.045 ký tự thay vì 10.675. Nay cắt theo hai vạch ▼▲, và script tự dừng nếu khối không bắt đầu bằng tiêu đề.

**Bảng màu:** dùng **chung một bộ token với `Agent-AdsOptimize-Kangnam-QT` và `Agent-LDP-Kangnam`** — nâu đỏ `#8A1F33` · vàng `#86560D` · nền kem `#EADDD8` · băng `#3A1425` · nhấn `#EDBD6B`, chữ **Be Vietnam Pro + Lora nghiêng** cho nhãn mục. Cả ba trạng thái theme (sáng · tối theo hệ thống · tối do người đọc chọn) đều khai đủ token.

> Lưu ý: đây là **bảng màu của bộ tài liệu hướng dẫn**, khác bảng màu của **ấn phẩm báo giá** (navy `#074E84` + cam `#EF6103`, xem `BG-08`). Hai thứ phục vụ hai người đọc khác nhau: trang hướng dẫn cho nhân viên, tờ báo giá cho khách hàng. ⛔ Không trộn hai bảng.

---

## v1.1 — 2026-10-21 · tri thức chuyên sâu CẮT MÍ

**Thêm `knowledge/BG-11-noi-dau-cat-mi.md`** — nguồn: tổng hợp nội bộ *"Tổng hợp nỗi đau khách hàng quan tâm cắt mí"*.
- **9 chân dung khách:** nhóm A chưa từng làm mí (A1 một mí · A2 mắt nhỏ khe hẹp · A3 sụp mí/da chùng/mỡ mí · A4 hai bên không đều) và nhóm B đã làm nhưng chưa hài lòng (B1 tái sụp · B2 mí trợn/nếp quá cao · B3 đa nếp mí · B4 mí lệch · B5 sẹo/nếp cứng). Mỗi chân dung có nỗi đau, lo lắng ngầm, mong muốn và cách viết khối 3–4.
- **10 nỗi lo trước khi quyết định** → cột *điều khách thực sự muốn biết* + câu trả lời mẫu đã qua cổng pháp lý.
- **Bản đồ chân dung → nhóm khách → điều bắt buộc có trong khối 4 và khối 9.**
- Hai điều ⛔ **không được hứa** dù khách rất muốn nghe: *mắt sẽ to hơn* (A2 — phụ thuộc cơ nâng mi) và *cân đối tuyệt đối* (A4 — chỉ cải thiện trong giới hạn giải phẫu). Toàn bộ nhóm B áp rào **R6**: không bình luận nơi cũ.

**Giải pháp dao Plasma** — câu mô tả chuẩn + bảng ✅/⛔ (*hạn chế tổn thương mô* chứ không phải *không tổn thương*; *nhằm giảm nguy cơ sẹo* chứ không phải *không sẹo*).

**Chính sách giá cắt mí Plasma** (`template/bang-gia.json`):
- `mat.cat-mi-plasma` — niêm yết **10.000.000đ**, thêm trường mới `uu_dai_hien_hanh` = **8.000.000đ**.
- Thêm `mat.phi-sua-mi` — niêm yết 3.000.000đ, giảm 40–50% tuỳ khu vực → thực thu **1.500.000–1.800.000đ**; tổng ca sửa mí dự kiến **9,5–9,8 triệu**.

**Tool & template:**
- Cổng bảng giá chấp nhận `uu_dai_hien_hanh` mà không cần `ly_do_lech`; bảng chi phí tự in **giá niêm yết gạch ngang** phía trên giá ưu đãi (cả PDF lẫn slide).
- Thêm `case_album` — link album ảnh khách gửi kèm báo giá, in ở khối case. Album cắt mí: `hcigroup.vn/app/albumkn/?album=theme-1792573778761`.
- Thêm cờ `can_anh` cho case: case kể **bằng chữ** không còn bị dựng ô ảnh tạm; chỉ case khai `can_anh: true` mới dựng ô nhắc đi xin ảnh.
- Câu miễn trừ ảnh chỉ in khi thật sự có ảnh (trong file hoặc qua album).

**Thêm `template/du-lieu.mau-sua-mi.json`** — ca mẫu thứ hai (B1 mí tái sụp, nhóm khách 5), đã render thật: PDF 3 trang + 5 ảnh, tổng 9.800.000đ.

**Sửa lỗi bố cục A4 (phát hiện khi render ca thứ hai):**
- `.page + .page{margin-top:6mm}` có độ ưu tiên cao hơn `.page{margin:0}` nên 6mm vẫn còn khi in → Chrome đẩy **mỗi trang thành hai trang PDF** (5–6 trang thay vì 3). Đã ghi đè đúng selector trong `@media print`.
- Trang 3 cao **360mm** (vượt 63mm) vì chứa case + album + lộ trình + băn khoăn + CTA + miễn trừ, trong khi trang 2 còn trống. Đã **chuyển khối lộ trình sang trang 2** và siết typography (body 11,5pt → 10,5pt, bảng 10pt → 9,5pt, giảm padding các khối). Cả hai ca mẫu nay đúng **3 trang, cả ba trang đều 297mm**.
- Bỏ ý định ép chiều cao cố định + script thu nhỏ: cách đó **cắt mất khối CTA và khối miễn trừ** ở trang 3. Nay `.page` dùng `min-height`, nội dung dài thì dãn sang trang in kế tiếp — **không bao giờ cắt chữ**.
- `render_baogia.py` **đếm số trang PDF** sau khi render và cảnh báo khi vượt 3 trang (`SO_TRANG_CHUAN`).

✅ **Đóng việc treo #2 của v1.0** (nghi vấn giá cắt mí Plasma 7.200.000đ) — chính sách mới đã chốt 10.000.000đ/8.000.000đ.

---

## v1.0 — 2026-10-21 · bản đầu tiên

**Dựng mới toàn bộ.** Agent sinh báo giá cá nhân hoá từ thông tin khách hàng, xuất PDF A4 + ảnh JPG.

### Bộ não
- `SYSTEM-PROMPT.md` (9.392 ký tự khối copy) · `SYSTEM-PROMPT-NGAN.md` (5.135 ký tự, vừa giới hạn 8.000 của Custom GPT).
- Quy trình 4 bước: đọc khách → chọn phương án & chi phí → viết 9 khối → kiểm & xuất.
- 7 lệnh: `/baogia` `/wizard` `/tinnhan` `/doichieu` `/kiemtra` `/lo` `/hoc`.

### Tri thức (10 file)
`BG-01` thương hiệu · `BG-02` bảng giá · `BG-03` cấu trúc 9 khối · `BG-04` chân dung khách · `BG-05` nỗi sợ · `BG-06` case & ảnh · `BG-07` cổng pháp lý · `BG-08` design · `BG-09` schema · `BG-10` vòng học.

Nguồn kế thừa: `Kangnam-Agent-Factory/knowledge/K1–K4` (thương hiệu, khách hàng, hành vi, dịch vụ + bảng giá) · `Agent-LDP-Kangnam/knowledge/KF-09, KF-11, KF-14` (design token, rào R0–R12, proof bank).

### Dữ liệu cứng
- `template/bang-gia.json` — **81 dịch vụ** 9 nhóm, trích từ K4 §5 (web `/bang-gia`, bản 09/2026). Mỗi mục có `ma`, `kieu` giá (cố định/khoảng/từ/liên hệ), cờ `dai_phau`, cờ `canh_bao`.
- `template/bac-si-duyet.json` — 22 hồ sơ, 4 trạng thái: **12 `duyet`** · 2 `can_xac_minh` · 3 `xung_dot` · 5 `ngung_dung`, theo đối chiếu web 16/10/2026.

### Công cụ
- `tools/render_baogia.py` — template engine mustache rút gọn + 3 cổng chặn + render qua Chrome headless (không cần cài thư viện ngoài). Xuất PDF A4 3 trang và 5 ảnh JPG 1080×1920.
- `tools/cong_phap_ly.py` — quét từ cấm (R1), mốc hồi phục cứng, bác sĩ sai trạng thái (R4), ảnh thiếu consent/mốc chụp (R5), ảnh cơ thể (R12), tên thương mại thuốc (R7), đại phẫu sai tuyến (R3), nghi CCCD.

### Template
`baogia-a4.html` (PDF) · `baogia-slide.html` (JPG) · `khach-hang.mau.json` · `du-lieu.mau.json`.

---

## 🔶 VIỆC CÒN TREO — cần người thật chốt

| # | Việc | Ai | Ảnh hưởng nếu không làm |
|---|---|---|---|
| 1 | **Chốt câu chữ bảo hành.** K1/K4 ghi USP *"bảo hành trọn đời"* (mũi) và *"cam kết không co thắt bao xơ"* (ngực) — cả hai **vi phạm R1**. Cần câu thay thế có thời hạn cụ thể | Pháp chế | Agent tự né, mất một USP mạnh; hoặc người dùng tự viết vào rồi bị cổng chặn |
| 2 | ✅ **ĐÃ ĐÓNG v1.1** — giá cắt mí Plasma: niêm yết 10.000.000đ, ưu đãi 8.000.000đ | — | — |
| 2b | **Xác nhận mức giảm phí sửa mí theo từng khu vực** (đang ghi 40–50% → 1,5–1,8tr) | Vận hành | Báo sai tổng chi phí ca sửa mí |
| 3 | **Xác nhận giá Lipo mini** — "nhiều vùng 18tr" rẻ hơn "1 vùng 34tr", nghi lệch dữ liệu | Vận hành | Báo sai giá |
| 4 | **Chốt danh sách bác sĩ duyệt quảng bá (KF-02)** — 3 hồ sơ đang `xung_dot` (Louis Truong, Alice Tran, Do Minh Vuong): web ghi verified nhưng KF-02 đã gỡ | Pháp chế + Chuyên môn | Nêu tên sai → rào R4 |
| 5 | **Bảng kê consent ảnh case** — ảnh ↔ mã case ↔ ngày consent ↔ hạn. Đề xuất dùng quy ước tag trong Album Kangnam (`consent-ok` / `consent-cho` / `consent-het-han` / `phap-che-duyet`) | CSKH + Pháp chế | Mọi case phải hỏi tay từng lần; ô ảnh tạm còn mãi |
| 6 | **Chính sách trả góp chính thức** — ngân hàng liên kết, số kỳ, có phí chuyển đổi không, áp dụng cơ sở nào | Vận hành | Agent không được nêu trả góp |
| 7 | **Bộ case chuẩn theo nhóm dịch vụ** để agent chọn nhanh | Marketing + CSKH | Mỗi lần phải tự tìm case |
| 8 | **Xác nhận hiệu lực báo giá** — 7 ngày hay 14 ngày là chuẩn của bệnh viện | Vận hành | Agent đang để mặc định 14 ngày |
| 9 | **Bảng giá có phải bản mới nhất không** — `bang-gia.json` lấy theo bản web 09/2026 | Vận hành | Toàn bộ con số có thể lệch |

> Mục 1–4 là **rủi ro pháp lý**, nên làm trước. Mục 5–9 là rủi ro vận hành.

---

## Ghi chú kỹ thuật đã biết

- **A4 dùng `min-height` chứ không phải `height`.** Ép chiều cao cố định sẽ cắt mất khối CTA và miễn trừ khi nội dung dài — lỗi im lặng, nguy hiểm hơn một file 4 trang. Thước đo là số trang PDF do tool đếm, không phải CSS.
- Trong `@media print` phải ghi đè cả `.page + .page`, không chỉ `.page` — selector sau có độ ưu tiên cao hơn.

- Tool đếm slide theo số thẻ `class="slide"` thật trong HTML đã render → thiếu case thì xuất 4 ảnh thay vì 5, không lệch số thứ tự.
- Slide có script tự thu nhỏ nội dung khi tràn khung 1920px (tối đa còn 62%) và ghi cảnh báo ra console. **Thấy chữ nhỏ bất thường nghĩa là nội dung quá dài — cắt chữ, đừng chấp nhận bản thu nhỏ.**
- Không nhúng Google Fonts: máy render có thể offline và font tải chậm làm Chrome chụp hụt. Dùng font hệ thống.
- Cổng pháp lý cảnh báo cụm "số 1" ở mức CẢNH (không CHẶN) vì hay trùng với địa chỉ *"số 1 Trường Chinh"*. Người đọc tự phân biệt.
