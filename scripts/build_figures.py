#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Pipeline de Generación y Calidad de Figuras TikZ -> SVG -> PNG
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
PNG_DIR = os.path.join(BASE_DIR, 'scripts', 'inspeccion_png')

os.makedirs(TEX_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)

STYLE_HEADER = """<style>
  :root {
    color: #1f2937;
    --fig-azul: #0284c7;
    --fig-rojo: #dc2626;
    --fig-verde: #16a34a;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      color: #f8fafc;
      --fig-azul: #38bdf8;
      --fig-rojo: #f87171;
      --fig-verde: #4ade80;
    }
  }
  [data-theme="dark"] svg, .dark-mode svg {
    color: #f8fafc;
    --fig-azul: #38bdf8;
    --fig-rojo: #f87171;
    --fig-verde: #4ade80;
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

    # 2. dvisvgm -> svg
    cmd_dvisvgm = ["dvisvgm", "--no-fonts", "-o", raw_svg_path, dvi_path]
    res_svg = subprocess.run(cmd_dvisvgm, cwd=TEX_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res_svg.returncode != 0 or not os.path.exists(raw_svg_path):
        print(f"[FAIL dvisvgm] {base_name}: {res_svg.stderr}")
        return False

    # 3. Post-process SVG
    with open(raw_svg_path, 'r', encoding='utf-8') as f:
        svg = f.read()

    # Replace colors
    # Negro -> currentColor
    svg = re.sub(r'stroke=[\'\"]#000(?:000)?[\'\"]', 'stroke="currentColor"', svg)
    svg = re.sub(r'fill=[\'\"]#000(?:000)?[\'\"]', 'fill="currentColor"', svg)
    # Azul -> var(--fig-azul, #0284c7)
    svg = re.sub(r'stroke=[\'\"](?:#0284c7|#0077cc|#0000ff|#1976d2)[\'\"]', 'stroke="var(--fig-azul, #0284c7)"', svg, flags=re.I)
    svg = re.sub(r'fill=[\'\"](?:#0284c7|#0077cc|#0000ff|#1976d2)[\'\"]', 'fill="var(--fig-azul, #0284c7)"', svg, flags=re.I)
    # Rojo -> var(--fig-rojo, #dc2626)
    svg = re.sub(r'stroke=[\'\"](?:#dc2626|#cc0000|#ff0000|#d32f2f)[\'\"]', 'stroke="var(--fig-rojo, #dc2626)"', svg, flags=re.I)
    svg = re.sub(r'fill=[\'\"](?:#dc2626|#cc0000|#ff0000|#d32f2f)[\'\"]', 'fill="var(--fig-rojo, #dc2626)"', svg, flags=re.I)
    # Verde -> var(--fig-verde, #16a34a)
    svg = re.sub(r'stroke=[\'\"](?:#16a34a|#009900|#388e3c)[\'\"]', 'stroke="var(--fig-verde, #16a34a)"', svg, flags=re.I)
    svg = re.sub(r'fill=[\'\"](?:#16a34a|#009900|#388e3c)[\'\"]', 'fill="var(--fig-verde, #16a34a)"', svg, flags=re.I)

    # Insert <style> after <svg...>
    svg = re.sub(r'(<svg[^>]*>)', r'\1\n' + STYLE_HEADER, svg, count=1)

    # Remove any white background rect
    svg = re.sub(r'<rect[^>]+fill=[\'\"](?:#fff(?:fff)?|white)[\'\"][^>]*/>', '', svg)

    with open(dest_svg_path, 'w', encoding='utf-8') as f:
        f.write(svg)

    # 4. Render to PNG for quality inspection (800px width)
    render_inspection_pngs(dest_svg_path, base_name)
    print(f"[OK] {base_name}.svg generado e inspeccionado")
    return True

def render_inspection_pngs(svg_path, base_name):
    doc = pymupdf.open(svg_path)
    page = doc[0]
    # Calculate scale for 800px width
    rect = page.rect
    scale = 800.0 / rect.width if rect.width > 0 else 2.0
    mat = pymupdf.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat, alpha=True)
    
    # Save transparent
    img_rgba = Image.frombytes("RGBA", [pix.width, pix.height], pix.samples)

    # 1. White background
    bg_white = Image.new("RGBA", img_rgba.size, (255, 255, 255, 255))
    bg_white.paste(img_rgba, (0, 0), img_rgba)
    bg_white.convert("RGB").save(os.path.join(PNG_DIR, f"{base_name}_light.png"))

    # 2. Dark background (#0f172a)
    bg_dark = Image.new("RGBA", img_rgba.size, (15, 23, 42, 255))
    # Invert colors or paste with light text
    # In dark mode currentColor is white, so let's render an SVG where currentColor is set to white
    with open(svg_path, 'r', encoding='utf-8') as f:
        dark_svg = f.read()
    dark_svg = dark_svg.replace('color: #1f2937;', 'color: #f8fafc;')
    dark_svg = dark_svg.replace('currentColor', '#f8fafc')
    dark_svg = dark_svg.replace('var(--fig-azul, #0284c7)', '#38bdf8')
    dark_svg = dark_svg.replace('var(--fig-rojo, #dc2626)', '#f87171')
    dark_svg = dark_svg.replace('var(--fig-verde, #16a34a)', '#4ade80')

    doc_dark = pymupdf.open("svg", dark_svg.encode('utf-8'))
    pix_dark = doc_dark[0].get_pixmap(matrix=mat, alpha=True)
    img_dark_rgba = Image.frombytes("RGBA", [pix_dark.width, pix_dark.height], pix_dark.samples)

    bg_dark.paste(img_dark_rgba, (0, 0), img_dark_rgba)
    bg_dark.convert("RGB").save(os.path.join(PNG_DIR, f"{base_name}_dark.png"))

if __name__ == '__main__':
    args = sys.argv[1:]
    if args:
        for a in args:
            compile_tikz(a)
    else:
        for f in sorted(os.listdir(TEX_DIR)):
            if f.endswith('.tex'):
                compile_tikz(f)
