# KANGNAM — TRI THỨC AGENT BÁO GIÁ
> Gộp 11 file trong `knowledge/` thành một. Sinh tự động ngày 2026-10-22 bằng `python tools/build-goi.py`.
> ⛔ **Không sửa file này** — sửa ở `knowledge/BG-xx-*.md` rồi chạy lại lệnh trên.

**Cách đọc:** mỗi mục `# BG-xx` dưới đây nguyên là **một file tri thức riêng**. Tham chiếu dạng `[[BG-07-cong-phap-ly]]` nằm trong văn bản trỏ tới **mục cùng tên ngay trong file này**, không phải file bên ngoài.

## MỤC LỤC

| Mã | Nội dung | Đọc khi |
|---|---|---|
| **BG-07** ⚠️ | Cổng pháp lý | Rào R0–R12 + bảng từ cấm. Fail = không xuất file |
| **BG-02** ⚠️ | Luật nói về tiền | Nguồn giá duy nhất · ưu đãi · giá lệch · đã gồm/chưa gồm |
| **BG-03** ⚠️ | Cấu trúc 9 khối | Xương sống của tờ báo giá — thứ tự không đảo |
| **BG-04** ⚠️ | Chân dung khách | 6 nhóm · 6 giai đoạn · khi nào CHƯA nên gửi báo giá |
| **BG-11** ⚠️ | Nỗi đau khách cắt mí | 9 chân dung · 10 nỗi lo · giải pháp Plasma · chính sách giá |
| **BG-05** | Nỗi sợ & phản đối | Khuôn trả lời 3 nhịp cho khối băn khoăn |
| **BG-06** | Case & ảnh trước–sau | 4 điều kiện dùng một case · link album · ô ảnh tạm |
| **BG-01** | Hồ sơ thương hiệu | Giọng viết · cơ sở & tuyến · bác sĩ · giới hạn phát ngôn |
| **BG-08** | Design system | Token màu · 4 trang A4 · 3 ảnh slide · font nhúng |
| **BG-09** | Schema dữ liệu | Cấu trúc du-lieu.json — đầu vào/đầu ra của tool |
| **BG-10** | Vòng học | 4 chỉ số thật — hiện đang trống, chờ dữ liệu |

⚠️ = đọc mọi lần lập báo giá. Còn lại đọc khi chạm tới việc đó.


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-07-cong-phap-ly.md -->
<!-- ======================================================================== -->

# BG-07 — CỔNG PHÁP LÝ CHO ẤN PHẨM BÁO GIÁ
Version 1.0 · Nguồn: `Agent-LDP-Kangnam/knowledge/KF-11-cong-phap-ly.md` (rào R0–R12) · `Agent-KN-CPW/knowledge/geo-rao-phap-ly.md`
Cập nhật: 2026-10-21 · **Tài liệu nội bộ, không thay thế ý kiến Pháp chế.**

> **RANH GIỚI: cổng CHẶN cái sai trong chữ, cổng CÂN NHẮC nhường quyết định cho người.**

| Mức | Dành cho | Ai quyết |
|---|---|---|
| **CHẶN** — không xuất file | Thứ **sai ngay trong chữ viết ra**: cam kết kết quả · mốc hồi phục cứng · mời đại phẫu sai tuyến · nêu trả góp (Kangnam không có). Những thứ này **không ai duyệt cho đúng được** | Tool, không thương lượng |
| **CÂN NHẮC** — vẫn xuất file, in rõ ra | Vài thứ tool không tự biết: ưu đãi còn hạn không · tên thương mại thuốc · ảnh cơ thể | **Người gửi** |

> **Đây là báo giá tham khảo gửi riêng một khách, không phải ấn phẩm phát hành.** Nên ở đây **không có quy trình phê duyệt**: không "bộ phận có thẩm quyền", không "chưa được phép phát hành", không đối chiếu danh sách bác sĩ duyệt, không hỏi consent từng tấm ảnh.
>
> Lý do bỏ: mỗi hàng rào kiểu đó đẻ ra một câu từ chối. Agent viết *"chưa đưa hình ảnh vào bản đề xuất vì chưa xác minh đầy đủ sự đồng ý sử dụng ảnh"* — trong khi ảnh nằm sẵn trong album đã duyệt, và khách thì xem ảnh trước cả giá. Thứ chặn được việc thật mà không chặn được rủi ro thật thì bỏ.
>
> Đổi lại, **cổng dữ liệu siết chặt hơn**: thiếu mô tả khách, thiếu câu *vì sao hợp*, thiếu dòng *đã gồm / chưa gồm*, thiếu lộ trình → **không xuất file**. Thà bắt điền đủ còn hơn chặn vì thiếu con dấu.

---

## 1. BÁO GIÁ CÁ NHÂN KHÁC LANDING Ở ĐIỂM NÀO

| | Landing / quảng cáo | Báo giá cá nhân gửi 1-1 |
|---|---|---|
| Đối tượng | công chúng | **một khách đã yêu cầu** |
| GXNNDQC (R9) | bắt buộc trước khi phát hành | thường không thuộc diện quảng cáo đại chúng — **nhưng** nếu dùng lại làm ấn phẩm phát hành/đăng công khai thì phải xin |
| Nêu giá cụ thể | hạn chế | **được**, vì khách đã hỏi — với điều kiện ghi rõ "tham khảo, bác sĩ chốt sau khám" |
| Ảnh before–after | chịu thêm policy nền tảng | lấy từ Album Kangnam, dùng thẳng |

> ⚠️ Điểm dễ sai nhất: lấy nguyên file báo giá đi đăng Fanpage / chạy quảng cáo. Lúc đó nó trở thành **nội dung quảng cáo dịch vụ KCB** và phải qua đủ quy trình duyệt + GXNNDQC.

## 2. CÁC RÀO ÁP CHO BÁO GIÁ

| Mã | Rào | Trong báo giá nghĩa là |
|---|---|---|
| **R1** | Cam kết kết quả | Không "cam kết đẹp", "vĩnh viễn", "trọn đời", "không biến chứng", "không đau", "không sẹo", "số 1/tốt nhất" |
| **R2** | Danh mục kỹ thuật | Chỉ báo giá dịch vụ có trong DMKT của đúng pháp nhân |
| **R3** | Đúng pháp nhân / tuyến | ⛔ Không mời **đại phẫu** tại cơ sở không có giấy phép đại phẫu. Tool tự chặn theo cờ `dai_phau` |
| ~~R4~~ | ~~Bác sĩ~~ | **Đã bỏ.** Tên bác sĩ in như khai, không đối chiếu danh sách duyệt |
| ~~R5~~ | ~~Hình ảnh khách~~ | **Đã bỏ.** Album Kangnam là nguồn đã duyệt — xem [[BG-06-proof-case]] mục 2 |
| **R6** | So sánh đối thủ | Không nêu tên, không hạ thấp, **không phán xét nơi cũ** với khách sửa lại |
| **R7** | Thiết bị & vật tư | Không nêu tên thương mại thuốc/filler/botox; thiết bị nêu đúng hồ sơ |
| **R9** | GXNNDQC | Xem mục 1 — nhắc khi file được dùng ngoài phạm vi 1-1 |
| **R12** | Hình ảnh cơ thể | Ảnh before/after **cơ thể** nhạy cảm hơn ảnh vùng mặt → chỉ **cảnh báo**, người gửi tự quyết. Vẫn ⛔ ngôn từ miệt thị cân nặng và hứa số kg |

### Hai luật riêng của gói Kangnam
**① Không hứa mốc hồi phục cứng.** Luôn dạng **khoảng** (vd 7–14 ngày) + *"tùy cơ địa mỗi người"*.
**② Không quảng cáo đại phẫu cho viện tỉnh.** Viện tỉnh ghi rõ: *tư vấn và đặt khám tại [viện], phẫu thuật tại [bệnh viện]*.

## 3. BẢNG TỪ CẤM → TỪ ĐÚNG (tool tự quét)

| Cấm | Thay bằng |
|---|---|
| cam kết kết quả / đẹp như hình | kết quả tuỳ cơ địa, bác sĩ đánh giá riêng từng trường hợp* |
| đẹp tuyệt đối / hoàn hảo 100% | kết quả hài hoà với gương mặt* |
| an toàn tuyệt đối / không biến chứng | quy trình chuẩn y khoa, môi trường vô khuẩn, hội đồng chuyên môn giám sát |
| không đau | giảm đau theo phác đồ, gây tê/gây mê do bác sĩ chỉ định |
| không để lại sẹo | vị trí đường mổ được chọn để hạn chế sẹo, chăm sóc theo hướng dẫn* |
| vĩnh viễn / trọn đời / bảo hành trọn đời | duy trì lâu dài, có chế độ bảo hành minh bạch (ghi rõ thời hạn) |
| số 1 / tốt nhất / duy nhất / hàng đầu | bỏ, hoặc nêu USP đo được: giấy phép, chứng chỉ, chính sách |
| rẻ nhất thị trường | chi phí minh bạch, công khai tại bảng giá |
| "3 ngày là đi làm được" | mốc dạng khoảng + "tùy cơ địa mỗi người" |

Mọi con số và mức độ phải gắn `*` dẫn chú thích **"Hiệu quả phụ thuộc cơ địa mỗi người."**

> ⚠️ **Xung đột đã biết:** K1/K4 ghi USP *"bảo hành trọn đời"* (mũi) và *"cam kết không co thắt bao xơ"* (ngực). Hai cụm này **vi phạm R1**. Trong báo giá phải viết lại thành chính sách có thời hạn cụ thể. Cần Pháp chế chốt câu chữ chuẩn — xem *Việc còn treo* ở `doc/CHANGELOG.md`.

## 4. DỮ LIỆU CÁ NHÂN
- ⛔ Không nạp CCCD/CMND · hồ sơ bệnh án · ảnh khách chưa có consent lên bất kỳ công cụ AI nào.
- ⛔ Không in tình trạng sức khoẻ, lịch sử dịch vụ của khách lên file gửi qua Zalo/Messenger — file có thể bị chuyển tiếp.
- Chỉ ghi điều ảnh hưởng trực tiếp tới tư vấn (vd *"đang cho con bú"*), ở mức tối thiểu.
- Tên khách trên file: dùng **tên hiển thị** khách tự xưng, không dùng tên đầy đủ trên giấy tờ nếu không cần.

## 5. CHECKLIST CỔNG — chạy trước khi gửi khách
```
☐ R3  Dịch vụ khớp tuyến cơ sở; đại phẫu → tuyến bệnh viện
☐ R1  Rà toàn bộ chữ qua bảng từ cấm; mọi con số có dấu * + chú thích
☐ —   Mốc hồi phục dạng khoảng + "tùy cơ địa mỗi người"
☐ R7  Không tên thương mại thuốc/filler/botox
☐ R5  Mọi ảnh case có consent + mốc chụp; không còn ô ảnh tạm
☐ R12 Không ảnh before/after cơ thể
☐ —   Mọi dòng giá truy được về bang-gia.json; có dòng đã gồm / chưa gồm
☐ —   Có đủ 3 câu miễn trừ (BG-02 mục 6)
☐ —   Không chứa CCCD, bệnh án, tình trạng sức khoẻ chi tiết
☐ R9  Nếu file sẽ đăng công khai → dừng, chuyển quy trình duyệt quảng cáo
```
**Một ô không tick = không gửi.** Ghi rõ ô nào vướng và cần ai xử lý.

Tool in sẵn bảng này cuối mỗi lần render, dưới tiêu đề **CÂN NHẮC TRƯỚC KHI GỬI** — chỉ gồm những câu áp vào đúng báo giá đó, kèm câu chốt: *"Người gửi là người chịu trách nhiệm cho bản này."*

## 6. TOOL CHẠY CỔNG TỰ ĐỘNG
```
python tools/cong_phap_ly.py out/<ma>/du-lieu.json     # chạy riêng
python tools/render_baogia.py out/<ma>/du-lieu.json    # chạy kèm, CHẶN thì không xuất file
```
Tool bắt được: từ cấm · mốc hồi phục cứng · bác sĩ sai trạng thái · ảnh thiếu consent/mốc chụp · ảnh cơ thể · thiếu câu miễn trừ · đại phẫu sai tuyến · nghi CCCD.

**Tool không bắt được** (vẫn cần người): consent còn hiệu lực không · dịch vụ có trong DMKT của đúng pháp nhân không · ưu đãi có văn bản không · case có đúng là ca thật không. Cổng tự động là lưới thứ hai, **không phải người duyệt**.

Liên quan: [[BG-02-bang-gia]] · [[BG-06-proof-case]] · [[BG-01-ho-so-thuong-hieu]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-02-bang-gia.md -->
<!-- ======================================================================== -->

# BG-02 — BẢNG GIÁ & LUẬT NÓI VỀ TIỀN
Version 1.1 · Nguồn số: `template/bang-gia.json` — **đã đối chiếu trực tiếp với web `/bang-gia/` ngày 2026-10-21**
Cập nhật: 2026-10-21

---

## 1. MỘT NGUỒN GIÁ DUY NHẤT

```
template/bang-gia.json   ← nguồn đúng duy nhất cho mọi con số trong báo giá
```

**Luật tối thượng: agent không được tự tạo dịch vụ, không được tự đặt giá.**
Mỗi dòng chi phí trong `du-lieu.json` phải có trường `ma` trỏ về một mục trong bảng. Tool `render_baogia.py` chạy **CỔNG BẢNG GIÁ** trước khi xuất file: mã không có trong bảng → **không xuất**.

Khách hỏi dịch vụ không có trong bảng → trả lời *"Mục này em cần xác nhận lại chi phí với bệnh viện rồi gửi chị ngay"*, **không đoán**.

## 2. BỐN KIỂU GIÁ TRONG BẢNG

| `kieu` | Nghĩa | Cách ghi trong báo giá |
|---|---|---|
| `co_dinh` | Giá niêm yết một mức | Ghi đúng số đó |
| `khoang` | Có dải (vd nám 4,4–5,6tr/lần) | Ghi dải, nói rõ yếu tố quyết định nằm ở đâu trong dải |
| `tu_` | "Từ X" (implant, răng sứ…) | Ghi *từ X*, ⛔ không ghi thành giá chốt |
| `lien_he` | Web ghi Liên hệ (spa) | ⛔ Không tự đặt số. Ghi *liên hệ để được báo giá* |

## 2b. ƯU ĐÃI ĐANG HIỆU LỰC — trường `uu_dai_hien_hanh`
Một số dịch vụ có **giá niêm yết** và **giá ưu đãi đang chạy**, cả hai đều nằm trong bảng:

```json
{"ma": "mat.cat-mi-plasma", "gia_min": 10000000, "uu_dai_hien_hanh": 8000000,
 "nguon_uu_dai": "Chính sách giá cắt mí Plasma, cập nhật 2026-10-21"}
```

| Luật | |
|---|---|
| Báo theo giá ưu đãi | hợp lệ, **không cần** khai `ly_do_lech` — cổng bảng giá chấp nhận cả hai mức |
| In ra báo giá | **ghi cả hai số**: niêm yết gạch ngang + ưu đãi. Tool tự in khi `gia` = `uu_dai_hien_hanh` |
| Hết hạn ưu đãi | sửa `bang-gia.json` (gỡ `uu_dai_hien_hanh`), không sửa lẻ từng báo giá |
| Số thứ ba | ⛔ không có. Giá nào khác hai số này phải khai `ly_do_lech` |

**Đang áp dụng:** cắt mí Plasma — niêm yết **10.000.000đ**, ưu đãi **8.000.000đ**. Khách sửa mí cộng thêm `mat.phi-sua-mi` (niêm yết 3.000.000đ, giảm 40–50% tuỳ khu vực → thực thu 1.500.000–1.800.000đ, tổng dự kiến **9,5–9,8 triệu**). Chi tiết và cách viết: [[BG-11-noi-dau-cat-mi]] mục 4.

## 3. GIÁ LỆCH BẢNG — khi nào được phép
Giá trong báo giá khác giá niêm yết **chỉ khi** có lý do thật và được ghi ra:

```json
{"ma": "mat.cat-mi-6d", "gia": 10800000, "ly_do_lech": "Ưu đãi tháng 10 đã duyệt — CV số ..."}
```

Không khai `ly_do_lech` → cổng bảng giá chặn. Ba lý do hợp lệ:
1. **Ưu đãi có văn bản** của tháng (nguồn: K7 chiến dịch tháng / thông báo nội bộ).
2. **Giá gói combo** đã được duyệt riêng.
3. **Bệnh viện cập nhật bảng giá mới** → lúc đó phải cập nhật `bang-gia.json` trước, không sửa lẻ từng báo giá.

⛔ Tuyệt đối không "giảm giá cho chị vì chị dễ thương" — giảm giá không nguồn là rủi ro vận hành, không phải kỹ năng bán hàng.

## 4. CẢNH BÁO ĐANG CÓ TRONG BẢNG (phải hỏi lại trước khi báo)
- **Cắt mí Plasma — lệch nguồn.** Web `/bang-gia/` niêm yết **8.000.000đ**; chính sách nội bộ 21/10/2026 ghi niêm yết **10.000.000đ** + ưu đãi **8.000.000đ**. Khách trả 8.000.000đ ở cả hai cách hiểu, nhưng **chỉ in giá gạch ngang 10.000.000đ khi Vận hành xác nhận** mức niêm yết đó — in một mức giảm giá không có thật là rủi ro.
- **Phí sửa mí** — mức giảm 40–50% **tuỳ khu vực**. Xác nhận với cơ sở thực hiện trước khi chốt con số; chưa xác nhận thì ghi khoảng 1.500.000–1.800.000đ kèm `[CHỜ XÁC NHẬN]`.
- **Lipo mini nhiều vùng 18.000.000đ** rẻ hơn **mini 1 vùng 34.000.000đ** — nghi lệch dữ liệu.

> ✅ Đã đóng: nghi vấn giá cắt mí Plasma **7.200.000đ** (meta website cũ) — web `/bang-gia/` ngày 21/10/2026 ghi 8.000.000đ, không còn con số 7,2tr.

Ba mục trên mang cờ `canh_bao` trong JSON; cổng sẽ nhắc. Báo giá cho khách → **xác nhận với bệnh viện trước**.

## 5. GIÁ ĐÃ GỒM / CHƯA GỒM — luôn phải ghi
Khách không sợ đắt, khách sợ **phát sinh**. Mỗi báo giá phải có một dòng dạng:

> *Chi phí đã gồm khám, phòng mổ, vật tư và các lần tái khám theo lịch. Chưa gồm xét nghiệm tiền phẫu nếu bác sĩ chỉ định thêm.*

Chưa chắc hạng mục nào nằm trong giá → ghi **"cần xác nhận"**, không im lặng, cũng không hứa gồm.

## 6. BA CÂU BẮT BUỘC CỦA MỌI BÁO GIÁ
1. *"Giá niêm yết tham khảo tại thời điểm lập báo giá."*
2. *"Chi phí cuối cùng do bác sĩ quyết định sau khi thăm khám trực tiếp."*
3. *"Kết quả thẩm mỹ phụ thuộc cơ địa từng người."*

Template đã in sẵn; nếu sửa `phap_ly.mien_tru` thì vẫn phải giữ đủ ba ý — cổng pháp lý kiểm câu 3.

## 7. ⛔ KANGNAM KHÔNG CÓ TRẢ GÓP

**Kangnam không có chính sách trả góp.** Không nêu trả góp, không "chia nhỏ theo tháng", không "trả theo kỳ", không gợi ý thẻ tín dụng trả dần — dưới mọi cách diễn đạt.

Hứa một cách thanh toán không tồn tại là thứ khách phát hiện ra **sau khi đã tới viện**: lúc đó mất cả niềm tin lẫn ca khách. Đó là sai thông tin, không phải cách nói hay.

Hai tầng chặn: cổng dữ liệu bắt trường `chi_phi.tra_gop`, cổng pháp lý bắt chữ *trả góp / chia nhỏ nhiều kỳ / trả theo tháng* trong văn bản (rào `KN-②`). Cả hai đều **CHẶN**, không xuất file.

**Khách lo chi phí thì làm gì?** Ba cách thật, không cần chính sách nào:
1. **Ghi rõ từng khoản** — khách sợ phát sinh hơn sợ đắt (mục 5).
2. **Đưa phương án vừa ngân sách** ở khối *Phương án khác*, nói thẳng khác biệt.
3. **Chia lộ trình theo giai đoạn điều trị** — làm phần ảnh hưởng nhiều nhất trước. Đây là chia **việc**, không phải chia **tiền**.

## 8. CÁCH NÓI VỀ TIỀN THEO NHÓM KHÁCH (chi tiết ở [[BG-04-chan-dung-khach]])
| Nhóm | Neo giá trị vào đâu |
|---|---|
| 1 · công sở, tích góp | An toàn · bảo hành · không phát sinh · chia lộ trình theo giai đoạn |
| 2 · doanh nhân | Riêng tư · bác sĩ đích danh · thời gian được tôn trọng. ⛔ không nhấn khuyến mãi |
| 3 · KOC/Gen Z | Kết quả lên hình · lịch hồi phục khớp lịch quay |
| 4 · sinh viên, mới đi làm | Minh bạch từng khoản · phương án vừa túi · ⛔ không đẩy gói cao |
| 5 · khách sửa lại | Chi phí xử lý phần hỏng nằm riêng một dòng, không gộp để che |
| 6 · trung niên trẻ hoá | Lộ trình nhiều mốc · chi phí theo giai đoạn thay vì một cục |

## 9. CẬP NHẬT BẢNG GIÁ

**Đối chiếu với web trước, đừng sửa tay:**
```bash
python tools/doi_chieu_gia_web.py          # tải https://benhvienthammykangnam.com.vn/bang-gia/ rồi so
python tools/doi_chieu_gia_web.py --ghi    # lấy giá web ghi đè các mục LỆCH GIÁ
```
Tool khớp tên theo **độ trùng từ** (ghép cặp tốt nhất toàn cục), nên web đổi cách viết tên vẫn nhận ra. Tên web khác hẳn thì khai `ten_web` trong JSON để lần sau khớp tuyệt đối.
⛔ Không có `--ghi` thì tool **không tự sửa giá** — giá là thứ đi thẳng vào túi khách, không để máy đổi sau lưng người.

**Kết quả lần đối chiếu 2026-10-21:** 86 dòng trên web · **85 khớp · 0 lệch giá** · 1 mục lệch nguồn (cắt mí Plasma, xem mục 4) · `mat.phi-sua-mi` là chính sách nội bộ, web không đăng.

Khi bệnh viện đổi giá:
1. Sửa `template/bang-gia.json` (mục `cap_nhat` ghi ngày mới).
2. Ghi lại thay đổi vào `doc/CHANGELOG.md`.
3. Các báo giá **đã gửi** vẫn giữ nguyên giá trong hiệu lực đã ghi — không gửi lại báo giá sửa giá ngầm.

Liên quan: [[BG-07-cong-phap-ly]] · [[BG-09-schema-du-lieu]] · [[BG-03-cau-truc-bao-gia]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-03-cau-truc-bao-gia.md -->
<!-- ======================================================================== -->

# BG-03 — CẤU TRÚC MỘT TỜ BÁO GIÁ CÁ NHÂN HOÁ
Version 1.0 · Cập nhật: 2026-10-21

---

## 1. CHÍN KHỐI — thứ tự cố định, không đảo

| # | Khối | Trả lời câu hỏi ngầm của khách | Bắt buộc |
|---|---|---|---|
| 1 | **Đầu trang + mã báo giá** | "Cái này có phải gửi riêng cho mình không?" | ✔ |
| 2 | **Tiêu đề + lời mở cá nhân hoá** | "Họ có nhớ mình nói gì không?" | ✔ |
| 3 | **Điều khách đang gặp** | "Họ hiểu đúng vấn đề của mình chưa?" | ✔ |
| 3b | **Vấn đề → cách xử lý** (từng cặp) | "Cái tôi lo, họ giải quyết kiểu gì?" | ✔ *(hoặc khối 9)* |
| 4 | **Phương án bác sĩ đề xuất** | "Làm gì, vì sao là cái này?" | ✔ |
| 5 | **Chi phí dự tính** | "Bao nhiêu, gồm gì, có phát sinh không?" | ✔ |
| 6 | **Phương án khác để cân nhắc** | "Có lựa chọn nào khác không?" | nên có |
| 7 | **Trường hợp tương tự + ảnh trước–sau** | "Có ai giống mình đã làm chưa?" | nên có |
| 8 | **Lộ trình từng bước** | "Rồi sao nữa? Mất bao lâu?" | ✔ |
| 9 | **Băn khoăn + Bước tiếp theo (CTA)** | "Mình có phải quyết ngay không?" | ✔ |

Chân trang: khối **miễn trừ pháp lý** — luôn in, không bỏ dù file ngắn.

## 1b. MẠCH ĐỌC — mượn cách email bán hàng dẫn dắt, không mượn giọng

Thứ làm một email marketing tốt không phải màu mè, mà là **mạch**: gọi đúng vấn đề người đọc đang có → nói cách xử lý từng vấn đề → rồi mới tới tiền → rồi mới tới bằng chứng. Tờ báo giá đi đúng mạch đó, **nhưng giữ giọng tư vấn y khoa** — điềm tĩnh, không chào mời.

```
Trang 1  Vấn đề   — lời hứa cá nhân hoá · điều khách đang gặp · VẤN ĐỀ → CÁCH XỬ LÝ
Trang 2  Giải pháp — phương án bác sĩ đề xuất · các bước · lưu ý riêng · phương án khác
Trang 3  Chi phí   — bảng chi phí · ưu đãi · tổng · đã gồm/chưa gồm · lộ trình
Trang 4  Bằng chứng — case tương tự + ảnh trước–sau · album · CTA · chữ ký
```

⛔ Thứ **không** mượn từ email marketing: nhãn mục kiểu chào mời (*"Em hiểu đúng chưa ạ"*), giục chốt, khan hiếm giả, emoji. Xem [[BG-01-ho-so-thuong-hieu]] mục 3.

### Khối 3b — vấn đề → cách xử lý
Mỗi cặp một dòng: bên trái là **vấn đề bằng chữ của khách**, bên phải là **cách bên em xử lý đúng vấn đề đó**.

```json
"van_de_giai_phap": [
  {"van_de": "Sợ lộ sẹo mỗi khi trang điểm.",
   "giai_phap": "Đường mổ đặt đúng nếp mí nên khi mở mắt bị nếp che. Mức độ mờ sẹo tuỳ cơ địa mỗi người."}
]
```

| Luật | |
|---|---|
| Số cặp | **3–4**. Nhiều hơn là đang liệt kê, không phải tư vấn |
| Nguồn vấn đề | **chữ khách đã nói**, không phải nỗi lo chung của ngành |
| Mỗi giải pháp | nói **cơ chế thật** + **giới hạn trung thực** ([[BG-05-noi-so-phan-doi]] khuôn 3 nhịp) |
| ⛔ Trùng lặp | Khối 3b và khối 9 **không nói cùng một nỗi lo**. Có 3b rồi thì khối 9 chỉ giữ câu hỏi còn lại, hoặc bỏ hẳn |

Cổng dữ liệu đòi **ít nhất một trong hai**: `van_de_giai_phap` hoặc `giai_toa`. Có cả hai mà nói cùng một nỗi lo thì vừa loãng vừa đội thêm một trang giấy.

## 2. LUẬT NỀN — bốn điều

**① Cá nhân hoá nằm ở khối 2–3–4, không nằm ở việc điền tên khách.**
Thay tên vào mẫu chung thì vẫn là bảng giá chung. Cá nhân hoá thật = nhắc lại **đúng chữ khách đã nói** (mong muốn, nỗi lo, ràng buộc về thời gian/ngân sách) rồi gắn phương án vào đó.

**② Giá đứng sau lý do, không bao giờ đứng trước.**
Khối 5 chỉ xuất hiện sau khi khối 4 đã giải thích vì sao phương án này hợp. Tờ báo giá mở đầu bằng con số là tờ báo giá bị so sánh với tờ của nơi khác.

**③ Không chẩn đoán, không chốt giá thay bác sĩ.**
Mọi phương án đều là **đề xuất để mang tới buổi khám**. Chữ dùng: *"bác sĩ sẽ xác nhận sau khi khám"*, không phải *"chị cần làm X"*.

**④ CTA của báo giá là ĐẶT KHÁM, không phải CHỐT CỌC.**
Bước tiếp theo luôn là một việc nhỏ, miễn phí, có thể rút lui: chọn khung giờ khám. Xin cọc qua file báo giá là tự bắn vào chân.

## 2b. BỐN DẤU HIỆU CÁ NHÂN HOÁ — thiếu một là tờ báo giá tụt về bảng giá chung

| # | Dấu hiệu | Ở đâu | Tool/template lo phần nào |
|---|---|---|---|
| 1 | **Lời chào đích danh viết tay** — *"Gửi chị Thu Hà,"* | ngay trên tiêu đề trang 1 và bìa slide | template tự dựng từ `khach.ten_hien_thi` |
| 2 | **Nhắc lại đúng chữ khách nói** | khối 3, và câu *vì sao hợp* ở khối 4 | agent phải viết — không ai viết hộ được |
| 3 | **Lý do phương án này hợp với khách NÀY** | khối 4 | agent viết |
| 4 | **Chữ ký người tư vấn** — *"Đồng hành cùng chị — Ngọc Anh"* | cuối trang 3 | template tự dựng từ `meta.nguoi_lap` |

Dấu hiệu 1 và 4 là **hình thức** — template lo. Dấu hiệu 2 và 3 là **nội dung** — và đó mới là thứ quyết định.
Một tờ báo giá có đủ lời chào đích danh, chữ ký tay, mà phần *vì sao hợp* viết chung chung kiểu *"đây là phương án được nhiều khách lựa chọn"* thì **vẫn là bảng giá chung có điền tên**.

**Phép thử:** che tên khách và ba dòng meta đi. Nếu tờ báo giá vẫn gửi được cho một khách khác cùng dịch vụ mà không phải sửa chữ nào → **chưa cá nhân hoá**, làm lại khối 3 và khối 4.

## 3. KHỐI 2 — lời mở, công thức 3 câu
```
Câu 1  Nhắc lại bối cảnh:   "Em tổng hợp lại những gì chị chia sẻ hôm qua..."
Câu 2  Nói rõ đây là gì:    "...thành một phương án cụ thể kèm chi phí dự tính."
Câu 3  Hạ áp lực:           "Đây là báo giá tham khảo riêng cho trường hợp của chị."
```
⛔ Không mở bằng *"Kangnam là bệnh viện thẩm mỹ hàng đầu..."* — khách không cần profile, khách cần câu trả lời.

## 4. KHỐI 4 — phương án, công thức
```
Tên phương án           ngắn, đọc là hiểu làm gì
Vì sao hợp với khách    nối thẳng vào tình trạng khách đã mô tả — đây là phần đắt giá nhất
2–4 bước thành phần     mỗi bước 1 dòng: làm gì + lợi ích cho khách
Lưu ý riêng             điều bác sĩ cần xác nhận khi khám + mốc hồi phục dạng khoảng
```

## 5. KHỐI 5 — chi phí, thứ tự dòng
1. Hạng mục chính (dịch vụ lõi)
2. Hạng mục đi kèm (làm cùng thì, tiết kiệm cho khách)
3. Ưu đãi — ghi rõ điều kiện và hạn
4. **Chi phí dự tính sau ưu đãi** — số to nhất trên trang
5. Đã gồm / chưa gồm

⛔ **Không có dòng trả góp** — Kangnam không có chính sách đó ([[BG-02-bang-gia]] mục 7). Khách lo tiền thì đưa phương án vừa ngân sách ở khối 6, không hứa cách thanh toán không tồn tại.

## 6. KHỐI 7 — case tương tự
Chọn case **giống khách**, không phải case đẹp nhất. Tiêu chí khớp, theo thứ tự ưu tiên:
tình trạng ban đầu → độ tuổi/nghề → ràng buộc (thời gian nghỉ, ngân sách) → cơ sở thực hiện.

Chưa có ảnh đủ điều kiện → **để ô ảnh tạm**, không bỏ khối, không dùng ảnh stock/AI. Chi tiết: [[BG-06-proof-case]].

## 7. KHỐI 9 — băn khoăn
Lấy **đúng 2–3 nỗi lo khách đã nói**, không bê nguyên FAQ chung. Mỗi câu trả lời theo khuôn:
> thừa nhận nỗi lo → nói cơ chế xử lý thật → nêu giới hạn trung thực ("tùy cơ địa", "bác sĩ đánh giá khi khám").

Thư viện câu trả lời theo rào cản: [[BG-05-noi-so-phan-doi]].

## 8. ĐỘ DÀI
| Bản | Khổ | Dung lượng chữ |
|---|---|---|
| PDF A4 | **4 trang**, mỗi trang một mạch | ~900–1.100 chữ. Quá 4 trang là đang viết brochure, không phải báo giá |
| JPG slide | **3 ảnh** 1080×1920 | mỗi ảnh ≤ 170 chữ. Tràn khung → tool tự thu nhỏ và cảnh báo |

Tool đếm số trang PDF và cảnh báo khi vượt 4. Ba chỗ cắt được nhiều nhất: số cặp vấn đề→giải pháp (3 là đủ) · lời mở (giữ đúng 3 câu) · số bước trong `giai_phap.gom`.

## 9. TỰ KIỂM TRƯỚC KHI RENDER — 9 ô
```
☐ Khối 3 có ít nhất 2 chi tiết chỉ đúng với khách này
☐ Khối 4 nối thẳng vào tình trạng ở khối 3
☐ Che tên khách đi vẫn KHÔNG gửi được cho khách khác (phép thử mục 2b)
☐ Mọi dòng chi phí có mã trỏ về bang-gia.json
☐ Có dòng đã gồm / chưa gồm
☐ Mốc thời gian đều dạng khoảng + "tùy cơ địa mỗi người"
☐ Tên bác sĩ (nếu có) ở trạng thái duyet
☐ CTA là đặt khám, không phải chuyển cọc
☐ Mỗi trang chỉ có MỘT thứ to nhất (BG-08 mục 1c)
```

Liên quan: [[BG-01-ho-so-thuong-hieu]] · [[BG-02-bang-gia]] · [[BG-09-schema-du-lieu]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-04-chan-dung-khach.md -->
<!-- ======================================================================== -->

# BG-04 — CHÂN DUNG KHÁCH & GIAI ĐOẠN — ĐIỀU CHỈNH BÁO GIÁ THEO AI ĐỌC
Version 1.0 · Nguồn: `Kangnam-Agent-Factory/knowledge/K2-khach-hang.md` · `K3-hanh-vi-trang-thai.md`
Cập nhật: 2026-10-21

---

## 1. INSIGHT GỐC — bắt đầu mọi báo giá từ đây
> *"Tôi muốn thay đổi ngoại hình để tự tin hơn, nhưng chỉ sẵn sàng thực hiện khi thật sự tin tưởng vào bác sĩ, quy trình và kết quả."*

Thứ tự bất biến: **giải quyết nỗi đau → tăng niềm tin → rồi mới CTA.** Báo giá đi ngược thứ tự này sẽ bị đọc như tờ rơi.

**Ba câu hỏi ngầm phải trả lời đúng cái lo thật:**
| Khách hỏi | Thật ra đang hỏi | Trong báo giá phải có |
|---|---|---|
| "Có đau không?" | *Tôi có chịu nổi không?* | Phác đồ giảm đau, mô tả cảm giác thật |
| "Bao lâu thì đẹp?" | *Khi nào tôi đi làm lại được?* | Mốc hồi phục dạng khoảng + xếp lịch theo công việc khách |
| "Bao nhiêu tiền?" | *Có đáng với số tiền đó không?* | Giá đứng sau phần giải thích giá trị |

## 2. SÁU NHÓM KHÁCH — chỉnh gì trong báo giá

| # | Nhóm | Tuổi | Nỗi đau chính | Báo giá phải nhấn | ⛔ Tránh |
|---|---|---|---|---|---|
| 1 | Công sở & tích góp | 25–45 | Tích góp mới làm được; sợ rủi ro; sợ ảnh hưởng công việc | An toàn, bảo hành rõ, không phát sinh, chia lộ trình theo giai đoạn | Giục chốt, giá "sốc" |
| 2 | Doanh nhân / thu nhập cao | 35–55 | Sợ lộ dấu phẫu thuật; cần riêng tư | Bác sĩ đích danh, lịch riêng, cá nhân hoá tối đa, câu chữ tinh gọn | Khuyến mãi, so sánh giá |
| 3 | KOC/KOL, Gen Z | 20–30 | Sợ lỗi trend, xấu khi lên hình, hồi phục lâu | Kết quả lên hình, lịch hồi phục khớp lịch quay, mô phỏng trước | Giọng già, dài dòng |
| 4 | Sinh viên / mới đi làm | 18–25 | Thu nhập thấp; sợ mua hớ; sợ đau | Minh bạch từng khoản, phương án vừa túi, feedback thật | Đẩy gói cao, gây FOMO |
| 5 | Khách sửa lại (hỏng nơi khác) | 28–50 | Ám ảnh thất bại; kiệt niềm tin | Bước **khám đánh giá lại** đứng riêng, chi phí xử lý phần hỏng tách dòng, giọng lắng nghe | ⛔ Phán xét nơi cũ (rào R6) |
| 6 | Trung niên trẻ hoá | 40–55+ | Lão hóa lộ rõ; sợ mặt đơ, sợ rủi ro sức khỏe | Tự nhiên, kín đáo, lộ trình nhiều mốc, chi phí theo giai đoạn | Ngôn ngữ trẻ hoá quá đà |

> Nhóm 4 có thể là **vị thành niên** → giữ nội dung phù hợp lứa tuổi, hướng có người giám hộ, **không nạp tuổi/DOB thật vào công cụ**.

## 3. SÁU GIAI ĐOẠN — quyết định báo giá có nên gửi chưa

| Giai đoạn | Nhiệt | Tín hiệu | Báo giá nên là gì |
|---|---|---|---|
| **NHẬN BIẾT** | Cold | Hỏi chung, hỏi giá ngay câu đầu | ⚠️ **Chưa gửi báo giá đầy đủ.** Trả lời câu hỏi + mời khám. Gửi sớm = bị đem đi so giá |
| **TÌM HIỂU** | Warm | Hỏi phương pháp, bác sĩ, before-after | Bản rút gọn: phương án + khoảng chi phí + 1 case |
| **CÂN NHẮC & NỖI SỢ** | Warm→Hot | Hỏi đau/rủi ro/bảo hành/"để hỏi người nhà" | ✅ **Đúng lúc nhất.** Bản đầy đủ, khối băn khoăn làm nặng |
| **THỰC HIỆN** | Hot | Hỏi lịch, địa chỉ, cho SĐT | Bản đầy đủ + lộ trình + khung giờ khám cụ thể |
| **HẬU PHẪU** | Existing | Sau làm, hỏi chăm sóc | Không báo giá; chuyển hướng dẫn hậu phẫu |
| **GẮN BÓ** | LTV | Quay lại, giới thiệu người quen | Báo giá cross-sell, nhắc lịch sử đã làm (⛔ không in tình trạng sức khoẻ) |

**Luật:** khách ở **NHẬN BIẾT** mà đòi báo giá → agent vẫn làm được bản rút gọn, nhưng phải nói rõ trong lời mở rằng đây là khoảng tham khảo và chỉ chốt được sau khám. Ghi trạng thái này vào `khach.giai_doan` để người vận hành biết.

## 4. RÀO CẢN → MÃ L6 (nối với CRM)
Thiếu tự tin · sợ đau **L6.5** · sợ biến chứng/kết quả không tự nhiên **L6.5** · không biết chọn cơ sở uy tín **L6.2** · lo chi phí **L6.3** · chưa sắp xếp thời gian **L6.4** · cần hỏi người thân **L6.6** · chưa thấy minh chứng.

Mỗi rào cản có cách xử lý riêng trong [[BG-05-noi-so-phan-doi]]. Báo giá chỉ nên gỡ **đúng 2–3 rào cản khách thật sự nêu** — gỡ hết mọi rào cản là tự tạo nỗi lo khách chưa có.

## 5. CROSS-SELL (chỉ với khách Existing/LTV)
Cắt mí → trẻ hoá da / nâng mũi · Nâng mũi → cắt mí / độn cằm / trẻ hoá · Điều trị da → tiêm trẻ hoá / căng da / chăm sóc định kỳ.
⛔ Không nhét cross-sell vào báo giá của khách lần đầu — làm loãng quyết định chính.

Liên quan: [[BG-05-noi-so-phan-doi]] · [[BG-03-cau-truc-bao-gia]] · [[BG-02-bang-gia]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-11-noi-dau-cat-mi.md -->
<!-- ======================================================================== -->

# BG-11 — NỖI ĐAU KHÁCH HÀNG CẮT MÍ (chuyên sâu theo chân dung)
Version 1.0 · Nguồn: tổng hợp nội bộ Kangnam "Tổng hợp nỗi đau khách hàng quan tâm cắt mí" (2026-10-21)
Cập nhật: 2026-10-21

> Đây là file **chuyên sâu cho một dịch vụ**. Dùng kèm [[BG-04-chan-dung-khach]] (6 nhóm khách chung) và [[BG-05-noi-so-phan-doi]] (khuôn trả lời 3 nhịp).
> Khách cắt mí **không phải một tệp**. Chín chân dung dưới đây cần chín cách viết khối 3 và khối 4 khác nhau — dùng chung một đoạn mô tả cho cả chín là quay về bảng giá chung.

---

## 1. NHÓM A — CHƯA TỪNG LÀM MÍ (4 chân dung)

| # | Chân dung | Nỗi đau khách nói | Lo lắng ngầm | Mong muốn |
|---|---|---|---|---|
| **A1** | **Mắt một mí, không có nếp mí** | Mắt thiếu chiều sâu, đường nét chưa rõ · trang điểm khó tạo mí, phải dán kích mí thường xuyên | Phẫu thuật xong mắt bị **giả**, không tự nhiên | Nếp mí tự nhiên, hài hoà với khuôn mặt |
| **A2** | **Mắt nhỏ, khe mắt hẹp** | Mắt trông nhỏ, thiếu sức sống | Cắt mí xong **vẫn không cải thiện độ mở**; không biết nên cắt mí đơn thuần hay cần phương án khác | Đôi mắt trông to, sáng và cân đối hơn |
| **A3** | **Mí sụp, da chùng, nhiều mỡ mí** | Da mí che khuất nếp, mắt nặng nề · gương mặt mệt mỏi, già hơn tuổi | Cắt mí bị **trợn** hoặc **để lại sẹo** | Mắt gọn gàng, trẻ trung, nếp mí rõ nhưng mềm mại |
| **A4** | **Hai bên mí không đều** | Một bên có mí một bên không, hoặc hai bên khác độ cao · trang điểm khó cân đối | Làm xong **vẫn lệch** hoặc mất tự nhiên | Hai bên hài hoà hơn, phù hợp cấu trúc mắt |

### Cách viết khối 3–4 cho nhóm A
- **A1** — khối 3 nhắc *"phải dán kích mí mỗi ngày"*; khối 4 nhấn **thiết kế nếp theo tỉ lệ gương mặt**, có mô phỏng và chốt trước khi làm. Đây là cách gỡ đúng nỗi lo "sợ giả".
- **A2** — ⚠️ **không hứa mắt sẽ to hơn.** Độ mở của mắt phụ thuộc cơ nâng mi và cấu trúc hốc mắt, không phải lúc nào cắt mí đơn thuần cũng cải thiện. Khối 4 phải viết: *"cần bác sĩ khám trực tiếp để phân biệt khe mắt hẹp do da dư hay do cơ nâng mi yếu — hai tình trạng này có cách xử lý và chi phí khác nhau"*. Đưa khả năng cần phương án kèm (mở góc, chỉnh cơ nâng mi) vào khối *Phương án khác*.
- **A3** — phân biệt **da dư** với **sụp mí do cơ** là việc bắt buộc nêu ra, vì nó quyết định cả cách làm lẫn chi phí (`K4` §2). Khối 9 phải có câu trả lời cho *sợ trợn* và *sợ sẹo*.
- **A4** — ⚠️ **không hứa cân đối tuyệt đối.** Chữ đúng: *"cải thiện sự cân đối trong giới hạn cấu trúc giải phẫu của từng mắt"*. Hai mắt người bình thường vốn không đối xứng hoàn toàn — nói trước điều này **tăng** niềm tin, không giảm.

---

## 2. NHÓM B — ĐÃ LÀM MÍ NHƯNG CHƯA HÀI LÒNG (5 chân dung)

> Toàn bộ nhóm B thuộc **nhóm khách 5** trong `BG-04` (khách sửa lại): ám ảnh thất bại, cảnh giác cao, kiệt niềm tin, quyết theo bằng chứng y khoa.
> ⛔ **Rào R6 áp cho cả nhóm:** không bình luận, không phán xét nơi đã làm. Không dùng chữ *"làm hỏng"*, *"cứu ca hỏng"*, *"bác sĩ kia tay nghề kém"*.

| # | Chân dung | Nỗi đau khách nói | Lo lắng ngầm | Mong muốn |
|---|---|---|---|---|
| **B1** | **Mí tái sụp sau khi làm** | Nếp mí mờ dần hoặc da mí tiếp tục che nếp | Phải phẫu thuật lại, **tốn thêm chi phí** · mất niềm tin vì kết quả không duy trì | Xác định **nguyên nhân** và phương án chỉnh sửa phù hợp |
| **B2** | **Mí trợn, nếp quá cao hoặc quá sâu** | Mắt trông dữ, thiếu tự nhiên · khó biểu cảm, không giống diện mạo mong muốn | Chỉnh sửa lần nữa **vẫn không đẹp** | Nếp mí mềm mại, tự nhiên, hài hoà hơn |
| **B3** | **Đa nếp mí, mí lộn xộn** | Nhiều đường gấp mí, nếp chồng chéo · mắt thiếu cân đối, khó trang điểm | **Mô sẹo hoặc dính mô** khiến việc sửa phức tạp | Đánh giá nguyên nhân và tìm cách cải thiện đường mí |
| **B4** | **Mí lệch, bên to bên nhỏ** | Hai mắt không đồng đều sau phẫu thuật · nếp bên cao bên thấp hoặc độ mở khác nhau | Chỉnh sửa sẽ **ảnh hưởng thêm** đến mắt | Cải thiện cân đối trong giới hạn cấu trúc giải phẫu |
| **B5** | **Sẹo, nếp mí cứng, lộ dấu vết thẩm mỹ** | Đường mí rõ, cứng hoặc không tự nhiên | Sẹo **khó cải thiện, hồi phục lâu** · ngại giao tiếp, chụp ảnh, để mặt mộc | Được bác sĩ đánh giá **khả năng** cải thiện sẹo và đường mí |

### Luật viết báo giá cho nhóm B — bốn điều

**① Bước đầu tiên luôn là KHÁM ĐÁNH GIÁ LẠI, không phải phương án mổ.**
Mô hiện tại (sẹo, dính, lượng da còn lại, vị trí nếp cũ) quyết định cách xử lý. Khối 4 mở bằng: *"Trường hợp đã can thiệp trước đó cần khám đánh giá lại trước khi chốt phương án — chị không phải cam kết gì ở bước này."*

**② Nói đúng mong muốn của khách: họ muốn biết NGUYÊN NHÂN, không chỉ muốn báo giá.**
B1 và B3 ghi thẳng mong muốn là *"xác định nguyên nhân"*. Một tờ báo giá chỉ có số tiền sẽ trượt với nhóm này.

**③ Nêu giới hạn trước khi nêu kết quả.** Sửa mí là bài toán bị ràng buộc bởi phần đã mất. Chữ dùng:
> *"Mức cải thiện phụ thuộc tình trạng mô hiện tại và được bác sĩ đánh giá sau khi khám. Có những điểm cải thiện được nhiều, có điểm chỉ cải thiện một phần — bác sĩ sẽ nói rõ từng điểm khi khám."*

⛔ Cấm với nhóm B: *"sửa là đẹp ngay"*, *"xoá sạch sẹo"*, *"khắc phục hoàn toàn"*, *"về lại như chưa từng làm"*.

**④ Chi phí phần xử lý phần cũ phải TÁCH DÒNG RIÊNG**, không gộp để che (xem mục 4 — phí sửa mí).

---

## 3. NHÓM C — MƯỜI NỖI LO TRƯỚC KHI QUYẾT ĐỊNH

Bảng này là **nguồn trực tiếp cho khối 9** của báo giá. Cột 2 là thứ khách thật sự muốn biết — trả lời đúng cột 2, đừng trả lời cột 1 theo nghĩa đen.

| Nỗi lo | Điều khách thực sự muốn biết | Câu trả lời mẫu (đã qua cổng pháp lý) |
|---|---|---|
| **Sợ đau** | Mức độ đau trong và sau khi làm, phương pháp vô cảm | "Thực hiện với gây tê tại chỗ do bác sĩ chỉ định, kèm phác đồ giảm đau sau thủ thuật. Phần lớn khách mô tả là cảm giác căng tức hơn là đau." ⛔ không nói "không đau" |
| **Sợ sưng, bầm** | Thời gian hồi phục, **khi nào đi làm được** | "Sưng rõ nhất ở những ngày đầu rồi giảm dần, thường trong khoảng 7–14 ngày, tùy cơ địa mỗi người. Chị nói lịch công việc khi khám để bác sĩ xếp ngày phù hợp." ⛔ không mốc cứng |
| **Sợ mí bị trợn, giả** | **Bác sĩ thiết kế nếp mí như thế nào** để hài hoà | "Bác sĩ đo tỉ lệ mắt – chân mày – khuôn mặt rồi chọn độ cao nếp theo gương mặt chị, không theo một dáng có sẵn. Chị được xem mô phỏng và chốt trước khi thực hiện." |
| **Sợ sẹo** | Nguy cơ sẹo và **cách chăm sóc** sau phẫu thuật | "Đường mổ đặt đúng nếp mí nên khi mở mắt bị nếp che. Dao Plasma giúp thao tác chính xác và hạn chế tổn thương mô xung quanh, kết hợp chăm sóc đúng hướng dẫn nhằm giảm nguy cơ sẹo. Mức độ mờ sẹo phụ thuộc cơ địa mỗi người." ⛔ không nói "không sẹo" |
| **Sợ kết quả không như ảnh mẫu** | **Mắt của mình** có phù hợp dáng mí mong muốn không | "Dáng mí trong ảnh phụ thuộc cấu trúc mắt của từng người. Khi khám, bác sĩ sẽ nói rõ dáng chị thích có hợp với mắt chị không và đề xuất dáng hài hoà nhất." ⛔ không hứa "giống hình" |
| **Sợ biến chứng** | **Rủi ro, dấu hiệu bất thường và cách xử lý** | "Bác sĩ trao đổi trực tiếp về rủi ro có thể gặp trước khi chị quyết định. Sau thủ thuật chị có đầu mối liên hệ và lịch tái khám; thấy dấu hiệu bất thường thì báo ngay để được xử lý sớm." ⛔ không nói "không biến chứng" |
| **Sợ phải sửa lại** | **Khả năng duy trì** kết quả và yếu tố ảnh hưởng | "Độ bền của nếp mí phụ thuộc kỹ thuật, cơ địa và cách chăm sóc. Bệnh viện có chế độ theo dõi và chỉnh sửa theo chính sách bảo hành — em gửi chị điều kiện cụ thể kèm báo giá." ⛔ không nói "vĩnh viễn/trọn đời" |
| **Lo chi phí phát sinh** | **Tổng chi phí dự kiến**: thuốc, tái khám, chỉnh sửa nếu cần | Dòng *đã gồm / chưa gồm* ở khối 5 — đây là lý do dòng đó bắt buộc ([[BG-02-bang-gia]] mục 5) |
| **Không biết chọn bác sĩ** | Kinh nghiệm, chuyên môn và **ca thực tế phù hợp với tình trạng mình** | Nêu bác sĩ ở trạng thái `duyet` + case tương tự **giống tình trạng khách**, kèm link album ảnh khách đã thực hiện (mục 5) |
| **Từng làm hỏng ở nơi khác** | **Có sửa được không**, thời điểm nào phù hợp, **giới hạn cải thiện** | Xem luật nhóm B mục 2. Thêm: thời điểm sửa thường cần mô ổn định sau lần can thiệp trước — bác sĩ xác định khi khám |

---

## 4. GIẢI PHÁP & CHÍNH SÁCH GIÁ — CẮT MÍ BẰNG DAO PLASMA

### 4.1 Cách mô tả giải pháp — chép đúng, đừng viết lại cho "kêu" hơn
> **Ứng dụng dao Plasma trong tạo hình đường mí**, hỗ trợ thao tác chính xác, tạo đường mí sắc nét, thẩm mỹ và **hạn chế tổn thương mô xung quanh**. Kết hợp kỹ thuật thực hiện phù hợp và chăm sóc hậu phẫu đúng cách **nhằm giảm nguy cơ sẹo**, giúp nếp mí hồi phục tự nhiên hơn.

| ✅ Được nói | ⛔ Không được nói |
|---|---|
| hỗ trợ thao tác chính xác | "chính xác tuyệt đối" |
| hạn chế tổn thương mô xung quanh | "không tổn thương mô" |
| **nhằm giảm nguy cơ** sẹo | "không để lại sẹo", "xoá sẹo" |
| giúp nếp mí hồi phục **tự nhiên hơn** | "hồi phục siêu tốc", "3 ngày là xong" |
| đường mí sắc nét, thẩm mỹ | "đẹp như ý", "chuẩn từng milimet" |

⚠️ **R7:** Plasma là **thiết bị/kỹ thuật**, chỉ nêu đúng tính năng theo hồ sơ thiết bị của cơ sở. Không gắn thêm "công nghệ độc quyền", "duy nhất tại Việt Nam" nếu không có tài liệu.

### 4.2 Chính sách giá (cập nhật 2026-10-21)

| Trường hợp | Mã trong `bang-gia.json` | Niêm yết | Thực thu |
|---|---|---|---|
| **Khách cắt mí lần đầu** | `mat.cat-mi-plasma` | 10.000.000đ | **8.000.000đ** (giá ưu đãi) |
| **Khách sửa mí** | `mat.cat-mi-plasma` + `mat.phi-sua-mi` | 10.000.000đ + 3.000.000đ | **8.000.000đ + 1.500.000–1.800.000đ** (phí sửa mí giảm 40–50% tuỳ khu vực) |
| | | | → **tổng dự kiến 9.500.000 – 9.800.000đ** |

**Luật ghi vào báo giá:**
1. Khách lần đầu → ghi **hai dòng số**: niêm yết 10.000.000đ và ưu đãi 8.000.000đ. Khách cần thấy mình đang được gì, không chỉ thấy một con số.
2. Khách sửa mí → **phí sửa mí tách thành một dòng riêng**, ghi rõ đây là phần xử lý tình trạng đã can thiệp trước đó. ⛔ Không gộp vào giá cắt mí để tổng trông gọn — nhóm B rất nhạy với cảm giác bị giấu.
3. Mức giảm phí sửa mí **tuỳ khu vực** → phải **xác nhận với cơ sở thực hiện** trước khi chốt con số. Chưa xác nhận → ghi khoảng *1.500.000 – 1.800.000đ* và gắn `[CHỜ XÁC NHẬN]`.
4. Ưu đãi có thời hạn → ghi hạn vào `meta.hieu_luc_den`.

### 4.3 Hai dịch vụ hay đi kèm (có trong bảng giá, dùng khi bác sĩ chỉ định)
`mat.lay-mo-noi-soi-mi` 6.400.000đ (A3 nhiều mỡ mí) · `mat.chinh-sup-mi-bam-sinh` 12.000.000đ (A2/A3 sụp mí do cơ) · `mat.tao-khoe` 6.400.000đ (A2 khe mắt hẹp).
⚠️ Chỉ đưa vào báo giá khi **có căn cứ từ mô tả của khách hoặc chỉ định của bác sĩ** — không nhét thêm dòng để tăng tổng.

---

## 5. LINK ALBUM ẢNH KHÁCH HÀNG CẮT MÍ

```
https://hcigroup.vn/app/albumkn/?album=theme-1792573778761
```

- Đây là **link chia sẻ album ảnh khách hàng cắt mí đã thực hiện**, dùng để **gửi kèm báo giá**.
- Khai vào `du-lieu.json` ở trường `case_album.link`; template in thành một dòng mời xem ở khối case.
- **Gửi Zalo/Messenger:** dán link vào **tin nhắn**, không chỉ để trong ảnh — link trong ảnh JPG không bấm được.
- ⛔ Link album **không thay thế** điều kiện consent của từng ảnh khi bạn lấy ảnh ra chèn vào file báo giá ([[BG-06-proof-case]] mục 2). Gửi link là một việc, chèn ảnh vào ấn phẩm là việc khác.
- Kiểm link còn sống trước mỗi đợt gửi.

---

## 6. BẢN ĐỒ NHANH: CHÂN DUNG → NHÓM KHÁCH → ĐIỀU PHẢI CÓ TRONG BÁO GIÁ

| Chân dung | Nhóm `BG-04` | Khối 4 bắt buộc nói | Khối 9 bắt buộc có |
|---|---|---|---|
| A1 một mí | 1 · 3 · 4 | thiết kế nếp theo tỉ lệ gương mặt | sợ mí giả |
| A2 mắt nhỏ | 1 · 4 | phân biệt da dư / cơ nâng mi yếu | sợ kết quả không như ảnh mẫu |
| A3 sụp mí, mỡ mí | 1 · 6 | phân biệt da dư / sụp do cơ; xử lý mỡ mí | sợ trợn · sợ sẹo |
| A4 hai bên không đều | 1 · 3 | giới hạn cấu trúc giải phẫu | sợ làm xong vẫn lệch |
| B1 tái sụp | 5 | khám đánh giá lại để tìm nguyên nhân | sợ phải sửa lại · lo chi phí |
| B2 mí trợn | 5 | giới hạn cải thiện, không hứa lần này chắc đẹp | sợ sửa lần nữa vẫn không đẹp |
| B3 đa nếp mí | 5 | đánh giá mô sẹo / dính mô trước | lo việc sửa phức tạp |
| B4 mí lệch | 5 | cân đối trong giới hạn giải phẫu | sợ ảnh hưởng thêm đến mắt |
| B5 sẹo, nếp cứng | 5 | **khả năng** cải thiện, không hứa xoá sẹo | sợ hồi phục lâu · ngại giao tiếp |

Liên quan: [[BG-04-chan-dung-khach]] · [[BG-05-noi-so-phan-doi]] · [[BG-02-bang-gia]] · [[BG-06-proof-case]] · [[BG-07-cong-phap-ly]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-05-noi-so-phan-doi.md -->
<!-- ======================================================================== -->

# BG-05 — NỖI SỢ & PHẢN ĐỐI — THƯ VIỆN CÂU TRẢ LỜI TRONG BÁO GIÁ
Version 1.0 · Nguồn: `Kangnam-Agent-Factory/knowledge/K2-khach-hang.md` mục 4–5 · chi tiết sâu hơn ở `Agent-LDP-Kangnam/knowledge/KF-13-noi-so-phan-doi.md`
Cập nhật: 2026-10-21

---

## 1. KHUÔN TRẢ LỜI — ba nhịp, không đổi

```
① Thừa nhận    — gọi đúng tên nỗi lo, không gạt đi ("chị yên tâm" là câu vô nghĩa)
② Cơ chế thật  — nói cách bệnh viện xử lý điều đó, cụ thể, kiểm chứng được
③ Giới hạn     — nêu phần không hứa được: "tùy cơ địa", "bác sĩ đánh giá khi khám"
```

Thiếu nhịp ③ là **rào R1** — mọi câu chỉ có ①② đều trượt cổng pháp lý.

## 2. BẢY RÀO CẢN THƯỜNG GẶP

### L6.5 — Sợ đau
> **Mẫu:** "Thủ thuật thực hiện với gây tê/gây mê do bác sĩ chỉ định, kèm phác đồ giảm đau sau mổ. Phần lớn khách mô tả là cảm giác căng tức hơn là đau. Nếu chị khó chịu nhiều, báo ngay để bác sĩ điều chỉnh thuốc."

⛔ Cấm tuyệt đối: *"không đau"*, *"đau như kiến cắn"*, *"ngủ một giấc là xong"*.

### L6.5 — Sợ kết quả không tự nhiên / biến chứng
> **Mẫu:** "Nếp mí/dáng mũi được thiết kế theo tỉ lệ gương mặt của chị chứ không theo một dáng có sẵn; chị được xem mô phỏng và chốt trước khi làm. Quy trình thực hiện trong phòng mổ vô khuẩn, có hội chẩn chuyên môn. Kết quả cuối cùng vẫn phụ thuộc cơ địa mỗi người và được bác sĩ đánh giá riêng."

⛔ Cấm: *"an toàn tuyệt đối"*, *"không biến chứng"*, *"đẹp như hình"*.

### L6.3 — Lo chi phí
> **Mẫu:** "Em ghi rõ từng khoản để chị thấy tiền đi đâu, và phần nào chưa nằm trong giá. Nếu khoản này đang quá tầm, em đưa chị một phương án thấp hơn và nói thẳng nó khác ở đâu — chị chọn, em không đẩy."

Cách xử lý mạnh hơn giảm giá: **tách phương án thành giai đoạn** (làm phần ảnh hưởng nhiều nhất trước), hoặc đưa phương án thấp hơn ở khối *Phương án khác*.
⛔ **Không nêu trả góp** — Kangnam không có chính sách đó ([[BG-02-bang-gia]] mục 7).
⛔ Không tự giảm giá ngoài ưu đãi có văn bản ([[BG-02-bang-gia]] mục 3).

### L6.4 — Chưa sắp xếp được thời gian
> **Mẫu:** "Sưng nhiều trong vài ngày đầu rồi giảm dần, thường rõ trong khoảng 7–14 ngày, tùy cơ địa mỗi người. Chị nói lịch công việc khi khám để bác sĩ xếp ngày mổ hợp lý."

⛔ Cấm mốc cứng: *"3 ngày là đi làm được"*. Luôn dạng khoảng + *"tùy cơ địa mỗi người"*.

### L6.2 — Không biết chọn cơ sở nào
> **Mẫu:** "Chị có thể kiểm tra ba thứ ở bất kỳ cơ sở nào: giấy phép hoạt động, chứng chỉ hành nghề của bác sĩ trực tiếp thực hiện, và dịch vụ có nằm trong danh mục kỹ thuật được duyệt không. Bên em cung cấp đủ ba thông tin này khi chị tới khám."

⛔ **Rào R6:** không nêu tên, không hạ thấp cơ sở khác. Đưa **bộ tiêu chí** để khách tự đánh giá.

### L6.6 — Cần hỏi người nhà
> **Mẫu:** "Chị cứ gửi file này cho người nhà xem cùng. Trong đó có đủ phương án, chi phí và lộ trình. Nếu anh/chị ở nhà có câu hỏi, em sắp xếp cho cả hai cùng nghe bác sĩ tư vấn."

Đây là lý do tờ báo giá phải **đứng một mình đọc được** — người đọc thứ hai không có bối cảnh hội thoại.

### Khách sửa lại (nhóm 5) — ám ảnh thất bại
> **Mẫu:** "Trường hợp đã can thiệp trước đó cần khám đánh giá lại trước khi bàn phương án, vì tình trạng mô hiện tại quyết định cách xử lý. Em tách riêng bước đánh giá này để chị không phải cam kết gì trước khi biết rõ."

⛔ Không bình luận nơi cũ, không dùng chữ *"làm hỏng"*, *"cứu ca hỏng"*.

## 3. BA CÂU KHÁCH HAY NÓI — và cách xử lý trong báo giá

| Khách nói | Nghĩa thật | Báo giá cần |
|---|---|---|
| "Để em suy nghĩ thêm" | Chưa đủ tin hoặc chưa đủ tiền | Khối case tương tự + phương án theo giai đoạn |
| "Bên kia rẻ hơn" | Chưa thấy khác biệt nằm ở đâu | Dòng *đã gồm / chưa gồm* + bộ tiêu chí tự đánh giá (L6.2) |
| "Chị hỏi lại chồng/mẹ đã" | Cần tài liệu mang về | File PDF gọn, đọc độc lập được |

## 4. ĐIỀU KHÔNG BAO GIỜ LÀM
- ⛔ Khoét sâu nỗi sợ ("để lâu sẽ chảy xệ hơn") — quảng cáo dịch vụ khám chữa bệnh không được gây hoang mang.
- ⛔ Tạo khan hiếm giả ("còn 2 suất hôm nay").
- ⛔ Trả lời thay bác sĩ về chỉ định y khoa.
- ⛔ Hứa bất kỳ điều gì không có trong chính sách bằng văn bản.

Liên quan: [[BG-04-chan-dung-khach]] · [[BG-07-cong-phap-ly]] · [[BG-03-cau-truc-bao-gia]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-06-proof-case.md -->
<!-- ======================================================================== -->

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


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-01-ho-so-thuong-hieu.md -->
<!-- ======================================================================== -->

# BG-01 — HỒ SƠ THƯƠNG HIỆU & GIỌNG VIẾT TRONG BÁO GIÁ
Version 1.0 · Nguồn: `Kangnam-Agent-Factory/knowledge/K1-thuong-hieu.md` · `Agent-LDP-Kangnam/knowledge/KF-01-ho-so-thuong-hieu.md`
Cập nhật: 2026-10-21

---

## 1. ĐỊNH VỊ — quyết định cách báo giá

**"KANGNAM — CHUẨN MỰC ĐẦU TƯ NHAN SẮC."** Điểm đến **y khoa**, không phải spa làm đẹp.
Phân khúc trung–cao cấp, cạnh tranh bằng **giá trị** (bác sĩ · công nghệ · kết quả), **không bằng giá thấp**.

> Hệ quả trực tiếp cho agent này: một tờ báo giá của Kangnam **không được trông như bảng giá chợ**.
> Nó là **một phương án y khoa có giá kèm theo**, không phải một con số có dịch vụ kèm theo.

| Làm | Không làm |
|---|---|
| Nói *vì sao* phương án này hợp với khách trước, rồi mới tới tiền | Mở đầu bằng con số |
| Ghi rõ giá đã gồm gì, chưa gồm gì | Để khách tự đoán |
| Gọi tiền là **khoản đầu tư**, chia lộ trình theo giai đoạn khi hợp | Ép giảm giá để chốt nhanh · hứa trả góp (Kangnam không có) |
| Mời **thăm khám** như bước tiếp theo | Chốt cọc qua tin nhắn |

## 2. BỐN TRỤ CỘT — nguồn "bằng chứng" hợp lệ khi viết báo giá
1. **Bác sĩ** đúng chuyên khoa trực tiếp khám – tư vấn – thực hiện; chỉ định theo y khoa, không chạy doanh thu.
2. **Công nghệ** chuẩn Hàn, cập nhật Âu/Mỹ, nguồn gốc rõ ràng.
3. **Quy trình chuẩn hoá** khép kín trước – trong – sau; **hội chẩn 3 lớp**; phòng mổ vô khuẩn.
4. **Y đức** — minh bạch rủi ro, tôn trọng lựa chọn của khách.

⛔ Ngoài bốn trụ này, **không tự nghĩ ra lợi thế mới** (giải thưởng, số ca, tỉ lệ hài lòng…). Không có nguồn thì không viết.

## 3. GIỌNG VIẾT
**Chuyên môn – Điềm tĩnh – Trách nhiệm.** Không phô trương, không giật gân.

- Xưng hô: **em – chị/anh**; chưa rõ giới tính → **mình**. Không suy đoán giới tính qua tên hay avatar.
- Câu ngắn, mỗi ý một dòng. Khách đọc trên điện thoại, phần lớn trong lúc đang làm việc khác.
- Hạn chế thuật ngữ y khoa; cần dùng thì giải thích ngay trong ngoặc.
- ⛔ Không dùng emoji trong file báo giá (được dùng trong tin nhắn gửi kèm, tối đa 1–2).
- ⛔ Không hối thúc kiểu *"chỉ còn 2 suất"*, *"giá tăng sau hôm nay"* nếu đó không phải chính sách có thật bằng văn bản.

## 4. KEY MESSAGE (giữ tinh thần, không chép nguyên văn)
Đẹp an toàn · Đẹp chuẩn y khoa · Đẹp tự nhiên · Chuyên môn tạo nên khác biệt · Đồng hành cùng khách hàng.

## 5. CƠ SỞ & TUYẾN — luật cứng, không linh động
Hệ thống gồm **tuyến bệnh viện** và **tuyến viện thẩm mỹ / phòng khám tỉnh**.

| Tuyến | Được làm gì | Trong báo giá |
|---|---|---|
| **Bệnh viện thẩm mỹ** | Đại phẫu (hàm mặt, ngực, hút mỡ lớn, sụn sườn…) + toàn bộ dịch vụ khác | Ghi đúng tên bệnh viện thực hiện |
| **Viện thẩm mỹ / clinic tỉnh** | Da · spa · tiểu phẫu · tư vấn · tái khám | ⛔ **Không** mời đại phẫu. Phải ghi rõ: *tư vấn và đặt khám tại [viện], phẫu thuật tại [bệnh viện]* |

Trong `template/bang-gia.json`, dịch vụ đại phẫu được gắn cờ `"dai_phau": true` — tool render **tự chặn** nếu `meta.co_so` không phải tuyến bệnh viện (rào R3).

## 6. BÁC SĨ
Nêu tên bác sĩ theo đúng thông tin người lập báo giá đưa — đây là báo giá tham khảo gửi riêng một khách, không phải ấn phẩm phát hành, nên không có danh sách duyệt nào phải đối chiếu.

⛔ Vẫn không bịa: số ca, giải thưởng, số CCHN, học hàm học vị — không có nguồn thì không nhắc.

## 7. GIỚI HẠN BẮT BUỘC (trích K1 mục 6)
Không cam kết kết quả tuyệt đối · không tự tạo bằng cấp/giải thưởng/ca bệnh của bác sĩ · không gọi "số 1 / giỏi nhất" nếu không có tài liệu chính thức · **không báo giá cứng chưa xác nhận**.

> Câu cuối là lý do cổng bảng giá tồn tại: mọi con số trong báo giá phải truy được về `template/bang-gia.json`, và mọi báo giá đều phải mang dòng *"Chi phí cuối cùng do bác sĩ quyết định sau khi thăm khám trực tiếp."*

Liên quan: [[BG-02-bang-gia]] · [[BG-07-cong-phap-ly]] · [[BG-04-chan-dung-khach]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-08-design-system.md -->
<!-- ======================================================================== -->

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
"Google Sans","Google Sans Text","Be Vietnam Pro","Segoe UI",Roboto,…
```

**Google Sans**, font chính. Nó từng là font nội bộ của Google, nay đã phát hành trên Google Fonts **giấy phép OFL** (`fonts.google.com/metadata/fonts/Google%20Sans` → `"license":"ofl"`) nên nhúng lại được, và có sẵn bộ chữ tiếng Việt. Be Vietnam Pro đứng sau làm lớp đỡ. ⛔ **Product Sans thì không** — font đó vẫn thuộc giấy phép `googlerestricted`, không được nhúng.

| Luật | |
|---|---|
| **Độ đậm tối đa 700** | Google Sans là font **variable, trục wght chỉ tới 700**. ⛔ Không khai `800`/`900` trong CSS: trình duyệt hoặc kẹp về 700, hoặc tự bôi đậm giả — chữ nhoè, dấu tiếng Việt dính vào thân chữ |
| Một file cho cả dải | Google Fonts trả **cùng một woff2** cho mọi độ đậm 400–700. Bộ nhúng gom theo URL rồi khai `font-weight: 400 700`; không gom thì file phình gấp bốn |

Font **nhúng thẳng vào file** dưới dạng data URI, không dùng `<link>` tới CDN:
```bash
python tools/nhung-font.py --font "Google Sans" --nang 400 500 600 700
python tools/nhung-font.py --font "Inter"      # đổi sang font khác
```
Kết quả: `template/font-nhung.css` — **59 KB**, hai mảnh (latin + vietnamese).
⛔ **Không `<link>` tới Google Fonts** — máy render có thể không có mạng, font tải chậm làm Chrome chụp hụt chữ, và file khách mở lại sau một tháng sẽ phụ thuộc CDN còn sống. Nhúng data URI giải quyết cả ba.

Thiếu `font-nhung.css` thì tool in cảnh báo và file vẫn ra, chỉ là dùng font hệ thống — **không gửi khách bản đó** nếu đang cần bản đúng nhận diện.

| Vai trò | A4 | Slide |
|---|---|---|
| Tiêu đề chính | 19pt/700 | 56–74px/700 |
| Tiêu đề khối | 12,5pt/700 | 42px/700 |
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


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-09-schema-du-lieu.md -->
<!-- ======================================================================== -->

# BG-09 — SCHEMA DỮ LIỆU: ĐẦU VÀO & ĐẦU RA
Version 1.0 · Cập nhật: 2026-10-21
File mẫu: `template/du-lieu.mau.json` (ca cắt mí lần đầu) · `template/du-lieu.mau-sua-mi.json` (ca sửa mí — có giá ưu đãi, phí sửa mí tách dòng, album ảnh)

---

## 0. ĐẦU VÀO — thông tin khách do tư vấn viên đưa

Agent nhận **đoạn chat với khách**, lời kể, hoặc khối dưới đây, rồi sinh ra `du-lieu.json`:

```json
{
  "ten_hien_thi": "Chị Thu Hà", "xung_ho": "chị", "tuoi": 32,
  "khu_vuc": "Hà Nội", "kenh": "Zalo",
  "co_so_du_kien": "Bệnh viện thẩm mỹ Kangnam Hà Nội",
  "nhom_kh": 1,              // 1 công sở/tích góp · 2 doanh nhân · 3 KOC-Gen Z
                             // 4 sinh viên/mới đi làm · 5 khách sửa lại · 6 trung niên (BG-04)
  "giai_doan": "CÂN NHẮC",   // NHẬN BIẾT · TÌM HIỂU · CÂN NHẮC · THỰC HIỆN · HẬU PHẪU · GẮN BÓ
  "nhu_cau": "chữ của khách, chép nguyên văn",
  "mong_muon": ["...", "..."],
  "noi_so": ["...", "..."],
  "ngan_sach": 20000000,
  "thoi_diem_mong_muon": "trong tháng 11",
  "da_tu_van": "tóm tắt những gì đã trao đổi",
  "nguoi_lap": "Ngọc Anh — CSKH"
}
```

⛔ **Không nhận vào, không nhắc lại:** CCCD/CMND · số bảo hiểm · bệnh án · tình trạng bệnh lý chi tiết. Chỉ ghi điều **ảnh hưởng tới tư vấn** (vd *"đang cho con bú"*). Khách chưa xác minh danh tính thì tuổi ghi dạng khoảng (*30–35*).

---

## 1. LUỒNG

```
Thông tin khách hàng  →  [AGENT]  →  du-lieu.json  →  render_baogia.py  →  PDF + JPG
 (chat / JSON / CSV)      viết        dữ liệu có         3 cổng chặn         gửi khách
                        cá nhân hoá    cấu trúc
```

Agent **chỉ sinh ra `du-lieu.json`** và câu lệnh render. Agent **không tự vẽ PDF**, không tự bịa số.

## 2. ĐẦU VÀO — thông tin khách hàng

| Trường | Bắt buộc | Ghi chú |
|---|---|---|
| `ten_hien_thi` | ✔ | Tên khách tự xưng. ⛔ Không dùng tên trên giấy tờ nếu không cần |
| `xung_ho` | ✔ | `chị` / `anh` / `mình`. Chưa rõ giới tính → `mình` |
| `nhu_cau` | ✔ | Mô tả tình trạng + mong muốn, bằng **chữ của khách** |
| `mong_muon` | ✔ | 2–4 gạch đầu dòng ngắn — in thành chip trên báo giá |
| `noi_so` | nên | 2–3 nỗi lo khách đã nói → quyết định khối "băn khoăn" |
| `nhom_kh` | nên | 1–6 theo [[BG-04-chan-dung-khach]] → quyết định giọng |
| `giai_doan` | nên | NHẬN BIẾT / TÌM HIỂU / CÂN NHẮC / THỰC HIỆN / HẬU PHẪU / GẮN BÓ |
| `ngan_sach` | nên | `{tu, den}` — để chọn phương án, ⛔ không in lên file gửi khách |
| `co_so_du_kien` | ✔ | Quyết định cổng R3 (đại phẫu phải tuyến bệnh viện) |
| `thoi_diem_mong_muon` | nên | Ảnh hưởng lộ trình và hiệu lực báo giá |
| `da_tu_van` | nên | Đã khám chưa, bác sĩ nào đã xem — tránh nói quá |
| `nguoi_lap` | ✔ | In lên file |
| `hotline` | — | Bỏ trống thì lấy `template/thong-tin-lien-he.json`. Chỉ khai khi chi nhánh có số riêng |

⛔ **Không nhập:** CCCD/CMND · số bảo hiểm · bệnh án · ảnh khách chưa có consent · tình trạng bệnh lý chi tiết.

### `[CHỜ XÁC NHẬN]` dùng đúng chỗ

| Thứ | Có nguồn chưa | Ghi gì |
|---|---|---|
| **Hotline** | ✅ `template/thong-tin-lien-he.json` | Để trống `meta.hotline`, tool điền. ⛔ **Không bao giờ** `[CHỜ XÁC NHẬN]` |
| **Giá dịch vụ** | ✅ `template/bang-gia.json` | Mã không có trong bảng mới ghi `[CHỜ XÁC NHẬN]` |
| **Ưu đãi** | ❌ cần chứng từ | `[CHỜ XÁC NHẬN]` đúng chỗ |
| **Địa chỉ chi nhánh** | ❌ chưa có trong repo | `[CHỜ XÁC NHẬN]` đúng chỗ |

Thấy `[CHỜ XÁC NHẬN]` ở ba dòng đầu nghĩa là **quên nạp file dữ liệu cứng vào Knowledge**, không phải thiếu dữ liệu thật. Tool render tự thay placeholder của hotline bằng số thật và in cảnh báo.

Thiếu trường bắt buộc → agent chạy `/wizard` hỏi dẫn, tối đa 3 câu một lượt.

## 3. ĐẦU RA — `du-lieu.json`

```jsonc
{
  "meta": {
    "ma_bao_gia": "BG-2026-1021-01",   // bắt buộc, duy nhất
    "ngay": "21/10/2026",              // bắt buộc
    "hieu_luc_den": "04/11/2026",      // nên có — 7-14 ngày
    "co_so": "Bệnh viện thẩm mỹ Kangnam Hà Nội",  // bắt buộc, quyết định cổng R3
    "nguoi_lap": "Ngọc Anh — CSKH",    // bắt buộc
    "sdt_tu_van": "", "kenh_gui": "Zalo"
    // hotline: bỏ trống -> lấy template/thong-tin-lien-he.json
  },

  "khach": {
    "ten_hien_thi": "Chị Thu Hà",      // bắt buộc
    "xung_ho": "chị",
    "mo_ta_ngan": "...",               // 2-3 câu, nhắc lại đúng chữ khách nói
    "mong_muon": ["...", "..."],       // in thành chip xanh
    "noi_so": ["...", "..."]           // in thành chip cam
  },

  "mo_dau": { "tieu_de": "...", "loi_mo": "..." },   // bắt buộc, xem BG-03 mục 3

  "van_de_giai_phap": [            // 3-4 cặp. Xương sống của mạch đọc (BG-03 mục 1b)
    { "van_de": "nỗi lo bằng CHỮ CỦA KHÁCH",
      "giai_phap": "cách bên em xử lý đúng vấn đề đó + giới hạn trung thực" }
  ],                               // bắt buộc có cái này HOẶC giai_toa, ⛔ không nói trùng nhau

  "giai_phap": {
    "ten_phuong_an": "...",            // bắt buộc
    "vi_sao_hop": "...",               // phần đắt giá nhất — nối vào tình trạng khách
    "gom": [ {"buoc": "...", "noi_dung": "..."} ],
    "diem_can_luu_y": ["..."]          // điều bác sĩ cần xác nhận khi khám
  },

  "chi_phi": {
    "dong": [                          // bắt buộc, ít nhất 1 dòng
      { "ma": "mat.cat-mi-6d",         // BẮT BUỘC trỏ về bang-gia.json
        "gia": 12800000,
        "so_luong": 1,
        "dien_giai": "...",
        "ly_do_lech": "..."            // chỉ khi giá khác bảng niêm yết
      }
    ],
    "uu_dai": [ {"ten": "...", "gia_tri": 2000000, "dieu_kien": "...", "han": "..."} ],
    "ghi_chu_gia": "đã gồm ... chưa gồm ..."       // nên có
  },                               // ⛔ KHÔNG có trường tra_gop — Kangnam không có
                                   //    chính sách trả góp, cổng dữ liệu CHẶN (BG-02 mục 7)

  "phuong_an_khac": [ {"ten": "...", "gia": 8000000, "khac_biet": "..."} ],

  "case_tuong_tu": [
    { "ma_case": "CM-0423", "mo_ta": "...", "bac_si": "Henry Nguyen",
      "moc_chup": "sau 1 tháng",       // BẮT BUỘC nếu có ảnh
      "ket_qua": "...",
      "nhom": "mat",                   // body/lipo/giảm cân → chặn ảnh (R12)
      "can_anh": true,                 // case SẼ có ảnh nhưng đang chờ xin → dựng ô ảnh tạm
      "anh_truoc": "anh/truoc-01.jpg",
      "anh_sau": "anh/sau-01.jpg",
      "anh_them": "anh/them-01.jpg",   // ô ảnh THỨ BA — lưới tự chuyển 3 cột
      "chu_thich_truoc": "Trước",      // ba nhãn đều đặt lại được. Ảnh album Kangnam
      "chu_thich_sau": "sau 1 tháng",  // thường ĐÃ ghép sẵn trước–sau → lúc đó đặt
      "chu_thich_them": "Góc khác" }   // "Ca 1 · Ca 2 · Ca 3" (BG-08 mục 5)
  ],

  "case_album": {                      // album ảnh khách thật (BG-06 mục 2)
    "album": "theme-1792573778761",    // id album -> TOOL TỰ GỌI API LẤY 3 ẢNH
                                       //   cho case nào chưa có ảnh. Danh mục:
                                       //   template/album-index.json (29 album)
    "link": "https://hcigroup.vn/app/albumkn/?album=theme-1792573778761",
    "nhan": "Hình ảnh khách hàng đã cắt mí tại Kangnam"
  },

  "lo_trinh": [ {"moc": "Bước 1 — Đặt lịch khám", "viec": "..."} ],
  "giai_toa": [ {"noi_so": "...", "tra_loi": "..."} ],

  "cta": { "buoc_tiep": "...", "mo_ta": "...", "nut": "...", "dia_chi": "..." },

  "phap_ly": {
    "gxnndqc": false,
    "ghi_chu": "Báo giá cá nhân gửi 1-1 theo yêu cầu khách hàng."
    // "mien_tru": [...]  — để trống thì tool tự điền 3 câu chuẩn
  }
}
```

## 4. TRƯỜNG TOOL TỰ TÍNH — agent không cần ghi
`chi_phi.tong_tam_tinh` · `tong_ht` · `sau_uu_dai` · `sau_uu_dai_ht` · `*_ht` (chuỗi tiền) · `gia_niem_yet_ht` (tự in khi `gia` = `uu_dai_hien_hanh` của bảng giá) · `co_van_de` · `co_case` · `co_album` · `co_bang_chung` · `co_anh_bat_ky` · `hien_anh` · `co_anh_them` · `chu_thich_*` · `co_lo_trinh` · `co_giai_toa` · `co_phuong_an_khac` · `co_luu_y` · `_co_dai_phau` · `phap_ly.mien_tru` (nếu để trống) · `font_nhung` (nội dung `template/font-nhung.css`).

Muốn ghi đè tổng (vd giá gói đã duyệt) thì khai thẳng `chi_phi.sau_uu_dai`.

## 5. QUY ƯỚC ĐẶT TÊN & THƯ MỤC
```
out/<ma_bao_gia>/
├── du-lieu.json          dữ liệu agent sinh ra
├── anh/                  ảnh case (nếu có)
├── BG-....html           bản A4 dựng ra
├── BG-....pdf            gửi email / in
├── BG-....-slide.html
└── BG-....-01..05.jpg    gửi Zalo
```
Mã báo giá: `BG-<năm>-<ngàytháng>-<số thứ tự trong ngày>`.

## 6. BA CỔNG CHẶN CỦA TOOL
| Cổng | Chặn khi |
|---|---|
| **Dữ liệu** | thiếu trường bắt buộc, `chi_phi.dong` rỗng |
| **Bảng giá** | mã không có trong `bang-gia.json` · giá lệch mà không khai `ly_do_lech` · dịch vụ `lien_he` mà tự đặt số |
| **Pháp lý** | từ cấm · mốc hồi phục cứng · bác sĩ sai trạng thái · ảnh thiếu consent/mốc chụp · ảnh cơ thể · thiếu câu miễn trừ · đại phẫu sai tuyến |

Liên quan: [[BG-02-bang-gia]] · [[BG-07-cong-phap-ly]] · [[BG-08-design-system]]


<!-- ======================================================================== -->
<!-- NGUỒN: knowledge/BG-10-vong-hoc.md -->
<!-- ======================================================================== -->

# BG-10 — VÒNG HỌC: BÁO GIÁ NÀO CHỐT ĐƯỢC
Version 1.0 · Cập nhật: 2026-10-21

> Agent chỉ khá lên nếu kết quả thật được ghi lại. Không có file này, mỗi báo giá là một lần đoán mới.

---

## 1. BỐN CHỈ SỐ — không có chỉ số thứ năm

| Chỉ số | Đo gì | Nguồn |
|---|---|---|
| **Tỉ lệ phản hồi** | gửi file → khách nhắn lại | tư vấn viên |
| **Tỉ lệ đặt khám** | gửi file → đặt lịch khám | CRM |
| **Tỉ lệ show-up** | đặt khám → tới thật | lễ tân / ERP |
| **Tỉ lệ chốt** | tới khám → thực hiện dịch vụ | ERP |

⛔ Không tối ưu cho "file đẹp" hay "khách khen". Một tờ báo giá đẹp mà không ai đặt khám là một tờ thất bại.

## 2. BẢNG GHI — mỗi báo giá một dòng

| Mã BG | Ngày | Nhóm KH | Giai đoạn | Dịch vụ | Tổng | Kênh gửi | Phản hồi | Đặt khám | Show-up | Chốt | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(ví dụ)* BG-2026-1021-01 | 21/10 | 1 | CÂN NHẮC | cắt mí 6D | 17,2tr | Zalo | có | có | — | — | khách hỏi thêm về nghỉ làm |

> Bảng này bắt đầu trống. Điền tay sau mỗi ca, hoặc xuất từ CRM rồi dán vào.

## 3. BỐN CÂU HỎI RÀ MỖI THÁNG
1. **Nhóm khách nào chốt tốt nhất?** → ưu tiên mẫu câu của nhóm đó.
2. **Giai đoạn nào gửi báo giá hiệu quả nhất?** (giả thuyết hiện tại: CÂN NHẮC) → nếu dữ liệu nói khác, sửa [[BG-04-chan-dung-khach]] mục 3.
3. **Khối nào khách hay hỏi lại sau khi nhận file?** Khách hỏi lại = khối đó viết chưa đủ.
   - Hỏi lại về tiền → thiếu dòng *đã gồm / chưa gồm*
   - Hỏi lại về nghỉ bao lâu → khối lộ trình yếu
   - Hỏi "có thật không" → thiếu case/ảnh
4. **Báo giá nào bị đem đi so giá?** → thường do gửi quá sớm (giai đoạn NHẬN BIẾT) hoặc mở đầu bằng con số.

## 4. BA GIẢ THUYẾT ĐANG CHỜ KIỂM CHỨNG
| # | Giả thuyết | Đo bằng |
|---|---|---|
| 1 | Gửi **cả PDF + ảnh slide** chốt tốt hơn chỉ gửi một loại | so tỉ lệ phản hồi |
| 2 | Báo giá có **case tương tự kèm ảnh thật** tăng tỉ lệ đặt khám với nhóm 1, 4, 5 | so nhóm có ảnh vs ô ảnh tạm |
| 3 | Khối **"phương án khác"** làm tăng chốt (khách thấy mình được chọn) hay giảm chốt (phân vân) | A/B theo tuần |

Có số rồi thì ghi kết luận vào đây và sửa thẳng vào knowledge tương ứng.

## 5. CÁCH CẬP NHẬT KNOWLEDGE TỪ KẾT QUẢ
```
Thấy mẫu lặp lại ≥ 5 ca
   → viết thành một dòng luật trong file knowledge đúng chủ đề
   → ghi vào doc/CHANGELOG.md (ngày + lý do + dựa trên bao nhiêu ca)
   → nói cho người dùng agent biết luật mới
```
⛔ Không sửa luật vì **một** ca. Một ca là giai thoại, không phải dữ liệu.

Liên quan: [[BG-03-cau-truc-bao-gia]] · [[BG-04-chan-dung-khach]]

