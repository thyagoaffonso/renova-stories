# -*- coding: utf-8 -*-
"""
Motor de render RENOVA DO BRASIL - Assessoria
Stories 9:16 (1080x1920) e Carrossel de feed 4:5 (1080x1350).
Tema proprio da Renova: azul institucional + dourado como unico acento + neutros.
Distinto do motor da banca (que era Georgia serif + dourado sobre preto).
"""
import os
from PIL import Image, ImageDraw, ImageFont

# ----------------------------------------------------------------------------
# PALETA OFICIAL (Plano de Marketing Renova)
# ----------------------------------------------------------------------------
AZUL       = (15, 92, 168)     # #0F5CA8  primaria
AZUL_PROF  = (8, 50, 92)       # #08325C  fundos de destaque / capas
DOURADO    = (192, 138, 60)    # #C08A3C  UNICO acento (regra de ouro)
GRAFITE    = (35, 39, 43)      # #23272B  texto corrido
CINZA      = (110, 114, 118)   # #6E7276  apoio / secundario
NEVOA      = (242, 245, 249)   # #F2F5F9  fundo claro arejado
PRETO_INST = (11, 12, 14)      # #0B0C0E  alto contraste
BRANCO     = (255, 255, 255)

# fundo navy com leve gradiente para dar profundidade (sem poluir)
def _vertical_gradient(size, top, bottom):
    w, h = size
    base = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / max(1, h - 1)
        base.putpixel((0, y), tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return base.resize((w, h))

# ----------------------------------------------------------------------------
# FONTES  (display pesada em caixa alta + corpo sans humanista)
# ----------------------------------------------------------------------------
FDIR = r"C:\Windows\Fonts"
def _f(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)

def black(size):    return _f("seguibl.ttf", size)    # Segoe UI Black (reta) -> display
def bold(size):     return _f("segoeuib.ttf", size)   # Segoe UI Bold
def semibold(size): return _f("seguisb.ttf", size)    # Segoe UI Semibold
def regular(size):  return _f("segoeui.ttf", size)    # Segoe UI Regular -> corpo

# ----------------------------------------------------------------------------
# LOGO  (reaproveita as formas reais; recolore para branco em fundo escuro)
# ----------------------------------------------------------------------------
_ASSETS = r"C:\Users\thyag\OneDrive\Área de Trabalho\ÁREA DE TRABALHO\RENOVA DO BRASIL IMAGENS"
_logo_cache = {}
def logo(color):
    """Retorna o wordmark RENOVA DO BRASIL na cor pedida ('blue' ou 'white'), RGBA transparente."""
    if color in _logo_cache:
        return _logo_cache[color]
    src = Image.open(os.path.join(_ASSETS, "Logo Original.png")).convert("RGBA")
    if color == "blue":
        out = src
    else:
        alpha = src.split()[3]
        fill = BRANCO if color == "white" else color
        out = Image.new("RGBA", src.size, fill + (0,))
        solid = Image.new("RGBA", src.size, fill + (255,))
        out = Image.composite(solid, out, alpha)
    _logo_cache[color] = out
    return out

def paste_logo(img, color, max_w, xy_topright):
    lg = logo(color)
    ratio = max_w / lg.width
    lg = lg.resize((max_w, int(lg.height * ratio)), Image.LANCZOS)
    x = xy_topright[0] - lg.width
    img.paste(lg, (x, xy_topright[1]), lg)
    return lg.height

def cover_photo(path, tw, th, focus_y=0.32):
    """Crop-to-fill preservando proporcao, foco no terco superior (rosto)."""
    im = Image.open(os.path.join(_ASSETS, path)).convert("RGB")
    scale = max(tw / im.width, th / im.height)
    nw, nh = int(im.width * scale), int(im.height * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    x = (nw - tw) // 2
    y = int((nh - th) * focus_y)
    return im.crop((x, y, x + tw, y + th))

def _blend_down(img, panel_top, color, span=220):
    """Gradiente do transparente ao 'color' descendo, para o texto assentar sobre foto."""
    w = img.width
    grad = Image.new("RGBA", (w, span), color + (0,))
    gd = ImageDraw.Draw(grad)
    for i in range(span):
        a = int(255 * (i / span) ** 1.3)
        gd.line([(0, i), (w, i)], fill=color + (a,))
    img.paste(grad, (0, panel_top - span), grad)

# ----------------------------------------------------------------------------
# HELPERS DE TEXTO
# ----------------------------------------------------------------------------
def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def fit_lines(draw, text, font_factory, max_w, max_h, start, minimum=34, leading=1.12):
    """Escolhe o maior tamanho de fonte que faz o texto caber em (max_w, max_h)."""
    size = start
    while size >= minimum:
        font = font_factory(size)
        lines = wrap(draw, text, font, max_w)
        lh = int(size * leading)
        if len(lines) * lh <= max_h:
            return font, lines, lh
        size -= 2
    font = font_factory(minimum)
    return font, wrap(draw, text, font, max_w), int(minimum * leading)

def draw_lines(draw, lines, font, lh, x, y, fill, align_center=False, max_w=0):
    for ln in lines:
        if align_center:
            w = draw.textlength(ln, font=font)
            draw.text((x + (max_w - w) / 2, y), ln, font=font, fill=fill)
        else:
            draw.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def kicker(draw, text, x, y, color=DOURADO, size=30):
    """Filete curto dourado + rotulo em caixa alta espacado."""
    draw.line([(x, y + size // 2), (x + 64, y + size // 2)], fill=color, width=4)
    f = bold(size)
    draw.text((x + 82, y - 4), text.upper(), font=f, fill=color,
              features=None)

def cta_pill(img, draw, text, cx, y, w=760, h=118):
    x0 = cx - w // 2
    draw.rounded_rectangle([x0, y, x0 + w, y + h], radius=h // 2, fill=DOURADO)
    # grupo [icone + texto] centralizado no pill
    f = bold(int(h * 0.37))
    r = int(h * 0.22)
    gap = 22
    tw = draw.textlength(text, font=f)
    group_w = r * 2 + gap + tw
    gx = cx - group_w / 2
    icx, icy = gx + r, y + h / 2
    # bolha whatsapp em navy: circulo cheio + cauda
    draw.ellipse([icx - r, icy - r, icx + r, icy + r], fill=AZUL_PROF)
    draw.polygon([(icx - r * 0.55, icy + r * 0.35), (icx - r * 0.95, icy + r * 0.95),
                  (icx - r * 0.15, icy + r * 0.7)], fill=AZUL_PROF)
    # fone dentro da bolha
    draw.arc([icx - r * 0.5, icy - r * 0.5, icx + r * 0.5, icy + r * 0.5], 200, 70,
             fill=DOURADO, width=max(4, r // 6))
    ty = y + (h - (f.getbbox(text)[3] - f.getbbox(text)[1])) / 2 - f.getbbox(text)[1]
    draw.text((gx + r * 2 + gap, ty), text, font=f, fill=AZUL_PROF)

# ----------------------------------------------------------------------------
# STORIES  1080x1920
# ----------------------------------------------------------------------------
SW, SH = 1080, 1920
MARGIN = 96

def story_bg(kind):
    if kind == "navy":
        return _vertical_gradient((SW, SH), (11, 60, 108), AZUL_PROF).convert("RGB")
    return Image.new("RGB", (SW, SH), NEVOA)

def _story_dots(d, total, idx, navy):
    if total > 1:
        gap, r = 26, 7
        for i in range(total):
            col = DOURADO if i == idx else (BRANCO if navy else (200,205,212))
            d.ellipse([MARGIN + i*gap - r, 150 - r, MARGIN + i*gap + r, 150 + r], fill=col)

def _story_photo(role, data, idx, total):
    """Layout com foto: imagem no topo + painel navy embaixo (institucional / prova social)."""
    is_cta = role == "cta"
    img = Image.new("RGB", (SW, SH), AZUL_PROF)
    panel_top = 1000 if is_cta else 1120
    photo = cover_photo(data["photo"], SW, panel_top, data.get("focus", 0.30))
    img.paste(photo, (0, 0))
    d = ImageDraw.Draw(img, "RGBA")
    _blend_down(img, panel_top, AZUL_PROF, span=260)
    d.rectangle([0, panel_top, SW, SH], fill=AZUL_PROF)
    d = ImageDraw.Draw(img)
    paste_logo(img, "white", 280, (SW - MARGIN, 92))
    _story_dots(d, total, idx, True)
    kicker(d, data.get("kicker", "RENOVA DO BRASIL"), MARGIN, panel_top + 66)
    title_h = 300 if is_cta else 380
    font, lines, lh = fit_lines(d, data["title"], black, SW-2*MARGIN, title_h, 72, minimum=48)
    y = draw_lines(d, lines, font, lh, MARGIN, panel_top + 146, BRANCO)
    if is_cta:
        cta_pill(img, d, data.get("cta", "Chamar no WhatsApp"), SW//2, SH - 230, w=740, h=112)
    elif data.get("sub"):
        fs, sl, slh = fit_lines(d, data["sub"], semibold, SW-2*MARGIN, 160, 46, minimum=34, leading=1.2)
        draw_lines(d, sl, fs, slh, MARGIN, y + 24, DOURADO)
    return img

def story_frame(role, data, idx, total):
    """role: 'gancho' | 'ponto' | 'cta' | 'interacao'"""
    if data.get("photo"):
        return _story_photo(role, data, idx, total)
    navy = role in ("gancho", "cta", "interacao")
    img = story_bg("navy" if navy else "nevoa")
    d = ImageDraw.Draw(img)
    logo_color = "white" if navy else "blue"
    paste_logo(img, logo_color, 300, (SW - MARGIN, 92))
    _story_dots(d, total, idx, navy)

    if role == "interacao":
        kicker(d, data.get("kicker", "RESPONDA"), MARGIN, 250)
        font, lines, lh = fit_lines(d, data["title"], black, SW-2*MARGIN, 560, 88, minimum=52)
        y = draw_lines(d, lines, font, lh, MARGIN, 440, BRANCO)
        y += 60
        for opt in data.get("options", [])[:4]:
            h = 118
            d.rounded_rectangle([MARGIN, y, SW-MARGIN, y+h], radius=20, outline=DOURADO, width=4)
            fo = semibold(46)
            d.text((MARGIN+44, y+(h-58)/2), opt, font=fo, fill=BRANCO)
            y += h + 26
        note = data.get("note", "responda aqui nos comentarios ou no direct")
        fn = semibold(38); nw = d.textlength(note, font=fn)
        d.text(((SW-nw)/2, SH-220), note, font=fn, fill=(210,220,232))
        return img
    if role == "gancho":
        kicker(d, data.get("kicker", "SÍNDICO, UMA PERGUNTA"), MARGIN, 250)
        font, lines, lh = fit_lines(d, data["title"], black, SW - 2*MARGIN, 900, 108, minimum=64)
        y = 470
        draw_lines(d, lines, font, lh, MARGIN, y, BRANCO)
        if data.get("sub"):
            fs, sl, slh = fit_lines(d, data["sub"], semibold, SW-2*MARGIN, 300, 52, minimum=38)
            draw_lines(d, sl, fs, slh, MARGIN, y + len(lines)*lh + 40, DOURADO)
        d.text((MARGIN, SH - 150), "arraste  ›", font=bold(38), fill=(255,255,255,160))
    elif role == "ponto":
        # numero grande dourado
        num = data.get("num")
        top = 250
        if num:
            d.text((MARGIN, top), str(num), font=black(150), fill=DOURADO)
            top += 190
        font, lines, lh = fit_lines(d, data["title"], black, SW - 2*MARGIN, 460, 92, minimum=54)
        y = draw_lines(d, lines, font, lh, MARGIN, top, AZUL)
        if data.get("body"):
            fb, bl, blh = fit_lines(d, data["body"], regular, SW-2*MARGIN, 560, 50, minimum=34, leading=1.28)
            draw_lines(d, bl, fb, blh, MARGIN, y + 40, GRAFITE)
    elif role == "cta":
        kicker(d, data.get("kicker", "RENOVA DO BRASIL"), MARGIN, 300)
        font, lines, lh = fit_lines(d, data["title"], black, SW - 2*MARGIN, 620, 96, minimum=56)
        y = draw_lines(d, lines, font, lh, MARGIN, 500, BRANCO)
        if data.get("sub"):
            fs, sl, slh = fit_lines(d, data["sub"], semibold, SW-2*MARGIN, 260, 48, minimum=34, leading=1.25)
            y = draw_lines(d, sl, fs, slh, MARGIN, y + 30, DOURADO)
        cta_pill(img, d, data.get("cta", "Chamar no WhatsApp"), SW//2, SH - 470)
        note = data.get("note", "diagnóstico gratuito da sua gestão")
        fn = semibold(40)
        nw = d.textlength(note, font=fn)
        d.text(((SW - nw) / 2, SH - 300), note, font=fn, fill=(210, 220, 232))
    return img

def render_story(outdir, day_key, frames):
    paths = []
    for i, fr in enumerate(frames):
        img = story_frame(fr["role"], fr, i, len(frames))
        p = os.path.join(outdir, f"{day_key}_story_{i+1}.png")
        img.save(p, "PNG")
        paths.append(p)
    return paths

# ----------------------------------------------------------------------------
# CARROSSEL  1080x1350
# ----------------------------------------------------------------------------
CW, CH = 1080, 1350
CM = 88

def _carousel_photo(role, data, idx, total):
    img = Image.new("RGB", (CW, CH), AZUL_PROF)
    panel_top = 720
    photo = cover_photo(data["photo"], CW, panel_top, data.get("focus", 0.28))
    img.paste(photo, (0, 0))
    ImageDraw.Draw(img, "RGBA")
    _blend_down(img, panel_top, AZUL_PROF, span=220)
    d = ImageDraw.Draw(img)
    d.rectangle([0, panel_top, CW, CH], fill=AZUL_PROF)
    paste_logo(img, "white", 230, (CW - CM, 70))
    kicker(d, data.get("kicker", "RENOVA DO BRASIL"), CM, panel_top + 54, size=28)
    font, lines, lh = fit_lines(d, data["title"], black, CW-2*CM, 300, 66, minimum=42)
    y = draw_lines(d, lines, font, lh, CM, panel_top + 120, BRANCO)
    if data.get("sub"):
        fs, sl, slh = fit_lines(d, data["sub"], semibold, CW-2*CM, 120, 40, minimum=30, leading=1.2)
        y = draw_lines(d, sl, fs, slh, CM, y + 18, DOURADO)
    if role == "fecho":
        cta_pill(img, d, data.get("cta", "Chamar no WhatsApp"), CW//2, CH - 150, w=640, h=100)
    return img

def carousel_slide(role, data, idx, total):
    if data.get("photo"):
        return _carousel_photo(role, data, idx, total)
    navy = role in ("capa", "fecho")
    if navy:
        img = _vertical_gradient((CW, CH), (11, 60, 108), AZUL_PROF).convert("RGB")
    else:
        img = Image.new("RGB", (CW, CH), NEVOA)
    d = ImageDraw.Draw(img)
    paste_logo(img, "white" if navy else "blue", 250, (CW - CM, 78))

    if role == "capa":
        kicker(d, data.get("kicker", "PARA SÍNDICOS"), CM, 300, size=30)
        font, lines, lh = fit_lines(d, data["title"], black, CW - 2*CM, 620, 104, minimum=60)
        y = draw_lines(d, lines, font, lh, CM, 470, BRANCO)
        # filete dourado
        d.line([(CM, y + 24), (CM + 150, y + 24)], fill=DOURADO, width=6)
        if data.get("sub"):
            fs, sl, slh = fit_lines(d, data["sub"], semibold, CW-2*CM, 220, 46, minimum=32, leading=1.25)
            draw_lines(d, sl, fs, slh, CM, y + 60, DOURADO)
        d.text((CW - CM - 210, CH - 120), "arraste  ›", font=bold(36), fill=(255,255,255,170))
    elif role == "slide":
        num = data.get("num")
        top = 300
        if num is not None:
            d.text((CM, top), str(num), font=black(130), fill=DOURADO)
            top += 165
        font, lines, lh = fit_lines(d, data["title"], black, CW - 2*CM, 360, 78, minimum=46)
        y = draw_lines(d, lines, font, lh, CM, top, AZUL)
        if data.get("body"):
            fb, bl, blh = fit_lines(d, data["body"], regular, CW-2*CM, 380, 46, minimum=32, leading=1.3)
            draw_lines(d, bl, fb, blh, CM, y + 34, GRAFITE)
    elif role == "fecho":
        kicker(d, data.get("kicker", "RENOVA DO BRASIL"), CM, 300, size=30)
        font, lines, lh = fit_lines(d, data["title"], black, CW - 2*CM, 480, 84, minimum=48)
        y = draw_lines(d, lines, font, lh, CM, 460, BRANCO)
        if data.get("sub"):
            fs, sl, slh = fit_lines(d, data["sub"], semibold, CW-2*CM, 200, 44, minimum=30, leading=1.25)
            y = draw_lines(d, sl, fs, slh, CM, y + 26, DOURADO)
        cta_pill(img, d, data.get("cta", "Chamar no WhatsApp"), CW//2, CH - 330, w=680, h=104)
    return img

def render_carousel(outdir, car_key, slides):
    paths = []
    for i, sl in enumerate(slides):
        img = carousel_slide(sl["role"], sl, i, len(slides))
        p = os.path.join(outdir, f"{car_key}_slide_{i+1}.png")
        img.save(p, "PNG")
        paths.append(p)
    return paths


if __name__ == "__main__":
    OUT = os.path.join(os.path.dirname(__file__), "test_out")
    os.makedirs(OUT, exist_ok=True)
    # STORY de teste (pilar Dor do sindico) - gancho + 2 pontos + CTA
    story = [
        {"role":"gancho","kicker":"SÍNDICO, UMA PERGUNTA",
         "title":"Ser síndico virou um segundo emprego que ninguém te ensinou a fazer.",
         "sub":"E a responsabilidade toda no seu nome."},
        {"role":"ponto","num":1,"title":"Assembleia que vira briga",
         "body":"Reunião tensa, decisão sem registro e o desgaste sobrando para você no dia seguinte."},
        {"role":"ponto","num":2,"title":"Inadimplência que não para",
         "body":"Cobrança sem método, caixa apertado e prestação de contas que tira o seu sono."},
        {"role":"cta","kicker":"RENOVA DO BRASIL",
         "title":"O problema não é você. É a falta de estrutura.",
         "sub":"A Renova assume a gestão do lado do síndico.",
         "cta":"Chamar no WhatsApp"},
    ]
    render_story(OUT, "teste", story)
    # CARROSSEL de teste (Educacao) capa + 3 slides + fecho
    car = [
        {"role":"capa","kicker":"PARA SÍNDICOS",
         "title":"5 sinais de que seu condomínio está no improviso",
         "sub":"Marque quantos você reconhece."},
        {"role":"slide","num":1,"title":"Ninguém acha o documento quando precisa",
         "body":"Contrato, ata, convenção. Tudo espalhado, nada organizado num lugar só."},
        {"role":"slide","num":2,"title":"Decisão importante fica só na conversa",
         "body":"Sem registro, sem ata, sem respaldo. Quando dá problema, a palavra é do morador contra a sua."},
        {"role":"slide","num":3,"title":"A inadimplência cresce e ninguém cobra com método",
         "body":"Sem régua de cobrança, o caixa aperta e o rateio pesa em quem paga em dia."},
        {"role":"fecho","kicker":"RENOVA DO BRASIL",
         "title":"Marcou dois ou mais? A gente organiza isso com você.",
         "sub":"Peça o diagnóstico gratuito da sua gestão.",
         "cta":"Chamar no WhatsApp"},
    ]
    render_carousel(OUT, "teste_carrossel", car)
    print("OK ->", OUT)
