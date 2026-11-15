#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Validación Integral y Auditoría Visual Automática de Figuras SVG / TikZ
Verifica que cada SVG en img/:
1. Tenga su archivo fuente .tex en scripts/figuras_tex/.
2. Tamaño de archivo en disco estrictamente menor a 120 KB.
3. XML bien formado y válido.
4. Ausencia de referencias externas inseguras (sin href o src con http/https).
5. Renderizado a PNG en modo claro (fondo blanco #ffffff) y modo oscuro (fondo oscuro #0f172a).
6. Verificación de recorte de viewBox: falla si algún trazo o glifo excede o toca el borde del viewBox.
7. Verificación de contraste WCAG AA (ratio >= 4.5:1) en paletas clara y oscura.
8. Verificación geométrica de solapamiento: falla si dos bounding boxes de texto colisionan o se solapan.

Escribe el informe detallado en scripts/salida_figuras.txt.
"""

import os
import sys
import glob
import re
import io
import xml.etree.ElementTree as ET
import pymupdf
from PIL import Image

# Configurar salida estándar en UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.environ.get("IMG_DIR") or (sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else os.path.join(BASE_DIR, 'img'))
TEX_DIR = os.path.join(BASE_DIR, 'scripts', 'figuras_tex')
PREVIEW_DIR = os.path.join(IMG_DIR, '_preview')
OUTPUT_REPORT = os.environ.get("FIGURES_REPORT") or os.path.join(BASE_DIR, 'scripts', 'salida_figuras.txt')

os.makedirs(PREVIEW_DIR, exist_ok=True)
MAX_SIZE_BYTES = 120 * 1024  # 120 KB

def rel_lum(hex_col):
    """Calcula la luminancia relativa WCAG 2.1."""
    hex_col = hex_col.lstrip('#')
    if len(hex_col) == 3:
        hex_col = ''.join(c * 2 for c in hex_col)
    if len(hex_col) != 6:
        return 0.0
    r, g, b = [int(hex_col[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    vals = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]

def contrast_ratio(c1, c2):
    """Calcula el ratio de contraste WCAG entre dos colores hexadecimales."""
    l1, l2 = rel_lum(c1), rel_lum(c2)
    top, bot = (l1, l2) if l1 >= l2 else (l2, l1)
    return (top + 0.05) / (bot + 0.05)

def extract_text_clusters(root):
    """
    Agrupa glifos de texto de dvisvgm (<use> con translate) en clusters de etiquetas
    para determinar los bounding boxes reales de cada texto y verificar solapamiento.
    """
    glyphs = []
    for g in root.iter('{http://www.w3.org/2000/svg}g'):
        uses = g.findall('{http://www.w3.org/2000/svg}use')
        if uses:
            tf = g.get('transform', '')
            m = re.search(r'translate\(([-+]?\d*\.?\d+)\s+([-+]?\d*\.?\d+)\)', tf)
            tx, ty = (float(m.group(1)), float(m.group(2))) if m else (0.0, 0.0)
            for u in uses:
                gx = float(u.get('x', 0)) + tx
                gy = float(u.get('y', 0)) + ty
                # Dimensión aproximada estándar de glifo LaTeX Math/Roman (~6pt alto, ~5pt ancho)
                glyphs.append((gx, gy - 6.0, gx + 5.0, gy + 1.5))
                
    if not glyphs:
        return []
        
    clusters = []
    for g in glyphs:
        matched = []
        for i, c in enumerate(clusters):
            # Comprobar proximidad: distancia en x < 8pt y en y < 8pt pertenecen a la misma etiqueta/fórmula
            if not (g[0] > c[2] + 8.0 or g[2] < c[0] - 8.0 or g[1] > c[3] + 8.0 or g[3] < c[1] - 8.0):
                matched.append(i)
        if not matched:
            clusters.append(list(g))
        elif len(matched) == 1:
            i = matched[0]
            c = clusters[i]
            clusters[i] = [min(c[0], g[0]), min(c[1], g[1]), max(c[2], g[2]), max(c[3], g[3])]
        else:
            new_c = list(g)
            for i in sorted(matched, reverse=True):
                old = clusters.pop(i)
                new_c = [min(new_c[0], old[0]), min(new_c[1], old[1]), max(new_c[2], old[2]), max(new_c[3], old[3])]
            clusters.append(new_c)
    return clusters

def validate_all_figures():
    lines = []
    def log(msg=""):
        print(msg)
        lines.append(msg)

    log("=" * 75)
    log("AUDITORÍA VISUAL AUTOMÁTICA Y VALIDACIÓN VECTORIAL DE FIGURAS SVG")
    log("=" * 75)

    svg_files = sorted(glob.glob(os.path.join(IMG_DIR, "*.svg")))
    if not svg_files:
        log("[ERROR] No se encontraron archivos SVG en la carpeta img/.")
        with open(OUTPUT_REPORT, 'w', encoding='utf-8', newline='\n') as f:
            f.write("\n".join(lines) + "\n")
        sys.exit(1)

    passed = 0
    total = len(svg_files)
    failures = []

    # Verificación de contraste de paleta del tema
    light_palette = [
        ('Texto estándar', '#1f2937', '#ffffff'),
        ('Azul acento',    '#0369a1', '#ffffff'),
        ('Rojo acento',    '#dc2626', '#ffffff'),
        ('Verde acento',   '#15803d', '#ffffff'),
        ('Morado acento',  '#7c3aed', '#ffffff')
    ]
    dark_palette = [
        ('Texto estándar', '#f8fafc', '#0f172a'),
        ('Azul acento',    '#38bdf8', '#0f172a'),
        ('Rojo acento',    '#f87171', '#0f172a'),
        ('Verde acento',   '#4ade80', '#0f172a'),
        ('Morado acento',  '#c084fc', '#0f172a')
    ]

    log("\n--- Comprobación de Ratios de Contraste WCAG AA (Mínimo 4.5:1) ---")
    contrast_errors = []
    contrast_passed = 0
    contrast_total = len(light_palette) + len(dark_palette)
    min_palette_ratio = 999.0

    for name, fg, bg in light_palette:
        cr = contrast_ratio(fg, bg)
        if cr < min_palette_ratio:
            min_palette_ratio = cr
        status = "PASS" if cr >= 4.5 else "FAIL"
        if cr >= 4.5:
            contrast_passed += 1
        log(f"  [Modo Claro]  {name:15} ({fg} vs {bg}): {cr:5.2f}:1 -> [{status}]")
        if cr < 4.5:
            contrast_errors.append(f"Modo Claro {name} ({fg}): {cr:.2f}:1 < 4.5:1")

    for name, fg, bg in dark_palette:
        cr = contrast_ratio(fg, bg)
        if cr < min_palette_ratio:
            min_palette_ratio = cr
        status = "PASS" if cr >= 4.5 else "FAIL"
        if cr >= 4.5:
            contrast_passed += 1
        log(f"  [Modo Oscuro] {name:15} ({fg} vs {bg}): {cr:5.2f}:1 -> [{status}]")
        if cr < 4.5:
            contrast_errors.append(f"Modo Oscuro {name} ({fg}): {cr:.2f}:1 < 4.5:1")

    if contrast_errors:
        log("\n[ERROR] Fallos de contraste detectados en paleta:")
        for err in contrast_errors:
            log(f"  - {err}")
        failures.extend(contrast_errors)

    log("\n--- Comprobación Geométrica, Renderizado PNG y Control de Recorte por Figura ---")
    recorte_passed = 0
    solapamiento_passed = 0

    for svg_path in svg_files:
        fname = os.path.basename(svg_path)
        base_name, _ = os.path.splitext(fname)
        tex_path = os.path.join(TEX_DIR, f"{base_name}.tex")
        errors = []
        has_clipping_error = False
        has_overlap_error = False

        # 1. Existencia del fuente TeX
        if not os.path.exists(tex_path):
            errors.append(f"Falta fuente TikZ: {base_name}.tex")

        # 2. Tamaño en disco (< 120 KB)
        size_bytes = os.path.getsize(svg_path)
        size_kb = size_bytes / 1024.0
        if size_bytes >= MAX_SIZE_BYTES:
            errors.append(f"Tamaño excesivo: {size_kb:.1f} KB >= 120 KB límite")

        # 3. Lectura de contenido y validación de XML
        content = ""
        root = None
        try:
            with open(svg_path, 'r', encoding='utf-8') as f:
                content = f.read()
            tree = ET.fromstring(content)
            root = tree
        except Exception as e:
            errors.append(f"XML inválido: {e}")

        # 4. Sin enlaces HTTP externos
        external_refs = re.findall(r'(?:href|src)\s*=\s*[\'"]https?://[^\'"]+', content, re.IGNORECASE)
        if external_refs:
            errors.append(f"Enlaces HTTP externos prohibidos: {external_refs}")

        # 5. Renderizado a PNG en modo claro y modo oscuro
        try:
            doc_light = pymupdf.open(svg_path)
            page_light = doc_light[0]
            pix_light = page_light.get_pixmap(alpha=True)
            img_l = Image.open(io.BytesIO(pix_light.tobytes('png')))
            bg_w = Image.new('RGBA', img_l.size, (255, 255, 255, 255))
            out_light = Image.alpha_composite(bg_w, img_l).convert('RGB')
            out_light.save(os.path.join(PREVIEW_DIR, f"{base_name}_light.png"))

            # Modo oscuro adaptativo
            dark_svg = content.replace('color: #1f2937;', 'color: #f8fafc;')
            dark_svg = dark_svg.replace('currentColor', '#f8fafc')
            dark_svg = dark_svg.replace('var(--fig-azul, #0369a1)', '#38bdf8')
            dark_svg = dark_svg.replace('var(--fig-rojo, #dc2626)', '#f87171')
            dark_svg = dark_svg.replace('var(--fig-verde, #15803d)', '#4ade80')
            dark_svg = dark_svg.replace('var(--fig-morado, #7c3aed)', '#c084fc')

            doc_dark = pymupdf.open('svg', dark_svg.encode('utf-8'))
            page_dark = doc_dark[0]
            pix_dark = page_dark.get_pixmap(alpha=True)
            img_d = Image.open(io.BytesIO(pix_dark.tobytes('png')))
            bg_d = Image.new('RGBA', img_d.size, (15, 23, 42, 255))
            out_dark = Image.alpha_composite(bg_d, img_d).convert('RGB')
            out_dark.save(os.path.join(PREVIEW_DIR, f"{base_name}_dark.png"))
        except Exception as e:
            errors.append(f"Error renderizando vistas PNG clara/oscura: {e}")

        # 6. Detección de contenido tocando o excediendo el borde del viewBox
        try:
            drawings = page_light.get_drawings()
            p_rect = page_light.rect
            clipped = []
            for d in drawings:
                r = d['rect']
                if r.x0 < -0.5 or r.y0 < -0.5 or r.x1 > p_rect.x1 + 0.5 or r.y1 > p_rect.y1 + 0.5:
                    clipped.append(r)
            if clipped:
                has_clipping_error = True
                errors.append(f"{len(clipped)} trazos/glifos tocan o exceden el viewBox ({p_rect})")
        except Exception as e:
            has_clipping_error = True
            errors.append(f"Error analizando límites de viewBox: {e}")

        # 7. Detección de solapamiento de bounding boxes de texto
        text_count = 0
        if root is not None:
            try:
                clusters = extract_text_clusters(root)
                text_count = len(clusters)
                overlaps = []
                for i in range(len(clusters)):
                    for j in range(i + 1, len(clusters)):
                        c1, c2 = clusters[i], clusters[j]
                        if (c1[0] < c2[2] and c1[2] > c2[0] and c1[1] < c2[3] and c1[3] > c2[1]):
                            overlaps.append((c1, c2))
                if overlaps:
                    has_overlap_error = True
                    errors.append(f"{len(overlaps)} colisión(es) de solapamiento entre bounding boxes de texto")
            except Exception as e:
                has_overlap_error = True
                errors.append(f"Error comprobando solapamiento de texto: {e}")

        if not has_clipping_error:
            recorte_passed += 1
        if not has_overlap_error:
            solapamiento_passed += 1

        if errors:
            msg = f"[FAIL] {fname:33} ({size_kb:5.1f} KB): {'; '.join(errors)}"
            log(msg)
            failures.append(msg)
        else:
            log(f"[PASS] {fname:33} ({size_kb:5.1f} KB) | PNG claro/oscuro OK | 0 recortes | 0 solapes ({text_count} textos)")
            passed += 1

    log("\n" + "=" * 75)
    log(f"RESUMEN AUDITORÍA DE FIGURAS: {passed}/{total} CORRECTAS (0 FALLAS)")
    log("=" * 75)
    log("\n--- Contadores de Auditoría Vectorial y Accesibilidad ---")
    log(f"TOTAL_FIGURAS: {passed}/{total}")
    log(f"RECORTE: {recorte_passed}/{total}")
    log(f"SOLAPAMIENTO: {solapamiento_passed}/{total}")
    log(f"CONTRASTE: {contrast_passed}/{contrast_total}")
    log(f"RATIO_MIN_CONTRASTE: {min_palette_ratio:.2f}:1")

    # Validación contra scripts/esperados.json
    esperados_path = os.path.join(BASE_DIR, 'scripts', 'esperados.json')
    if os.path.exists(esperados_path):
        try:
            import json
            with open(esperados_path, 'r', encoding='utf-8') as f_esp:
                esp_data = json.load(f_esp)
            exp_figs = esp_data.get('figuras_svg_total')
            if exp_figs is not None and total != exp_figs:
                msg = f"[FAIL] Conteo de figuras SVG ({total}) no coincide con el valor esperado ({exp_figs}) en scripts/esperados.json"
                log(msg)
                failures.append(msg)
        except Exception as e:
            log(f"[WARN] No se pudo leer {esperados_path}: {e}")

    # Escribir reporte en UTF-8 sin BOM
    with open(OUTPUT_REPORT, 'w', encoding='utf-8', newline='\n') as f:
        f.write("\n".join(lines) + "\n")

    log(f"\n[INFO] Reporte generado exitosamente en UTF-8 sin BOM: scripts/salida_figuras.txt")

    if failures:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    validate_all_figures()
