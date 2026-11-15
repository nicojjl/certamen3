#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación de Renderizado KaTeX y Ausencia de Errores en Navegador
Soporta detección dinámica de navegadores (Chrome, Chromium, Edge, Playwright)
y parámetros de host/puerto configurables por CLI o variables de entorno.
"""

import os
import sys
import shutil
import subprocess
import re
import argparse

MODULES = [f"mod{i}" for i in range(12)]

def find_browser():
    # 1. Variable de entorno explícita
    env_browser = os.environ.get("CHROME_BIN") or os.environ.get("BROWSER_PATH")
    if env_browser and os.path.exists(env_browser):
        return env_browser

    # 2. Búsqueda en PATH del sistema
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

    # 3. Rutas canónicas según plataforma
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
    else:  # Linux / Unix
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

def check_with_chrome_cli(browser_bin, host, port):
    all_ok = True
    print(f"[INFO] Utilizando navegador: {browser_bin}")
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

        # 1. Contar fórmulas renderizadas correctamente
        katex_spans = re.findall(r'class="katex"', dom)
        num_formulas = len(katex_spans)

        # 2. Contar errores sintácticos o de parseo de KaTeX
        katex_errors = re.findall(r'<span class="katex-error"[^>]*title="([^"]*)"', dom)
        num_errors = len(katex_errors)

        # 3. Detectar comandos LaTeX sin procesar o barras sueltas en texto visible
        # Eliminamos <script>, <style>, <annotation> (fuente TeX interna de KaTeX MathML) y <svg>
        clean_text = re.sub(r'<script[^>]*>.*?</script>', ' ', dom, flags=re.DOTALL)
        clean_text = re.sub(r'<style[^>]*>.*?</style>', ' ', clean_text, flags=re.DOTALL)
        clean_text = re.sub(r'<annotation[^>]*>.*?</annotation>', ' ', clean_text, flags=re.DOTALL)
        clean_text = re.sub(r'<svg[^>]*>.*?</svg>', ' ', clean_text, flags=re.DOTALL)
        clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
        # Decodificar entidades comunes
        clean_text = clean_text.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')

        # Buscar secuencias como \frac, \theta, \vec, \alpha, \cr, \\
        stray_latex = re.findall(r'\\[a-zA-Z]{2,}', clean_text)
        # Buscar barras dobles visibles sueltas
        stray_double_slash = re.findall(r'\\\\', clean_text)

        num_stray = len(stray_latex) + len(stray_double_slash)

        # Validaciones
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
            for err in katex_errors[:3]:
                print(f"       -> Error KaTeX: {err}")
        else:
            print(f"[OK]   {mod:5s}: 0 errores | {num_formulas:3d} fórmulas renderizadas (reveal=all)")

    return all_ok

def main():
    parser = argparse.ArgumentParser(description="Verificador automatizado de KaTeX en navegador")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8080")), help="Puerto del servidor local")
    parser.add_argument("--host", default=os.environ.get("HOST", "localhost"), help="Host del servidor local")
    parser.add_argument("--browser", default=None, help="Ruta al binario del navegador")
    args = parser.parse_args()

    browser = args.browser or find_browser()
    if not browser:
        print("[ERROR] No se encontró ningún navegador compatible (Chrome/Chromium/Edge) en el sistema.")
        print("        Define la variable de entorno CHROME_BIN o pasa el argumento --browser <ruta>.")
        sys.exit(1)

    print("=" * 70)
    print("VERIFICANDO RENDERIZADO DE KATEX EN NAVEGADOR (MODO REVEAL=ALL)")
    print("=" * 70)

    ok = check_with_chrome_cli(browser, args.host, args.port)
    if ok:
        print("\n[ÉXITO] Todos los 12 módulos cargan y renderizan 100% de las fórmulas sin errores ni barras sueltas.")
        sys.exit(0)
    else:
        print("\n[ERROR] Se detectaron módulos con fallos en el renderizado matemático.")
        sys.exit(1)

if __name__ == "__main__":
    main()
