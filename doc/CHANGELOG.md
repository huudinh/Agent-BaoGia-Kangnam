# CHANGELOG — Agent-BaoGia-Kangnam

## v1.9 — 2026-10-21 · hotline không bao giờ là [CHỜ XÁC NHẬN]

Agent đang ghi `[CHỜ XÁC NHẬN]` vào ô hotline. Đó là triệu chứng của **quên nạp `template/thong-tin-lien-he.json` vào Knowledge** — file này mới có từ v1.6 nên mọi GPT cấu hình trước đó đều thiếu.

Sửa ở ba lớp, để lỗi này không lặp lại dù người dùng quên:

**Tool** — `meta.hotline` chứa `CHỜ` hoặc bắt đầu bằng `[` thì coi như bỏ trống, tự điền số thật từ nguồn và in cảnh báo. Người dùng không phải sửa tay.

**Bộ não** — phân biệt rõ: `[CHỜ XÁC NHẬN]` chỉ dành cho thứ **thật sự chưa ai chốt** (ưu đãi chưa có chứng từ · trả góp · địa chỉ chi nhánh · ảnh chưa consent). Hotline, giá và tên bác sĩ đều **có nguồn** — không thấy nguồn thì nói thẳng *"thiếu file X trong Knowledge"*, ⛔ không thay bằng placeholder.

**Trang hướng dẫn** — in thẳng **số đang dùng** ở mục Kiến thức và trên thẻ copy của file, số lấy động từ JSON nên không lệch. Ai thấy placeholder là biết ngay mình quên nạp file nào.

Bảng *"`[CHỜ XÁC NHẬN]` dùng đúng chỗ"* nằm ở `BG-09` mục 2.

---

## v1.8 — 2026-10-21 · cả bộ render gói trong MỘT file

v1.7 bảo người dùng ChatGPT "kẹp file ZIP của repo vào chat" — đúng về kỹ thuật nhưng **không ai làm vậy mỗi lần báo giá**. Nên gói lại.

**`tools/baogia-1file.py` (156 KB)** nhúng sẵn 8 file nguồn: `render_baogia.py` · `cong_phap_ly.py` · hai template HTML · `bang-gia.json` · `bac-si-duyet.json` · `thong-tin-lien-he.json` · `logo-kangnam.png`.

Cách gói **không chép lại logic**: nhúng nguyên văn dưới dạng base64, lúc chạy bung ra thư mục tạm rồi gọi đúng `render_baogia.py`, xong chép file kết quả ra cạnh `du-lieu.json` và dọn thư mục tạm. Nhờ vậy bản một-file **không bao giờ lệch** với repo — sửa template xong chạy `python tools/build-1file.py` là xong.

```
python baogia-1file.py du-lieu.json              # HTML + PDF + 5 ảnh (cần Chrome)
python baogia-1file.py du-lieu.json --chi-html   # chỉ HTML (chạy được ở ChatGPT)
```

Đã kiểm từ **thư mục trống**, chỉ có 2 file (`baogia-1file.py` + `du-lieu.json`), không có repo: ra đủ PDF 3 trang + 5 ảnh. Kiểm tiếp với `KN_CHROME` trỏ vào đường dẫn không tồn tại (giả lập sandbox ChatGPT): ra 2 file HTML tự đứng một mình, **ba cổng chặn vẫn chạy đủ**.

Hướng dẫn ChatGPT viết lại quanh file này: upload **một lần** vào Knowledge, mỗi lần báo giá chỉ dán JSON. Cập nhật ở: `prompts/prompt-van-hanh.md` mục 4b · `SYSTEM-PROMPT.md` §9b · bản ngắn · tab ChatGPT của trang hướng dẫn · `doc/01-cai-dat.md` mục E2.

---

## v1.7 — 2026-10-21 · lấy file PDF khi không có Python

Thiếu hẳn một đường: người cài agent trên **ChatGPT** không có lệnh nào để ra file. Tool render cần **Python + Chrome**, mà sandbox của ChatGPT **không có Chrome** — nên lệnh `render_baogia.py` đầy đủ chạy ở đó là hỏng.

Đường đi được, và nó vốn đã có sẵn: file HTML do tool dựng **tự đứng một mình** (logo nhúng base64, không tham chiếu file ngoài, 92 KB). Mở bằng trình duyệt rồi in ra PDF là khớp y hệt bản `render_baogia.py` dựng.

```
1. Bật Code Interpreter, kẹp file ZIP của repo vào chat
2. python tools/render_baogia.py out/KH/du-lieu.json --chi-html
3. Mở file HTML -> Ctrl+P -> Lề: Không + bật Đồ hoạ nền -> Save as PDF
```

`--chi-html` trả về **trước** bước tìm Chrome, nên chạy được ở nơi không có trình duyệt — và **ba cổng chặn vẫn chạy đủ**. Không vì đổi cách xuất mà mất lớp bảo vệ.

Hai thiết lập in ở bước 3 là **bắt buộc**, đã ghi rõ ở mọi chỗ nhắc tới cách này:
- thiếu **Lề: Không** → nội dung tràn thành 4–5 trang (lề mặc định của trình duyệt đè lên `@page{margin:0}`);
- thiếu **Đồ hoạ nền** → mất hết khối navy: dải tổng chi phí và khối CTA thành trắng trơn.

⛔ **Ảnh JPG gửi Zalo không dựng được ở ChatGPT** — ảnh cần Chrome chụp. Bộ não được dạy **nói thẳng** điều đó thay vì đưa lệnh người dùng không chạy được; máy nào cũng có Chrome sẵn nên cách nhanh nhất vẫn là cài thêm Python rồi chạy tool trên máy.

Thêm vào: `prompts/prompt-van-hanh.md` mục 4b (có prompt copy được, nay 26 prompt mẫu) · `SYSTEM-PROMPT.md` §9b · bản ngắn · tab ChatGPT của trang hướng dẫn (kèm bước **bật Code Interpreter**).

---

## v1.6 — 2026-10-21 · hotline 0968.999.777, gom về một nguồn

Hotline đổi từ `1900 6466` sang **`0968.999.777`**.

Nhưng số cũ đang nằm **rải ở 5 file** (hai file mẫu `du-lieu`, `khach-hang.mau.json`, `prompt-bao-gia.md`, `BG-09`) — đó chính là cách nó lệch nhau về sau. Nên gom lại trước khi đổi:

**Thêm `template/thong-tin-lien-he.json`** — nguồn duy nhất. `render_baogia.py` lấy số từ đây khi `du-lieu.json` **không khai** `meta.hotline`; khai rồi thì dùng số đã khai, để chừa chỗ cho hotline riêng của chi nhánh. Thiếu cả hai → tool in cảnh báo.
`meta.hotline` **không còn là trường bắt buộc** của cổng dữ liệu.

Hai bộ não nay ghi rõ: ⛔ **agent không tự ghi hotline**, bỏ trống để tool điền. Từ nay đổi số chỉ sửa **một file**.

> 🔧 Bẫy khi kiểm: `out/MAU/du-lieu.json` là bản copy cũ vẫn còn hotline cứng nên fallback không chạy, file xuất ra vẫn in số cũ — suýt tưởng code hỏng. Đã copy lại từ `template/` rồi kiểm cả hai nhánh: có file nguồn → in `0968.999.777`; xoá file nguồn → in đúng dòng cảnh báo.

---

## v1.5 — 2026-10-21 · ba ô của form tạo agent

Trang hướng dẫn chỉ nói điền **Tên** và **Instructions**, bỏ trống ô **Mô tả** (`Description`) và **Câu mở đầu hội thoại** (`Conversation starters`) — người cài mở form ChatGPT ra là khựng ngay ở ô thứ hai.

Thêm khối **Tên & mô tả — dán vào form** ngay trước phần chọn nền tảng, theo đúng mẫu của `Agent-AdsOptimize-Kangnam-QT`: ba ô, mỗi ô một nút Copy.

| Ô | Nội dung |
|---|---|
| **Tên** | `Agent-BaoGia-Kangnam` |
| **Mô tả** | 225 ký tự — dưới giới hạn 300 của ChatGPT. Builder in kèm số ký tự thật để biết còn cách giới hạn bao xa |
| **Câu mở đầu** | 4 câu: `/baogia` (dán đoạn chat) · `/wizard cắt mí` · `/tinnhan` · `/kiemtra` |

Nội dung ba ô khai trong `META_FORM` của `tools/build-huong-dan.py` — sửa một chỗ, trang và nút Copy khớp luôn. Ba ô cũng được chép vào `doc/01-cai-dat.md` mục 0b cho người đọc trong repo.
Tab ChatGPT nay có bước **Description** riêng; tab Claude nhắc lấy tên và mô tả từ khối đó.

---

## v1.4 — 2026-10-21 · đọc được trên điện thoại

Ảnh JPG vốn đã hợp điện thoại, nhưng **file HTML và PDF khổ A4 thì không** — mở lên phải kéo ngang. Thêm lớp hiển thị riêng cho màn hình nhỏ, **không đụng tới bản in**.

**Lỗi nặng nhất, và là lỗi im lặng: thiếu `<meta name="viewport">`.** Không có thẻ này, trình duyệt điện thoại dựng trang trong khung ảo ~980px rồi thu nhỏ toàn bộ, nên media query **không bao giờ khớp** — khách thấy bản A4 chữ li ti. Trên máy tính nhìn vẫn đúng nên rất dễ bỏ sót. Đã thêm vào cả hai template.

| Dưới 860px | |
|---|---|
| `.page` | bỏ khổ 210mm, `width:auto` — đây là thứ duy nhất gây kéo ngang |
| Lưới 2 cột | về 1 cột (các bước phương án · ảnh case · khối liên hệ) |
| Chân trang | `position:absolute` → `static`, nếu không nó đè lên dòng cuối |
| Tiêu đề hero | 22pt → 19pt (17pt dưới 420px) |

| Dưới 620px | |
|---|---|
| Bảng chi phí 4 cột | **xếp dọc**: mỗi dòng một khối, nhãn cột sinh bằng `::before` nên không phải đổi HTML do tool dựng |
| Dòng ưu đãi | cho nhãn dài xuống dòng, số tiền `white-space:nowrap` — trước đó bị cắt mất **đúng con số giảm giá** |
| Dải tổng sau ưu đãi | giữ nền navy, bo góc, đọc được không cần phóng to |

**Bản slide** tự thu khung 1080px vừa bề ngang bằng `zoom`, chạy **sau** vòng đo tràn khung vì `zoom` làm lệch phép đo bằng `getBoundingClientRect`. Khi đang chụp ảnh (có `?s=`) thì bỏ qua hẳn, nên JPG xuất ra không đổi.

> ⚠️ Ghi lại để khỏi mất thời gian lần sau: **Chrome headless có bề ngang tối thiểu 500px**. Chụp `--window-size=390` ra ảnh bị cắt bên phải dù layout đúng — suýt nữa sửa nhầm một lỗi không tồn tại. Đo bằng `matchMedia` thay vì tin vào ảnh chụp.

Luật đầy đủ: `BG-08` mục 2c. PDF của cả hai ca mẫu vẫn đúng **3 trang** — lớp màn hình không chạm vào bản in.

---

## v1.3 — 2026-10-21 · logo thật · một điểm nhấn mỗi trang · siết cá nhân hoá

Sửa theo ba nhận xét trên một bản báo giá do agent ChatGPT dựng: **sai logo · nội dung quá nhiều, không có điểm nhấn · chưa đủ cá nhân hoá.**

**① Logo thật** — thêm `template/logo-kangnam.png` (518×78, nền trắng). `render_baogia.py` nhúng logo vào file xuất ra dưới dạng **data URI**, nên PDF và JPG đứng một mình được. Logo xuất hiện ở: A4 trang 1 (13mm) · A4 trang 2–3 (8,5mm) · bìa slide (trong **khung trắng bo góc**, vì nền file logo là trắng — đặt thẳng lên navy sẽ ra ô vuông trắng) · chân slide CTA.
Thiếu file → tool in cảnh báo và dùng chữ thay tạm, bản đó **không được gửi khách**. Luật dùng logo: `BG-08` mục 1b.
⛔ Gỡ hẳn cách gõ chữ *"BỆNH VIỆN THẨM MỸ KANGNAM"* thay logo.

**② Một điểm nhấn mỗi trang** (`BG-08` mục 1c) — mỗi trang có **đúng một thứ to nhất**: trang 1 tiêu đề lời hứa (22pt) · trang 2 con số sau ưu đãi · trang 3 khối CTA. Trang 1 dựng lại thành khối **hero** riêng; khối *Điều khách mong muốn* hạ cấp từ card nền sang vạch màu bên trái; bốn bước phương án xếp **2 cột** thay vì dọc. ⛔ Tối đa 2 khối nền đặc một trang.

**③ Bốn dấu hiệu cá nhân hoá** (`BG-03` mục 2b) — thêm **lời chào đích danh viết tay** trên tiêu đề trang 1 và bìa slide, **chữ ký tư vấn viên** cuối trang 3 (font script hệ thống, không tải mạng).
Kèm **phép thử**: che tên khách và ba dòng meta đi, nếu vẫn gửi được cho khách khác cùng dịch vụ thì chưa cá nhân hoá. Hai dấu hiệu hình thức do template lo **không tính** — thứ quyết định vẫn là khối 3 và câu *vì sao hợp*. Phép thử này đã vào cả hai bộ não và ô tự kiểm (nay 9 ô).

> 🔧 Trang 3 của ca sửa mí tràn **1,4px** (0,37mm) sau khi thêm chữ ký → 4 trang. Đã đo bằng px thật thay vì mm làm tròn, cắt 4px ở `.ky` và `.phap-ly`. Cả hai ca mẫu nay đúng 3 trang, cả ba trang đều 1121px / ngưỡng 1122,52px.

---

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
