"""Ferramentas de composicao para a colecao de imagens da Rede Bolha."""
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import numpy as np

SRC = '/home/user/redebolha/redebolha/'

# paleta do site (css/base.css)
BG     = (10, 10, 12)
BG2    = (18, 16, 19)
CARD   = (26, 23, 27)
GOLD   = (201, 162, 75)
GOLD_L = (231, 206, 138)
GOLD_D = (154, 122, 48)
WINE   = (107, 39, 55)
TXT    = (241, 236, 227)

# Recortes medidos nos arquivos originais (todos sao capas completas: verso+lombada+frente)
LIVROS = {
    'homem': dict(wrap='homem-voce-nao-e-ridiculo-ebook-capa.jpg', front=381, spine=(345, 400)),
    'amanha': dict(wrap='amanha-outro-agora.jpg',                  front=790, spine=(716, 786)),
    'poder': dict(wrap='poder-da-decisao.jpg',                     front=529, spine=(500, 528)),
}


def load_parts(key):
    """Devolve (frente, lombada) recortadas da capa completa."""
    d = LIVROS[key]
    im = Image.open(SRC + d['wrap']).convert('RGB')
    W, H = im.size
    top = 2 if key == 'poder' else 0          # linha clara no topo do arquivo original
    front = im.crop((d['front'], top, W, H))
    spine = im.crop((d['spine'][0], top, d['spine'][1], H))
    return front, spine


def find_coeffs(dst, src):
    """Coeficientes para Image.transform PERSPECTIVE (mapeia saida -> entrada)."""
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    A = np.matrix(m, dtype=float)
    B = np.array(src, dtype=float).reshape(8)
    return np.array(np.dot(np.linalg.inv(A.T * A) * A.T, B)).reshape(8)


def warp(img, quad, canvas_size):
    """Projeta img no quadrilatero quad (TL,TR,BR,BL) dentro de canvas_size."""
    img = img.convert('RGBA')
    coeffs = find_coeffs(quad, [(0, 0), (img.width, 0), (img.width, img.height), (0, img.height)])
    return img.transform(canvas_size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)


def shade(layer, quad, canvas_size, top_rgba, bottom_rgba):
    """Gradiente linear (esquerda->direita) aplicado dentro do quadrilatero."""
    g = Image.new('RGBA', (256, 256))
    d = ImageDraw.Draw(g)
    for x in range(256):
        t = x / 255
        d.line([(x, 0), (x, 256)], fill=tuple(
            int(top_rgba[i] + (bottom_rgba[i] - top_rgba[i]) * t) for i in range(4)))
    return Image.alpha_composite(layer, warp(g, quad, canvas_size))


def drop_shadow(canvas_size, quad, blur=42, spread=1.0, opacity=150, offset=(0, 0)):
    sh = Image.new('RGBA', canvas_size, (0, 0, 0, 0))
    d = ImageDraw.Draw(sh)
    cx = sum(p[0] for p in quad) / 4
    cy = sum(p[1] for p in quad) / 4
    pts = [(cx + (x - cx) * spread + offset[0], cy + (y - cy) * spread + offset[1]) for x, y in quad]
    d.polygon(pts, fill=(0, 0, 0, opacity))
    return sh.filter(ImageFilter.GaussianBlur(blur))


def floor_shadow(canvas_size, cx, cy, rx, ry, opacity=170, blur=48):
    sh = Image.new('RGBA', canvas_size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(0, 0, 0, opacity))
    return sh.filter(ImageFilter.GaussianBlur(blur))


def book_3d(key, height_px, canvas_size, center, tilt=0.040, spine_w=None, shadow=True):
    """Livro de pe, girado, mostrando frente e lombada a esquerda.

    tilt = quanto a aresta direita 'recua' (fracao da altura).
    """
    front, spine = load_parts(key)
    ratio = front.width / front.height
    fw = height_px * ratio
    sw = spine_w if spine_w else max(28, height_px * (spine.width / spine.height) * 1.35)

    cx, cy = center
    hinge_x = cx - fw * 0.18
    inset = height_px * tilt

    q_front = [(hinge_x, cy - height_px / 2),
               (hinge_x + fw, cy - height_px / 2 + inset),
               (hinge_x + fw, cy + height_px / 2 - inset),
               (hinge_x, cy + height_px / 2)]
    q_spine = [(hinge_x - sw, cy - height_px / 2 + inset * 0.65),
               (hinge_x, cy - height_px / 2),
               (hinge_x, cy + height_px / 2),
               (hinge_x - sw, cy + height_px / 2 - inset * 0.65)]

    layer = Image.new('RGBA', canvas_size, (0, 0, 0, 0))

    if shadow:
        layer = Image.alpha_composite(layer, drop_shadow(
            canvas_size, q_front, blur=46, spread=1.03, opacity=120, offset=(26, 30)))
        layer = Image.alpha_composite(layer, floor_shadow(
            canvas_size, cx, cy + height_px / 2 + 16, fw * 0.62, height_px * 0.035, 150, 34))

    # miolo (folhas) na aresta direita, recuando
    pe_w = max(6, sw * 0.30)
    q_pages = [(hinge_x + fw, cy - height_px / 2 + inset),
               (hinge_x + fw + pe_w, cy - height_px / 2 + inset * 1.9),
               (hinge_x + fw + pe_w, cy + height_px / 2 - inset * 1.9),
               (hinge_x + fw, cy + height_px / 2 - inset)]
    pages = Image.new('RGBA', (40, 400), (0, 0, 0, 0))
    dp = ImageDraw.Draw(pages)
    for x in range(40):
        t = x / 39
        v = int(206 - 104 * t)
        dp.line([(x, 0), (x, 400)], fill=(v, v - 8, int(v * 0.92), 255))
    layer = Image.alpha_composite(layer, warp(pages, q_pages, canvas_size))

    # lombada e frente
    layer = Image.alpha_composite(layer, warp(spine, q_spine, canvas_size))
    layer = shade(layer, q_spine, canvas_size, (0, 0, 0, 130), (0, 0, 0, 20))
    layer = Image.alpha_composite(layer, warp(front, q_front, canvas_size))
    # luz vindo da esquerda alta: frente escurece suavemente para a direita
    layer = shade(layer, q_front, canvas_size, (255, 240, 210, 26), (0, 0, 0, 70))
    return layer


def screen_device(key, w, h, canvas_size, center, radius=48, bezel=16, frame=(38, 36, 40),
                  mode='cover'):
    """Tablet/celular de frente com a capa na tela."""
    front, _ = load_parts(key)
    cx, cy = center
    w, h = int(w), int(h)
    dev = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(dev).rounded_rectangle([0, 0, w - 1, h - 1], radius, fill=frame + (255,))

    iw, ih = w - bezel * 2, h - bezel * 2
    # a capa preenche a tela sem distorcer: corta o excedente
    fr = front.convert('RGBA')
    if mode == 'cover':
        scale = max(iw / fr.width, ih / fr.height)
        fr = fr.resize((max(1, int(fr.width * scale)), max(1, int(fr.height * scale))), Image.LANCZOS)
        fr = fr.crop(((fr.width - iw) // 2, (fr.height - ih) // 2,
                      (fr.width - iw) // 2 + iw, (fr.height - ih) // 2 + ih))
    else:
        # 'contain': a capa inteira aparece, centrada sobre a tela escura
        scale = min(iw / fr.width, ih / fr.height) * 0.94
        cw, ch = max(1, int(fr.width * scale)), max(1, int(fr.height * scale))
        page = Image.new('RGBA', (iw, ih), (13, 12, 15, 255))
        page.paste(fr.resize((cw, ch), Image.LANCZOS), ((iw - cw) // 2, (ih - ch) // 2))
        fr = page

    # reflexo diagonal COMPOSTO sobre a capa (antes era colado por cima, com
    # alpha zero, e apagava a tela)
    gl = Image.new('RGBA', (iw, ih), (0, 0, 0, 0))
    ImageDraw.Draw(gl).polygon([(0, 0), (iw * 0.58, 0), (0, ih * 0.74)],
                               fill=(255, 255, 255, 24))
    fr = Image.alpha_composite(fr, gl.filter(ImageFilter.GaussianBlur(2)))

    mask = Image.new('L', (iw, ih), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, iw - 1, ih - 1],
                                           max(4, radius - bezel), fill=255)
    dev.paste(fr, (bezel, bezel), mask)
    ImageDraw.Draw(dev).rounded_rectangle([0, 0, w - 1, h - 1], radius,
                                          outline=(96, 92, 100, 255), width=2)

    layer = Image.new('RGBA', canvas_size, (0, 0, 0, 0))
    q = [(cx - w / 2, cy - h / 2), (cx + w / 2, cy - h / 2),
         (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)]
    layer = Image.alpha_composite(layer, drop_shadow(canvas_size, q, 40, 1.02, 130, (18, 26)))
    layer.paste(dev, (int(cx - w / 2), int(cy - h / 2)), dev)
    return layer


def tight(layer, pad=0.03):
    """Recorta a camada no conteudo, com uma folga proporcional."""
    bb = layer.getbbox()
    if not bb:
        return layer
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    m = int(max(w, h) * pad)
    box = (max(0, bb[0] - m), max(0, bb[1] - m),
           min(layer.width, bb[2] + m), min(layer.height, bb[3] + m))
    return layer.crop(box)


def place(canvas_size, items):
    """items: lista de (imagem RGBA, centro_x, centro_y), desenhadas na ordem."""
    out = Image.new('RGBA', canvas_size, (0, 0, 0, 0))
    for im, cx, cy in items:
        tmp = Image.new('RGBA', canvas_size, (0, 0, 0, 0))
        tmp.paste(im, (int(cx - im.width / 2), int(cy - im.height / 2)), im)
        out = Image.alpha_composite(out, tmp)
    return out


def atmosphere(size, glow_center=(0.5, 0.35), glow_r=0.85, glow_strength=0.60,
               base=BG, base2=BG2, vignette=0.85, grain=7.0, seed=7):
    """Fundo escuro com halo dourado, vinheta e grao de filme."""
    W, H = size
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    xn, yn = xx / W, yy / H

    img = np.zeros((H, W, 3), np.float32)
    for c in range(3):
        img[..., c] = base[c] + (base2[c] - base[c]) * yn

    gx, gy = glow_center
    d = np.sqrt(((xn - gx) * (W / max(W, H))) ** 2 + ((yn - gy) * (H / max(W, H))) ** 2)
    g = np.clip(1 - d / glow_r, 0, 1) ** 3.6 * glow_strength
    for c in range(3):
        img[..., c] += g * GOLD[c] * 0.78

    d2 = np.sqrt((xn - 0.5) ** 2 + (yn - 0.5) ** 2) / 0.72
    img *= (1 - np.clip(d2, 0, 1) ** 2.1 * vignette)[..., None]

    img += rng.normal(0, grain, (H, W, 1))
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), 'RGB')


def gold_haze(size, seed=3):
    """PNG transparente: nevoa dourada com particulas de poeira."""
    W, H = size
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt(((xx / W - 0.5)) ** 2 + ((yy / H - 0.5)) ** 2) / 0.5
    a = np.clip(1 - d, 0, 1) ** 3.0 * 120
    rgb = np.zeros((H, W, 3), np.float32)
    for c in range(3):
        rgb[..., c] = GOLD_L[c]
    out = Image.fromarray(np.dstack([rgb, a]).astype(np.uint8), 'RGBA')
    dust = Image.new('RGBA', size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(dust)
    for _ in range(520):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        r = rng.uniform(0.8, 3.2)
        dr = np.sqrt(((x / W - .5)) ** 2 + ((y / H - .5)) ** 2) / .5
        al = int(np.clip(1 - dr, 0, 1) ** 1.6 * rng.uniform(60, 210))
        dd.ellipse([x - r, y - r, x + r, y + r], fill=GOLD_L + (al,))
    dust = dust.filter(ImageFilter.GaussianBlur(0.7))
    return Image.alpha_composite(out.filter(ImageFilter.GaussianBlur(W * 0.02)), dust)


def add_grain(img, amount=6.0, seed=11):
    a = np.asarray(img).astype(np.float32)
    rng = np.random.default_rng(seed)
    a += rng.normal(0, amount, a.shape[:2] + (1,))
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), img.mode)
