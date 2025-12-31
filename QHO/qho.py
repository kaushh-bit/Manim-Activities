from manim import *
import numpy as np
from scipy.special import factorial, hermite

class QHO(Scene):
    def construct(self):
        # constants
        m = 1
        omega = 1
        hbar = 1

        # axes and labels
        ax1 = Axes(
            x_range=(-4, 4, 1),
            y_range=(-1, 1, 0.25),
            x_length=6,
            y_length=6,
            tips=False
        )

        labels1 = ax1.get_axis_labels("x", "\psi_{n}")

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
        
        # plotting the real and imaginary part of psi
        t = ValueTracker(0)
        n = 10

        def Re_psi(x):
            return np.real(psi_nt(n, x, t.get_value()))
        def Im_psi(x):
            return np.imag(psi_nt(n, x, t.get_value()))
        
        Re_wave = always_redraw(lambda: ax1.plot(Re_psi, x_range=(-4, 4), color=RED))
        Im_wave = always_redraw(lambda: ax1.plot(Im_psi, x_range=(-4, 4), color=BLUE))

        self.add(Re_wave, Im_wave)

        ax2 = Axes(
            x_range=(-4, 4, 1),
            y_range=(0, 0.5, 0.1),
            x_length=6,
            y_length=6,
            tips=False
        )
        ax2.next_to(ax1, RIGHT, buff=1)
        labels2 = ax2.get_axis_labels("x", MathTex(r"|\psi|^2"))
        axes = VGroup(ax1, ax2, labels1, labels2)
        axes.move_to(ORIGIN)
        self.add(axes)

        def prob_density(x):
            return np.abs(psi_nt(n, x, t.get_value()))**2
        
        pdf = always_redraw(lambda: ax2.plot(prob_density, x_range=(-4, 4)))
        self.add(pdf)

        self.play(t.animate.set_value(10), run_time=10, rate_func=linear)