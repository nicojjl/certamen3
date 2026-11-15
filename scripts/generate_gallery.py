#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Generador de la Galería de Control de Calidad de Figuras (img/galeria.html)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'img')
GALERIA_PATH = os.path.join(IMG_DIR, 'galeria.html')

FIGURES = [
    # Grupo 1 (Módulos 0-2)
    {
        "id": "mod0_coords",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Coordenadas Cilíndricas y Versores Canónicos",
        "source": "Módulo 0 Teoría (Repaso Vectorial)",
        "file": "mod0_coords.svg",
        "desc": "Punto P(r, θ, z), versores r̂, θ̂, k̂ y relaciones algebraicas de producto cruz."
    },
    {
        "id": "mod0_cross_product",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Producto Cruz y Regla de la Mano Derecha",
        "source": "Módulo 0 Teoría (Repaso Vectorial)",
        "file": "mod0_cross_product.svg",
        "desc": "Vectores A, B, ángulo θ y vector ortogonal C = A × B."
    },
    {
        "id": "mod1_wire_bfield",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Campo Magnético de Cable Infinito y Circulación Azimutal",
        "source": "Módulo 1 Teoría (Biot-Savart)",
        "file": "mod1_wire_bfield.svg",
        "desc": "Líneas de campo concéntricas, vector B(r) = (μ₀I / 2πr)θ̂ y regla de la mano derecha."
    },
    {
        "id": "mod1_sim2_geometry",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Superposición: Arco Circular y Segmento Finito Paralelo a z",
        "source": "Módulo 1 Ejercicio 6 (Ejercicio original no oficial)",
        "file": "mod1_sim2_geometry.svg",
        "desc": "Arco de radio R en plano xy (4to cuadrante) y segmento rectilíneo de longitud 4R en x=2R."
    },
    {
        "id": "mod2_j_profiles",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Perfiles de Densidad de Corriente J(r)",
        "source": "Módulo 2 Teoría (Densidad de Corriente)",
        "file": "mod2_j_profiles.svg",
        "desc": "Comparación de perfiles: Uniforme (J₀), Parabólico 2J₀(1 - r²/a²) y Escalonado (J₀ y 3J₀)."
    },
    {
        "id": "mod2_coaxial_stepped",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Efecto Pelicular Escalonado: Secciones r ≤ R/2 y R/2 < r ≤ R",
        "source": "Pauta C3 2026-1 Problema 1 / Módulo 2 Ex 6 / Módulo 3 Ex 6",
        "file": "mod2_coaxial_stepped.svg",
        "desc": "Cilindro con densidad escalonada J₀ y 3J₀, radios R/2 y R, corriente saliente ⊙."
    },
    {
        "id": "mod2_ayud9_p1_coaxial",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Cable Coaxial Asimétrico (Radios R, 2R, 4R)",
        "source": "Ayudantía 9 Problema 1 / Módulo 2 Ex 4 / Módulo 3 Ex 4",
        "file": "mod2_ayud9_p1_coaxial.svg",
        "desc": "Núcleo interior J₁ = J₀k̂ (⊙), aislante intermedio y cascarón exterior J₂ = 2J₀(-k̂) (⊗)."
    },
    {
        "id": "mod2_ayud9_p3_superposicion",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Superposición Fuera de Eje: Cilindro Desplazado y Cable Infinito",
        "source": "Ayudantía 9 Problema 3 / Módulo 2 Ex 5",
        "file": "mod2_ayud9_p3_superposicion.svg",
        "desc": "Cilindro macizo en (-a, 0) con J = βr' y cable infinito en (a, -a) con punto de observación en el origen O."
    },
    {
        "id": "mod2_ayud9_p4_angular",
        "group": "Módulos 0–2: Fundamentos y Fuentes de Campo",
        "title": "Densidad con Dependencia Angular J₁(θ) = α sin²θ k̂ y Cascarón",
        "source": "Ayudantía 9 Problema 4 / Módulo 2 Ex 7",
        "file": "mod2_ayud9_p4_angular.svg",
        "desc": "Cilindro interior R₁ con variación angular y cascarón exterior R₂ con densidad uniforme J₀(⊗)."
    },

    # Grupo 2 (Módulos 3-5)
    {
        "id": "mod3_toroid_simulacro",
        "group": "Módulos 3–5: Ampère, Faraday y fem de Movimiento",
        "title": "Toroide Ideal Rectangular (Vista Superior y Corte Transversal rz)",
        "source": "Simulacro C3 Problema 1 / Módulo 3 Ex 7 / Módulo 7 Ex 5 / Módulo 11 P1",
        "file": "mod3_toroid_simulacro.svg",
        "desc": "Radios a y b, altura h, N espiras, campo azimutal B y cable axial morado con corriente Ic."
    },
    {
        "id": "mod4_faraday_moving_loop",
        "group": "Módulos 3–5: Ampère, Faraday y fem de Movimiento",
        "title": "Espira Rectangular Alejándose de Cable Recto Infinito",
        "source": "Simulacro C3 Problema 2 / Módulo 4 Ex 7 / Módulo 11 P2",
        "file": "mod4_faraday_moving_loop.svg",
        "desc": "Cable infinito en eje y con corriente I, espira de lados a × b con velocidad v y distancia d(t)."
    },
    {
        "id": "mod4_ayud10_p1_rotating",
        "group": "Módulos 3–5: Ampère, Faraday y fem de Movimiento",
        "title": "Espira Cuadrada en Campo Magnético Rotatorio",
        "source": "Ayudantía 10 Problema 1 / Módulo 4 Ex 5",
        "file": "mod4_ayud10_p1_rotating.svg",
        "desc": "Espira de lado a en plano xy y campo B con ángulo de elevación variable ϕ(t) = k + ωt."
    },
    {
        "id": "mod4_ayud10_p2_concentric",
        "group": "Módulos 3–5: Ampère, Faraday y fem de Movimiento",
        "title": "Espira Circular con Espira Cuadrada Concéntrica en su Centro",
        "source": "Ayudantía 10 Problema 2 / Módulo 4 Ex 6",
        "file": "mod4_ayud10_p2_concentric.svg",
        "desc": "Espira circular de radio R con corriente I(t) y pequeña espira cuadrada central de lado a << R."
    },
    {
        "id": "mod4_ayud11_p3_spacetime",
        "group": "Módulos 3–5: Ampère, Faraday y fem de Movimiento",
        "title": "Rectángulo Conductor en Campo Espacial y Temporal B(y,t) con ⊙",
        "source": "Ayudantía 11 Problema 3 / Módulo 4 Ex 8",
        "file": "mod4_ayud11_p3_spacetime.svg",
        "desc": "Campo B(y,t) = αy² e^(-βt) k̂ sobre rectángulo H × L con lado inferior ubicado en y = C."
    },
    {
        "id": "mod5_motional_emf_rails",
        "group": "Módulos 3–5: Ampère, Faraday y fem de Movimiento",
        "title": "Varilla Conductora en Rieles Verticales con Gravedad y Campo Entrante",
        "source": "Ayudantía 10 Problema 3 / Módulo 5 Teoría y Ex 5",
        "file": "mod5_motional_emf_rails.svg",
        "desc": "Rieles verticales separados distancia L, varilla de masa m cayendo bajo gravedad g, campo B entrante ⊗."
    },
    {
        "id": "mod5_ayud10_p4_carrito",
        "group": "Módulos 3–5: Ampère, Faraday y fem de Movimiento",
        "title": "Carrito Conductor Ingresando a Región con Campo Magnético Uniforme",
        "source": "Ayudantía 10 Problema 4 / Módulo 5 Ex 6",
        "file": "mod5_ayud10_p4_carrito.svg",
        "desc": "Carrito de masa m, ancho a, largo w y velocidad inicial v₀ ingresando a zona con B₀k̂ (⊙)."
    },

    # Grupo 3 (Módulos 6-8)
    {
        "id": "mod6_mutual_solenoid_square",
        "group": "Módulos 6–8: Inductancia Mutua, Autoinductancia y Transientes",
        "title": "Solenoide Coaxial con Bobina Cuadrada Exterior",
        "source": "Simulacro C3 Problema 3 / Módulo 6 Teoría y Ex 7 / Módulo 11 P3",
        "file": "mod6_mutual_solenoid_square.svg",
        "desc": "Solenoide ideal de radio a rodeado por bobina cuadrada coaxial de N espiras y lado L > 2a."
    },
    {
        "id": "mod6_ayud11_p1_solenoids",
        "group": "Módulos 6–8: Inductancia Mutua, Autoinductancia y Transientes",
        "title": "Dos Solenoides Concéntricos Ideales Muy Largos (R y 3R)",
        "source": "Ayudantía 11 Problema 1 / Módulo 6 Ex 5",
        "file": "mod6_ayud11_p1_solenoids.svg",
        "desc": "Bobina interior de radio R y Ni vueltas con corriente I(t), bobina exterior de radio 3R y Ne vueltas."
    },
    {
        "id": "mod6_ayud11_p2_wire_rect",
        "group": "Módulos 6–8: Inductancia Mutua, Autoinductancia y Transientes",
        "title": "Alambre Infinito con Corriente Exponencial y Rectángulo Conductor",
        "source": "Ayudantía 11 Problema 2 / Módulo 6 Ex 6",
        "file": "mod6_ayud11_p2_wire_rect.svg",
        "desc": "Cable sobre eje y con I(t) = I₀ e^(-t/τ) y espira rectangular de lados a × b a distancia a del cable."
    },
    {
        "id": "mod6_solenoid_tilted_loop",
        "group": "Módulos 6–8: Inductancia Mutua, Autoinductancia y Transientes",
        "title": "Bobina Larga con Espira Inclinada en Ángulo α",
        "source": "Ayudantía 11 Problema 4 / Módulo 6 Ex 7b",
        "file": "mod6_solenoid_tilted_loop.svg",
        "desc": "Solenoide de radio a y espira circular de radio b inclinada ángulo α entre eje longitudinal y plano de la espira."
    },
    {
        "id": "mod6_pauta_p2_rollo",
        "group": "Módulos 6–8: Inductancia Mutua, Autoinductancia y Transientes",
        "title": "Rollo Plano Circular con Pequeña Espira Concéntrica Central",
        "source": "Pauta C3 2026-1 Problema 2 / Módulo 6 Ex 7c",
        "file": "mod6_pauta_p2_rollo.svg",
        "desc": "Rollo plano de N vueltas de radio R sobre una mesa con pequeña espira circular concéntrica de radio r << R."
    },
    {
        "id": "mod6_transformador",
        "group": "Módulos 6–8: Inductancia Mutua, Autoinductancia y Transientes",
        "title": "Transformador Ideal con Núcleo Ferromagnético Cerrado",
        "source": "Ayudantía 11 Conceptual 1 / Módulo 6 Ex 8",
        "file": "mod6_transformador.svg",
        "desc": "Núcleo ferromagnético toroidal cuadrado, devanado primario Np y devanado secundario Ns."
    },
    {
        "id": "mod8_switch_circuit",
        "group": "Módulos 6–8: Inductancia Mutua, Autoinductancia y Transientes",
        "title": "Circuito Transiente con Interruptor de 2 Posiciones (R, C, L, ε)",
        "source": "Pauta C3 2026-1 Problema 3 / Módulo 8 Teoría y Ex 4, 6",
        "file": "mod8_switch_circuit.svg",
        "desc": "Fuente de fem ε, resistencia R, interruptor de 2 posiciones, rama superior con C y rama inferior con L y R."
    },

    # Grupo 4 (Módulos 9-11)
    {
        "id": "mod9_rlc_circuit",
        "group": "Módulos 9–11: Oscilaciones RLC, Maxwell y Síntesis Final",
        "title": "Circuito RLC Serie Oscilante (Régimen Amortiguado)",
        "source": "Formulario C3 Oficial / Módulo 9 Ex 6",
        "file": "mod9_rlc_circuit.svg",
        "desc": "Circuito serie con inductor L, resistencia R, capacitor C, carga q(t) y corriente i(t)."
    },
    {
        "id": "mod10_maxwell_capacitor",
        "group": "Módulos 9–11: Oscilaciones RLC, Maxwell y Síntesis Final",
        "title": "Condensador Circular de Maxwell y Corriente de Desplazamiento",
        "source": "Simulacro C3 Pregunta Conceptual / Módulo 10 Teoría y Ex 5 / Módulo 11 P4",
        "file": "mod10_maxwell_capacitor.svg",
        "desc": "Vistas lateral y frontal: placas circulares radio R, lazo amperiano Γ, disco plano S₁ y bolsa interior S₂."
    }
]

def generate_html():
    cards_by_group = {}
    for fig in FIGURES:
        grp = fig['group']
        if grp not in cards_by_group:
            cards_by_group[grp] = []
        cards_by_group[grp].append(fig)

    groups_html = ""
    for grp_title, items in cards_by_group.items():
        items_html = ""
        for it in items:
            items_html += f"""
        <div class="figure-card">
          <div class="card-header">
            <span class="fig-badge">{it['id']}</span>
            <span class="fig-source">{it['source']}</span>
          </div>
          <h3 class="fig-title">{it['title']}</h3>
          <div class="preview-box">
            <img class="fig-preview" src="{it['file']}" alt="{it['title']}" loading="lazy">
          </div>
          <p class="fig-desc">{it['desc']}</p>
          <div class="card-footer">
            <code>img/{it['file']}</code>
            <a class="view-link" href="{it['file']}" target="_blank">Abrir SVG ↗</a>
          </div>
        </div>
            """
        groups_html += f"""
      <section class="group-section">
        <h2 class="group-title">{grp_title}</h2>
        <div class="figures-grid">
          {items_html}
        </div>
      </section>
        """

    html = f"""<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Galería de Figuras Oficiales · FIS120 Certamen 3 · UTFSM</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/dreampulse/computer-modern-web-font@master/fonts.css">
  <style>
    :root {{
      --bg-primary: #ffffff;
      --bg-secondary: #f8fafc;
      --bg-card: #ffffff;
      --border-color: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --accent: #1e3a8a;
      --accent-light: #eff6ff;
      --fig-azul: #0284c7;
      --fig-rojo: #dc2626;
      --fig-verde: #16a34a;
    }}
    [data-theme="dark"] {{
      --bg-primary: #0f172a;
      --bg-secondary: #1e293b;
      --bg-card: #1e293b;
      --border-color: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #60a5fa;
      --accent-light: #172554;
      --fig-azul: #38bdf8;
      --fig-rojo: #f87171;
      --fig-verde: #4ade80;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Computer Modern Serif', 'Latin Modern Roman', Georgia, serif;
      background: var(--bg-primary);
      color: var(--text-main);
      padding: 2rem 1.5rem;
      line-height: 1.6;
      transition: background 0.2s ease, color 0.2s ease;
    }}
    header {{
      max-width: 1200px;
      margin: 0 auto 2.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 1.2rem;
      flex-wrap: wrap;
      gap: 1rem;
    }}
    .header-info h1 {{ font-size: 1.8rem; font-weight: 700; margin-bottom: 0.3rem; }}
    .header-info p {{ font-size: 0.95rem; color: var(--text-muted); }}
    .theme-toggle {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.55rem 1.1rem;
      border-radius: 4px;
      cursor: pointer;
      font-family: inherit;
      font-size: 0.9rem;
      font-weight: 600;
    }}
    .theme-toggle:hover {{ background: var(--border-color); }}
    main {{ max-width: 1200px; margin: 0 auto; }}
    .group-section {{ margin-bottom: 3.5rem; }}
    .group-title {{
      font-size: 1.35rem;
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-color);
      color: var(--accent);
    }}
    .figures-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.8rem;
    }}
    .figure-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 1.2rem;
      display: flex;
      flex-direction: column;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.6rem;
      font-size: 0.8rem;
    }}
    .fig-badge {{
      background: var(--accent-light);
      color: var(--accent);
      padding: 0.2rem 0.5rem;
      border-radius: 3px;
      font-weight: 700;
      font-family: monospace;
    }}
    .fig-source {{ color: var(--text-muted); font-style: italic; }}
    .fig-title {{ font-size: 1.05rem; margin-bottom: 0.8rem; font-weight: 600; }}
    .preview-box {{
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 4px;
      padding: 1rem;
      min-height: 220px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 0.8rem;
    }}
    .fig-preview {{ max-width: 100%; max-height: 260px; height: auto; display: block; }}
    .fig-desc {{ font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem; flex-grow: 1; }}
    .card-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      border-top: 1px dashed var(--border-color);
      padding-top: 0.6rem;
    }}
    .card-footer code {{ color: var(--text-muted); font-size: 0.8rem; }}
    .view-link {{ color: var(--accent); text-decoration: none; font-weight: 600; }}
    .view-link:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <header>
    <div class="header-info">
      <h1>Galería de Figuras Oficiales TikZ · Certamen 3</h1>
      <p>FIS120 / FIS12125 · UTFSM · Renderizado vectorial nativo con tipografía Computer Modern</p>
    </div>
    <button class="theme-toggle" id="theme-btn" onclick="toggleTheme()">☾ Alternar Modo Oscuro</button>
  </header>

  <main>
    {groups_html}
  </main>

  <script>
    function toggleTheme() {{
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const target = cur === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', target);
      document.getElementById('theme-btn').innerText = target === 'dark' ? '☀ Modo Claro' : '☾ Modo Oscuro';
      // Inline SVGs or trigger currentColor recalculation
      inlineAllSVGs();
    }}

    function inlineAllSVGs() {{
      document.querySelectorAll('.preview-box').forEach(box => {{
        const img = box.querySelector('img');
        if (!img) return;
        const src = img.getAttribute('src');
        if (!src) return;
        fetch(src)
          .then(r => r.text())
          .then(svg => {{
            const div = document.createElement('div');
            div.innerHTML = svg;
            const svgEl = div.querySelector('svg');
            if (svgEl) {{
              svgEl.classList.add('fig-preview');
              img.replaceWith(svgEl);
            }}
          }})
          .catch(() => {{}});
      }});
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (prefersDark) {{
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById('theme-btn').innerText = '☀ Modo Claro';
      }}
      inlineAllSVGs();
    }});
  </script>
</body>
</html>
"""
    with open(GALERIA_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[OK] Galería generada en: {GALERIA_PATH}")

if __name__ == '__main__':
    generate_html()
