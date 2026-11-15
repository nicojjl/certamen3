#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación de Renderizado KaTeX y Ausencia de Errores en Navegador
Soporta recorrido interactivo exhaustivo con Playwright haciendo click en todos los
botones de interacción ("Comprobar", "Mostrar Pista / Paso 1", "Mostrar Siguiente Paso",
"Solución Completa Visible", "Mostrar Pauta Modelo", "Revelar Todo") y validación de
0 errores de consola y 0 errores de KaTeX, con fallback a Headless Chrome CLI.
"""

import os
import sys
import shutil
import subprocess
import re
import argparse

MODULES = [f"mod{i}" for i in range(12)]

def find_system_browser():
    """Busca un navegador compatible instalado en el sistema (Chrome, Chromium, Edge)."""
    env_browser = os.environ.get("CHROME_BIN") or os.environ.get("BROWSER_PATH")
    if env_browser and os.path.exists(env_browser):
        return env_browser

    candidates = [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "chrome",
        "msedge"
    ]
    for c in candidates:
        p = shutil.which(c)
        if p:
            return p

    if sys.platform == "win32":
        win_candidates = [
            os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)"), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.environ.get("PROGRAMFILES(X86)", "C:\\Program Files (x86)"), "Microsoft", "Edge", "Application", "msedge.exe"),
            os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"), "Microsoft", "Edge", "Application", "msedge.exe"),
        ]
        for p in win_candidates:
            if os.path.exists(p):
                return p
    elif sys.platform == "darwin":
        mac_candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
        ]
        for p in mac_candidates:
            if os.path.exists(p):
                return p
    else:
        linux_candidates = [
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/usr/bin/chromium",
            "/usr/bin/chromium-browser"
        ]
        for p in linux_candidates:
            if os.path.exists(p):
                return p

    return None

def check_with_playwright(host, port, browser_path=None):
    """
    Recorrido interactivo exhaustivo con Playwright:
    Navega por todos los módulos, interactúa haciendo click en botones de pasos,
    pistas, soluciones y comprobaciones, y valida ausencia total de errores.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[WARN] Playwright no está instalado. Usando fallback de Chrome CLI.")
        return None

    print("[INFO] Iniciando recorrido interactivo automatizado con Playwright...")
    all_ok = True
    total_formulas = 0
    total_modules = 0

    with sync_playwright() as p:
        browser = None
        launch_attempts = []

        if browser_path and os.path.exists(browser_path):
            launch_attempts.append({'executable_path': browser_path})
        
        launch_attempts.append({'channel': 'chrome'})
        launch_attempts.append({'channel': 'msedge'})
        launch_attempts.append({})

        for kwargs in launch_attempts:
            try:
                browser = p.chromium.launch(headless=True, **kwargs)
                break
            except Exception:
                pass

        if not browser:
            print("[WARN] No se pudo inicializar Playwright Chromium. Pasando a Chrome CLI.")
            return None

        context = browser.new_context(viewport={"width": 1280, "height": 900})
        page = context.new_page()

        console_errors = []
        page_errors = []

        def handle_console(msg):
            if msg.type == "error":
                text = msg.text
                if "favicon.ico" not in text:
                    console_errors.append(f"[{msg.type}] {text}")

        page.on("console", handle_console)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        for mod in MODULES:
            mod_url = f"http://{host}:{port}/#{mod}"
            try:
                page.goto(mod_url, wait_until="networkidle", timeout=10000)
            except Exception:
                page.goto(mod_url, timeout=10000)
                page.wait_for_timeout(400)

            # 1. Interactuar con todos los botones interactivos del módulo
            interaction_count = 0
            for round_idx in range(3):
                buttons = page.locator("button").all()
                clicked_any = False
                for btn in buttons:
                    try:
                        if not btn.is_visible():
                            continue
                        txt = (btn.text_content() or "").strip()
                        keywords = [
                            "Comprobar",
                            "Mostrar Pista",
                            "Paso 1",
                            "Mostrar Siguiente Paso",
                            "Mostrar Todos los Pasos",
                            "Solución Completa Visible",
                            "Mostrar Pauta Modelo",
                            "Revelar Todo",
                            "Ver Pauta"
                        ]
                        if any(kw.lower() in txt.lower() for kw in keywords):
                            btn.click(timeout=1000)
                            clicked_any = True
                            interaction_count += 1
                            page.wait_for_timeout(30)
                    except Exception:
                        pass
                if not clicked_any:
                    break

            # 2. Hacer click en opciones interactivas
            options = page.locator(".option-item").all()
            for opt in options[:8]:
                try:
                    if opt.is_visible():
                        opt.click(timeout=400)
                        page.wait_for_timeout(20)
                except Exception:
                    pass

            # 3. Revelar todo para verificar que no queden errores ocultos
            try:
                page.evaluate("""() => {
                    if (window.App && window.App.revealAll) window.App.revealAll();
                    if (window.renderMathInElement) renderMathInElement(document.body);
                }""")
            except Exception:
                pass
            page.wait_for_timeout(80)

            # 4. Inspeccionar el DOM resultante
            num_formulas = page.locator(".katex").count()
            katex_error_els = page.locator(".katex-error").all()
            num_katex_errors = len(katex_error_els)

            # Extraer posibles comandos TeX no renderizados en texto visible fuera de fórmulas KaTeX
            stray_latex = page.evaluate("""() => {
                const area = document.getElementById('main-content-area') || document.body;
                const walker = document.createTreeWalker(
                    area,
                    NodeFilter.SHOW_TEXT,
                    {
                        acceptNode(node) {
                            if (node.parentElement && node.parentElement.closest('.katex, script, style, svg, math')) {
                                return NodeFilter.FILTER_REJECT;
                            }
                            return NodeFilter.FILTER_ACCEPT;
                        }
                    }
                );
                const matches = [];
                while (walker.nextNode()) {
                    const text = walker.currentNode.nodeValue || '';
                    const m1 = text.match(/\\\\[a-zA-Z]{2,}/g);
                    const m2 = text.match(/\\\\\\\\/g);
                    if (m1) matches.push(...m1);
                    if (m2) matches.push(...m2);
                }
                return matches;
            }""")

            failures = []
            if num_formulas == 0:
                failures.append("0 fórmulas renderizadas")
            if num_katex_errors > 0:
                failures.append(f"{num_katex_errors} errores KaTeX")
            if stray_latex and len(stray_latex) > 0:
                failures.append(f"{len(stray_latex)} comandos LaTeX sueltos: {stray_latex[:3]}")
            if console_errors:
                failures.append(f"{len(console_errors)} errores de consola JS")
            if page_errors:
                failures.append(f"{len(page_errors)} excepciones de página")

            if failures:
                all_ok = False
                print(f"[FAIL] {mod:5s}: {', '.join(failures)} (fórmulas: {num_formulas})")
                for ce in console_errors[:3]:
                    print(f"       -> Consola: {ce}")
            else:
                print(f"[OK]   {mod:5s}: 0 errores de consola | {num_formulas:3d} fórmulas renderizadas | {interaction_count} interacciones")

            total_formulas += num_formulas
            total_modules += 1
            console_errors.clear()
            page_errors.clear()

        browser.close()

    return {
        "ok": all_ok,
        "total_modules": total_modules,
        "total_formulas": total_formulas
    }

def check_with_chrome_cli(browser_bin, host, port):
    """Fallback usando Chrome/Chromium en modo headless dump-dom."""
    all_ok = True
    total_formulas = 0
    total_modules = 0
    print(f"[INFO] Utilizando Chrome CLI fallback: {browser_bin}")
    print(f"[INFO] Destino: http://{host}:{port}/?reveal=all#modX\n")

    for mod in MODULES:
        url = f"http://{host}:{port}/?reveal=all#{mod}"
        cmd = [
            browser_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--virtual-time-budget=4000",
            "--dump-dom",
            url
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
        dom = res.stdout

        if not dom or len(dom.strip()) < 100:
            print(f"[FAIL] {mod:5s}: No se pudo obtener el DOM de {url}")
            all_ok = False
            continue

        katex_spans = re.findall(r'class="katex"', dom)
        num_formulas = len(katex_spans)

        katex_errors = re.findall(r'<span class="katex-error"[^>]*title="([^"]*)"', dom)
        num_errors = len(katex_errors)

        clean_text = re.sub(r'<script[^>]*>.*?</script>', ' ', dom, flags=re.DOTALL)
        clean_text = re.sub(r'<style[^>]*>.*?</style>', ' ', clean_text, flags=re.DOTALL)
        clean_text = re.sub(r'<span class="katex"[^>]*>.*?</span></span></span>', ' ', clean_text, flags=re.DOTALL)
        clean_text = re.sub(r'<annotation[^>]*>.*?</annotation>', ' ', clean_text, flags=re.DOTALL)
        clean_text = re.sub(r'<svg[^>]*>.*?</svg>', ' ', clean_text, flags=re.DOTALL)
        clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
        clean_text = clean_text.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')

        stray_latex = re.findall(r'\\[a-zA-Z]{2,}', clean_text)
        stray_double_slash = re.findall(r'\\\\', clean_text)
        num_stray = len(stray_latex) + len(stray_double_slash)

        failures = []
        if num_formulas == 0:
            failures.append("0 fórmulas renderizadas")
        if num_errors > 0:
            failures.append(f"{num_errors} errores KaTeX")
        if num_stray > 0:
            sample_stray = (stray_latex + stray_double_slash)[:3]
            failures.append(f"{num_stray} comandos LaTeX o barras sueltas visibles: {sample_stray}")

        if failures:
            all_ok = False
            print(f"[FAIL] {mod:5s}: {', '.join(failures)} (fórmulas: {num_formulas})")
        else:
            print(f"[OK]   {mod:5s}: 0 errores | {num_formulas:3d} fórmulas renderizadas (reveal=all)")

        total_formulas += num_formulas
        total_modules += 1

    return {
        "ok": all_ok,
        "total_modules": total_modules,
        "total_formulas": total_formulas
    }

def main():
    parser = argparse.ArgumentParser(description="Verificador automatizado de KaTeX en navegador")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8080")), help="Puerto del servidor local")
    parser.add_argument("--host", default=os.environ.get("HOST", "localhost"), help="Host del servidor local")
    parser.add_argument("--browser", default=None, help="Ruta al binario del navegador")
    parser.add_argument("--no-playwright", action="store_true", help="Forzar el uso de Chrome CLI en lugar de Playwright")
    args = parser.parse_args()

    browser = args.browser or find_system_browser()

    print("=" * 70)
    print("VERIFICANDO RENDERIZADO DE KATEX E INTERACTIVIDAD EN NAVEGADOR")
    print("=" * 70)

    result = None
    if not args.no_playwright:
        result = check_with_playwright(args.host, args.port, browser)

    if result is None:
        if not browser:
            print("[ERROR] No se encontró ningún navegador compatible (Chrome/Chromium/Edge) en el sistema.")
            print("        Define la variable de entorno CHROME_BIN o pasa el argumento --browser <ruta>.")
            sys.exit(1)
        result = check_with_chrome_cli(browser, args.host, args.port)

    ok = result["ok"]
    total_mods = result["total_modules"]
    total_forms = result["total_formulas"]

    if ok:
        print(f"\n[ÉXITO] {total_mods} módulos verificados, {total_forms} fórmulas matemáticas renderizadas, 0 errores KaTeX ni barras sueltas.")
        sys.exit(0)
    else:
        print(f"\n[ERROR] Se detectaron fallos en la verificación de navegador.")
        sys.exit(1)

if __name__ == "__main__":
    main()
