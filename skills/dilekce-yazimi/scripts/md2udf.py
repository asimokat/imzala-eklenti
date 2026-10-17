# -*- coding: utf-8 -*-
"""Markdown -> UYAP UDF donusturucu.

Destek: ### baslik (bold, ortali/sol), **kalin**, *italik*, "> " alinti blogu,
"- " madde, normal paragraf (iki yana yasli).
UDF = ZIP( content.xml ). Offsetler CDATA metnindeki karakter indeksleridir;
her paragraf kendi satir sonu karakterini de kapsar.
"""
import re, sys, zipfile, os

FONT = "Times New Roman"
SIZE = 12


class Doc:
    def __init__(self):
        self.text = []          # CDATA parcalari
        self.pos = 0
        self.paragraphs = []    # (alignment, indent, [(start, length, bold, italic)])

    def add(self, runs, alignment=3, indent=0.0):
        """runs: [(metin, bold, italic)] — paragraf sonuna \n eklenir."""
        spans = []
        for txt, bold, ital in runs:
            if txt == "":
                continue
            self.text.append(txt)
            spans.append((self.pos, len(txt), bold, ital))
            self.pos += len(txt)
        # satir sonu: son span'a dahil et (UDF boyle bekliyor)
        self.text.append("\n")
        if spans:
            s, l, b, i = spans[-1]
            spans[-1] = (s, l + 1, b, i)
        else:
            spans.append((self.pos, 1, False, False))
        self.pos += 1
        self.paragraphs.append((alignment, indent, spans))


INLINE = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*)", re.S)


def parse_inline(s):
    """**kalin** ve *italik* isaretlerini runs listesine cevirir."""
    out = []
    for part in INLINE.split(s):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append((part[2:-2], True, False))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            out.append((part[1:-1], False, True))
        else:
            out.append((part, False, False))
    return out or [(s, False, False)]


def build(md_path, udf_path):
    raw = open(md_path, encoding="utf-8").read().replace("\r", "")
    # UYAP editorunde sorun cikarmamasi icin ozel parantezleri sadelestir
    raw = raw.replace("【", "[").replace("】", "]")
    # yorum/talimat bloklarini at
    lines = raw.split("\n")
    doc = Doc()

    buf, mode = [], None

    def flush():
        nonlocal buf, mode
        if not buf:
            return
        text = " ".join(x.strip() for x in buf).strip()
        text = re.sub(r"\s+", " ", text)
        if text:
            if mode == "quote":
                doc.add(parse_inline(text), alignment=3, indent=14.0)
            elif mode == "bullet":
                doc.add(parse_inline("– " + text), alignment=3, indent=10.0)
            else:
                doc.add(parse_inline(text), alignment=3)
        buf, mode = [], None

    for raw_line in lines:
        line = raw_line.rstrip()
        st = line.strip()
        if st == "":
            flush()
            continue
        if st == "---":
            flush()
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", st)
        if m:
            flush()
            lvl, txt = len(m.group(1)), m.group(2).strip()
            txt = re.sub(r"\*+", "", txt)
            doc.add([(txt, True, False)], alignment=1 if lvl <= 2 else 0)
            continue
        if st.startswith(">"):
            t = re.sub(r"^>\s?", "", st)
            if mode != "quote":
                flush()
            mode = "quote"
            buf.append(t)
            continue
        if re.match(r"^[-•]\s+", st):
            flush()
            mode = "bullet"
            buf.append(re.sub(r"^[-•]\s+", "", st))
            continue
        if mode in ("quote", "bullet"):
            buf.append(st)
            continue
        mode = "p"
        buf.append(st)
    flush()

    body = "".join(doc.text)
    if "]]>" in body:
        body = body.replace("]]>", "] ]>")

    els = []
    for align, indent, spans in doc.paragraphs:
        runs = []
        for (s, l, b, i) in spans:
            attrs = ['family="%s"' % FONT, 'size="%d"' % SIZE,
                     'startOffset="%d"' % s, 'length="%d"' % l]
            if b:
                attrs.append('bold="true"')
            if i:
                attrs.append('italic="true"')
            runs.append("<content " + " ".join(attrs) + " />")
        pattrs = ['Alignment="%d"' % align, 'LineSpacing="0.0"',
                  'SpaceAbove="2.0"', 'SpaceBelow="4.0"', 'RightIndent="0.0"',
                  'LeftIndent="%.1f"' % indent]
        els.append("<paragraph " + " ".join(pattrs) + ">" + "".join(runs) + "</paragraph>")

    xml = (
        '<?xml version="1.0" encoding="UTF-8" ?>\n\n'
        '<template format_id="1.8" >\n'
        '<content><![CDATA[' + body + ']]></content>'
        '<properties><pageFormat mediaSizeName="1" leftMargin="70.0" rightMargin="50.0" '
        'topMargin="60.0" bottomMargin="50.0" paperOrientation="1" headerFOffset="20.0" '
        'footerFOffset="20.0" /></properties>\n'
        '<elements resolver="hvl-default" >\n' + "\n".join(els) + '\n</elements>\n'
        '<styles><style name="default" family="Dialog" size="12" description="Geçerli" />'
        '<style name="hvl-default" family="' + FONT + '" size="' + str(SIZE) + '" description="Gövde" /></styles>\n'
        '</template>'
    )

    with zipfile.ZipFile(udf_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("content.xml", xml.encode("utf-8"))
    return len(doc.paragraphs), len(body)


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    p, c = build(src, dst)
    print("OK %s | %d paragraf, %d karakter, %d bayt" % (os.path.basename(dst), p, c, os.path.getsize(dst)))
