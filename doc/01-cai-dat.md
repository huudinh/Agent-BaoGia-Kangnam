# 01 — CÀI ĐẶT (20 phút)

Agent này có **hai nửa**:
- **Nửa não** — prompt + knowledge, chạy trên Claude / ChatGPT / Gemini. Không cần cài gì lên máy.
- **Nửa tay** — `tools/render_baogia.py`, biến dữ liệu thành PDF + JPG. Cần Python và Chrome (hầu hết máy đã có sẵn).

Dùng được nửa não mà chưa có nửa tay thì vẫn ra nội dung báo giá, chỉ là phải tự trình bày.

---

> 📘 **Bản web của tài liệu này:** <https://claude.ai/artifact/WZuxB6N8YyEH4mQoCboJFj>
> Có nút Copy sẵn cho bộ não và từng file tri thức — đỡ phải mở file thủ công. Nội dung lấy thẳng từ repo nên luôn khớp.

## 0. Lấy code về máy (làm trước tiên)

**Repo:** <https://github.com/huudinh/Agent-BaoGia-Kangnam>

**Cách 1 — tải ZIP, không cần biết git:**
1. Mở <https://github.com/huudinh/Agent-BaoGia-Kangnam/archive/refs/heads/main.zip>
2. Chuột phải file ZIP → **Extract All…** → chọn thư mục.
   ⛔ **Đừng kéo file trực tiếp từ cửa sổ xem ZIP** — đây là lỗi hay gặp nhất, file ra thiếu và tool báo không tìm thấy template.
3. Thư mục dùng sau khi giải nén: `Agent-BaoGia-Kangnam-main\` — mọi lệnh trong tài liệu này chạy từ đây.

**Cách 2 — clone (nhận bản cập nhật bằng `git pull`):**
```bash
git clone https://github.com/huudinh/Agent-BaoGia-Kangnam.git
cd Agent-BaoGia-Kangnam
```

> Thư mục `out/` **không có trong repo** (đã `.gitignore`). File báo giá chứa thông tin khách hàng — không commit lên GitHub, kể cả repo riêng tư.

---

## 0b. Ba ô phải điền khi tạo agent mới

Nền tảng nào cũng hỏi ba ô này. Dán sẵn cho khớp — tên đặt lệch thì sau này tìm không ra giữa mấy agent anh em.

**Tên**
```
Agent-BaoGia-Kangnam
```

**Mô tả** — 225 ký tự, nằm dưới giới hạn 300 của ChatGPT. Đây là dòng người dùng thấy **trước khi mở agent**, đừng để trống.
```
Tạo báo giá cá nhân hoá cho từng khách hàng Kangnam: đọc thông tin khách, chọn phương án theo bảng giá chính thức, viết nội dung đã qua cổng pháp lý, rồi xuất ra PDF A4 và 3 ảnh gửi Zalo. Không bịa giá, không cam kết kết quả.
```

**Câu mở đầu hội thoại** — ô *Conversation starters* của ChatGPT. Claude và Gemini không có ô này, cứ dán vào chat lần đầu.
```
/baogia — em dán đoạn chat với khách vào đây
/wizard cắt mí
/tinnhan cho báo giá vừa làm
/kiemtra câu này có vi phạm gì không
```

> Ba ô này nằm sẵn trong [trang hướng dẫn](https://claude.ai/artifact/WZuxB6N8YyEH4mQoCboJFj) kèm nút Copy — tiện hơn copy từ file này.

---

## A. Nửa não — Claude Project (khuyến nghị)

1. Vào [claude.ai](https://claude.ai) → **Projects** → **Create project**. Tên: `Agent-BaoGia-Kangnam`.
2. Mở [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) → copy **toàn bộ khối giữa hai vạch ▼▲** → dán vào **Custom instructions**.
3. Vào **Project knowledge** → upload **2 file** trong [`goi/`](../goi/):

```
goi/KANGNAM-tri-thuc.md         96 KB — gộp đủ 11 file BG-01…BG-11
goi/KANGNAM-du-lieu-cung.json   34 KB — bảng giá · 29 album ảnh · hotline · mẫu JSON
```

> **Vì sao gộp:** Gemini Gems chỉ cho **tối đa 10 file** tri thức, và upload 15 file một lượt rất hay lỗi. Hai file này **cùng nội dung** với `knowledge/` + `template/*.json`, chỉ khác chỗ nằm — bộ não biết cả hai cách.
> Sinh lại sau khi sửa tri thức: `python tools/build-goi.py`. ⛔ Không sửa tay file trong `goi/`.

4. Muốn agent tự dựng được PDF/ảnh thì upload thêm `tools/baogia-1file.py` — **tổng 3 file**.

<details><summary>Thích nạp bản rời 15 file?</summary>

Vẫn chạy được: upload `knowledge/BG-01…BG-11.md` (11 file) + `template/bang-gia.json`, `template/album-index.json`, `template/thong-tin-lien-he.json`, `template/du-lieu.mau.json`. Bộ não ưu tiên bản rời khi thấy cả hai.
</details>

**Kiểm nhanh agent đã cài đúng:**
> Gõ: *"/baogia — khách muốn nâng ngực ở viện Kangnam Cần Thơ, ngân sách 50 triệu."*
> Agent **phải dừng lại**: nâng ngực là đại phẫu, chỉ thực hiện ở tuyến bệnh viện.
> Nó vui vẻ dựng báo giá → knowledge chưa nạp hoặc instructions dán thiếu.

---

## B. ChatGPT Custom GPT

Ô Instructions giới hạn **8.000 ký tự** → dùng bản ngắn.

1. ChatGPT → **Explore GPTs** → **Create** → tab **Configure**.
2. Name: `Agent-BaoGia-Kangnam`. Instructions: copy khối ▼▲ của [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) — dưới giới hạn 8.000 ký tự.
3. **Knowledge:** upload **2 file** trong `goi/` như mục A bước 3 (+ `tools/baogia-1file.py` nếu muốn dựng file ngay trong ChatGPT).
4. Tắt Web Browsing nếu không cần.

> ⚠️ Bản ngắn đã cắt nhiều luật chi tiết và **trông vào knowledge để bù**. Không nạp knowledge thì nó sẽ đoán, và đoán sai ở chỗ giá và pháp lý.

## C. Gemini (Gems)
Gemini → **Gems** → **New Gem** → dán khối ▼▲ của `SYSTEM-PROMPT.md` vào ô **Chỉ dẫn** → upload **2 file** trong `goi/`.
> Gems giới hạn **10 file**, nên bản rời 15 file **không nạp đủ** — phải dùng bản gộp.

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
=> PDF    : out\MAU\BG-2026-1021-01.pdf  (4 trang)
=> ảnh 1..5 : out\MAU\BG-2026-1021-01-0X.jpg
```

**Chrome ở chỗ khác thường:**
```bash
set KN_CHROME=D:\Apps\Chrome\chrome.exe        (cmd)
$env:KN_CHROME = "D:\Apps\Chrome\chrome.exe"   (PowerShell)
```
Không có Chrome → chạy `--chi-html` rồi mở file HTML, Ctrl+P → **Save as PDF**.

---

## E2. Không cài được Python? Dùng bản một-file trên ChatGPT

`tools/baogia-1file.py` (156 KB) gói sẵn **mọi thứ**: tool render, cổng pháp lý, hai template, bảng giá, danh sách bác sĩ, hotline, logo. Lúc chạy nó bung ra thư mục tạm rồi gọi đúng `render_baogia.py` của repo — không chép lại logic nên không lệch bản gốc.

```bash
# chạy thẳng trên máy — chỉ cần đúng file này, không cần cả repo
python baogia-1file.py du-lieu.json              # HTML + PDF + 3 ảnh (cần Chrome)
python baogia-1file.py du-lieu.json --chi-html   # chỉ HTML (chạy được ở ChatGPT)
```

**Trên ChatGPT:** bật **Code Interpreter** → upload `baogia-1file.py` vào Knowledge → mỗi lần làm báo giá chỉ cần dán JSON và bảo nó chạy lệnh `--chi-html` → tải file HTML về → mở bằng Chrome → **Ctrl+P** → **Lề: Không** + **bật Đồ hoạ nền** → Save as PDF.

⛔ **Ảnh JPG gửi Zalo không dựng được ở ChatGPT** (sandbox không có Chrome). Máy nào cũng có Chrome sẵn, nên cài thêm Python rồi chạy thẳng trên máy là ra đủ.

> Sửa template hoặc bảng giá xong, nhớ chạy lại `python tools/build-1file.py` rồi upload bản mới.

---

## F. Ba việc phải làm trước khi dùng thật

| # | Việc | Ai làm |
|---|---|---|
| 1 | **Xác nhận bảng giá** đang dùng là bản mới nhất; chốt mức giảm phí sửa mí theo từng khu vực và giá lipo mini | Vận hành + bệnh viện |
| 2 | **Chốt danh sách bác sĩ được duyệt quảng bá** (KF-02) và sửa `bac-si-duyet.json` theo đó | Pháp chế + Chuyên môn |
| 3 | **Chốt câu chữ bảo hành** thay cho cụm "bảo hành trọn đời" đang vi phạm R1 | Pháp chế |

Ba việc này không làm thì agent vẫn chạy, nhưng mỗi báo giá sẽ kèm một dòng `[CHỜ XÁC NHẬN]` mà người lập phải tự xử lý.
