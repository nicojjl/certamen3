#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Pipeline de Generación, Optimización y Control de Calidad de Figuras TikZ -> SVG -> PNG
Renderiza a PNG en fondo claro y oscuro en img/_preview/, detecta recorte y actualiza img/galeria.html.
"""

import os
import re
import sys
import subprocess
import shutil
import pymupdf
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_DIR = os.path.join(BASE_DIR, 'scripts', 'figuras_tex')
IMG_DIR = os.path.join(BASE_DIR, 'img')
PREVIEW_DIR = os.path.join(IMG_DIR, '_preview')
GALERIA_PATH = os.path.join(IMG_DIR, 'galeria.html')

os.makedirs(TEX_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)

STYLE_HEADER = """<style>
  :root {
    color: #1f2937;
    fill: currentColor;
    --fig-azul: #0284c7;
    --fig-rojo: #dc2626;
    --fig-verde: #16a34a;
    --fig-morado: #7c3aed;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      color: #f8fafc;
      fill: currentColor;
      --fig-azul: #38bdf8;
      --fig-rojo: #f87171;
      --fig-verde: #4ade80;
      --fig-morado: #c084fc;
    }
  }
  [data-theme="dark"] svg, .dark-mode svg {
    color: #f8fafc;
    fill: currentColor;
    --fig-azul: #38bdf8;
    --fig-rojo: #f87171;
    --fig-verde: #4ade80;
    --fig-morado: #c084fc;
  }
</style>"""

def compile_tikz(tex_name):
    base_name = os.path.splitext(tex_name)[0]
    tex_path = os.path.join(TEX_DIR, f"{base_name}.tex")
    dvi_path = os.path.join(TEX_DIR, f"{base_name}.dvi")
    raw_svg_path = os.path.join(TEX_DIR, f"{base_name}_raw.svg")
    dest_svg_path = os.path.join(IMG_DIR, f"{base_name}.svg")

    if not os.path.exists(tex_path):
        print(f"[ERROR] No existe {tex_path}")
        return False

    # 1. latex -> dvi
    cmd_latex = ["latex", "-interaction=nonstopmode", f"{base_name}.tex"]
    res = subprocess.run(cmd_latex, cwd=TEX_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"[FAIL LaTeX] {base_name}:")
        log_file = os.path.join(TEX_DIR, f"{base_name}.log")
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="latin1") as f:
                errors = [line for line in f if line.startswith("!")]
                print("   " + "\n   ".join(errors[:5]))
        return False

    # 2. dvisvgm -> svg (con optimizaciones -O -d2 -R)
    cmd_dvisvgm = ["dvisvgm", "--no-fonts", "-O", "-d2", "-R", "-o", raw_svg_path, dvi_path]
    res_svg = subprocess.run(cmd_dvisvgm, cwd=TEX_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res_svg.returncode != 0 or not os.path.exists(raw_svg_path):
        print(f"[FAIL dvisvgm] {base_name}: {res_svg.stderr}")
        return False

    # 3. Post-process SVG
    with open(raw_svg_path, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Reemplazo de colores para adaptabilidad CSS clara/oscura
    svg = re.sub(r'stroke=[\'\"]#000(?:000)?[\'\"]', 'stroke="currentColor"', svg)
    svg = re.sub(r'fill=[\'\"]#000(?:000)?[\'\"]', 'fill="currentColor"', svg)
    svg = re.sub(r'stroke=[\'\"](?:#0284c7|#0077cc|#0000ff|#1976d2)[\'\"]', 'stroke="var(--fig-azul, #0284c7)"', svg, flags=re.I)
    svg = re.sub(r'fill=[\'\"](?:#0284c7|#0077cc|#0000ff|#1976d2)[\'\"]', 'fill="var(--fig-azul, #0284c7)"', svg, flags=re.I)
    svg = re.sub(r'stroke=[\'\"](?:#dc2626|#cc0000|#ff0000|#d32f2f)[\'\"]', 'stroke="var(--fig-rojo, #dc2626)"', svg, flags=re.I)
    svg = re.sub(r'fill=[\'\"](?:#dc2626|#cc0000|#ff0000|#d32f2f)[\'\"]', 'fill="var(--fig-rojo, #dc2626)"', svg, flags=re.I)
    svg = re.sub(r'stroke=[\'\"](?:#16a34a|#009900|#388e3c)[\'\"]', 'stroke="var(--fig-verde, #16a34a)"', svg, flags=re.I)
    svg = re.sub(r'fill=[\'\"](?:#16a34a|#009900|#388e3c)[\'\"]', 'fill="var(--fig-verde, #16a34a)"', svg, flags=re.I)
    svg = re.sub(r'stroke=[\'\"](?:#7c3aed|#8b5cf6|#6d28d9)[\'\"]', 'stroke="var(--fig-morado, #7c3aed)"', svg, flags=re.I)
    svg = re.sub(r'fill=[\'\"](?:#7c3aed|#8b5cf6|#6d28d9)[\'\"]', 'fill="var(--fig-morado, #7c3aed)"', svg, flags=re.I)

    # Inyección de fill currentColor en la etiqueta raíz
    svg = re.sub(r'<svg\s+', '<svg fill="currentColor" ', svg, count=1)
    # Insertar bloque de estilos adaptativos
    svg = re.sub(r'(<svg[^>]*>)', r'\1\n' + STYLE_HEADER, svg, count=1)
    # Remover fondos rectangulares blancos estáticos
    svg = re.sub(r'<rect[^>]+fill=[\'\"](?:#fff(?:fff)?|white)[\'\"][^>]*/>', '', svg)

    with open(dest_svg_path, 'w', encoding='utf-8') as f:
        f.write(svg)

    # 4. Render a PNG en img/_preview/ y detección de recorte/viewBox
    light_png, dark_png = render_inspection_pngs(dest_svg_path, base_name)
    clipping_warns = check_clipping_and_viewbox(dest_svg_path)
    
    size_kb = os.path.getsize(dest_svg_path) / 1024.0
    status_str = "[OK]" if not clipping_warns else "[WARN]"
    print(f"{status_str} {base_name}.svg ({size_kb:.1f} KB) -> PNGs generados en img/_preview/")
    if clipping_warns:
        for w in clipping_warns:
            print(f"       -> Advertencia: {w}")

    return True

def render_inspection_pngs(svg_path, base_name):
    doc = pymupdf.open(svg_path)
    page = doc[0]
    rect = page.rect
    scale = 800.0 / rect.width if rect.width > 0 else 2.0
    mat = pymupdf.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat, alpha=True)
    img_rgba = Image.frombytes("RGBA", [pix.width, pix.height], pix.samples)

    # 1. Fondo blanco (Modo Claro)
    bg_white = Image.new("RGBA", img_rgba.size, (255, 255, 255, 255))
    bg_white.paste(img_rgba, (0, 0), img_rgba)
    light_png_path = os.path.join(PREVIEW_DIR, f"{base_name}_light.png")
    bg_white.convert("RGB").save(light_png_path)

    # 2. Fondo oscuro (#0f172a, Modo Oscuro)
    bg_dark = Image.new("RGBA", img_rgba.size, (15, 23, 42, 255))
    with open(svg_path, 'r', encoding='utf-8') as f:
        dark_svg = f.read()
    dark_svg = dark_svg.replace('color: #1f2937;', 'color: #f8fafc;')
    dark_svg = dark_svg.replace('currentColor', '#f8fafc')
    dark_svg = dark_svg.replace('var(--fig-azul, #0284c7)', '#38bdf8')
    dark_svg = dark_svg.replace('var(--fig-rojo, #dc2626)', '#f87171')
    dark_svg = dark_svg.replace('var(--fig-verde, #16a34a)', '#4ade80')
    dark_svg = dark_svg.replace('var(--fig-morado, #7c3aed)', '#c084fc')

    doc_dark = pymupdf.open("svg", dark_svg.encode('utf-8'))
    pix_dark = doc_dark[0].get_pixmap(matrix=mat, alpha=True)
    img_dark_rgba = Image.frombytes("RGBA", [pix_dark.width, pix_dark.height], pix_dark.samples)

    bg_dark.paste(img_dark_rgba, (0, 0), img_dark_rgba)
    dark_png_path = os.path.join(PREVIEW_DIR, f"{base_name}_dark.png")
    bg_dark.convert("RGB").save(dark_png_path)

    return light_png_path, dark_png_path

def check_clipping_and_viewbox(svg_path):
    warnings = []
    try:
        doc = pymupdf.open(svg_path)
        page = doc[0]
        rect = page.rect
        out_of_bounds = 0
        for d in page.get_drawings():
            r = d['rect']
            if r.x0 < rect.x0 - 2 or r.x1 > rect.x1 + 2 or r.y0 < rect.y0 - 2 or r.y1 > rect.y1 + 2:
                out_of_bounds += 1
        if out_of_bounds > 0:
            warnings.append(f"{out_of_bounds} trazos vectoriales/glifos exceden el viewBox ({rect})")
    except Exception as e:
        warnings.append(f"Error analizando geometría vectorial: {e}")
    return warnings

def generate_gallery():
    # Importar metadatos si existen en generate_gallery
    sys.path.insert(0, os.path.join(BASE_DIR, 'scripts'))
    try:
        from generate_gallery import FIGURES
    except Exception:
        FIGURES = []

    # Obtener todas las figuras SVG
    all_svgs = sorted([f for f in os.listdir(IMG_DIR) if f.endswith('.svg')])
    meta_dict = {f['file']: f for f in FIGURES}

    cards_html = []
    for svg_file in all_svgs:
        base = os.path.splitext(svg_file)[0]
        meta = meta_dict.get(svg_file, {
            "title": base.replace('_', ' ').title(),
            "group": "Módulo General",
            "desc": f"Figura vectorial {svg_file}"
        })

        svg_path = os.path.join(IMG_DIR, svg_file)
        size_kb = os.path.getsize(svg_path) / 1024.0
        light_png = f"_preview/{base}_light.png"
        dark_png = f"_preview/{base}_dark.png"

        cards_html.append(f"""
        <div class="fig-card">
          <div class="card-header">
            <span class="card-id">{base}</span>
            <span class="card-size">{size_kb:.1f} KB</span>
          </div>
          <div class="preview-container">
            <img class="svg-display" src="{svg_file}" alt="{meta['title']}">
          </div>
          <div class="card-info">
            <div class="fig-title">{meta['title']}</div>
            <div class="fig-meta">{meta.get('group', '')}</div>
            <div class="fig-desc">{meta.get('desc', '')}</div>
            <div class="view-links">
              <a href="{svg_file}" target="_blank">SVG Original</a> · 
              <a href="{light_png}" target="_blank">PNG Claro</a> · 
              <a href="{dark_png}" target="_blank">PNG Oscuro</a>
            </div>
          </div>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Galería de Figuras Vectoriales · FIS120 UTFSM</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <style>
    :root {{
      --bg: #f8fafc;
      --bg-card: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --accent: #0284c7;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}
    [data-theme="dark"] {{
      --bg: #090d16;
      --bg-card: #0f172a;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --border: #1e293b;
      --accent: #38bdf8;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: "Latin Modern Roman", "Computer Modern Serif", Georgia, serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 2rem 1.5rem;
      transition: background 0.2s, color 0.2s;
    }}
    header {{
      max-width: 1300px;
      margin: 0 auto 2rem auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.2rem;
    }}
    h1 {{ font-size: 1.8rem; font-weight: 700; }}
    .subtitle {{ color: var(--text-muted); font-size: 0.95rem; margin-top: 0.2rem; }}
    .btn-toggle {{
      background: var(--accent);
      color: #fff;
      border: none;
      padding: 0.6rem 1.2rem;
      border-radius: 6px;
      font-family: inherit;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .gallery-grid {{
      max-width: 1300px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.5rem;
    }}
    .fig-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.6rem 1rem;
      background: rgba(0,0,0,0.03);
      border-bottom: 1px solid var(--border);
      font-family: monospace;
      font-size: 0.8rem;
    }}
    .card-id {{ font-weight: bold; color: var(--accent); }}
    .card-size {{ color: var(--text-muted); }}
    .preview-container {{
      padding: 1.2rem;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 220px;
      background: var(--bg-card);
    }}
    .svg-display {{
      max-width: 100%;
      height: auto;
      max-height: 260px;
      object-fit: contain;
    }}
    .card-info {{
      padding: 1rem;
      border-top: 1px solid var(--border);
      margin-top: auto;
    }}
    .fig-title {{ font-size: 1.05rem; font-weight: bold; margin-bottom: 0.2rem; }}
    .fig-meta {{ font-size: 0.85rem; color: var(--accent); margin-bottom: 0.4rem; }}
    .fig-desc {{ font-size: 0.88rem; color: var(--text-muted); margin-bottom: 0.6rem; }}
    .view-links {{ font-size: 0.82rem; }}
    .view-links a {{ color: var(--accent); text-decoration: none; }}
    .view-links a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Galería de Figuras Vectoriales (25 Figuras)</h1>
      <div class="subtitle">FIS120 / FIS12125 · Certamen 3 (2026-2) · Control de Calidad y Renderizado</div>
    </div>
    <button class="btn-toggle" onclick="toggleTheme()" id="btn-theme">🌓 Alternar Modo Claro / Oscuro</button>
  </header>
  <main class="gallery-grid">
    {''.join(cards_html)}
  </main>
  <script>
    function toggleTheme() {{
      const html = document.documentElement;
      const isDark = html.getAttribute('data-theme') === 'dark';
      html.setAttribute('data-theme', isDark ? 'light' : 'dark');
      inlineSVGs();
    }}
    function inlineSVGs() {{
      document.querySelectorAll('.svg-display').forEach(img => {{
        const src = img.getAttribute('src');
        if (!src) return;
        fetch(src)
          .then(r => r.text())
          .then(svgText => {{
            const div = document.createElement('div');
            div.innerHTML = svgText;
            const svg = div.querySelector('svg');
            if (svg) {{
              svg.style.maxWidth = '100%';
              svg.style.maxHeight = '260px';
              svg.style.height = 'auto';
              img.replaceWith(svg);
            }}
          }})
          .catch(() => {{}});
      }});
    }}
    document.addEventListener('DOMContentLoaded', () => {{
      const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (prefersDark) document.documentElement.setAttribute('data-theme', 'dark');
      inlineSVGs();
    }});
  </script>
</body>
</html>
"""
    with open(GALERIA_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[OK] Galería actualizada en: {GALERIA_PATH}")

if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        for a in args:
            compile_tikz(a)
    else:
        for f in sorted(os.listdir(TEX_DIR)):
            if f.endswith('.tex'):
                compile_tikz(f)
    generate_gallery()
