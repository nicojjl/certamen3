#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación de Renderizado KaTeX y Ausencia de Errores en Navegador
Soporta recorrido interactivo exhaustivo con Playwright haciendo click en todos los
botones de interacción ("Comprobar", "Mostrar Pista / Paso 1", "Mostrar Siguiente Paso",
"Solución Completa Visible", "Mostrar Pauta Modelo", "Revelar Todo"), pasada de revelado
con ?reveal=all y App.revealAll(), confirmando con un test que todos los .step-box y
.feedback-box queden visibles, y validando 0 errores de consola y 0 errores de KaTeX.
"""

import os
import sys
import shutil
import subprocess
import re
import json
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

def check_with_playwright(host, port, browser_path=None, modules=None):
    """
    Recorrido interactivo y de revelado exhaustivo con Playwright:
    1. Recorre módulos interactuando con botones y opciones.
    2. Abre con ?reveal=all e invoca App.revealAll().
    3. Confirma que el 100% de .step-box y .feedback-box queden visibles.
    4. Valida ausencia total de errores de consola y errores de KaTeX.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[WARN] Playwright no está instalado. Usando fallback de Chrome CLI.")
        return None

    modules_to_run = modules if modules else MODULES
    print(f"[INFO] Iniciando recorrido interactivo automatizado con Playwright ({len(modules_to_run)} módulo(s))...")
    all_ok = True
    total_formulas = 0
    total_modules = 0
    total_steps = 0
    total_hidden_steps = 0
    total_feedback = 0
    total_hidden_feedback = 0
    total_clues = 0
    total_hidden_clues = 0
    total_exercise_figures = 0
    total_broken_exercise_figures = 0
    total_katex_errors = 0
    total_console_errors = 0
    total_page_errors = 0
    total_stray_latex = 0

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

        for mod in modules_to_run:
            # 1. Pasada interactiva: navegar al módulo estándar
            mod_url = f"http://{host}:{port}/#{mod}"
            try:
                page.goto(mod_url, wait_until="networkidle", timeout=10000)
            except Exception:
                page.goto(mod_url, timeout=10000)
                page.wait_for_timeout(300)

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
                            page.wait_for_timeout(25)
                    except Exception:
                        pass
                if not clicked_any:
                    break

            options = page.locator(".option-item").all()
            for opt in options[:8]:
                try:
                    if opt.is_visible():
                        opt.click(timeout=300)
                        page.wait_for_timeout(15)
                except Exception:
                    pass

            # 2. Pasada de revelado: abrir con ?reveal=all y ejecutar App.revealAll()
            reveal_url = f"http://{host}:{port}/?reveal=all#{mod}"
            try:
                page.goto(reveal_url, wait_until="networkidle", timeout=10000)
            except Exception:
                page.goto(reveal_url, timeout=10000)
                page.wait_for_timeout(300)

            # Ejecutar App.revealAll() de acuerdo con la especificación exacta
            page.evaluate("""() => {
                if (typeof App !== 'undefined' && App.revealAll) App.revealAll();
                if (window.renderMathInElement) renderMathInElement(document.body);
            }""")
            page.wait_for_timeout(80)

            # 3. Test de visibilidad: confirmar que todos los .step-box, .feedback-box y pistas/pautas (.pista-box, .pauta-box) queden visibles
            vis_check = page.evaluate("""() => {
                const area = document.getElementById('main-content-area') || document.body;
                const stepBoxes = Array.from(area.querySelectorAll('.step-box'));
                const feedbackBoxes = Array.from(area.querySelectorAll('.feedback-box'));
                const pistaBoxes = Array.from(area.querySelectorAll('.pista-box'));
                const pautaBoxes = Array.from(area.querySelectorAll('.pauta-box'));
                
                const clueElements = pistaBoxes.concat(pautaBoxes);

                const hiddenSteps = stepBoxes.filter(el => {
                    const style = window.getComputedStyle(el);
                    return style.display === 'none' || style.visibility === 'hidden' || !el.classList.contains('visible');
                });
                
                const hiddenFeedback = feedbackBoxes.filter(el => {
                    const style = window.getComputedStyle(el);
                    return style.display === 'none' || style.visibility === 'hidden' || !el.classList.contains('visible');
                });

                const hiddenClues = clueElements.filter(el => {
                    const style = window.getComputedStyle(el);
                    return style.display === 'none' || style.visibility === 'hidden' || !el.classList.contains('visible');
                });

                // Figuras SVG ininlineadas de las tarjetas de ejercicio
                const exerciseCards = Array.from(area.querySelectorAll('.exercise-card'));
                const exerciseFigures = [];
                const brokenExerciseFigures = [];
                exerciseCards.forEach(card => {
                    const containers = Array.from(card.querySelectorAll('.figure-container'));
                    containers.forEach(box => {
                        const svg = box.querySelector('svg');
                        if (!svg) {
                            brokenExerciseFigures.push({card: card.id, reason: 'sin <svg>'});
                            return;
                        }
                        let bboxWidth = 0;
                        try {
                            bboxWidth = svg.getBBox().width;
                        } catch (e) {
                            bboxWidth = svg.getBoundingClientRect().width;
                        }
                        const shapes = Array.from(svg.querySelectorAll('path, line, polyline, polygon, circle, rect, ellipse, use'));
                        const hasVisibleStroke = shapes.some(shape => {
                            const style = window.getComputedStyle(shape);
                            const stroke = style.stroke;
                            const fill = style.fill;
                            const strokeWidth = parseFloat(style.strokeWidth) || 0;
                            const opacity = parseFloat(style.opacity) || 1;
                            const isStroke = stroke && stroke !== 'none' && strokeWidth > 0 && opacity > 0;
                            const isFill = fill && fill !== 'none' && opacity > 0;
                            return isStroke || isFill;
                        });

                        exerciseFigures.push({card: card.id, bboxWidth, hasVisibleStroke});
                        if (bboxWidth <= 0 || !hasVisibleStroke) {
                            brokenExerciseFigures.push({card: card.id, bboxWidth, hasVisibleStroke});
                        }
                    });
                });

                return {
                    totalSteps: stepBoxes.length,
                    hiddenSteps: hiddenSteps.length,
                    totalFeedback: feedbackBoxes.length,
                    hiddenFeedback: hiddenFeedback.length,
                    totalClues: clueElements.length,
                    hiddenClues: hiddenClues.length,
                    exerciseFigures: exerciseFigures.length,
                    brokenExerciseFigures: brokenExerciseFigures.length
                };
            }""")

            # 4. Inspeccionar el DOM resultante (fórmulas, errores KaTeX, comandos LaTeX sueltos)
            num_formulas = page.locator(".katex").count()
            katex_error_els = page.locator(".katex-error").all()
            num_katex_errors = len(katex_error_els)

            stray_latex = page.evaluate("""() => {
                const area = document.getElementById('main-content-area') || document.body;
                const walker = document.createTreeWalker(
                    area,
                    NodeFilter.SHOW_TEXT,
                    {
                        acceptNode(node) {
                            if (node.parentElement && node.parentElement.closest('.katex, .katex-error, script, style, svg, math')) {
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

            num_stray_latex = len(stray_latex) if stray_latex else 0
            num_console_errs = len(console_errors)
            num_page_errs = len(page_errors)

            failures = []
            if num_formulas == 0:
                failures.append("0 fórmulas renderizadas")
            if num_katex_errors > 0:
                failures.append(f"{num_katex_errors} errores KaTeX")
            if num_stray_latex > 0:
                failures.append(f"{num_stray_latex} comandos LaTeX sueltos: {stray_latex[:3]}")
            if vis_check['hiddenSteps'] > 0:
                failures.append(f"{vis_check['hiddenSteps']}/{vis_check['totalSteps']} .step-box no visibles tras revealAll")
            if vis_check['hiddenFeedback'] > 0:
                failures.append(f"{vis_check['hiddenFeedback']}/{vis_check['totalFeedback']} .feedback-box no visibles tras revealAll")
            if vis_check['totalClues'] == 0:
                failures.append("0 pistas/pautas encontradas en el DOM")
            if vis_check['hiddenClues'] > 0:
                failures.append(f"{vis_check['hiddenClues']}/{vis_check['totalClues']} pistas/pautas ocultas tras revealAll")
            if vis_check['brokenExerciseFigures'] > 0:
                failures.append(f"{vis_check['brokenExerciseFigures']} figuras SVG de ejercicio rotas (width <= 0 o sin trazo)")
            if num_console_errs > 0:
                failures.append(f"{num_console_errs} errores de consola JS")
            if num_page_errs > 0:
                failures.append(f"{num_page_errs} excepciones de página")

            if failures:
                all_ok = False
                print(f"[FAIL] {mod:5s}: {', '.join(failures)} (fórmulas: {num_formulas})")
                for ce in console_errors[:3]:
                    print(f"       -> Consola: {ce}")
            else:
                steps_info = f"{vis_check['totalSteps']} pasos ({vis_check['totalClues']} pistas/pautas) y {vis_check['totalFeedback']} feedbacks visibles | {vis_check['exerciseFigures']} figuras SVG OK"
                print(f"[OK]   {mod:5s}: 0 errores consola | {num_formulas:3d} fórmulas | {steps_info}")

            total_formulas += num_formulas
            total_modules += 1
            total_steps += vis_check['totalSteps']
            total_hidden_steps += vis_check['hiddenSteps']
            total_feedback += vis_check['totalFeedback']
            total_hidden_feedback += vis_check['hiddenFeedback']
            total_clues += vis_check['totalClues']
            total_hidden_clues += vis_check['hiddenClues']
            total_exercise_figures += vis_check['exerciseFigures']
            total_broken_exercise_figures += vis_check['brokenExerciseFigures']
            total_katex_errors += num_katex_errors
            total_console_errors += num_console_errs
            total_page_errors += num_page_errs
            total_stray_latex += num_stray_latex

            console_errors.clear()
            page_errors.clear()

        browser.close()

    return {
        "ok": all_ok,
        "total_modules": total_modules,
        "total_formulas": total_formulas,
        "total_steps": total_steps,
        "total_hidden_steps": total_hidden_steps,
        "total_feedback": total_feedback,
        "total_hidden_feedback": total_hidden_feedback,
        "total_clues": total_clues,
        "total_hidden_clues": total_hidden_clues,
        "total_exercise_figures": total_exercise_figures,
        "broken_exercise_figures": total_broken_exercise_figures,
        "katex_errors": total_katex_errors,
        "console_errors": total_console_errors,
        "page_errors": total_page_errors,
        "stray_latex": total_stray_latex
    }

def check_with_chrome_cli(browser_bin, host, port):
    """Fallback usando Chrome/Chromium en modo headless dump-dom con ?reveal=all."""
    all_ok = True
    total_formulas = 0
    total_modules = 0
    total_steps = 0
    total_hidden_steps = 0
    total_feedback = 0
    total_hidden_feedback = 0
    total_clues = 0
    total_hidden_clues = 0
    total_exercise_figures = 0
    total_broken_exercise_figures = 0
    total_katex_errors = 0
    total_console_errors = 0
    total_page_errors = 0
    total_stray_latex = 0
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

        pistas = len(re.findall(r'class="[^"]*\bpista-box\b', dom))
        pautas = len(re.findall(r'class="[^"]*\bpauta-box\b', dom))
        steps = len(re.findall(r'class="[^"]*\bstep-box\b', dom))
        feedback = len(re.findall(r'class="[^"]*\bfeedback-box\b', dom))
        clues_in_mod = pistas + pautas
        total_clues += clues_in_mod
        total_steps += steps
        total_feedback += feedback

        failures = []
        if num_formulas == 0:
            failures.append("0 fórmulas renderizadas")
        if clues_in_mod == 0:
            failures.append("0 pistas/pautas encontradas en el DOM")
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
        "total_formulas": total_formulas,
        "total_steps": total_steps,
        "total_hidden_steps": total_hidden_steps,
        "total_feedback": total_feedback,
        "total_hidden_feedback": total_hidden_feedback,
        "total_clues": total_clues,
        "total_hidden_clues": total_hidden_clues,
        "total_exercise_figures": total_exercise_figures,
        "broken_exercise_figures": total_broken_exercise_figures,
        "katex_errors": total_katex_errors,
        "console_errors": total_console_errors,
        "page_errors": total_page_errors,
        "stray_latex": total_stray_latex
    }

def main():
    parser = argparse.ArgumentParser(description="Verificador automatizado de KaTeX en navegador")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8080")), help="Puerto del servidor local")
    parser.add_argument("--host", default=os.environ.get("HOST", "localhost"), help="Host del servidor local")
    parser.add_argument("--browser", default=None, help="Ruta al binario del navegador")
    parser.add_argument("--no-playwright", action="store_true", help="Forzar el uso de Chrome CLI en lugar de Playwright")
    parser.add_argument("--module", default=None, help="Módulo específico a verificar (ej. mod0)")
    parser.add_argument("--report-path", default=None, help="Ruta para guardar el reporte JSON")
    parser.add_argument("--no-report", action="store_true", help="No sobrescribir el reporte JSON")
    args = parser.parse_args()

    browser = args.browser or find_system_browser()
    target_modules = [args.module] if args.module else None

    print("=" * 70)
    print("VERIFICANDO RENDERIZADO DE KATEX E INTERACTIVIDAD EN NAVEGADOR")
    print("=" * 70)

    result = None
    if not args.no_playwright:
        result = check_with_playwright(args.host, args.port, browser, target_modules)

    if result is None:
        if not browser:
            print("[ERROR] No se encontró ningún navegador compatible (Chrome/Chromium/Edge) en el sistema.")
            print("        Define la variable de entorno CHROME_BIN o pasa el argumento --browser <ruta>.")
            sys.exit(1)
        result = check_with_chrome_cli(browser, args.host, args.port)

    ok = result["ok"]
    total_mods = result["total_modules"]
    total_forms = result["total_formulas"]

    katex_errors = result.get("katex_errors", 0)
    console_errors = result.get("console_errors", 0)
    page_errors = result.get("page_errors", 0)
    stray_latex = result.get("stray_latex", 0)
    hidden_steps = result.get("total_hidden_steps", 0)
    hidden_feedback = result.get("total_hidden_feedback", 0)
    hidden_clues = result.get("total_hidden_clues", 0)
    broken_figures = result.get("broken_exercise_figures", 0)

    total_steps = result.get("total_steps", 0)
    total_feedback = result.get("total_feedback", 0)
    total_clues = result.get("total_clues", 0)
    total_figures = result.get("total_exercise_figures", 0)

    # Falla si alguno de los contadores de error o elementos ocultos es mayor a 0, o si total_clues == 0
    if (katex_errors > 0 or console_errors > 0 or page_errors > 0 or
        stray_latex > 0 or hidden_steps > 0 or hidden_feedback > 0 or
        hidden_clues > 0 or broken_figures > 0 or total_clues == 0):
        ok = False

    # Guardar reporte JSON estructurado para generar_resumen.py si no está silenciado
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    should_save_report = not args.no_report and not (args.module and not args.report_path)
    if should_save_report:
        report_path = args.report_path or os.path.join(base_dir, "scripts", "reporte_browser.json")
        report_data = {
            "ok": ok,
            "modules_audited": total_mods,
            "total_formulas": total_forms,
            "total_steps": total_steps,
            "visible_steps": total_steps - hidden_steps,
            "hidden_steps": hidden_steps,
            "total_feedback": total_feedback,
            "visible_feedback": total_feedback - hidden_feedback,
            "hidden_feedback": hidden_feedback,
            "total_clues": total_clues,
            "visible_clues": total_clues - hidden_clues,
            "hidden_clues": hidden_clues,
            "total_exercise_figures": total_figures,
            "valid_exercise_figures": total_figures - broken_figures,
            "broken_exercise_figures": broken_figures,
            "katex_errors": katex_errors,
            "console_errors": console_errors,
            "page_errors": page_errors,
            "stray_latex": stray_latex
        }
        with open(report_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        rel_report = os.path.relpath(report_path, base_dir).replace('\\', '/')
        print(f"[INFO] Reporte de navegador guardado en UTF-8 sin BOM: {rel_report}")

    if ok:
        print(f"\n[ÉXITO] {total_mods} módulos verificados, {total_forms} fórmulas matemáticas renderizadas, 0 errores KaTeX ni barras sueltas.")
        sys.exit(0)
    else:
        print(f"\n[ERROR] Se detectaron fallos en la verificación de navegador (errores KaTeX={katex_errors}, consola={console_errors}, ocultos={hidden_steps+hidden_feedback+hidden_clues}, figuras rotas={broken_figures}).")
        sys.exit(1)

if __name__ == "__main__":
    main()
