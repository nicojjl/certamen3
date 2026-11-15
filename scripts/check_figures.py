#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Validación de Figuras Vectoriales SVG y Código Fuente TikZ
Verifica que cada SVG en img/:
1. Sea XML bien formado y válido.
2. Tenga un tamaño en disco estrictamente menor a 120 KB.
3. No contenga referencias externas inseguras o no reproducibles (href o src con http:// o https://).
4. Tenga su archivo fuente .tex correspondiente en scripts/figuras_tex/.
"""

import os
import sys
import glob
import re
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'img')
TEX_DIR = os.path.join(BASE_DIR, 'scripts', 'figuras_tex')

MAX_SIZE_BYTES = 120 * 1024  # 120 KB

def validate_all_figures():
    print("=" * 70)
    print("VALIDACIÓN INTEGRAL DE FIGURAS VECTORIALES SVG Y FUENTES TIKZ")
    print("=" * 70)

    svg_files = sorted(glob.glob(os.path.join(IMG_DIR, "*.svg")))
    if not svg_files:
        print("[ERROR] No se encontraron archivos SVG en la carpeta img/.")
        sys.exit(1)

    passed = 0
    total = len(svg_files)
    failures = []

    for svg_path in svg_files:
        fname = os.path.basename(svg_path)
        base_name, _ = os.path.splitext(fname)
        tex_path = os.path.join(TEX_DIR, f"{base_name}.tex")

        errors = []

        # 1. Validar existencia del fuente TeX
        if not os.path.exists(tex_path):
            errors.append(f"Falta fuente TikZ: {base_name}.tex")

        # 2. Validar tamaño de archivo (< 120 KB)
        size_bytes = os.path.getsize(svg_path)
        size_kb = size_bytes / 1024.0
        if size_bytes >= MAX_SIZE_BYTES:
            errors.append(f"Tamaño excesivo: {size_kb:.1f} KB >= 120 KB límite")

        # 3. Leer contenido y validar XML
        try:
            with open(svg_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ET.fromstring(content)
        except Exception as e:
            errors.append(f"XML inválido: {e}")
            content = ""

        # 4. Validar ausencia de enlaces HTTP/HTTPS externos en href o src
        # (los atributos estándar xmlns='http://www.w3.org/...' son declaraciones de namespace válidas)
        external_refs = re.findall(r'(?:href|src)\s*=\s*[\'"]https?://[^\'"]+', content, re.IGNORECASE)
        if external_refs:
            errors.append(f"Referencias HTTP externas prohibidas en href/src: {external_refs}")

        if errors:
            msg = f"[FAIL] {fname:33} ({size_kb:5.1f} KB): {'; '.join(errors)}"
            print(msg)
            failures.append(msg)
        else:
            print(f"[PASS] {fname:33} ({size_kb:5.1f} KB) | XML válido | Fuente TeX OK | 0 URLs externas")
            passed += 1

    print("\n" + "=" * 70)
    print(f"RESUMEN DE FIGURAS: {passed}/{total} CORRECTAS")
    print("=" * 70)

    if failures:
        print(f"\nSE DETECTARON {len(failures)} FIGURAS CON FALLOS:")
        for f in failures:
            print(f" - {f}")
        sys.exit(1)
    else:
        print("Todas las figuras SVG cumplen los estándares de calidad del repositorio.")
        sys.exit(0)

if __name__ == '__main__':
    validate_all_figures()
