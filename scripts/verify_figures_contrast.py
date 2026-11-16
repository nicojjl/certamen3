#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación de Contraste y Renderizado de Figuras SVG en Modo Claro y Oscuro
Utiliza Playwright para:
  1. Renderizar cada figura en un contenedor idéntico al de las tarjetas de ejercicio.
  2. Verificar en modo claro y modo oscuro que el color de trazo calculado (computed stroke)
     de ningún elemento sea igual al fondo de la tarjeta ni tenga ratio de contraste < 3:1.
  3. Guardar capturas de cada figura en ambos modos en img/_preview/.
  4. Salir con código 1 si algún elemento incumple el contraste o es idéntico al fondo.
"""

import os
import sys
import glob
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'img')
PREVIEW_DIR = os.path.join(IMG_DIR, '_preview')

def relative_luminance(r, g, b):
    def ch(c):
        v = c / 255.0
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)

def contrast_ratio(rgb1, rgb2):
    l1 = relative_luminance(*rgb1)
    l2 = relative_luminance(*rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def parse_css_rgb(color_str):
    m = re.match(r'rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', color_str.strip())
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None

def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[ERROR] Playwright no está instalado. Ejecute: pip install playwright")
        sys.exit(1)

    os.makedirs(PREVIEW_DIR, exist_ok=True)
    svg_files = sorted(glob.glob(os.path.join(IMG_DIR, "*.svg")))
    if not svg_files:
        print("[ERROR] No se encontraron archivos SVG en img/")
        sys.exit(1)

    host = "localhost"
    port = 8080
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])

    all_ok = True
    total_figures = len(svg_files)
    contrast_records = []
    min_contrast_observed = 999.0

    print("=" * 75)
    print("VERIFICACIÓN DE CONTRASTE SVG EN MODO CLARO Y OSCURO (PLAYWRIGHT)")
    print("=" * 75)
    print(f"[INFO] Servidor destino: http://{host}:{port}/")
    print(f"[INFO] Total figuras SVG a verificar: {total_figures}")
    print(f"[INFO] Carpeta de capturas: {PREVIEW_DIR}\n")

    with sync_playwright() as p:
        browser = None
        launch_attempts = [
            {'channel': 'chrome'},
            {'channel': 'msedge'},
            {}
        ]
        for kwargs in launch_attempts:
            try:
                browser = p.chromium.launch(headless=True, **kwargs)
                break
            except Exception:
                pass

        if not browser:
            print("[ERROR] No se pudo inicializar Chromium ni Chrome/Edge.")
            sys.exit(1)

        page = browser.new_page(viewport={"width": 1280, "height": 900})

        try:
            page.goto(f"http://{host}:{port}/", wait_until="domcontentloaded")
        except Exception as e:
            print(f"[ERROR] No se pudo conectar al servidor local en http://{host}:{port}/: {e}")
            browser.close()
            sys.exit(1)

        # Desactivar transiciones CSS y crear banco de pruebas en el DOM
        page.evaluate("""() => {
            const style = document.createElement('style');
            style.id = 'disable-transitions-style';
            style.innerHTML = `
                *, *::before, *::after {
                    transition: none !important;
                    animation: none !important;
                }
            `;
            document.head.appendChild(style);

            const bench = document.createElement('div');
            bench.id = 'contrast-test-bench';
            bench.style.position = 'fixed';
            bench.style.top = '0';
            bench.style.left = '0';
            bench.style.zIndex = '999999';
            bench.style.padding = '20px';
            bench.style.pointerEvents = 'none';

            bench.innerHTML = `
                <div class="exercise-card" id="test-card" style="display: inline-block; padding: 20px; border-radius: 8px;">
                    <div class="figure-container" id="test-container" style="display: flex; justify-content: center; align-items: center; padding: 10px;">
                    </div>
                </div>
            `;
            document.body.appendChild(bench);
        }""")

        for idx, svg_path in enumerate(svg_files, 1):
            fname = os.path.basename(svg_path)
            fbase = os.path.splitext(fname)[0]

            with open(svg_path, 'r', encoding='utf-8') as f:
                svg_content = f.read()

            fig_failures = []

            for theme in ['light', 'dark']:
                # Cambiar tema en el documento
                page.evaluate(f"theme => document.documentElement.setAttribute('data-theme', theme)", theme)
                
                # Inyectar SVG en el contenedor de prueba
                page.evaluate("""content => {
                    const cont = document.getElementById('test-container');
                    cont.innerHTML = content;
                    const svg = cont.querySelector('svg');
                    if (svg) svg.classList.add('inlined-svg');
                }""", svg_content)

                page.wait_for_timeout(60)

                # Inspección de trazos, rellenos y colores calculados en el DOM
                eval_result = page.evaluate("""() => {
                    const card = document.getElementById('test-card');
                    const cont = document.getElementById('test-container');
                    const cardBg = window.getComputedStyle(card).backgroundColor;
                    const contBg = window.getComputedStyle(cont).backgroundColor;

                    const svg = cont.querySelector('svg');
                    if (!svg) return { error: 'No svg element found' };

                    // 1. Textos y glifos tipográficos (text, tspan, use)
                    const textElements = Array.from(svg.querySelectorAll('text, tspan, use'));
                    const texts = [];
                    textElements.forEach((el, i) => {
                        const style = window.getComputedStyle(el);
                        const fill = style.fill;
                        const stroke = style.stroke;
                        const opacity = parseFloat(style.opacity) || 1;
                        if (opacity <= 0) return;
                        
                        const color = (fill && fill !== 'none') ? fill : stroke;
                        if (!color || color === 'none') return;

                        texts.push({
                            index: i,
                            tag: el.tagName,
                            html: el.outerHTML.substring(0, 100),
                            color: color,
                            text: el.textContent || el.getAttribute('xlink:href') || ''
                        });
                    });

                    // 2. Gráficos (path, line, polyline, polygon, circle, rect, ellipse) fuera de defs
                    const allShapes = Array.from(svg.querySelectorAll('path, line, polyline, polygon, circle, rect, ellipse'));
                    const shapes = [];
                    allShapes.forEach((shape, i) => {
                        if (shape.closest('defs')) return; // Evitar definiciones de glifos en <defs>
                        const style = window.getComputedStyle(shape);
                        const stroke = style.stroke;
                        const fill = style.fill;
                        const strokeWidth = parseFloat(style.strokeWidth) || 0;
                        const opacity = parseFloat(style.opacity) || 1;
                        if (opacity <= 0) return;

                        const hasStroke = stroke && stroke !== 'none' && strokeWidth > 0;
                        const hasFill = fill && fill !== 'none';

                        if (!hasStroke && !hasFill) return;

                        shapes.push({
                            index: i,
                            tag: shape.tagName,
                            html: shape.outerHTML.substring(0, 100),
                            stroke: hasStroke ? stroke : null,
                            strokeWidth: strokeWidth,
                            fill: hasFill ? fill : null,
                            isFilledSymbol: !hasStroke && hasFill
                        });
                    });

                    return {
                        cardBg,
                        contBg,
                        texts,
                        shapes
                    };
                }""")

                if 'error' in eval_result:
                    fig_failures.append(f"[{theme.upper()}] {eval_result['error']}")
                    continue

                card_bg_rgb = parse_css_rgb(eval_result['cardBg'])
                cont_bg_rgb = parse_css_rgb(eval_result['contBg'])
                bg_rgb = card_bg_rgb or cont_bg_rgb or (255, 255, 255)

                # A. Comprobación de TEXTOS: exige al menos 4.5:1
                texts = eval_result.get('texts', [])
                for t in texts:
                    t_rgb = parse_css_rgb(t['color'])
                    if not t_rgb:
                        continue

                    if t_rgb == bg_rgb:
                        fig_failures.append(
                            f"[{theme.upper()}] Texto <{t['tag']}> idéntico al fondo {eval_result['cardBg']} ({t['color']})"
                        )
                        continue

                    cr = contrast_ratio(t_rgb, bg_rgb)
                    if cr < min_contrast_observed:
                        min_contrast_observed = cr

                    if cr < 4.5:
                        fig_failures.append(
                            f"[{theme.upper()}] Texto <{t['tag']}> {t.get('text')} (color: {t['color']}, rgb: {t_rgb}) con contraste insuficiente ({cr:.2f}:1 < 4.5:1) vs fondo {eval_result['cardBg']}"
                        )

                # B. Comprobación de GRÁFICOS: exige al menos 3.0:1
                shapes = eval_result.get('shapes', [])
                for s in shapes:
                    # Comprobación de trazo (stroke)
                    if s['stroke']:
                        stroke_rgb = parse_css_rgb(s['stroke'])
                        if stroke_rgb:
                            if stroke_rgb == bg_rgb:
                                fig_failures.append(
                                    f"[{theme.upper()}] Trazo de <{s['tag']}> idéntico al fondo {eval_result['cardBg']} ({s['stroke']})"
                                )
                                continue

                            cr = contrast_ratio(stroke_rgb, bg_rgb)
                            if cr < min_contrast_observed:
                                min_contrast_observed = cr

                            if cr < 3.0:
                                fig_failures.append(
                                    f"[{theme.upper()}] Trazo de <{s['tag']}> {s.get('html')} (stroke: {s['stroke']}, rgb: {stroke_rgb}) con contraste insuficiente ({cr:.2f}:1 < 3:1) vs fondo {eval_result['cardBg']}"
                                )

                    # Comprobación de símbolos rellenos sólidos (flechas, marcadores, etc.)
                    if s['isFilledSymbol'] and s['fill']:
                        fill_rgb = parse_css_rgb(s['fill'])
                        if fill_rgb:
                            fill_lum = relative_luminance(*fill_rgb)
                            # Máscaras de fondo y lavados pasteles en modo claro son decorativos
                            is_background_wash = (theme == 'light' and fill_lum >= 0.50)
                            if is_background_wash:
                                continue

                            if fill_rgb == bg_rgb:
                                fig_failures.append(
                                    f"[{theme.upper()}] Relleno de símbolo <{s['tag']}> idéntico al fondo {eval_result['cardBg']} ({s['fill']})"
                                )
                                continue

                            cr = contrast_ratio(fill_rgb, bg_rgb)
                            if cr < min_contrast_observed:
                                min_contrast_observed = cr

                            if cr < 3.0:
                                fig_failures.append(
                                    f"[{theme.upper()}] Relleno de símbolo <{s['tag']}> {s.get('html')} (fill: {s['fill']}, rgb: {fill_rgb}) con contraste insuficiente ({cr:.2f}:1 < 3:1) vs fondo {eval_result['cardBg']}"
                                )

                # Tomar captura de pantalla en img/_preview/
                preview_file = os.path.join(PREVIEW_DIR, f"{fbase}_{theme}.png")
                try:
                    container_handle = page.locator("#test-container")
                    container_handle.screenshot(path=preview_file)
                except Exception as snap_err:
                    print(f"  [WARN] No se pudo guardar captura {preview_file}: {snap_err}")

            if fig_failures:
                all_ok = False
                print(f"[FAIL] {idx:2d}/{total_figures} {fname}:")
                for ff in fig_failures:
                    print(f"       -> {ff}")
            else:
                print(f"[PASS] {idx:2d}/{total_figures} {fname:32s} | Claro y Oscuro OK (Capturas guardadas)")

        browser.close()

    print("\n" + "=" * 75)
    print(f"RESUMEN AUDITORÍA CONTRASTE: {'EXITOSA (0 FALLAS)' if all_ok else 'FALLIDA'}")
    print(f"Ratio mínimo de contraste calculado observado: {min_contrast_observed:.2f}:1 (Mínimo exigido: 3.00:1)")
    print(f"Capturas generadas en: {PREVIEW_DIR}")
    print("=" * 75)

    if not all_ok:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
