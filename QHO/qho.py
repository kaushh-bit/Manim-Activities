from manim import *
import numpy as np
from scipy.special import factorial, hermite

# constants
m = 1
omega = 1
hbar = 1

# defining eigenfunctions and eigenvalues
def psi_n(n, x):
    alpha = (m * omega) / hbar
    xi = np.sqrt(alpha) * x
    norm = np.sqrt(1 / (2**n * factorial(n))) * (alpha / PI)**0.25
    Hn = hermite(n)
    return norm * Hn(xi) * np.exp( - xi**2 / 2)

def E_n(n):
    return hbar * omega * (n + 0.5)

def psi_nt(n, x, t):
    return psi_n(n, x) * np.exp((-1j * E_n(n) * t) / hbar)


######################################################################################################


class QHO(ThreeDScene):
    def construct(self):
        
        #axes and labels
        ax = ThreeDAxes(
            x_range=(-10, 10, 1),
            y_range=(-1, 1, 0.5),
            z_range=(-10, 10, 1),
            x_length=10,
            y_length=6,
            z_length=8,
            tips=False,
        )
        self.add(ax)

        # plotting the real and imaginary part of psi
        t = ValueTracker(0)
        n = 7

        def Re_psi(x):
            return np.real(psi_nt(n, x, t.get_value()))
        def Im_psi(x):
            return np.imag(psi_nt(n, x, t.get_value()))
        
        Re_wave = always_redraw(lambda: ax.plot(Re_psi, x_range=(-7, 7), color=RED))
        Im_wave = always_redraw(lambda: ax.plot(Im_psi, x_range=(-7, 7), color=BLUE))

        self.add(ax, Re_wave, Im_wave)
        self.play(t.animate.set_value(4), run_time=5, rate_func=linear)

        #calling qho func
        x = np.linspace(-10,10,500)
        #t = np.linspace(1,10,500)
        qho_plot_tot = ax.plot_line_graph(x, psi_n(n, x), np.full_like(x, n), add_vertex_dots=False, line_color=YELLOW)
        '''qho_plot_Re = ax.plot_line_graph(x, Re_psi, add_vertex_dots=False, line_color=BLUE)
        qho_plot_Im = ax.plot_line_graph(x, Im_psi, add_vertex_dots=False, line_color=RED)'''

        self.play(
            ReplacementTransform(Re_wave, qho_plot_tot,),
            ReplacementTransform(Im_wave, qho_plot_tot,),
            run_time=2,
        )


        #other eigenstates
        self.move_camera(theta=-1.4)
        self.move_camera(phi=-0.5)

        plots = []
        _color = [RED, BLUE, GREEN, YELLOW, PINK, ORANGE]
        for n in range(0,6):
            qho_plot_ = ax.plot_line_graph(x, psi_n(n, x), np.full_like(x, n), add_vertex_dots=False, line_color=_color[n])
            plots.append(qho_plot_)

        '''self.play(
            AnimationGroup(
                *[Create(plot) for plot in plots]
            ), 
            run_time=6
        )'''

        self.play(Create(VGroup(*plots)), run_time=4)