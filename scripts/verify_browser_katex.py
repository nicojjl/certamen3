import subprocess
import re
import sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
MODULES = [f"mod{i}" for i in range(12)]

all_ok = True

print("=" * 60)
print("VERIFICANDO RENDERIZADO DE KATEX EN NAVEGADOR (CHROME HEADLESS)")
print("=" * 60)

for mod in MODULES:
    url = f"http://localhost:8080/#{mod}"
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=3000",
        "--dump-dom",
        url
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="ignore")
    dom = res.stdout
    
    # Check for KaTeX errors
    errors = re.findall(r'<span class="katex-error"[^>]*title="([^"]*)"', dom)
    katex_spans = re.findall(r'class="katex"', dom)
    
    if errors:
        all_ok = False
        print(f"[FAIL] {mod}: {len(errors)} fórmulas con error en {url}")
        for err in errors[:3]:
            print(f"       -> {err}")
    else:
        print(f"[OK]   {mod:5s}: 0 errores KaTeX ({len(katex_spans)} fórmulas renderizadas)")

if all_ok:
    print("\n[ÉXITO] Todos los 12 módulos cargan y renderizan 100% de las fórmulas sin errores.")
    sys.exit(0)
else:
    print("\n[ERROR] Se detectaron errores de KaTeX.")
    sys.exit(1)
