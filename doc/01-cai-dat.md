# 01 — CÀI ĐẶT (20 phút)

Agent này có **hai nửa**:
- **Nửa não** — prompt + knowledge, chạy trên Claude / ChatGPT / Gemini. Không cần cài gì lên máy.
- **Nửa tay** — `tools/render_baogia.py`, biến dữ liệu thành PDF + JPG. Cần Python và Chrome (hầu hết máy đã có sẵn).

Dùng được nửa não mà chưa có nửa tay thì vẫn ra nội dung báo giá, chỉ là phải tự trình bày.

---

## A. Nửa não — Claude Project (khuyến nghị)

1. Vào [claude.ai](https://claude.ai) → **Projects** → **Create project**. Tên: `Agent-BaoGia-Kangnam`.
2. Mở [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) → copy **toàn bộ khối giữa hai vạch ▼▲** → dán vào **Custom instructions**.
3. Vào **Project knowledge** → upload **đủ 11 file** trong [`knowledge/`](../knowledge/):

```
BG-01-ho-so-thuong-hieu.md   thương hiệu · giọng · cơ sở & tuyến · bác sĩ
BG-02-bang-gia.md            luật nói về tiền            ← quan trọng
BG-03-cau-truc-bao-gia.md    9 khối — xương sống
BG-04-chan-dung-khach.md     6 nhóm khách · 6 giai đoạn  ← lõi cá nhân hoá
BG-05-noi-so-phan-doi.md     thư viện câu trả lời
BG-06-proof-case.md          case & ảnh trước–sau
BG-07-cong-phap-ly.md        cổng chặn                   ← quan trọng nhất
BG-08-design-system.md       khổ ấn phẩm · màu · độ dài
BG-09-schema-du-lieu.md      cấu trúc du-lieu.json
BG-10-vong-hoc.md            ghi kết quả
BG-11-noi-dau-cat-mi.md      9 chân dung cắt mí + giá Plasma  ← dịch vụ bán chạy
```

4. Upload thêm **hai file dữ liệu cứng** (bắt buộc, không có thì agent sẽ đoán giá):
```
template/bang-gia.json        nguồn giá duy nhất
template/bac-si-duyet.json    ai được nêu tên
```
5. Nên upload thêm `template/du-lieu.mau.json` để agent sinh JSON đúng cấu trúc ngay lần đầu.

**Kiểm nhanh agent đã cài đúng:**
> Gõ: *"/baogia — khách muốn nâng ngực ở viện Kangnam Cần Thơ, ngân sách 50 triệu."*
> Agent **phải dừng lại**: nâng ngực là đại phẫu, chỉ thực hiện ở tuyến bệnh viện.
> Nó vui vẻ dựng báo giá → knowledge chưa nạp hoặc instructions dán thiếu.

---

## B. ChatGPT Custom GPT

Ô Instructions giới hạn **8.000 ký tự** → dùng bản ngắn.

1. ChatGPT → **Explore GPTs** → **Create** → tab **Configure**.
2. Name: `Agent-BaoGia-Kangnam`. Instructions: copy khối ▼▲ của [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) (5.135 ký tự).
3. **Knowledge:** upload đủ 10 file `knowledge/` + `bang-gia.json` + `bac-si-duyet.json`.
4. Tắt Web Browsing nếu không cần.

> ⚠️ Bản ngắn đã cắt nhiều luật chi tiết và **trông vào knowledge để bù**. Không nạp knowledge thì nó sẽ đoán, và đoán sai ở chỗ giá và pháp lý.

## C. Gemini (Gems)
Gemini → **Gems** → **New Gem** → dán khối ▼▲ của `SYSTEM-PROMPT.md` vào ô **Chỉ dẫn** → upload knowledge + 2 file JSON.

## D. Claude Code / VS Code (không cần tạo project)
Mở thư mục này rồi gõ:
> *"Đọc SYSTEM-PROMPT.md và toàn bộ knowledge/, rồi đóng vai agent đó. Tôi bắt đầu bằng /baogia."*

Cách này tiện nhất vì agent **chạy được luôn tool render** — không phải copy JSON qua lại.

---

## E. Nửa tay — tool render

**Cần:** Python 3.9+ · Google Chrome hoặc Microsoft Edge · (tuỳ chọn) Pillow để xuất JPG.

```bash
python --version          # kiểm tra Python
python -m pip install pillow   # không có Pillow thì ảnh ra PNG, vẫn gửi được
```

**Chạy thử ngay với dữ liệu mẫu:**
```bash
cd Agent-BaoGia-Kangnam
mkdir out\MAU
copy template\du-lieu.mau.json out\MAU\du-lieu.json
python tools\render_baogia.py out\MAU\du-lieu.json
```

Kết quả đúng phải là:
```
cổng dữ liệu  : PASS
cổng bảng giá : PASS
=> PDF    : out\MAU\BG-2026-1021-01.pdf
=> ảnh 1..5 : out\MAU\BG-2026-1021-01-0X.jpg
```

**Chrome ở chỗ khác thường:**
```bash
set KN_CHROME=D:\Apps\Chrome\chrome.exe        (cmd)
$env:KN_CHROME = "D:\Apps\Chrome\chrome.exe"   (PowerShell)
```
Không có Chrome → chạy `--chi-html` rồi mở file HTML, Ctrl+P → **Save as PDF**.

---

## F. Ba việc phải làm trước khi dùng thật

| # | Việc | Ai làm |
|---|---|---|
| 1 | **Xác nhận bảng giá** đang dùng là bản mới nhất; chốt mức giảm phí sửa mí theo từng khu vực và giá lipo mini | Vận hành + bệnh viện |
| 2 | **Chốt danh sách bác sĩ được duyệt quảng bá** (KF-02) và sửa `bac-si-duyet.json` theo đó | Pháp chế + Chuyên môn |
| 3 | **Chốt câu chữ bảo hành** thay cho cụm "bảo hành trọn đời" đang vi phạm R1 | Pháp chế |

Ba việc này không làm thì agent vẫn chạy, nhưng mỗi báo giá sẽ kèm một dòng `[CHỜ XÁC NHẬN]` mà người lập phải tự xử lý.
