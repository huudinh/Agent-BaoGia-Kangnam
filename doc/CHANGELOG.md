# CHANGELOG — Agent-BaoGia-Kangnam

## v2.4 — 2026-10-21 · Kangnam không có trả góp, bỏ hẳn

Vận hành xác nhận: **Kangnam không có chính sách trả góp.** Đây là việc còn treo số 6 từ v1.0 (*"chính sách trả góp chính thức — ngân hàng liên kết, số kỳ, phí chuyển đổi"*) — nay **đóng, bằng câu trả lời không**.

Trước v2.4, repo xử lý trả góp theo kiểu *"chỉ nêu khi có chính sách thật"*: template có khối **Chia nhỏ khoản đầu tư**, renderer tự chia `sau_uu_dai / so_ky`, hai mẫu dữ liệu đều ghi *"trả góp 0% qua thẻ tín dụng của ngân hàng liên kết"*, và `BG-05` còn mời khách trả góp khi khách lo chi phí. Cách đặt luật mềm như vậy chỉ đúng khi chính sách **có thể** tồn tại. Nó không tồn tại, nên thành ra cả bộ đang dạy agent hứa một cách thanh toán không có — thứ khách phát hiện ra **sau khi đã tới viện**.

**Bỏ:** khối trả góp trong `baogia-a4.html` và `baogia-slide.html` · phép chia `so_tien_moi_ky` trong `render_baogia.py` · trường `tra_gop` trong hai mẫu dữ liệu · câu hỏi *"chính sách trả góp này đúng với cơ sở … chứ?"* trong mục CÂN NHẮC · dòng trả góp trong bảng *việc còn treo* của trang hướng dẫn.

**Chặn hai tầng** — vì bỏ khỏi template không ngăn được agent viết chữ "trả góp" vào một ô văn bản khác:
- **Cổng dữ liệu** CHẶN trường `chi_phi.tra_gop`.
- **Cổng pháp lý** thêm rào **`KN-②`**, CHẶN *trả góp · trả dần · chia nhỏ … theo tháng/kỳ · trả theo tháng/kỳ · `<số tiền>/tháng`* ở mọi ô văn bản.

Rào này phải siết đúng chỗ. Bản đầu dùng `[0-9][^.;]{0,10}/\s*th[aá]ng` nên chặn luôn **"tái khám 1 lần/tháng"** — một lịch điều trị hợp lệ. Nay chỉ bắt khi trước `/tháng` là **số tiền** (`đ`, `triệu`, `tr`): *"2.867.000đ/tháng"* bị chặn, *"điều trị 2 lần/tháng"* đi qua. Tương tự, *"chia **lộ trình** theo giai đoạn"* đi qua — đó là chia **việc**, không chia **tiền**.

**Thay bằng ba cách thật** khi khách lo chi phí (`BG-02` mục 7, `BG-05` L6.3): ghi rõ từng khoản · đưa phương án vừa ngân sách ở khối *Phương án khác* · chia lộ trình theo giai đoạn điều trị. Câu mẫu trong `BG-05` đổi từ mời trả góp sang *"nếu khoản này đang quá tầm, em đưa chị một phương án thấp hơn và nói thẳng nó khác ở đâu — chị chọn, em không đẩy."*

Nhân đây sửa nốt **mọi chỗ còn ghi "3 trang / 5 ảnh"** của trước v2.3: `README` · `doc/01` `doc/02` `doc/03` `doc/04` · `BG-06` `BG-08` · ba file prompt · `build-huong-dan.py` · `huong-dan.tpl.html`. Bản ngắn thêm luật mới thì vọt lên 8.127 ký tự, phải dồn luật vào mục CHI PHÍ và cắt chỗ rườm → **7.951 / 8.000**.

---

## v2.3 — 2026-10-21 · dựng lại mạch đọc: vấn đề trước, tiền sau, bằng chứng cuối

Yêu cầu: *tham khảo* cách một email bán hàng dẫn dắt người đọc để tối ưu thiết kế — **không bắt chước giọng của nó**.

Thứ mượn là **mạch**, không phải giọng: gọi đúng vấn đề khách đang có → nói cách xử lý từng vấn đề → rồi mới tới tiền → rồi mới tới bằng chứng. Trước v2.3 tờ báo giá mở bằng *mong muốn của khách* viết thành mấy cái chip rời, rồi nhảy thẳng sang phương án — khách chưa thấy mình được hiểu đã phải đọc con số.

**Khối mới `van_de_giai_phap`** — 3–4 cặp, lưới hai cột **VẤN ĐỀ | CÁCH XỬ LÝ**:
- Bên trái là nỗi lo bằng **chữ khách đã nói**, không phải nỗi lo chung của ngành.
- Bên phải là **cơ chế xử lý thật + giới hạn trung thực**, theo khuôn ba nhịp của `BG-05`.
- Cổng dữ liệu đòi **ít nhất một trong hai**: `van_de_giai_phap` **hoặc** `giai_toa`.

Lần đầu thêm khối này vào thì cả hai mẫu **nói lặp ba nỗi lo y nguyên hai lần** (một lần ở lưới mới, một lần ở khối *băn khoăn*) và đội lên 5 trang. Nên hai khối thành **loại trừ nhau**: dùng `van_de_giai_phap` thì `giai_toa` chỉ giữ câu hỏi còn lại, hoặc bỏ. Chip *mong muốn* cũng tắt khi đã có lưới vấn đề — nó nói lại đúng thứ lưới vừa nói.

**A4: 3 → 4 trang, mỗi trang một việc.**
```
T1 VẤN ĐỀ     lời hứa cá nhân hoá · điều khách đang gặp · vấn đề → cách xử lý
T2 GIẢI PHÁP  phương án · các bước · lưu ý riêng · phương án khác
T3 CHI PHÍ    bảng chi phí · ưu đãi · tổng sau ưu đãi · đã gồm/chưa gồm · lộ trình
T4 BẰNG CHỨNG case + ảnh trước–sau · album · băn khoăn · CTA · chữ ký
```
Gộp vấn đề và phương án chung một trang làm trang 1 phình lên **1.429px / ngưỡng 1.122px**. Tách ra vừa hết tràn vừa đúng mạch hơn. Bỏ luôn luật cũ *"có ảnh case thật thì được thêm 1 trang"* — ảnh nằm ở trang 4, không đội thêm.

**Slide: 5 → 6 ảnh.** Slide 2 cũ nhồi cả vấn đề lẫn phương án; nay slide 2 là *vấn đề → cách xử lý* (xếp dọc cho vừa màn hình điện thoại), slide 3 là phương án.

Cập nhật theo: `BG-03` (khối 3b, mạch đọc, độ dài) · `BG-08` (bố cục 4 trang, 6 slide, điểm nhấn từng trang) · `BG-09` (schema) · hai bộ não. Bản ngắn phải cắt 242 ký tự chỗ trùng lặp để vẫn dưới 8.000.

---

## v2.2 — 2026-10-21 · đối chiếu bảng giá với web chính thức

Việc còn treo số 1 từ v1.0 — *"xác nhận bảng giá đang dùng là bản mới nhất"* — nay **đóng được**.

**`tools/doi_chieu_gia_web.py`** tải thẳng <https://benhvienthammykangnam.com.vn/bang-gia/>, đọc 9 bảng HTML, so từng dòng với `bang-gia.json` và chia bốn nhóm: KHỚP · LỆCH GIÁ · WEB CÓ REPO THIẾU · REPO CÓ WEB KHÔNG THẤY.

**Kết quả: 86 dòng trên web → 85 khớp, 0 lệch giá.** Bảng giá trong repo đúng.

Hai lỗi trong chính bộ so khớp, sửa trước khi tin kết quả:
- Hàm `khoa()` ban đầu **bỏ cả phần trong ngoặc**, nên *"Chỉnh hàm 1 hàm"* và *"Chỉnh hàm 1 hàm khó, ghép xương"* thành cùng một khoá → đẻ ra một "lệch giá" giả 59tr↔85,5tr. Nay so theo **tập từ (Jaccard)**, giữ nguyên phần trong ngoặc vì đó mới là thứ phân biệt.
- Duyệt **tuần tự** làm dòng web đứng trước giành mất mục của dòng đứng sau (*Tạo hình vú combo* cướp mục *Treo ngực sa trễ*) → thêm một "lệch giá" giả nữa. Nay **ghép cặp tốt nhất toàn cục**: xếp mọi cặp theo độ giống rồi lấy dần từ cao xuống.

**Thay đổi trong `bang-gia.json`** (81 → 87 dịch vụ):
- Thêm `ten_web` cho 10 mục web viết tên khác, để lần sau khớp tuyệt đối.
- Tách `spa.lien-he` gộp thành **5 dịch vụ Spa riêng** đúng như web; thêm `nha.danh-bong`.
- `mat.phi-sua-mi` đánh dấu `khong_tren_web` — đó là chính sách nội bộ.
- `nguon` ghi rõ đã đối chiếu web ngày nào bằng tool nào.

🔶 **Một lệch nguồn cần Vận hành chốt:** web niêm yết cắt mí Plasma **8.000.000đ**, chính sách nội bộ ghi niêm yết **10.000.000đ** + ưu đãi **8.000.000đ**. Khách trả 8.000.000đ ở cả hai cách hiểu — nhưng **chỉ in giá gạch ngang 10.000.000đ khi Vận hành xác nhận**. In một mức giảm giá không có thật là rủi ro, nên mục này mang cờ `canh_bao`.

---

## v2.1 — 2026-10-21 · đổi cổng duyệt thành trách nhiệm người gửi + ảnh thật từ album

**Nới ràng buộc "ai đã duyệt chưa", siết ràng buộc "đã điền đủ chưa".**

| | Trước | Nay |
|---|---|---|
| Tên bác sĩ chưa duyệt / xung đột | **CHẶN**, không xuất file | **CÂN NHẮC** — in câu hỏi, người gửi quyết |
| Ảnh thiếu consent / thiếu mốc chụp | **CHẶN** | **CÂN NHẮC** |
| Thiếu mô tả khách, câu *vì sao hợp*, dòng *đã gồm/chưa gồm*, lộ trình, khối băn khoăn | bỏ qua | **CHẶN** |

Lý do: chặn vì *"chưa thấy con dấu"* chỉ làm người dùng tìm đường lách, trong khi **người ngồi đó mới biết** bác sĩ nào đang được duyệt, ảnh nào đã xin phép. Thứ vẫn CHẶN cứng là cái **sai ngay trong chữ**: cam kết kết quả · mốc hồi phục cứng · đại phẫu sai tuyến · ảnh cơ thể — không ai duyệt cho đúng được.

Cuối mỗi lần render, tool in bảng **CÂN NHẮC TRƯỚC KHI GỬI**: chỉ gồm câu hỏi áp vào đúng báo giá đó, chốt bằng *"Người gửi là người chịu trách nhiệm cho bản này."* Cổng dữ liệu nay kiểm **17 trường**, mỗi trường thiếu in kèm lý do vì sao cần.

**Ảnh khách thật từ Album Kangnam.** Album có API công khai (khoá chỉ cần để liệt kê, tải ảnh thì không):

```bash
python tools/anh_album.py                            # 29 album
python tools/anh_album.py --album "cắt mí" --lay 2    # in sẵn JSON để dán
```

`render_baogia.py` **tự tải ảnh về nhúng data URI** — nhận link album, URL bất kỳ, hay file trên máy. Bản gửi khách tự đứng một mình: album đổi hay link chết thì file đã gửi vẫn nguyên. Lấy không được thì dựng ô ảnh tạm + cảnh báo, **không bao giờ để `<img>` trỏ vào link chết**.

Báo giá có ảnh thật được **thêm 1 trang** (3 → 4): ảnh trước–sau là thứ khách xem trước cả giá. Ảnh case đổi sang tỉ lệ 4/3 cho gọn. Bộ não được dạy **luôn tự đề xuất** gắn ảnh khi báo giá chưa có.

⛔ **Khoá API không nằm trong repo** — `template/album-key.local.json`, `.gitignore` chặn `*.local.json`. Repo là public.

> 🔧 Lỗi bắt được khi làm: cổng pháp lý quét cả chuỗi base64 của logo và "tìm thấy" chữ **HIV** → báo động giả PDPA. Chuỗi base64 dài chứa đủ mọi tổ hợp chữ cái nên chắc chắn trúng từ cấm. Nay bỏ qua chuỗi `data:` và chuỗi dài quá 4.000 ký tự.

---

## v2.0 — 2026-10-21 · lệnh `/banggia` + prompt nói thường

Prompt kiểu *"Tạo cho tôi bảng giá dịch vụ nâng mũi để gửi cho khách hàng bằng html"* là **việc hằng ngày** của tư vấn viên, nhưng agent chưa có năng lực đó — thêm prompt mà không có năng lực thì agent sẽ tự bịa bảng giá. Nên làm năng lực trước.

**`tools/render_banggia.py` + `template/banggia.html`** — xuất bảng giá **một nhóm dịch vụ** ra HTML tự đứng một mình (logo nhúng sẵn), kèm PDF nếu muốn.

- Lấy **đủ** dịch vụ trong nhóm từ `bang-gia.json`, không sót, không bịa.
- Bốn kiểu giá hiển thị đúng: cố định · khoảng · *từ X* · Liên hệ.
- **Ưu đãi đang chạy** in giá niêm yết gạch ngang kèm giá ưu đãi (cắt mí Plasma ~~10.000.000đ~~ → **8.000.000đ**).
- Dịch vụ **đại phẫu** tự sinh khối nhắc *chỉ thực hiện tại tuyến bệnh viện*.
- Mục có cờ `canh_bao` → in ra màn hình để người lập xác nhận trước khi gửi.
- Hotline từ `thong-tin-lien-he.json`, ba câu miễn trừ ở chân trang, đọc được trên điện thoại (bảng xếp dọc dưới 560px).
- Khớp tên nhóm kiểu dễ dãi: `mũi` · `mui` · `nâng mũi` đều ra nhóm **Mũi**.

**`prompts/prompt-bang-gia.md`** — 10 prompt viết theo **cách nhân viên gõ thật**, không phải cú pháp lệnh. Trang hướng dẫn nay có **36 prompt mẫu** và nhóm lọc mới *Bảng giá nhóm*.

⚠️ Luật đi kèm, có trong cả hai bộ não: **bảng giá cả nhóm là bước lùi so với báo giá cá nhân hoá** — khách cầm bảng giá chung rất dễ đem đi so giá. Agent luôn kèm lời mời chuyển sang `/baogia`; khách ở giai đoạn NHẬN BIẾT mà xin bảng giá thì vẫn làm, nhưng nói rõ đánh đổi.

Bản một-file cũng có: `python baogia-1file.py --banggia "nâng mũi"` (nay 179 KB, gói thêm 2 file). Đã kiểm từ thư mục trống.

---

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
