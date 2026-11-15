import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.fonttype'] = 'none'
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Output directory
IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'img')
os.makedirs(IMG_DIR, exist_ok=True)

# Common styling helper for theme adaptability
def setup_ax(ax, title=""):
    ax.set_aspect('equal')
    ax.axis('off')
    if title:
        ax.set_title(title, fontsize=12, pad=10, color='#333333', fontfamily='serif')

# -------------------------------------------------------------
# Module 0: Coordinate systems & cross product
# -------------------------------------------------------------
def fig_coords_cylindrical():
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    setup_ax(ax)
    
    # Axes
    ax.annotate('', xy=(3, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5, color='#444'))
    ax.annotate('', xy=(0, 3.2), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5, color='#444'))
    ax.annotate('', xy=(-1.8, -1.8), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5, color='#444'))
    ax.text(3.1, 0, r'$y$', fontsize=12, va='center', fontfamily='serif')
    ax.text(0, 3.3, r'$z$', fontsize=12, ha='center', fontfamily='serif')
    ax.text(-2.0, -2.0, r'$x$', fontsize=12, ha='center', fontfamily='serif')
    
    # Point P(r, theta, z)
    px, py, pz = 1.8, 1.2, 2.0
    # Projection on xy-plane
    ax.plot([0, px], [0, py], 'k--', lw=1.2, color='#1976d2')
    ax.plot([px, px], [py, py + pz], 'k--', lw=1.2, color='#388e3c')
    ax.scatter([px], [py + pz], color='#d32f2f', s=45, zorder=5)
    ax.text(px + 0.1, py + pz + 0.1, r'$P(r, \theta, z)$', fontsize=11, color='#d32f2f', fontfamily='serif', fontweight='bold')
    
    # Unit vectors
    ax.annotate('', xy=(px + 0.8, py + 0.53), xytext=(px, py), arrowprops=dict(arrowstyle="->", lw=1.5, color='#1976d2'))
    ax.text(px + 0.9, py + 0.5, r'$\hat{r}$', fontsize=11, color='#1976d2', fontfamily='serif')
    
    ax.annotate('', xy=(px - 0.5, py + 0.75), xytext=(px, py), arrowprops=dict(arrowstyle="->", lw=1.5, color='#e65100'))
    ax.text(px - 0.7, py + 0.8, r'$\hat{\theta}$', fontsize=11, color='#e65100', fontfamily='serif')
    
    ax.annotate('', xy=(px, py + pz + 0.8), xytext=(px, py + pz), arrowprops=dict(arrowstyle="->", lw=1.5, color='#388e3c'))
    ax.text(px + 0.1, py + pz + 0.8, r'$\hat{k}$', fontsize=11, color='#388e3c', fontfamily='serif')
    
    # Arc for theta
    arc = patches.Arc((0, 0), 1.2, 1.2, angle=0, theta1=225, theta2=33.7, color='#e65100', lw=1.2)
    ax.add_patch(arc)
    ax.text(0.5, 0.1, r'$\theta$', fontsize=11, color='#e65100', fontfamily='serif')
    
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod0_coords.svg'), format='svg', transparent=True)
    plt.close(fig)

def fig_right_hand_rule():
    fig, ax = plt.subplots(figsize=(4.5, 3.5), dpi=150)
    setup_ax(ax)
    
    # Vector A, Vector B, Vector C = A x B
    ax.annotate('', xy=(2.5, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=2, color='#1976d2'))
    ax.annotate('', xy=(1.5, 1.8), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=2, color='#388e3c'))
    ax.annotate('', xy=(0, 2.5), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=2.5, color='#d32f2f'))
    
    ax.text(2.6, -0.1, r'$\vec{A}$', fontsize=13, color='#1976d2', fontfamily='serif', fontweight='bold')
    ax.text(1.6, 1.9, r'$\vec{B}$', fontsize=13, color='#388e3c', fontfamily='serif', fontweight='bold')
    ax.text(-0.1, 2.6, r'$\vec{C} = \vec{A} \times \vec{B}$', fontsize=13, color='#d32f2f', fontfamily='serif', fontweight='bold')
    
    # Curved arrow from A to B
    arc = patches.Arc((0, 0), 1.6, 1.6, angle=0, theta1=0, theta2=50, color='#e65100', lw=1.5)
    ax.add_patch(arc)
    ax.annotate('', xy=(1.0, 0.7), xytext=(1.1, 0.5), arrowprops=dict(arrowstyle="->", lw=1.5, color='#e65100'))
    ax.text(0.9, 0.25, r'$\theta$', fontsize=11, color='#e65100', fontfamily='serif')
    
    ax.set_xlim(-1, 3.2)
    ax.set_ylim(-0.8, 3.0)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod0_cross_product.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 1: Biot-Savart and straight wire / circular loop
# -------------------------------------------------------------
def fig_biot_savart_wire():
    fig, ax = plt.subplots(figsize=(5, 4), dpi=150)
    setup_ax(ax)
    
    # Wire carrying current I along z
    ax.plot([0, 0], [-2.5, 2.5], color='#212121', lw=3)
    ax.annotate('', xy=(0, 2.6), xytext=(0, 2.0), arrowprops=dict(arrowstyle="->", lw=2, color='#212121'))
    ax.text(0.2, 2.4, r'$I$ (cable infinito)', fontsize=11, color='#212121', fontfamily='serif', fontweight='bold')
    
    # Concentric B field lines
    for r, col in zip([0.8, 1.6, 2.4], ['#1976d2', '#1976d2', '#1976d2']):
        ell = patches.Ellipse((0, 0), r*2, r*0.7, fill=False, edgecolor=col, lw=1.4, linestyle='-')
        ax.add_patch(ell)
        # Arrow on front
        ax.annotate('', xy=(0.1, -r*0.35), xytext=(-0.1, -r*0.35), arrowprops=dict(arrowstyle="->", lw=1.5, color=col))
    
    ax.text(1.7, -0.7, r'$\vec{B}(r) = \frac{\mu_0 I}{2\pi r} \hat{\theta}$', fontsize=12, color='#1976d2', fontfamily='serif', fontweight='bold')
    ax.set_xlim(-2.8, 3.5)
    ax.set_ylim(-2.8, 2.8)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod1_wire_bfield.svg'), format='svg', transparent=True)
    plt.close(fig)

def fig_biot_savart_sim2():
    # sim2 geometry: circular arc (quarter circle in 4th quadrant) + finite wire parallel to z at x=2R
    fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=150)
    setup_ax(ax)
    
    # Axes
    ax.annotate('', xy=(3.5, 0), xytext=(-1.5, 0), arrowprops=dict(arrowstyle="->", lw=1.2, color='#555'))
    ax.annotate('', xy=(0, 2.5), xytext=(0, -2.5), arrowprops=dict(arrowstyle="->", lw=1.2, color='#555'))
    ax.text(3.6, 0, r'$x$', fontsize=11, va='center', fontfamily='serif')
    ax.text(0, 2.6, r'$y$', fontsize=11, ha='center', fontfamily='serif')
    ax.text(-0.25, -0.25, r'$O$', fontsize=11, fontfamily='serif', fontweight='bold')
    
    # Quarter arc in 4th quadrant from -pi/2 to 0
    R = 1.5
    arc = patches.Arc((0, 0), 2*R, 2*R, angle=0, theta1=270, theta2=360, color='#d32f2f', lw=2.5)
    ax.add_patch(arc)
    # Arrow on arc (counter-clockwise: from -pi/2 to 0)
    ax.annotate('', xy=(R*0.75, -R*0.65), xytext=(R*0.65, -R*0.75), arrowprops=dict(arrowstyle="->", lw=2, color='#d32f2f'))
    ax.text(R*0.6, -R*0.4, r'$I$ (arco radio $R$)', fontsize=10, color='#d32f2f', fontfamily='serif', fontweight='bold')
    
    # Finite wire parallel to z at x = 2R (in 2D projection, it's at (2R, 0) pointing out of page / +z)
    ax.scatter([2*R], [0], color='#1976d2', s=80, zorder=5)
    ax.text(2*R - 0.15, -0.4, r'$x=2R$', fontsize=10, color='#1976d2', fontfamily='serif')
    ax.text(2*R + 0.15, 0.25, r'$\odot I\,(+\hat{k})$', fontsize=11, color='#1976d2', fontfamily='serif', fontweight='bold')
    ax.text(2*R + 0.15, -0.15, r'long. $4R$', fontsize=9, color='#1976d2', fontfamily='serif')
    
    ax.set_xlim(-1.8, 4.2)
    ax.set_ylim(-2.8, 3.0)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod1_sim2_geometry.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 2: Current density J and coaxial cable
# -------------------------------------------------------------
def fig_current_density_profiles():
    fig, ax = plt.subplots(figsize=(6, 3.8), dpi=150)
    
    r = np.linspace(0, 1, 100)
    # Profile 1: J(r) = 2J0(1 - r^2/a^2)
    j1 = 2 * (1 - r**2)
    # Profile 2: J(r) = 3J0 (r/a)
    j2 = 3 * r
    # Profile 3: stepped pauta: 1 for r <= 0.5, 3 for 0.5 < r <= 1
    j3 = np.where(r <= 0.5, 1.0, 3.0)
    
    ax.plot(r, j1, label=r'$J(r) = 2J_0(1 - r^2/a^2)$ (Ayud. 9 P2)', color='#1976d2', lw=2.2)
    ax.plot(r, j2, label=r'$J(r) = \beta r$ (Ayud. 9 P3)', color='#388e3c', lw=2.2, linestyle='--')
    ax.step(r, j3, label=r'Escalonado $J_0 / 3J_0$ (Pauta C3 P1)', color='#d32f2f', lw=2.2, where='post')
    
    ax.set_xlabel(r'Radio normalizado $r/a$', fontsize=11, fontfamily='serif')
    ax.set_ylabel(r'Densidad $J / J_0$', fontsize=11, fontfamily='serif')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(frameon=True, fontsize=9.5)
    
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod2_j_profiles.svg'), format='svg', transparent=True)
    plt.close(fig)

def fig_coaxial_stepped():
    # Coaxial cross-section as in Pauta C3 P1 (r <= R/2 with J0, R/2 < r <= R with 3J0)
    fig, ax = plt.subplots(figsize=(4.5, 4.5), dpi=150)
    setup_ax(ax)
    
    # Outer circle R
    c_out = patches.Circle((0, 0), 2.0, fill=True, facecolor='#ffcdd2', edgecolor='#b71c1c', lw=2)
    ax.add_patch(c_out)
    
    # Inner circle R/2
    c_in = patches.Circle((0, 0), 1.0, fill=True, facecolor='#bbdefb', edgecolor='#0d47a1', lw=2)
    ax.add_patch(c_in)
    
    ax.text(0, 0, r'$\odot J_0$', fontsize=12, color='#0d47a1', ha='center', va='center', fontfamily='serif', fontweight='bold')
    ax.text(0, 1.45, r'$\odot 3J_0$', fontsize=12, color='#b71c1c', ha='center', va='center', fontfamily='serif', fontweight='bold')
    
    # Dimension arrows
    ax.annotate('', xy=(1.0, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0d47a1'))
    ax.text(0.5, -0.25, r'$R/2$', fontsize=11, color='#0d47a1', ha='center', fontfamily='serif', fontweight='bold')
    
    ax.annotate('', xy=(0, 2.0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.5, color='#b71c1c'))
    ax.text(-0.25, 1.0, r'$R$', fontsize=11, color='#b71c1c', va='center', fontfamily='serif', fontweight='bold')
    
    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(-2.4, 2.4)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod2_coaxial_stepped.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 3: Ampere's Law & Toroid / Solenoid
# -------------------------------------------------------------
def fig_toroid_simulacro():
    # Rectangular cross section toroid from Simulacro P1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.8), dpi=150)
    setup_ax(ax1, "Vista superior")
    setup_ax(ax2, "Corte transversal (plano rz)")
    
    # Top view: concentric circles of radii a and b
    c_b = patches.Circle((0, 0), 2.2, fill=False, edgecolor='#333', lw=2)
    c_a = patches.Circle((0, 0), 1.2, fill=False, edgecolor='#333', lw=2)
    ax1.add_patch(c_b)
    ax1.add_patch(c_a)
    
    # Amperian loop in between
    c_loop = patches.Circle((0, 0), 1.7, fill=False, edgecolor='#1976d2', lw=1.5, linestyle='--')
    ax1.add_patch(c_loop)
    
    ax1.annotate('', xy=(0, 1.7), xytext=(-0.1, 1.7), arrowprops=dict(arrowstyle="->", lw=2, color='#1976d2'))
    ax1.text(0, 1.85, r'$\vec{B}(r) = \frac{\mu_0 N I}{2\pi r}\hat{\phi}$', fontsize=9.5, color='#1976d2', ha='center', fontfamily='serif')
    
    # Radii arrows
    ax1.annotate('', xy=(1.2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.2, color='#555'))
    ax1.text(0.6, -0.25, r'$a$', fontsize=10, ha='center', fontfamily='serif')
    ax1.annotate('', xy=(0, -2.2), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.2, color='#555'))
    ax1.text(0.15, -1.2, r'$b$', fontsize=10, fontfamily='serif')
    
    # Central wire in purple
    ax1.scatter([0], [0], color='#7b1fa2', s=45, zorder=5)
    ax1.text(0.1, 0.1, r'$I_c$', fontsize=10, color='#7b1fa2', fontfamily='serif', fontweight='bold')
    
    ax1.set_xlim(-2.6, 2.6)
    ax1.set_ylim(-2.6, 2.6)
    
    # Cross section view (rz)
    # Rectangle of width (b - a) and height h
    rect = patches.Rectangle((1.2, -1.0), 1.0, 2.0, fill=True, facecolor='#e0f2fe', edgecolor='#0284c7', lw=1.8)
    ax2.add_patch(rect)
    ax2.text(1.7, 0, r'$\otimes \vec{B}$', fontsize=12, color='#0284c7', ha='center', va='center', fontfamily='serif', fontweight='bold')
    
    # Axis z
    ax2.plot([0, 0], [-1.8, 1.8], 'k-', lw=1.5)
    ax2.annotate('', xy=(0, 1.9), xytext=(0, 1.5), arrowprops=dict(arrowstyle="->", lw=1.5, color='#333'))
    ax2.text(0.1, 1.8, r'$z$', fontsize=11, fontfamily='serif')
    
    # Height h and radii a, b
    ax2.annotate('', xy=(2.3, 1.0), xytext=(2.3, -1.0), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#333'))
    ax2.text(2.4, 0, r'$h$', fontsize=10, va='center', fontfamily='serif')
    
    ax2.plot([0, 1.2], [-1.2, -1.2], 'k:', lw=1)
    ax2.annotate('', xy=(1.2, -1.2), xytext=(0, -1.2), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#555'))
    ax2.text(0.6, -1.4, r'$a$', fontsize=10, ha='center', fontfamily='serif')
    
    ax2.plot([0, 2.2], [-1.6, -1.6], 'k:', lw=1)
    ax2.annotate('', xy=(2.2, -1.6), xytext=(0, -1.6), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#555'))
    ax2.text(1.1, -1.85, r'$b$', fontsize=10, ha='center', fontfamily='serif')
    
    ax2.set_xlim(-0.5, 2.8)
    ax2.set_ylim(-2.1, 2.1)
    
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod3_toroid_simulacro.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 4: Faraday-Lenz & Moving loop from infinite wire
# -------------------------------------------------------------
def fig_faraday_moving_loop():
    # Rectangular loop moving away from infinite wire (Simulacro P2)
    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    setup_ax(ax)
    
    # Infinite wire on y-axis
    ax.plot([0, 0], [-2.5, 2.5], color='#212121', lw=3)
    ax.annotate('', xy=(0, 2.6), xytext=(0, 2.0), arrowprops=dict(arrowstyle="->", lw=2, color='#212121'))
    ax.text(0.15, 2.4, r'$I$ (eje $y$)', fontsize=11, color='#212121', fontfamily='serif', fontweight='bold')
    
    # Distance d(t)
    d = 1.4
    a_len = 1.6
    b_len = 2.0
    
    # Loop rectangle
    rect = patches.Rectangle((d, -b_len/2), a_len, b_len, fill=True, facecolor='#fef3c7', edgecolor='#d97706', lw=2)
    ax.add_patch(rect)
    ax.text(d + a_len/2, 0, r'Espira $R$', fontsize=11, color='#d97706', ha='center', fontfamily='serif', fontweight='bold')
    
    # Velocity vector v
    ax.annotate('', xy=(d + a_len + 0.8, 0), xytext=(d + a_len, 0), arrowprops=dict(arrowstyle="->", lw=2.2, color='#dc2626'))
    ax.text(d + a_len + 0.3, 0.25, r'$\vec{v} = v\hat{\imath}$', fontsize=11, color='#dc2626', fontfamily='serif', fontweight='bold')
    
    # Magnetic field dots / crosses
    for x_pos in [0.7, 1.8, 2.6, 3.4]:
        for y_pos in [-1.5, -0.5, 0.5, 1.5]:
            ax.text(x_pos, y_pos, r'$\otimes$', fontsize=11, color='#94a3b8', ha='center', va='center')
    ax.text(3.5, 2.1, r'$\vec{B} = -\frac{\mu_0 I}{2\pi x}\hat{k}$', fontsize=10.5, color='#475569', fontfamily='serif')
    
    # Dimensions d(t), a, b
    ax.annotate('', xy=(d, -1.3), xytext=(0, -1.3), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#333'))
    ax.text(d/2, -1.55, r'$d(t) = d_0 + vt$', fontsize=10, ha='center', fontfamily='serif')
    
    ax.annotate('', xy=(d + a_len, -1.3), xytext=(d, -1.3), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#333'))
    ax.text(d + a_len/2, -1.55, r'$a$', fontsize=10, ha='center', fontfamily='serif')
    
    ax.annotate('', xy=(d - 0.25, b_len/2), xytext=(d - 0.25, -b_len/2), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#333'))
    ax.text(d - 0.45, 0, r'$b$', fontsize=10, va='center', fontfamily='serif')
    
    ax.set_xlim(-0.8, 4.5)
    ax.set_ylim(-2.2, 2.7)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod4_faraday_moving_loop.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 5: Motional EMF - Rod on rails with gravity
# -------------------------------------------------------------
def fig_motional_emf_rails():
    # Ayudantia 10 P3: Rod on rails with gravity and B = -B0 j
    fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=150)
    setup_ax(ax)
    
    # Rails (vertical)
    L = 2.4
    ax.plot([-L/2, -L/2], [-2.2, 2.0], color='#475569', lw=3.5)
    ax.plot([L/2, L/2], [-2.2, 2.0], color='#475569', lw=3.5)
    # Top connection
    ax.plot([-L/2, L/2], [2.0, 2.0], color='#475569', lw=3.5)
    
    # Moving rod at y = 0
    ax.plot([-L/2 - 0.2, L/2 + 0.2], [0.2, 0.2], color='#dc2626', lw=4.5)
    ax.text(0, 0.45, r'Varilla $(m, R)$', fontsize=11, color='#dc2626', ha='center', fontfamily='serif', fontweight='bold')
    
    # Gravity arrow
    ax.annotate('', xy=(0, -0.9), xytext=(0, -0.2), arrowprops=dict(arrowstyle="->", lw=2, color='#1e293b'))
    ax.text(0.15, -0.6, r'$\vec{g}$', fontsize=12, color='#1e293b', fontfamily='serif', fontweight='bold')
    
    # Velocity arrow
    ax.annotate('', xy=(-0.6, -0.8), xytext=(-0.6, -0.2), arrowprops=dict(arrowstyle="->", lw=2, color='#2563eb'))
    ax.text(-0.85, -0.6, r'$\vec{v}(t)$', fontsize=11, color='#2563eb', fontfamily='serif', fontweight='bold')
    
    # Magnetic force arrow upward
    ax.annotate('', xy=(0.6, 0.8), xytext=(0.6, 0.2), arrowprops=dict(arrowstyle="->", lw=2, color='#16a34a'))
    ax.text(0.75, 0.6, r'$\vec{F}_m$', fontsize=11, color='#16a34a', fontfamily='serif', fontweight='bold')
    
    # Magnetic field crosses
    for x_pos in [-0.7, 0, 0.7]:
        for y_pos in [1.2, -1.4]:
            ax.text(x_pos, y_pos, r'$\otimes \vec{B}$', fontsize=11, color='#94a3b8', ha='center')
            
    # Induced current arrows (counterclockwise)
    ax.annotate('', xy=(0.5, 0.2), xytext=(-0.5, 0.2), arrowprops=dict(arrowstyle="->", lw=2.4, color='#b45309'))
    ax.text(0, -0.05, r'$I_{ind}$ (hacia derecha)', fontsize=9.5, color='#b45309', ha='center', fontfamily='serif', fontweight='bold')
    ax.annotate('', xy=(L/2, 1.4), xytext=(L/2, 0.8), arrowprops=dict(arrowstyle="->", lw=2, color='#b45309'))
    ax.annotate('', xy=(-0.3, 2.0), xytext=(0.3, 2.0), arrowprops=dict(arrowstyle="->", lw=2, color='#b45309'))
    ax.annotate('', xy=(-L/2, 0.8), xytext=(-L/2, 1.4), arrowprops=dict(arrowstyle="->", lw=2, color='#b45309'))
    ax.text(0, 1.35, r'Giro antihorario ($I_{ind}$)', fontsize=10, color='#b45309', ha='center', fontfamily='serif', fontweight='bold')
    ax.text(0, 0.95, r'$\odot \vec{B}_{ind}$ (Lenz opone a $\Delta\Phi > 0$)', fontsize=9, color='#0284c7', ha='center', fontfamily='serif')

    # Rail width L
    ax.annotate('', xy=(L/2, 2.3), xytext=(-L/2, 2.3), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#333'))
    ax.text(0, 2.45, r'$L$', fontsize=11, ha='center', fontfamily='serif', fontweight='bold')
    
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.5, 2.8)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod5_motional_emf_rails.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 6: Mutual inductance - Solenoid & Square loop
# -------------------------------------------------------------
def fig_mutual_solenoid_square():
    # Long solenoid with coaxial square coil (Simulacro P3)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.8), dpi=150)
    setup_ax(ax1, "Vista lateral")
    setup_ax(ax2, "Vista frontal")
    
    # Lateral view: long horizontal cylinder (solenoid)
    ax1.plot([-2.0, 2.0], [0.8, 0.8], 'k-', lw=1.8)
    ax1.plot([-2.0, 2.0], [-0.8, -0.8], 'k-', lw=1.8)
    for x in np.linspace(-1.8, 1.8, 10):
        ax1.plot([x-0.1, x+0.1], [-0.8, 0.8], color='#64748b', lw=1.2)
    ax1.text(0, 0, r'$\vec{B} = \mu_0 n I \hat{\imath}$', fontsize=10, ha='center', va='center', color='#0284c7', fontfamily='serif', fontweight='bold')
    
    # Square coil around center
    ax1.plot([0, 0], [-1.3, 1.3], color='#d97706', lw=3.0)
    ax1.text(0.1, 1.35, r'Bobina cuadrada ($N$ espiras, lado $L$)', fontsize=9, color='#d97706', fontfamily='serif')
    ax1.set_xlim(-2.3, 2.3)
    ax1.set_ylim(-1.8, 1.8)
    
    # Frontal view
    # Solenoid circle radius a
    c_sol = patches.Circle((0, 0), 1.0, fill=True, facecolor='#e0f2fe', edgecolor='#0284c7', lw=2)
    ax2.add_patch(c_sol)
    ax2.text(0, 0, r'$\odot \vec{B}$', fontsize=12, color='#0284c7', ha='center', va='center', fontfamily='serif', fontweight='bold')
    
    # Square coil of side L > 2a
    sq = patches.Rectangle((-1.4, -1.4), 2.8, 2.8, fill=False, edgecolor='#d97706', lw=2.2)
    ax2.add_patch(sq)
    
    # Radius a arrow
    ax2.annotate('', xy=(1.0, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.2, color='#0284c7'))
    ax2.text(0.5, 0.1, r'$a$', fontsize=10, color='#0284c7', fontfamily='serif', fontweight='bold')
    
    # Side L arrow
    ax2.annotate('', xy=(1.4, -1.6), xytext=(-1.4, -1.6), arrowprops=dict(arrowstyle="<->", lw=1.2, color='#d97706'))
    ax2.text(0, -1.85, r'$L > 2a$', fontsize=10, color='#d97706', ha='center', fontfamily='serif', fontweight='bold')
    
    ax2.set_xlim(-1.9, 1.9)
    ax2.set_ylim(-2.0, 1.9)
    
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod6_mutual_solenoid_square.svg'), format='svg', transparent=True)
    plt.close(fig)

def fig_solenoid_tilted_loop():
    # Long solenoid with tilted circular loop inside (Ayudantia 11 P4)
    fig, ax = plt.subplots(figsize=(6.8, 4.2), dpi=150)
    setup_ax(ax)

    # Solenoid cylinder outline
    ax.plot([-3.0, 3.0], [1.7, 1.7], color='#334155', lw=2)
    ax.plot([-3.0, 3.0], [-1.7, -1.7], color='#334155', lw=2)
    # Radius a dimension
    ax.annotate('', xy=(-2.6, 1.7), xytext=(-2.6, 0), arrowprops=dict(arrowstyle='<->', lw=1.2, color='#64748b'))
    ax.text(-2.45, 0.85, r'$a$', fontsize=11, color='#64748b', fontfamily='serif', fontweight='bold', va='center')

    # Turns of solenoid
    for x in np.linspace(-2.8, 2.8, 15):
        ax.plot([x - 0.15, x + 0.15], [-1.7, 1.7], color='#cbd5e1', lw=1.2, linestyle=':')

    # Axis z (horizontal)
    ax.plot([-3.2, 3.2], [0, 0], color='#475569', lw=1.2, linestyle='--')
    ax.annotate('', xy=(3.3, 0), xytext=(3.1, 0), arrowprops=dict(arrowstyle='->', lw=1.5, color='#475569'))
    ax.text(3.4, 0, r'$\hat{z}$ (eje)', fontsize=11, color='#475569', fontfamily='serif', va='center')

    # Magnetic field B inside
    for y_b in [-1.1, 1.1]:
        ax.annotate('', xy=(1.5, y_b), xytext=(-1.5, y_b), arrowprops=dict(arrowstyle='->', lw=1.5, color='#0284c7'))
    ax.text(0, 1.25, r'$\vec{B} = \mu_0 n I \hat{z}$', fontsize=11, color='#0284c7', fontfamily='serif', fontweight='bold', ha='center')

    # Tilted loop of radius b
    alpha_deg = 36
    alpha_rad = np.radians(alpha_deg)
    b = 1.25
    ell = patches.Ellipse((0, 0), 2*b, 2*b*0.4, angle=alpha_deg, fill=True, facecolor='#fef3c7', edgecolor='#d97706', lw=2.5, zorder=5)
    ax.add_patch(ell)

    # Line along major axis (plane of loop)
    dx = b * np.cos(alpha_rad)
    dy = b * np.sin(alpha_rad)
    ax.plot([-dx*1.2, dx*1.2], [-dy*1.2, dy*1.2], color='#b45309', lw=1.5, linestyle='-.', zorder=6)
    ax.text(dx*1.2 + 0.1, dy*1.2 + 0.05, r'Plano de la espira (radio $b$)', fontsize=10, color='#b45309', fontfamily='serif', fontweight='bold')

    # Normal vector n_hat (perpendicular to plane of loop, angle = alpha_deg + 90 = 126 deg)
    norm_angle_deg = alpha_deg + 90
    norm_rad = np.radians(norm_angle_deg)
    nx = 1.1 * np.cos(norm_rad)
    ny = 1.1 * np.sin(norm_rad)
    ax.annotate('', xy=(nx, ny), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=2, color='#dc2626'), zorder=7)
    ax.text(nx - 0.35, ny + 0.1, r'$\hat{n}$', fontsize=12, color='#dc2626', fontfamily='serif', fontweight='bold')

    # Arc for angle alpha between z axis (angle 0) and loop plane (angle alpha_deg)
    arc_alpha = patches.Arc((0, 0), 1.5, 1.5, angle=0, theta1=0, theta2=alpha_deg, color='#d97706', lw=1.8, zorder=6)
    ax.add_patch(arc_alpha)
    ax.text(0.9, 0.25, r'$\alpha$', fontsize=12, color='#d97706', fontfamily='serif', fontweight='bold')

    # Arc / explanatory text
    ax.text(0, -1.2, r'Ángulo entre $\vec{B}$ y plano = $\alpha \quad \Rightarrow \quad$ Ángulo entre $\vec{B}$ y $\hat{n} = 90^\circ - \alpha$', fontsize=9.5, color='#1e293b', fontfamily='serif', ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    ax.text(0, -1.95, r'$\Phi_B = B A \cos(90^\circ - \alpha) = \mu_0 n I (\pi b^2) \sin\alpha \quad \Rightarrow \quad M = \mu_0 n \pi b^2 \sin\alpha$', fontsize=10, color='#0f766e', fontfamily='serif', fontweight='bold', ha='center')

    ax.set_xlim(-3.4, 3.8)
    ax.set_ylim(-2.3, 2.0)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod6_solenoid_tilted_loop.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 8: Circuit with 2-position switch (Pauta C3 P3)
# -------------------------------------------------------------
def fig_circuit_pauta():
    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=150)
    setup_ax(ax)
    
    # Source on left
    ax.plot([0, 0], [0.5, 2.0], 'k-', lw=1.5)
    ax.plot([0, 0], [-0.5, -2.0], 'k-', lw=1.5)
    ax.plot([-0.3, 0.3], [0.5, 0.5], 'k-', lw=2.5) # long plate
    ax.plot([-0.15, 0.15], [-0.5, -0.5], 'k-', lw=3.5) # short plate
    ax.text(-0.6, 0, r'$\mathcal{E}$', fontsize=12, va='center', fontfamily='serif', fontweight='bold')
    
    # Wire to bottom
    ax.plot([0, 5.0], [-2.0, -2.0], 'k-', lw=1.5)
    
    # Wire to top switch
    ax.plot([0, 1.2], [2.0, 2.0], 'k-', lw=1.5)
    
    # Switch node 0, and terminals 1, 2
    ax.scatter([1.2], [2.0], color='#1e293b', s=40, zorder=5)
    ax.text(1.2, 2.2, r'$0$', fontsize=10, ha='center', fontfamily='serif', fontweight='bold')
    
    ax.scatter([2.0], [2.3], color='#2563eb', s=40, zorder=5)
    ax.text(2.0, 2.5, r'$1$', fontsize=10, color='#2563eb', ha='center', fontfamily='serif', fontweight='bold')
    
    ax.scatter([2.0], [1.3], color='#dc2626', s=40, zorder=5)
    ax.text(2.0, 1.0, r'$2$', fontsize=10, color='#dc2626', ha='center', fontfamily='serif', fontweight='bold')
    
    # Switch arm pointing to 1
    ax.plot([1.2, 1.95], [2.0, 2.28], color='#2563eb', lw=2.2)
    
    # Branch RC (connected to terminal 1 or 2 via switch)
    ax.plot([2.0, 3.2], [2.3, 2.3], 'k-', lw=1.5)
    # Resistor R
    ax.plot([3.2, 3.8], [2.3, 2.3], color='#d97706', lw=3.0)
    ax.text(3.5, 2.55, r'$R$', fontsize=10, ha='center', color='#d97706', fontfamily='serif')
    ax.plot([3.8, 4.3], [2.3, 2.3], 'k-', lw=1.5)
    # Capacitor C
    ax.plot([4.3, 4.3], [2.1, 2.5], 'k-', lw=2.2)
    ax.plot([4.5, 4.5], [2.1, 2.5], 'k-', lw=2.2)
    ax.text(4.4, 2.65, r'$C$', fontsize=10, ha='center', fontfamily='serif')
    ax.plot([4.5, 5.0], [2.3, 2.3], 'k-', lw=1.5)
    ax.plot([5.0, 5.0], [2.3, -2.0], 'k-', lw=1.5)
    
    # Branch RL (always connected to source)
    ax.plot([0.6, 0.6], [2.0, 0.3], 'k-', lw=1.5)
    # Inductor L
    ax.plot([0.6, 1.8], [0.3, 0.3], color='#16a34a', lw=3.2)
    ax.text(1.2, 0.55, r'$L$', fontsize=10, ha='center', color='#16a34a', fontfamily='serif')
    # Resistor R
    ax.plot([1.8, 3.0], [0.3, 0.3], color='#d97706', lw=3.0)
    ax.text(2.4, 0.55, r'$R$', fontsize=10, ha='center', color='#d97706', fontfamily='serif')
    ax.plot([3.0, 5.0], [0.3, 0.3], 'k-', lw=1.5)
    
    ax.set_xlim(-1.0, 5.6)
    ax.set_ylim(-2.5, 2.9)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod8_switch_circuit.svg'), format='svg', transparent=True)
    plt.close(fig)

# -------------------------------------------------------------
# Module 10: Maxwell Ampere Paradox (Capacitor S1, S2)
# -------------------------------------------------------------
def fig_maxwell_capacitor():
    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=150)
    setup_ax(ax)
    
    # Wire in from left
    ax.plot([-3.0, -1.0], [0, 0], color='#212121', lw=2.5)
    ax.annotate('', xy=(-1.5, 0), xytext=(-2.2, 0), arrowprops=dict(arrowstyle="->", lw=2, color='#212121'))
    ax.text(-2.0, 0.25, r'$I(t)$', fontsize=11, color='#212121', fontfamily='serif', fontweight='bold')
    
    # Plates
    ax.plot([-1.0, -1.0], [-1.5, 1.5], color='#1e293b', lw=4)
    ax.plot([1.0, 1.0], [-1.5, 1.5], color='#1e293b', lw=4)
    ax.text(-1.3, 1.6, r'$+Q$', fontsize=11, color='#2563eb', fontfamily='serif', fontweight='bold')
    ax.text(1.1, 1.6, r'$-Q$', fontsize=11, color='#dc2626', fontfamily='serif', fontweight='bold')
    
    # Wire out to right
    ax.plot([1.0, 3.0], [0, 0], color='#212121', lw=2.5)
    ax.annotate('', xy=(2.5, 0), xytext=(1.8, 0), arrowprops=dict(arrowstyle="->", lw=2, color='#212121'))
    ax.text(2.0, 0.25, r'$I(t)$', fontsize=11, color='#212121', fontfamily='serif', fontweight='bold')
    
    # Electric field arrows between plates
    for y in [-0.8, 0, 0.8]:
        ax.annotate('', xy=(0.8, y), xytext=(-0.8, y), arrowprops=dict(arrowstyle="->", lw=1.5, color='#ea580c'))
    ax.text(0, 1.0, r'$\vec{E}(t)$', fontsize=11, color='#ea580c', ha='center', fontfamily='serif', fontweight='bold')
    
    # Loop Gamma on wire
    ell = patches.Ellipse((-2.0, 0), 0.5, 1.8, fill=False, edgecolor='#16a34a', lw=2)
    ax.add_patch(ell)
    ax.text(-2.0, 1.1, r'Lazo $\Gamma$', fontsize=10, color='#16a34a', ha='center', fontfamily='serif', fontweight='bold')
    
    # Surface S1 (flat disk)
    ax.text(-2.4, -0.6, r'Disco $S_1$', fontsize=9.5, color='#16a34a', fontfamily='serif')
    
    # Surface S2 (bag bulging into capacitor)
    arc_s2 = patches.Arc((-0.5, 0), 3.0, 1.8, angle=0, theta1=270, theta2=90, color='#7c3aed', lw=1.8, linestyle='--')
    ax.add_patch(arc_s2)
    ax.text(0.1, -1.2, r'Bolsa $S_2$ (entre placas)', fontsize=9.5, color='#7c3aed', fontfamily='serif', fontweight='bold')
    
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-2.0, 2.0)
    plt.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, 'mod10_maxwell_capacitor.svg'), format='svg', transparent=True)
    plt.close(fig)

if __name__ == '__main__':
    print("Generating SVG diagrams...")
    fig_coords_cylindrical()
    fig_right_hand_rule()
    fig_biot_savart_wire()
    fig_biot_savart_sim2()
    fig_current_density_profiles()
    fig_coaxial_stepped()
    fig_toroid_simulacro()
    fig_faraday_moving_loop()
    fig_motional_emf_rails()
    fig_mutual_solenoid_square()
    fig_solenoid_tilted_loop()
    fig_circuit_pauta()
    fig_maxwell_capacitor()
    print("All SVGs generated successfully in", IMG_DIR)
