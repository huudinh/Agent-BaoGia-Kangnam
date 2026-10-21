# Agent-BaoGia-Kangnam

**Agent biến thông tin một khách hàng cụ thể thành một tờ báo giá cá nhân hoá — xuất ra PDF và ảnh JPG gửi thẳng cho khách.**

Kiêm ba vai: **50% tư vấn viên y khoa · 30% copywriter chuyển đổi · 20% kiểm soát tuân thủ.**

Đầu vào: thông tin khách hàng (hoặc nguyên đoạn chat).
Đầu ra: **1 file PDF A4 4 trang** (gửi email, in, đưa người nhà xem) + **3 ảnh JPG 1080×1920** (gửi Zalo/Messenger).

Đo bằng 4 chỉ số, không có chỉ số thứ 5: **tỉ lệ phản hồi · tỉ lệ đặt khám · tỉ lệ show-up · tỉ lệ chốt.**
Không tối ưu cho "file đẹp". Một tờ báo giá đẹp mà không ai đặt khám là một tờ thất bại.

> **Bắt đầu nhanh:** chưa từng dùng agent nào → [`doc/04-prompt-nguoi-moi.md`](doc/04-prompt-nguoi-moi.md). Muốn cài ngay → [`doc/01-cai-dat.md`](doc/01-cai-dat.md).

## 📘 Hướng dẫn cài đặt

**<https://claude.ai/artifact/WZuxB6N8YyEH4mQoCboJFj>**

Trang gồm đúng ba mục: **① Cài đặt** — nút tải ZIP, 5 bước, 4 tab nền tảng, ba thẻ Copy bộ não và **thẻ copy từng file tri thức + dữ liệu cứng** · **② 25 prompt mẫu** copy được, 5 nhóm lọc (có nhóm *Hỏi dẫn* cho người chưa có thông tin khách) · **③ Kiến thức** — bảng 11 file, ba cổng chặn, chính sách giá cắt mí Plasma, album ảnh và việc còn treo.

> Nội dung trong trang lấy thẳng từ repo này nên luôn khớp bản mới nhất. Dựng lại sau khi sửa knowledge hoặc bảng giá: `python tools/build-huong-dan.py` rồi republish cùng URL.

---

## 📦 Lấy code

**Repo:** <https://github.com/huudinh/Agent-BaoGia-Kangnam>

| Cách | Làm gì |
|---|---|
| **Tải ZIP** (không cần biết git) | <https://github.com/huudinh/Agent-BaoGia-Kangnam/archive/refs/heads/main.zip> → giải nén bằng **Extract All**, ⛔ đừng kéo file trực tiếp từ cửa sổ ZIP (lỗi hay gặp nhất) |
| **Clone** | `git clone https://github.com/huudinh/Agent-BaoGia-Kangnam.git` |
| **Cập nhật bản mới** | `git pull` — hoặc tải lại ZIP và **giữ lại thư mục `out/` của bạn** |

Thư mục `out/` không nằm trong repo (đã `.gitignore`) — file báo giá của khách là dữ liệu cá nhân, không commit lên GitHub.

---

## 1. Vì sao agent này tồn tại

Phần lớn báo giá thẩm mỹ thất bại không vì giá cao, mà vì **nó là bảng giá chung có điền tên khách**. Triệu chứng quen thuộc:

| Triệu chứng | Nguyên nhân thật |
|---|---|
| Khách nhận file xong im luôn | File mở đầu bằng con số, khách đem đi so giá với nơi khác |
| Khách hỏi lại "sao đắt thế" | Thiếu dòng *đã gồm / chưa gồm* — khách sợ phát sinh chứ không sợ đắt |
| Khách nói "để em hỏi người nhà" rồi mất hút | File không đọc độc lập được, người nhà không có bối cảnh |
| Mỗi tư vấn viên báo một giá | Không có nguồn giá duy nhất, ai cũng "ưu đãi riêng" |
| Lỡ hứa "không đau", "3 ngày đi làm được" | Không ai rà trước khi gửi — và đây là rủi ro pháp lý, không phải lỗi đánh máy |

Agent này xử lý cả năm, bằng một quy trình cố định và ba cổng chặn.

## 2. Luật nền — bốn điều

**① Cá nhân hoá nằm ở nội dung, không nằm ở chỗ điền tên.**
Nhắc lại **đúng chữ khách đã nói** rồi gắn phương án vào đó.

**② Giá đứng sau lý do.** Khối chi phí chỉ xuất hiện sau khi đã giải thích vì sao phương án này hợp.

**③ Không chẩn đoán, không chốt giá thay bác sĩ.** Mọi phương án là đề xuất mang tới buổi khám.

**④ CTA là ĐẶT KHÁM, không phải CHUYỂN CỌC.**

## 3. Quy trình 4 bước — không đảo, không bỏ

```
B1 ĐỌC KHÁCH      → nhóm 1-6 · giai đoạn · 2-3 nỗi lo thật
B2 CHỌN PHƯƠNG ÁN → tra bang-gia.json, mỗi dòng chi phí có mã
B3 VIẾT 9 KHỐI    → thứ tự cố định, giọng theo nhóm khách
B4 KIỂM & XUẤT    → 3 cổng chặn → du-lieu.json → PDF + JPG
```

### Chín khối của một tờ báo giá

| # | Khối | Trả lời câu hỏi ngầm |
|---|---|---|
| 1 | Đầu trang + mã báo giá | "Có phải gửi riêng cho mình không?" |
| 2 | Tiêu đề + lời mở | "Họ có nhớ mình nói gì không?" |
| 3 | Điều khách mong muốn | "Họ hiểu đúng vấn đề của mình chưa?" |
| 4 | Phương án đề xuất | "Làm gì, vì sao là cái này?" |
| 5 | Chi phí | "Bao nhiêu, gồm gì, có phát sinh không?" |
| 6 | Phương án khác | "Có lựa chọn nào khác không?" |
| 7 | Case tương tự + ảnh | "Có ai giống mình đã làm chưa?" |
| 8 | Lộ trình | "Rồi sao nữa? Mất bao lâu?" |
| 9 | Băn khoăn + CTA | "Mình có phải quyết ngay không?" |

## 4. Cấu trúc thư mục

```
Agent-BaoGia-Kangnam/
├── SYSTEM-PROMPT.md          bộ não đầy đủ (Claude/Gemini)
├── SYSTEM-PROMPT-NGAN.md     bản ngắn, dưới 8.000 ký tự (ChatGPT Custom GPT)
├── goi/                      2 file gộp để upload lên agent (sinh bằng build-goi.py)
├── knowledge/                11 file tri thức — bản rời
│   ├── BG-01-ho-so-thuong-hieu.md
│   ├── BG-02-bang-gia.md
│   ├── BG-03-cau-truc-bao-gia.md
│   ├── BG-04-chan-dung-khach.md
│   ├── BG-05-noi-so-phan-doi.md
│   ├── BG-06-proof-case.md
│   ├── BG-07-cong-phap-ly.md        ← quan trọng nhất
│   ├── BG-08-design-system.md
│   ├── BG-09-schema-du-lieu.md
│   ├── BG-10-vong-hoc.md
│   └── BG-11-noi-dau-cat-mi.md      ← chuyên sâu cắt mí: 9 chân dung + 10 nỗi lo
├── template/
│   ├── bang-gia.json         87 dịch vụ — NGUỒN GIÁ DUY NHẤT, đã đối chiếu web
│   ├── bac-si-duyet.json     22 hồ sơ, 4 trạng thái
│   ├── thong-tin-lien-he.json  hotline — NGUỒN DUY NHẤT
│   ├── logo-kangnam.png      logo thật, tool nhúng vào file xuất ra
│   ├── baogia-a4.html        khổ A4 → PDF
│   ├── baogia-slide.html     1080×1920 → JPG
│   ├── banggia.html          bảng giá một nhóm dịch vụ → HTML
│   ├── khach-hang.mau.json   mẫu đầu vào
│   ├── du-lieu.mau.json      mẫu ca cắt mí lần đầu
│   └── du-lieu.mau-sua-mi.json  mẫu ca sửa mí (giá ưu đãi + phí sửa mí + link album)
├── tools/
│   ├── render_baogia.py      3 cổng chặn + render qua Chrome headless
│   ├── render_banggia.py     bảng giá một nhóm dịch vụ
│   ├── doi_chieu_gia_web.py  so bảng giá repo với web chính thức
│   ├── anh_album.py          lấy link ảnh khách thật từ Album Kangnam
│   ├── cong_phap_ly.py       quét rào R0-R12 + bảng từ cấm
│   ├── baogia-1file.py       ★ CẢ BỘ TRONG MỘT FILE — upload lên ChatGPT
│   ├── build-1file.py        dựng file trên (chạy lại sau khi sửa template)
│   ├── build-huong-dan.py    dựng trang hướng dẫn từ nội dung thật trong repo
│   └── huong-dan.tpl.html    template trang hướng dẫn (sửa file này, không sửa .html sinh ra)
├── prompts/                  mẫu prompt copy được
├── doc/                      cài đặt · lệnh · output mẫu · CHANGELOG
└── out/                      file xuất ra (không commit)
```

## 5. Tám lệnh

| Lệnh | Việc |
|---|---|
| `/baogia` | lệnh chính — từ thông tin khách ra `du-lieu.json` + lệnh render |
| `/banggia` | bảng giá **một nhóm dịch vụ** ra HTML — khi khách mới hỏi, chưa có gì để cá nhân hoá |
| `/wizard` | hỏi dẫn 3 vòng × 3 câu, hoặc đọc thẳng đoạn chat với khách |
| `/tinnhan` | tin nhắn Zalo/Messenger gửi kèm file (≤ 60 chữ) |
| `/doichieu` | soi báo giá làm tay với bảng giá chuẩn, chỉ chỗ lệch |
| `/kiemtra` | chạy cổng pháp lý trên chữ đã viết |
| `/lo` | làm hàng loạt từ danh sách khách |
| `/hoc` | ghi kết quả thật vào vòng học |

Chi tiết: [`doc/02-cau-lenh.md`](doc/02-cau-lenh.md) · mẫu prompt: [`prompts/`](prompts/).

## 6. Ba cổng chặn — tính năng, không phải lỗi

```
CỔNG DỮ LIỆU   thiếu trường bắt buộc
CỔNG BẢNG GIÁ  mã không có trong bang-gia.json · giá lệch mà không khai lý do ·
               dịch vụ "liên hệ" bị tự đặt số
CỔNG PHÁP LÝ   từ cấm (R1) · mốc hồi phục cứng · nêu trả góp (KN-②) ·
               đại phẫu sai tuyến (R3) · tên thương mại thuốc (R7) · nghi CCCD
               (ảnh cơ thể R12 chỉ cảnh báo, người gửi tự quyết)
```

**Fail = không xuất file.** Không có ngoại lệ vì khách đang chờ.
Cần xem bố cục khi còn lỗi → `--nhap`, file ra đóng dấu **NHÁP** và không được gửi khách.

> ⛔ **Không có quy trình phê duyệt ở đây.** Đây là báo giá tham khảo gửi riêng một khách, không phải ấn phẩm phát hành — nên không có "bộ phận có thẩm quyền", không đối chiếu danh sách bác sĩ duyệt, không hỏi consent từng tấm ảnh. Cuối mỗi báo giá agent chỉ in **F. LIẾC QUA TRƯỚC KHI GỬI**: 2–3 câu ngắn.

## 7. Nguồn dữ liệu — mỗi loại một nguồn đúng

| Loại | Nguồn đúng duy nhất | ⛔ Không lấy từ |
|---|---|---|
| Giá | `template/bang-gia.json` | trí nhớ, báo giá cũ, lời đồng nghiệp |
| Ảnh case | Album Kangnam — khai `case_album.album`, tool tự lấy | ảnh stock, ảnh AI, ảnh trên mạng |
| Ưu đãi | thông báo nội bộ có số hiệu | "tháng này hình như có giảm" |
| Hotline | `template/thong-tin-lien-he.json` | gõ tay vào từng báo giá |
| Màu & khổ | `BG-08-design-system` | tự chọn |

## 7b. Cắt mí — dịch vụ đã có tri thức chuyên sâu
[`BG-11-noi-dau-cat-mi.md`](knowledge/BG-11-noi-dau-cat-mi.md) gom **9 chân dung khách** (4 nhóm chưa từng làm mí + 5 nhóm đã làm nhưng chưa hài lòng), **10 nỗi lo trước khi quyết định** kèm câu trả lời đã qua cổng pháp lý, cách mô tả **giải pháp dao Plasma** đúng luật, và **chính sách giá**:

| Trường hợp | Thực thu |
|---|---|
| Cắt mí lần đầu | niêm yết 10.000.000đ → **ưu đãi 8.000.000đ** |
| Sửa mí | 8.000.000đ + phí sửa mí 1.500.000–1.800.000đ → **tổng 9,5–9,8 triệu** |

Chạy thử ca sửa mí: `python tools\render_baogia.py out\MAU2\du-lieu.json` (nguồn: `template/du-lieu.mau-sua-mi.json`).

## 8. Còn 9 việc cần người thật chốt
Xem *Việc còn treo* trong [`doc/CHANGELOG.md`](doc/CHANGELOG.md). Ưu tiên:
chốt câu chữ thay cụm "bảo hành trọn đời" (vi phạm R1) · xác nhận mức giảm phí sửa mí theo từng khu vực · xác nhận giá Lipo mini.

## 9. Quan hệ với các agent khác trong repo

| Agent | Quan hệ |
|---|---|
| `Kangnam-Agent-Factory` | nguồn gốc tri thức thương hiệu (K1–K4) và bảng giá |
| `Agent-LDP-Kangnam` | dùng chung design token (KF-09), rào pháp lý (KF-11), proof bank (KF-14) |
| `Agent-CRM-Automation` | nguồn trạng thái khách L1–L6; báo giá là bước sau hội thoại tư vấn |
| `Agent-AdsOptimize-Kangnam` | đưa khách vào phễu; agent này xử lý khúc cuối trước khi đặt khám |

## 10. Vòng học — bước duy nhất làm agent khá hơn
Sau mỗi tuần, đưa kết quả thật bằng `/hoc`: phản hồi · đặt khám · show-up · chốt.
Thấy mẫu lặp lại **≥ 5 ca** mới được rút thành luật và sửa vào knowledge. Một ca là giai thoại, không phải dữ liệu.
"# Agent-BaoGia-Kangnam" 
