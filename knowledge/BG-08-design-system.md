# BG-08 — DESIGN SYSTEM ẤN PHẨM BÁO GIÁ
Version 1.0 · Token lấy nguyên từ `Agent-LDP-Kangnam/knowledge/KF-09-design-system.md` (production v3.0)
Cập nhật: 2026-10-21

> ⚠️ **File này nói về ấn phẩm GỬI KHÁCH** (PDF + slide JPG): navy `#074E84` + cam `#EF6103`, font nhúng sẵn.
> **Trang hướng dẫn nội bộ** (`tools/huong-dan.tpl.html`) dùng **bảng màu khác** — nâu đỏ `#8A1F33` + vàng `#86560D` + nền kem, chung với `Agent-LDP-Kangnam` và `Agent-AdsOptimize-Kangnam-QT`.
> Hai bảng phục vụ hai người đọc: khách hàng và nhân viên. ⛔ Không trộn.

---

## 1. TOKEN MÀU — dùng đúng bảng production, không trộn

```css
--navy:#074E84; --navy-900:#04365E; --navy-950:#022544;
--cyan:#00A5E0; --gold:#A66E29; --amber:#FBBF65;
--cta:#EF6103;
--bg:#F3F6FA;  --surface:#FFFFFF;
--ink:#0E2338; --ink-2:#4A5C70; --ink-3:#6E7E90;
--line:#DCE3EC; --ok:#1E8E5A;
```

| Luật | |
|---|---|
| **Tỷ lệ** | ~80% trắng/`--bg` · 15% navy · 5% cam. ⛔ Không trang nền toàn navy (trừ bìa slide) |
| `--cta` | **màu nền nút**, không phải màu chữ. Chữ trắng trên cam chỉ đạt 3,29:1 → chỉ dùng cho chữ lớn đậm |
| ⛔ Cấm | `--amber` làm chữ trên trắng (1,65:1) · `--cyan` làm chữ trên trắng (2,82:1) · `--ink-3` cho chữ nhỏ (3,84) — chữ phụ dùng `--ink-2` |
| An toàn | navy trên trắng 8,63 AAA · ink trên bg 14,72 AAA · amber trên navy 9,43 AAA |

Trên nền navy (bìa slide, khối CTA): chữ trắng, nhãn phụ dùng `--amber`.

## 2. HAI KHỔ ẤN PHẨM

| Bản | File | Kích thước | Dùng khi |
|---|---|---|---|
| **A4 / PDF** | `template/baogia-a4.html` | 210×297mm, 4 trang | Gửi email, khách in ra, khách đưa người nhà xem |
| **Slide / JPG** | `template/baogia-slide.html` | 1080×1920, **3 ảnh** | Gửi Zalo / Messenger — khách xem ngay trong luồng chat |

> Mặc định xuất **cả hai**. Khách chat Zalo thường không mở PDF; khách cần bàn với người nhà thì cần PDF.

## 1b. LOGO — dùng file thật, không gõ chữ thay

```
template/logo-kangnam.png     518×78, nền TRẮNG (không trong suốt)
```

Tool tự nhúng logo vào file xuất ra dưới dạng **data URI**, nên PDF và ảnh JPG đứng một mình được — gửi đi không lo mất logo.

| Luật | |
|---|---|
| Nền sáng (trang A4, slide chi phí) | đặt logo thẳng lên nền trắng |
| Nền navy (bìa slide) | đặt trong **khung trắng bo góc**. ⛔ Không đặt thẳng — nền trắng của file logo sẽ thành một ô vuông trắng xấu |
| Kích thước | A4 trang 1 cao **13mm** · A4 trang 2–4 cao **8,5mm** · bìa slide cao **62px** |
| ⛔ Cấm | gõ chữ *"BỆNH VIỆN THẨM MỸ KANGNAM"* thay cho logo · đổi màu logo · kéo méo tỉ lệ · thêm hiệu ứng đổ bóng |
| Thiếu file | tool in cảnh báo và dùng chữ thay tạm — **bản đó không được gửi khách** |

Dòng định vị **"Chuẩn mực đầu tư nhan sắc"** đặt dưới logo, chữ nhỏ in hoa giãn chữ. Đây là định vị chính thức trong [[BG-01-ho-so-thuong-hieu]] — ⛔ không tự chế khẩu hiệu khác.

## 1c. MỘT ĐIỂM NHẤN MỖI TRANG

> Lỗi hay gặp nhất của báo giá do AI dựng: **nhồi mọi thứ vào một trang, cái gì cũng to, cái gì cũng có khung** — khách mở ra không biết nhìn đâu trước, và đóng lại.

Mỗi trang có **đúng một thứ to nhất**. Mọi thứ còn lại phải nhỏ hơn rõ rệt, không chỉ nhỏ hơn một chút.

| Trang | Điểm nhấn | Mọi thứ khác |
|---|---|---|
| **A4 trang 1** | **Tiêu đề lời hứa** (22pt) — thứ khách đọc đầu tiên | mong muốn · phương án · các bước: cỡ chữ thường |
| **A4 trang 2** | **Card phương án navy** | các bước · lưu ý · phương án khác: nền trắng |
| **A4 trang 3** | **Con số sau ưu đãi** trong dải navy | bảng chi phí · đã gồm/chưa gồm · lộ trình: nền trắng |
| **A4 trang 4** | **Khối CTA navy** | case · băn khoăn · miễn trừ: nền trắng |
| **Slide 1** | Tiêu đề lời hứa trên nền navy | — |
| **Slide 2** | Con số sau ưu đãi (50px, màu amber) | — |

Ba cách hạ cấp một khối mà không phải xoá nó: bỏ nền card → dùng vạch màu bên trái · giảm cỡ chữ xuống cỡ chú thích · xếp 2 cột thay vì 1 cột dọc.

⛔ **Không dùng quá 2 khối có nền đặc trên một trang.** Trang 1 chỉ có một (card phương án navy).

## 2b. BỐN TRANG A4 — khối nào nằm trang nào
```
Trang 1  VẤN ĐỀ    — lời hứa cá nhân hoá · điều khách đang gặp · vấn đề → cách xử lý
Trang 2  GIẢI PHÁP — phương án đề xuất · các bước · lưu ý riêng · phương án khác
Trang 3  CHI PHÍ   — bảng chi phí · ưu đãi · tổng sau ưu đãi · đã gồm/chưa gồm · lộ trình
Trang 4  BẰNG CHỨNG — case + ảnh trước–sau · album · băn khoăn · CTA · chữ ký · miễn trừ
```
> **Một mạch mỗi trang.** Trước đây gộp vấn đề và phương án chung trang 1 — khi thêm khối *vấn đề → cách xử lý* thì trang 1 phình lên 1.429px / ngưỡng 1.122px. Tách ra là vừa, và mạch đọc cũng đúng hơn: khách thấy mình được hiểu trước khi thấy con số.

## 2c. ĐỌC TRÊN ĐIỆN THOẠI

Phần lớn khách mở báo giá **trên điện thoại, trong lúc đang làm việc khác**. Ba file xuất ra phục vụ ba tình huống khác nhau:

| Khách nhận bằng | Gửi file nào | Vì sao |
|---|---|---|
| **Zalo · Messenger** | **3 ảnh JPG** | Hiện thẳng trong luồng chat, không phải tải, không phải phóng to |
| **Muốn lưu lại · đưa người nhà · in** | **PDF** | Đọc độc lập, in ra được |
| **Gửi link mở trên điện thoại** | **file HTML** | Tự co theo bề ngang màn hình |

**Điều kiện để HTML đọc được trên điện thoại — thiếu một là hỏng:**

1. **`<meta name="viewport" content="width=device-width, initial-scale=1">`.** Thiếu thẻ này, trình duyệt điện thoại dựng trang trong khung ảo ~980px rồi thu nhỏ toàn bộ — media query **không bao giờ khớp**, khách thấy bản A4 chữ li ti. Đây là lỗi im lặng: trên máy tính nhìn vẫn đúng.
2. **Khổ 210mm chỉ áp cho bản in.** Trên màn hình hẹp, `.page` chuyển sang `width:auto` — đó là thứ duy nhất gây kéo ngang, vì cỡ chữ vốn tính bằng `pt` (10,5pt = 14px) đã vừa đọc sẵn.
3. **Bảng chi phí 4 cột phải xếp dọc** dưới 620px: mỗi dòng thành một khối, nhãn cột sinh bằng `::before`. ⛔ Không để khách kéo ngang mới thấy được con số — đó đúng là thứ họ mở file ra để xem.
4. **Lưới 2 cột về 1 cột** (các bước phương án, ảnh case, khối liên hệ) và **chân trang chuyển `position:static`**, nếu không nó đè lên dòng cuối.
5. **Bản slide** tự thu cả khung 1080px vừa bề ngang bằng `zoom` — chạy **sau** vòng đo tràn khung, vì `zoom` làm lệch phép đo bằng `getBoundingClientRect`.

**Luật kiểm:** mở file HTML ở bề ngang **390px**. Không được có thanh cuộn ngang, và con số *chi phí sau ưu đãi* phải đọc được mà không phóng to.
⚠️ Chrome headless có bề ngang tối thiểu **500px** — chụp ở 390px sẽ ra ảnh bị cắt dù layout đúng. Đo bằng `matchMedia` thay vì tin vào ảnh chụp.

## 3. BA ẢNH — nội dung cố định

Bộ gửi Zalo **luôn đúng 3 ảnh**, không nhiều hơn. Gửi 6 ảnh vào một khung chat là bắt khách vuốt qua sáu lần trước khi thấy con số; ba ảnh thì đọc hết trong một lần vuốt.

```
1  Bìa + vấn đề  navy đặc · tên khách · tiêu đề · từng cặp vấn đề → cách xử lý
2  Giải pháp+tiền card phương án · bảng chi phí · tổng sau ưu đãi (số lớn nhất)
3  Bằng chứng    case tương tự · 3 ô ảnh thật · album · khối CTA · liên hệ
```

Mỗi ảnh trả lời đúng một câu của khách: *"họ có hiểu tôi không"* → *"làm gì, bao nhiêu"* → *"ai giống tôi đã làm, giờ tôi làm gì tiếp"*.

| Luật | |
|---|---|
| Số ảnh | **luôn 3**. Thiếu case thì ảnh 3 chỉ còn phần CTA, không bỏ ảnh |
| Dung lượng chữ | ≤ **170 chữ** mỗi ảnh (trước đây 120 khi còn 6 ảnh) |
| Lộ trình & các bước phương án | **không lên ảnh** — chúng nằm ở PDF. Ảnh là bản liếc qua, PDF là bản đọc kỹ |
| Ảnh 1 | là slide **duy nhất không có `.than`** → có vòng đo tràn khung riêng, xem mục 6 |

## 4. TYPOGRAPHY
```css
"Google Sans","Google Sans Text","Product Sans","Be Vietnam Pro","Segoe UI",Roboto,…
```

**Google Sans là font nội bộ của Google** — không bán, không có trên Google Fonts, không được phép nhúng lại. Nó đứng đầu danh sách để máy nào *đã có sẵn* thì dùng; máy không có (gần như tất cả) rơi xuống **Be Vietnam Pro** — font mở, thiết kế riêng cho tiếng Việt nên dấu chồng (ồ, ể, ữ) dựng đúng, hình chữ hình học gần với Google Sans.

Font **nhúng thẳng vào file** dưới dạng data URI, không dùng `<link>` tới CDN:
```bash
python tools/nhung-font.py                    # sinh template/font-nhung.css (~225 KB)
python tools/nhung-font.py --font "Inter"     # đổi sang font khác
```
⛔ **Không `<link>` tới Google Fonts** — máy render có thể không có mạng, font tải chậm làm Chrome chụp hụt chữ, và file khách mở lại sau một tháng sẽ phụ thuộc CDN còn sống. Nhúng data URI giải quyết cả ba.

Thiếu `font-nhung.css` thì tool in cảnh báo và file vẫn ra, chỉ là dùng font hệ thống — **không gửi khách bản đó** nếu đang cần bản đúng nhận diện.

| Vai trò | A4 | Slide |
|---|---|---|
| Tiêu đề chính | 19pt/800 | 62–74px/800 |
| Tiêu đề khối | 12,5pt/800 | 42px/800 |
| Thân | 11,5pt | 30px |
| Chú thích / miễn trừ | 8,3–9pt | 21–25px |

Chữ nhỏ nhất trên slide gửi Zalo **không dưới 21px** — dưới mức đó khách đọc trên điện thoại sẽ bỏ qua.

## 5. ẢNH — ba ô, không phải hai
- **Ba ô ảnh** mỗi case: `anh_truoc` · `anh_sau` · `anh_them`. Ô thứ ba có thì lưới tự chuyển 3 cột.
- **Nhãn dưới ô đặt lại được**: `chu_thich_truoc` (mặc định *Trước*) · `chu_thich_sau` (mặc định lấy `moc_chup`) · `chu_thich_them` (mặc định *Góc khác*).
  > ⚠️ Ảnh trong Album Kangnam phần lớn **đã là ảnh ghép trước–sau sẵn**. Dán ba ảnh đó vào rồi để nhãn mặc định là sai: mỗi ô đã có cả trước lẫn sau. Lúc đó đặt nhãn kiểu *Ca 1 · Ca 2 · Ca 3*, hoặc tên kỹ thuật từng ca.
- Ô thứ ba **không có ô ảnh tạm** — hai ô trước–sau đã đủ để nhắc đi xin ảnh.
- Tỉ lệ ô ảnh case: **1:1**, `object-fit:cover`.
- Đường dẫn ảnh trong `du-lieu.json`: để **cùng thư mục** với file `du-lieu.json` rồi ghi tên file (`anh/truoc-01.jpg`), hoặc dùng URL tuyệt đối.
- Chưa có ảnh → để trống, template tự dựng **ô ảnh tạm** gạch chéo ghi rõ cần ảnh gì.
- ⛔ Không `<img>` trỏ tới URL không tồn tại — Chrome render ra ô vỡ, gửi khách là mất điểm.

## 6. TRÀN KHUNG
Slide có script tự thu nhỏ nội dung (zoom xuống tối đa 62%) khi tràn 1920px. Nội dung ngắn thì tự dồn vào giữa khung.

Thu hết cỡ mà vẫn tràn thì script gắn `data-tran` lên slide, và tool **đọc lại DOM bằng `--dump-dom`** để báo ra màn hình:
```
! Slide 1 TRÀN KHUNG — nội dung bị cắt ở mép dưới.
```
Phải đọc DOM mới biết, vì `overflow:hidden` **cắt gọn phần thừa** — ảnh chụp ra trông vẫn "đẹp", chỉ là mất mất đoạn cuối.

> Ảnh 1 (bìa) không có `.than` nên vòng đo cũ bỏ qua nó. Từ khi bìa gánh thêm lưới vấn đề thì nó cũng tràn được, nên có nhánh đo riêng: đo cả khung slide, thu khối giữa.
→ Thấy chữ nhỏ bất thường trong ảnh xuất ra nghĩa là **nội dung đang quá dài**: cắt bớt chữ, đừng chấp nhận bản thu nhỏ.

**A4 không thu nhỏ và không cắt chữ** — nội dung dài thì trang tự dãn sang trang in kế tiếp. Tool **đếm số trang PDF** sau khi render và cảnh báo nếu vượt 4:

```
=> PDF : ...pdf  (5 trang)
! Báo giá dài 5 trang, chuẩn là 4. Rút gọn lời mở, cặp vấn đề→giải pháp hoặc bước phương án.
```

Ba chỗ cắt được nhiều nhất mà không mất chất: lời mở (giữ đúng 3 câu) · số bước trong `giai_phap.gom` (4 bước là tối đa) · số câu hỏi ở khối băn khoăn (3 là tối đa).
⚠️ Đừng cắt dòng *đã gồm / chưa gồm* và khối miễn trừ để lấy chỗ — hai thứ đó bắt buộc.

## 7. DẤU NHÁP
Chạy `--nhap` → đóng dấu **NHÁP** chéo trang, dùng cho bản xem nội bộ khi cổng pháp lý còn lỗi CHẶN.
⛔ File có dấu NHÁP tuyệt đối không gửi khách.

## 8. SỬA TEMPLATE
Template dùng cú pháp mustache rút gọn do `tools/render_baogia.py` tự xử lý:

| Cú pháp | Nghĩa |
|---|---|
| `{{ten.truong}}` | chèn giá trị, tự thoát HTML |
| `{{{ten}}}` | chèn thô, không thoát (dùng khi chủ động chèn HTML) |
| `{{#ds}}…{{/ds}}` | lặp theo list, hoặc hiện khi giá trị "thật" |
| `{{^ds}}…{{/ds}}` | hiện khi rỗng/không có |
| `{{.}}` | phần tử hiện tại của list chuỗi |

⛔ Không bọc cả `<section>` bằng `{{#mot_list}}` — section sẽ lặp theo từng phần tử. Dùng cờ `co_case`, `co_lo_trinh`, `co_giai_toa`, `co_phuong_an_khac`, `co_luu_y` (tool tự tính).

Liên quan: [[BG-09-schema-du-lieu]] · [[BG-03-cau-truc-bao-gia]]
