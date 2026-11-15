# FIS120 / FIS12125 · Certamen 3 · Estudio Interactivo (2026-2)
**Universidad Técnica Federico Santa María (UTFSM)**

Plataforma web de estudio interactiva, estática y ultra-minimalista, orientada a preparar a los estudiantes de física general para el **Certamen 3 de Electricidad y Magnetismo** (semestre 2026-2). Basada en el formulario oficial, ayudantías 9, 10 y 11, simulacros y pautas de certámenes anteriores.

---

## 🚀 Demo en Vivo (GitHub Pages)
Una vez activado GitHub Pages en la rama `main` (directorio raíz `/`), el sitio está disponible en:
👉 **[https://nicojjl.github.io/certamen3/](https://nicojjl.github.io/certamen3/)**

---

## 🛠️ Stack Tecnológico
- **Frontend puro**: HTML5 semántico, CSS3 modular (con variables nativas para temas claro/oscuro) y JavaScript Vanilla (ES6+).
- **Cero dependencias pesadas ni bundlers**: No requiere Node.js, Webpack, Vite ni compilación. 100% estático.
- **Tipografía Matemática**: [KaTeX](https://katex.org/) (v0.16.9 vía CDN) y tipografía tipo LaTeX (*Computer Modern Serif* / *Latin Modern Roman*).
- **Figuras Vectoriales**: Diagramas SVG limpios en `/img`, generados mediante scripts de Python (`/scripts/generate_figures.py`).
- **Persistencia**: `localStorage` guarda automáticamente el tema elegido (claro/oscuro), estado de ejercicios resueltos y módulos completados.

---

## 📁 Estructura del Repositorio
```text
fis120-certamen3/
├── index.html                 # Contenedor SPA con header, drawer de formulario y navegación
├── README.md                  # Documentación del proyecto
├── NOTAS_REVISION.md          # Bitácora de resoluciones físicas, límites y verificación
├── css/
│   └── style.css              # Variables de tema (light/dark), diseño editorial tipo LaTeX (~740px)
├── js/
│   ├── app.js                 # Router, control de tema, apertura de formulario, KaTeX re-render
│   ├── components.js          # Renderizadores de preguntas (alternativas, numéricas, V/F, paso a paso)
│   ├── interactive.js         # Widgets canvas interactivos (perfil B(r), transientes RC/RL, regímenes RLC)
│   └── data/                  # Datos pedagógicos desacoplados por módulo
│       ├── module0.js         # Repaso matemático, vectores, cilíndricas y unidades
│       ├── module1.js         # Biot-Savart, cables finitos/infinitos, arcos
│       ├── module2.js         # Densidad de corriente J(r)
│       ├── module3.js         # Ley de Ampère, cables coaxiales, toroide y solenoide
│       ├── module4.js         # Flujo magnético y Faraday-Lenz
│       ├── module5.js         # fem de movimiento y varilla en rieles con gravedad
│       ├── module6.js         # Inductancia mutua y transformadores
│       ├── module7.js         # Autoinductancia y energía magnética
│       ├── module8.js         # Circuitos transientes RC y RL
│       ├── module9.js         # Circuitos oscilantes LC y RLC
│       ├── module10.js        # Ecuaciones de Maxwell y síntesis conceptual
│       └── module11.js        # Simulacro final completo cronometrado
├── img/                       # Diagramas vectoriales SVG
├── scripts/
│   └── generate_figures.py    # Generador de figuras matplotlib/SVG
└── referencias/               # PDFs oficiales de base (Formulario, Ayudantías, Pauta, Simulacro)
```

---

## 💻 Cómo Correrlo en Local
Al ser un proyecto estático, puedes visualizarlo de varias formas sencillas:

### Opción A (Python - Recomendada):
Desde la carpeta raíz del proyecto, ejecuta:
```bash
python -m http.server 8000
```
Luego abre tu navegador en: `http://localhost:8000`

### Opción B (VS Code Live Server):
Si usas VS Code o Antigravity IDE, haz clic derecho en `index.html` y selecciona **"Open with Live Server"**.

### Opción C (Doble clic):
Puedes abrir `index.html` directamente en tu navegador favorito. Para habilitar la carga completa de módulos vía script sin restricciones CORS de `file://`, se recomienda la Opción A o B.

---

## ➕ Cómo Agregar un Módulo o Ejercicio Nuevo

### Para agregar un ejercicio a un módulo existente:
1. Abre el archivo de datos correspondiente en `js/data/moduleX.js`.
2. En la lista `exercises: [ ... ]`, añade un nuevo objeto con la siguiente estructura según el tipo:

#### 1. Alternativas (`multiple_choice`):
```javascript
{
  id: 'm1_ex9',
  title: 'Título del ejercicio',
  level: 'basic' | 'intermediate' | 'certamen',
  source: 'Ayudantía / Control',
  type: 'multiple_choice',
  statement: 'Enunciado en texto o $LaTeX$...',
  options: [
    'Opción A',
    'Opción B',
    'Opción C',
    'Opción D'
  ],
  correctOption: 1, // Índice (0 a 3)
  explanation: 'Explicación detallada con fórmulas en LaTeX...'
}
```

#### 2. Respuesta Numérica con Tolerancia (`numerical`):
```javascript
{
  id: 'm2_ex7',
  title: 'Cálculo de Corriente Total',
  level: 'intermediate',
  type: 'numerical',
  statement: 'Calcule el valor de...',
  placeholder: 'Ej: 3.14',
  units: 'A',
  correctValue: 3.1416,
  tolerance: 0.03, // ±3% de tolerancia relativa
  explanation: 'Desarrollo de la integral...'
}
```

#### 3. Problema Completo Revelable Paso a Paso (`step_by_step`):
```javascript
{
  id: 'm3_ex_pauta',
  title: 'Cable Coaxial Escalonado',
  level: 'certamen',
  type: 'step_by_step',
  figure: 'img/nombre_figura.svg',
  statement: 'Enunciado del problema de certamen...',
  steps: [
    { title: 'Paso 1: Simetría y Lazo Amperiano', content: '...' },
    { title: 'Paso 2: Corriente Encerrada', content: '...' },
    { title: 'Paso 3: Campo y Casos Límite', content: '...' }
  ]
}
```

### Para regenerar las figuras SVG:
```bash
python scripts/generate_figures.py
```
