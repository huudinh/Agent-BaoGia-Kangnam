#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng trang hướng dẫn Agent-BaoGia-Kangnam — nhúng nội dung THẬT từ repo.

Chạy:     python tools/build-huong-dan.py
Kết quả:  tools/huong-dan.html  -> publish đè lại cùng URL artifact (xem README mục
          "Hướng dẫn cài đặt"). File .html là bản sinh ra, KHÔNG sửa tay.
Sửa nội dung trang: sửa tools/huong-dan.tpl.html rồi chạy lại script này.
"""
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "huong-dan.html")

for _l in (sys.stdout, sys.stderr):
    if hasattr(_l, "reconfigure"):
        _l.reconfigure(encoding="utf-8", errors="replace")

# (tên file, tiêu đề, mô tả, có phải file lõi không)
BG_ORDER = [
    ("BG-07-cong-phap-ly", "Cổng pháp lý", "Rào R0–R12 + bảng từ cấm. Fail = không xuất file", True),
    ("BG-02-bang-gia", "Luật nói về tiền", "Nguồn giá duy nhất · ưu đãi · giá lệch · đã gồm/chưa gồm", True),
    ("BG-03-cau-truc-bao-gia", "Cấu trúc 9 khối", "Xương sống của tờ báo giá — thứ tự không đảo", True),
    ("BG-04-chan-dung-khach", "Chân dung khách", "6 nhóm · 6 giai đoạn · khi nào CHƯA nên gửi báo giá", True),
    ("BG-11-noi-dau-cat-mi", "Nỗi đau khách cắt mí", "9 chân dung · 10 nỗi lo · giải pháp Plasma · chính sách giá", True),
    ("BG-05-noi-so-phan-doi", "Nỗi sợ & phản đối", "Khuôn trả lời 3 nhịp cho khối băn khoăn", False),
    ("BG-06-proof-case", "Case & ảnh trước–sau", "4 điều kiện dùng một case · link album · ô ảnh tạm", False),
    ("BG-01-ho-so-thuong-hieu", "Hồ sơ thương hiệu", "Giọng viết · cơ sở & tuyến · bác sĩ · giới hạn phát ngôn", False),
    ("BG-08-design-system", "Design system", "Token màu · 3 trang A4 · 5 slide · giới hạn độ dài", False),
    ("BG-09-schema-du-lieu", "Schema dữ liệu", "Cấu trúc du-lieu.json — đầu vào/đầu ra của tool", False),
    ("BG-10-vong-hoc", "Vòng học", "4 chỉ số thật — hiện đang trống, chờ dữ liệu", False),
]

PROMPT_FILES = [
    ("baogia", "Tạo báo giá", "prompts/prompt-bao-gia.md"),
    ("wizard", "Hỏi dẫn từ đầu", "prompts/prompt-wizard.md"),
    ("tinnhan", "Tin nhắn gửi kèm", "prompts/prompt-tin-nhan.md"),
    ("vanhanh", "Vận hành & kiểm tra", "prompts/prompt-van-hanh.md"),
]

# Ba ô mà nền tảng nào cũng hỏi khi tạo agent mới.
# Mô tả giữ dưới 300 ký tự — giới hạn ô Description của ChatGPT Custom GPT.
META_FORM = {
    "ten": "Agent-BaoGia-Kangnam",
    "mota": ("Tạo báo giá cá nhân hoá cho từng khách hàng Kangnam: đọc thông tin khách, "
             "chọn phương án theo bảng giá chính thức, viết nội dung đã qua cổng pháp lý, "
             "rồi xuất ra PDF A4 và 5 ảnh gửi Zalo. Không bịa giá, không cam kết kết quả."),
    "starters": [
        "/baogia — em dán đoạn chat với khách vào đây",
        "/wizard cắt mí",
        "/tinnhan cho báo giá vừa làm",
        "/kiemtra câu này có vi phạm gì không",
    ],
}

DATA_FILES = [
    ("bang-gia.json", "Bảng giá — nguồn giá duy nhất",
     "Mọi con số tiền trong báo giá phải truy về file này. Thiếu nó, agent sẽ đoán giá.", True),
    ("bac-si-duyet.json", "Bác sĩ được nêu tên",
     "4 trạng thái: duyet · can_xac_minh · xung_dot · ngung_dung. Chỉ duyet mới được in ra file.", True),
    ("thong-tin-lien-he.json", "Hotline in lên báo giá",
     "Nguồn duy nhất. Đổi số ở đây là mọi báo giá sinh ra sau đó đổi theo.", True),
    ("du-lieu.mau.json", "Mẫu đầu ra — ca cắt mí lần đầu",
     "Nạp kèm để agent sinh JSON đúng cấu trúc ngay lần đầu.", False),
    ("du-lieu.mau-sua-mi.json", "Mẫu đầu ra — ca sửa mí",
     "Có giá ưu đãi, phí sửa mí tách dòng và link album. Ca khó nhất, dùng làm chuẩn.", False),
]


def doc(path):
    return io.open(os.path.join(REPO, path), encoding="utf-8").read()


def copyblock(path):
    """Rút khối giữa hai vạch ▼▲ của SYSTEM-PROMPT.

    ⛔ Không dùng regex ``` … ```: bộ não có khối ``` lồng bên trong (hộp quy trình,
    checklist cổng) nên regex sẽ cắt cụt ở fence đầu tiên.
    """
    s = doc(path)
    try:
        a, b = s.index("▼▼▼"), s.index("▲▲▲")
    except ValueError:
        sys.exit("Khong tim thay vach ▼▲ trong " + path)
    seg = s[a:b].split("\n", 1)[1].strip()
    if seg.startswith("```"):
        seg = seg.split("\n", 1)[1]
    if seg.rstrip().endswith("```"):
        seg = seg.rstrip().rsplit("\n", 1)[0]
    seg = seg.strip()
    if not seg.startswith("#"):
        sys.exit("Khoi copy trong %s khong bat dau bang tieu de" % path)
    return seg


def kb(name):
    return doc("knowledge/" + name + ".md")


def fmt(n):
    return "{:,}".format(n).replace(",", ".")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ------------------------------------------------------------------ prompts
def parse_prompts(path):
    """Rút prompt nguyên văn từ file .md: khối ``` và dòng bảng có prompt trong backtick."""
    lines = doc(path).split("\n")
    out, head, i = [], None, 0
    while i < len(lines):
        l = lines[i]
        if re.match(r"^#{2,3} ", l):
            head = re.sub(r"^#{2,3} ", "", l).strip()
            i += 1
            continue
        if l.strip().startswith("```"):
            j, buf = i + 1, []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            body = "\n".join(buf).strip()
            if body and not body.startswith(("python ", "for /d", "Get-ChildItem")):
                out.append(("full", head, body))
            i = j + 1
            continue
        if l.startswith("|") and l.count("`") >= 2:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) >= 2 and re.fullmatch(r"`[^`]+`", cells[-1]):
                out.append(("short", re.sub(r"[*`]", "", cells[0]).strip(), cells[-1].strip("`")))
            i += 1
            continue
        i += 1
    return out


def clean_title(t):
    t = re.sub(r"^\d+[a-z]?\.\s*", "", t or "")
    t = re.sub(r"\s*\(.*?\)\s*$", "", t)
    return t.strip() or "Prompt"


def build_prompts(payload):
    cards, n, counts = [], 0, {}
    for key, label, path in PROMPT_FILES:
        items = parse_prompts(path)
        counts[key] = len(items)
        seen = {}
        for kind, title, body in items:
            n += 1
            pid = "p%d" % n
            payload[pid] = body
            t = clean_title(title)
            seen[t] = seen.get(t, 0) + 1
            if seen[t] > 1:
                t = "%s · %d" % (t, seen[t])
            cards.append(
                '<article class="prompt" data-g="%s">'
                '<div class="prompt-h"><span class="n">%02d</span>'
                '<span class="t">%s</span><span class="k">%s</span></div>'
                '<pre class="prompt-b">%s</pre>'
                '<div class="prompt-f"><span class="get">%s · %s ký tự</span>'
                '<button class="copy" data-copy="%s" type="button">Copy prompt</button></div>'
                "</article>"
                % (key, n, esc(t), "Đầy đủ" if kind == "full" else "Một dòng",
                   esc(body), label, fmt(len(body)), pid))
    return "\n".join(cards), n, counts


def build_meta(payload):
    """Ba ô Tên · Mô tả · Câu mở đầu, mỗi ô một nút copy."""
    payload["m_ten"] = META_FORM["ten"]
    payload["m_mota"] = META_FORM["mota"]
    st = []
    for i, c in enumerate(META_FORM["starters"], 1):
        payload["m_st%d" % i] = c
        st.append('<div class="st-i"><span>%s</span>'
                  '<button class="copy" data-copy="m_st%d" type="button">Copy</button></div>'
                  % (esc(c), i))
    return (
        '<div class="mrow"><span class="lb">Tên</span>'
        '<span class="vl mono">%s</span>'
        '<button class="copy" data-copy="m_ten" type="button">Copy</button></div>'
        '<div class="mrow"><span class="lb">Mô tả</span>'
        '<span class="vl">%s</span>'
        '<button class="copy" data-copy="m_mota" type="button">Copy</button></div>'
        '<div class="mrow"><span class="lb">Câu mở đầu</span>'
        '<div class="st">%s</div></div>'
        % (esc(META_FORM["ten"]), esc(META_FORM["mota"]), "".join(st)))


# ------------------------------------------------------------------ file cards
def build_files(payload):
    cards = []
    items = [(nm + ".md", ti, de, st, "knowledge/" + nm + ".md") for nm, ti, de, st in BG_ORDER]
    items += [(fn, ti, de, st, "template/" + fn) for fn, ti, de, st in DATA_FILES]
    for i, (fname, title, desc, star, rel) in enumerate(items, 1):
        body = doc(rel)
        fid = "f%d" % i
        payload[fid] = body
        xem = esc(body[:2600])
        if len(body) > 2600:
            xem += "\n\n… (còn %s ký tự — bấm Copy để lấy đủ)" % fmt(len(body) - 2600)
        cards.append(
            '<article class="fcard%s">'
            '<div class="fcard-h"><span class="fname">%s</span>%s'
            '<span class="fsize">%s ký tự</span>'
            '<button class="copy" data-copy="%s" type="button">Copy</button></div>'
            '<p class="fhow"><b>%s</b> — %s</p>'
            '<details class="fview"><summary>Xem nội dung</summary>'
            '<pre class="filebody">%s</pre></details>'
            "</article>"
            % (" hi" if star else "", esc(fname),
               '<span class="fbadge">★ lõi</span>' if star else "",
               fmt(len(body)), fid, esc(title), esc(desc), xem))
    return "\n".join(cards)


# ------------------------------------------------------------------ dựng trang
brain = copyblock("SYSTEM-PROMPT.md")
short = copyblock("SYSTEM-PROMPT-NGAN.md")

merged = ("# TRI THỨC GỘP — AGENT-BAOGIA-KANGNAM\n"
          "# 11 file knowledge nối liền, thứ tự đọc: pháp lý → tiền → cấu trúc → khách → dịch vụ\n"
          "# Dùng khi nền tảng không cho upload nhiều file.\n"
          "# Bản gốc: github.com/huudinh/Agent-BaoGia-Kangnam/tree/main/knowledge\n"
          "# LƯU Ý: bản gộp này KHÔNG chứa bang-gia.json và bac-si-duyet.json —\n"
          "# hai file dữ liệu cứng đó phải nạp riêng, nếu không agent sẽ đoán giá.\n\n"
          + "\n\n".join("<!-- ===== %s.md ===== -->\n\n%s" % (nm, kb(nm))
                        for nm, _t, _d, _s in BG_ORDER))

payload = {"a": brain, "b": short, "c": merged}
prompt_cards, prompt_n, counts = build_prompts(payload)
meta_box = build_meta(payload)
file_cards = build_files(payload)

bang_gia = json.loads(doc("template/bang-gia.json"))
bac_si = json.loads(doc("template/bac-si-duyet.json"))
n_duyet = sum(1 for b in bac_si["bac_si"] if b["trang_thai"] == "duyet")

rows = []
for nm, title, desc, star in BG_ORDER:
    rows.append(
        '<tr%s><td><code>%s.md</code>%s</td><td><b>%s</b><br><span class="dim">%s</span></td>'
        '<td class="num">%s</td></tr>'
        % (' class="hl"' if star else "", nm, ' <span class="star">★</span>' if star else "",
           esc(title), esc(desc), fmt(len(kb(nm)))))

blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

html = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "huong-dan.tpl.html"),
               encoding="utf-8").read()
for k, v in [
    ("@@KB_ROWS@@", "\n".join(rows)),
    ("@@FILE_CARDS@@", file_cards),
    ("@@META_BOX@@", meta_box),
    ("@@LEN_MOTA@@", str(len(META_FORM["mota"]))),
    ("@@PROMPT_CARDS@@", prompt_cards),
    ("@@PROMPT_N@@", str(prompt_n)),
    ("@@N_BAOGIA@@", str(counts["baogia"])),
    ("@@N_WIZARD@@", str(counts["wizard"])),
    ("@@N_TINNHAN@@", str(counts["tinnhan"])),
    ("@@N_VANHANH@@", str(counts["vanhanh"])),
    ("@@LEN_A@@", fmt(len(brain))),
    ("@@LEN_B@@", fmt(len(short))),
    ("@@LEN_C@@", fmt(len(merged))),
    ("@@KB_C@@", str(round(len(merged.encode("utf-8")) / 1024))),
    ("@@N_FILE@@", str(len(BG_ORDER))),
    ("@@N_DICHVU@@", str(len(bang_gia["dich_vu"]))),
    ("@@N_BACSI@@", str(n_duyet)),
    ("@@CAP_NHAT@@", bang_gia["cap_nhat"]),
    ("@@PAYLOAD@@", blob),
]:
    html = html.replace(k, v)

con_lai = re.findall(r"@@[A-Z_]+@@", html)
if con_lai:
    sys.exit("Con placeholder chua thay: " + ", ".join(sorted(set(con_lai))))

io.open(OUT, "w", encoding="utf-8").write(html)
print("Đã ghi:", OUT, "-", round(os.path.getsize(OUT) / 1024), "KB")
print("Thẻ A:", fmt(len(brain)), "| Thẻ B:", fmt(len(short)), "| Thẻ C:", fmt(len(merged)))
print("Prompt:", prompt_n, counts)
print("Bảng giá:", len(bang_gia["dich_vu"]), "dịch vụ |", n_duyet, "bác sĩ duyệt")
