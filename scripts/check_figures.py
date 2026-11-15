import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_gallery import FIGURES

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_dir = os.path.join(base_dir, 'img')
tex_dir = os.path.join(base_dir, 'scripts', 'figuras_tex')

missing_svg = 0
missing_tex = 0
for f in FIGURES:
    fname = f['file']
    tid = f['id']
    svg_p = os.path.join(img_dir, fname)
    tex_p = os.path.join(tex_dir, tid + '.tex')
    svg_ok = os.path.exists(svg_p)
    tex_ok = os.path.exists(tex_p)
    if not svg_ok: missing_svg += 1
    if not tex_ok: missing_tex += 1
    s_svg = 'OK' if svg_ok else 'MISSING'
    s_tex = 'OK' if tex_ok else 'MISSING'
    print(f"[{s_svg}] SVG: {fname:33} | [{s_tex}] TEX: {tid}.tex")

print(f"\nTotal: {len(FIGURES)}, Missing SVG: {missing_svg}, Missing TEX: {missing_tex}")
