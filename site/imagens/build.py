import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

OUT = '/tmp/claude-0/-home-user-Romario-/a5b06475-c298-584f-9b3c-adb8e08c4dcb/scratchpad/redebolha-imagens'
for d in ['01_hero', '02_mockups', '03_provas', '07_social', '09_capas-frente']:
    os.makedirs(f'{OUT}/{d}', exist_ok=True)

def save_jpg(im, path, q=84):
    im.convert('RGB').save(path, 'JPEG', quality=q, optimize=True, progressive=True)
    im.convert('RGB').save(path.rsplit('.', 1)[0] + '.webp', 'WEBP', quality=80, method=6)

def save_png(im, path):
    im.save(path, 'PNG', optimize=True)
    im.save(path.rsplit('.', 1)[0] + '.webp', 'WEBP', quality=88, method=6, lossless=False)

# ---------------------------------------------------------------- 09 capas
# Corrige o defeito encontrado: a home mostra a capa COMPLETA (verso+lombada+
# frente) nos cartoes da estante. Aqui saem as frentes limpas.
for k, nome in [('homem', 'homem-voce-nao-e-ridiculo'),
                ('amanha', 'amanha-e-outro-agora'),
                ('poder', 'o-poder-da-decisao')]:
    front, spine = load_parts(k)
    front.save(f'{OUT}/09_capas-frente/{nome}-frente.jpg', 'JPEG', quality=90, optimize=True)
    front.save(f'{OUT}/09_capas-frente/{nome}-frente.webp', 'WEBP', quality=86, method=6)

# ---------------------------------------------------------------- 01 hero
hero_d = atmosphere((2400, 1400), glow_center=(0.30, 0.24), glow_r=1.00,
                    glow_strength=0.62, vignette=0.92, grain=6.5, seed=21)
save_jpg(hero_d, f'{OUT}/01_hero/hero-fundo-desktop.jpg', 82)

hero_m = atmosphere((1200, 1600), glow_center=(0.50, 0.18), glow_r=1.05,
                    glow_strength=0.60, vignette=0.90, grain=6.5, seed=22)
save_jpg(hero_m, f'{OUT}/01_hero/hero-fundo-mobile.jpg', 82)

save_png(gold_haze((1600, 1600), seed=9), f'{OUT}/01_hero/hero-textura-ouro.png')

# ---------------------------------------------------------------- 02 mockups
BIG = (2600, 2600)   # tela de trabalho; cada peca sai recortada no conteudo

def render_book(key, h, tilt=0.042):
    return tight(book_3d(key, h, BIG, (1300, 1300), tilt=tilt), pad=0.02)

def fit(im, canvas, occupy=0.86):
    """Encaixa im centrado em canvas ocupando `occupy` do menor eixo util."""
    W, H = canvas
    sc = min(W * occupy / im.width, H * occupy / im.height)
    im2 = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.LANCZOS)
    return place(canvas, [(im2, W / 2, H / 2)])

# 1. livro fisico em 3D
save_png(fit(render_book('homem', 1700), (1600, 1600), 0.88),
         f'{OUT}/02_mockups/mockup-livro-fisico-3d.png')

# 2. combo: livro fisico + tablet com o e-book ao lado
cs = (2000, 1400)
livro = render_book('homem', 1180)
tabl = tight(screen_device('homem', 780, 1060, BIG, (1300, 1300), radius=38, bezel=20), 0.02)
gap = int(livro.width * 0.10)
total = livro.width + gap + tabl.width
sc = min(1.0, cs[0] * 0.90 / total, cs[1] * 0.88 / max(livro.height, tabl.height))
livro = livro.resize((int(livro.width * sc), int(livro.height * sc)), Image.LANCZOS)
tabl = tabl.resize((int(tabl.width * sc), int(tabl.height * sc)), Image.LANCZOS)
gap = int(gap * sc)
total = livro.width + gap + tabl.width
x0 = (cs[0] - total) / 2
base = cs[1] * 0.94
save_png(place(cs, [
    (tabl,  x0 + livro.width + gap + tabl.width / 2,  base - tabl.height / 2),
    (livro, x0 + livro.width / 2,                     base - livro.height / 2),
]), f'{OUT}/02_mockups/mockup-combo-fisico-ebook.png')

# 3. e-book no celular
cel = tight(screen_device('homem', 620, 1240, BIG, (1300, 1300), radius=68, bezel=15,
                          mode='contain'), 0.02)
save_png(fit(cel, (1200, 1600), 0.88), f'{OUT}/02_mockups/mockup-ebook-celular.png')

# 4. os tres livros: o principal na frente e ao centro
cs = (2000, 1200)
esq = render_book('amanha', 880, 0.048)
dir_ = render_book('poder', 880, 0.048)
cen = render_book('homem', 1060, 0.040)
sc = min(1.0, cs[1] * 0.90 / cen.height)
esq, dir_, cen = [i.resize((int(i.width * sc), int(i.height * sc)), Image.LANCZOS)
                  for i in (esq, dir_, cen)]
base = cs[1] * 0.93
ov = int(cen.width * 0.30)      # sobreposicao dos laterais sob o central
save_png(place(cs, [
    (esq,  cs[0] / 2 - cen.width / 2 - esq.width / 2 + ov,  base - esq.height / 2),
    (dir_, cs[0] / 2 + cen.width / 2 + dir_.width / 2 - ov, base - dir_.height / 2),
    (cen,  cs[0] / 2,                                       base - cen.height / 2),
]), f'{OUT}/02_mockups/mockup-tres-ebooks.png')

# ---------------------------------------------------------------- 03 provas
faixa = atmosphere((2400, 800), glow_center=(0.5, 0.55), glow_r=0.75,
                   glow_strength=0.40, vignette=0.86, grain=6.0, seed=31)
d = ImageDraw.Draw(faixa)
for i in range(3):
    a = 90 - i * 28
    d.line([(0, 400 + i), (2400, 400 + i)], fill=(GOLD[0], GOLD[1], GOLD[2]))
faixa = faixa.filter(ImageFilter.GaussianBlur(0.4))
save_jpg(faixa, f'{OUT}/03_provas/fundo-dados-faixa.jpg', 82)

# ---------------------------------------------------------------- 07 social
og = atmosphere((1200, 630), glow_center=(0.24, 0.44), glow_r=0.95,
                glow_strength=0.54, vignette=0.88, grain=6.0, seed=41).convert('RGBA')
_b = tight(book_3d('homem', 900, (2600, 2600), (1300, 1300), tilt=0.042), 0.02)
_s = 520 / _b.height
_b = _b.resize((int(_b.width * _s), 520), Image.LANCZOS)
og = Image.alpha_composite(og, place((1200, 630), [(_b, 310, 318)]))
save_jpg(og.convert('RGB'), f'{OUT}/07_social/og-livro.jpg', 85)

ogp = atmosphere((1200, 630), glow_center=(0.5, 0.42), glow_r=0.95,
                 glow_strength=0.48, vignette=0.88, grain=6.0, seed=42)
save_jpg(ogp, f'{OUT}/07_social/og-padrao.jpg', 85)

print('gerado')
for root, _, files in os.walk(OUT):
    for f in sorted(files):
        p = os.path.join(root, f)
        print(f'{os.path.getsize(p)//1024:>5} KB  {p[len(OUT)+1:]}')
