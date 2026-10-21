# BG-08 — DESIGN SYSTEM ẤN PHẨM BÁO GIÁ
Version 1.0 · Token lấy nguyên từ `Agent-LDP-Kangnam/knowledge/KF-09-design-system.md` (production v3.0)
Cập nhật: 2026-10-21

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
| **A4 / PDF** | `template/baogia-a4.html` | 210×297mm, 3 trang | Gửi email, khách in ra, khách đưa người nhà xem |
| **Slide / JPG** | `template/baogia-slide.html` | 1080×1920, 5 ảnh | Gửi Zalo / Messenger — khách xem ngay trong luồng chat |

> Mặc định xuất **cả hai**. Khách chat Zalo thường không mở PDF; khách cần bàn với người nhà thì cần PDF.

## 2b. BA TRANG A4 — khối nào nằm trang nào
```
Trang 1  khối 1 đầu trang · 2 tiêu đề + lời mở · 3 điều khách mong muốn · 4 phương án
Trang 2  khối 5 chi phí · trả góp · 6 phương án khác · 8 lộ trình
Trang 3  khối 7 case + album · 9 băn khoăn + CTA · chân trang miễn trừ
```
> Lộ trình nằm ở **trang 2** chứ không phải trang 3: trang 2 thường còn chỗ sau bảng chi phí, còn trang 3 phải đủ chỗ cho case, băn khoăn, CTA và khối miễn trừ. Đổi lại thứ tự này là trang 3 tràn sang trang 4.

## 3. NĂM SLIDE — nội dung cố định
```
1  Bìa      navy đặc · tên khách · tiêu đề cá nhân hoá · mã báo giá
2  Phương án mong muốn của khách (chip) + phương án + các bước
3  Chi phí  bảng rút gọn + tổng sau ưu đãi (số lớn nhất) + trả góp
4  Case     case tương tự + ảnh trước–sau + câu miễn trừ   (ẩn nếu không có case)
5  Bước tiếp lộ trình + khối CTA + miễn trừ
```
Tool tự đếm số slide thật và chụp từng ảnh; thiếu case thì còn 4 ảnh.

## 4. TYPOGRAPHY
Một họ chữ hệ thống: `"Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`.
⛔ **Không nhúng Google Fonts** — máy render có thể không có mạng, và font tải chậm làm Chrome chụp hụt.

| Vai trò | A4 | Slide |
|---|---|---|
| Tiêu đề chính | 19pt/800 | 62–74px/800 |
| Tiêu đề khối | 12,5pt/800 | 42px/800 |
| Thân | 11,5pt | 30px |
| Chú thích / miễn trừ | 8,3–9pt | 21–25px |

Chữ nhỏ nhất trên slide gửi Zalo **không dưới 21px** — dưới mức đó khách đọc trên điện thoại sẽ bỏ qua.

## 5. ẢNH
- Tỉ lệ ô ảnh case: **1:1**, `object-fit:cover`.
- Đường dẫn ảnh trong `du-lieu.json`: để **cùng thư mục** với file `du-lieu.json` rồi ghi tên file (`anh/truoc-01.jpg`), hoặc dùng URL tuyệt đối.
- Chưa có ảnh → để trống, template tự dựng **ô ảnh tạm** gạch chéo ghi rõ cần ảnh gì.
- ⛔ Không `<img>` trỏ tới URL không tồn tại — Chrome render ra ô vỡ, gửi khách là mất điểm.

## 6. TRÀN KHUNG
Slide có script tự thu nhỏ nội dung (zoom xuống tối đa 62%) khi tràn 1920px, và ghi cảnh báo ra console. Nội dung ngắn thì tự dồn vào giữa khung.
→ Thấy chữ nhỏ bất thường trong ảnh xuất ra nghĩa là **nội dung đang quá dài**: cắt bớt chữ, đừng chấp nhận bản thu nhỏ.

**A4 không thu nhỏ và không cắt chữ** — nội dung dài thì trang tự dãn sang trang in kế tiếp. Tool **đếm số trang PDF** sau khi render và cảnh báo nếu vượt 3:

```
=> PDF : ...pdf  (4 trang)
! Báo giá dài 4 trang, chuẩn là 3. Rút gọn lời mở, bước phương án hoặc khối băn khoăn.
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
