from manim import *
import numpy as np
from scipy.special import factorial, hermite



class axes(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=(0, 10, 1),
            y_range=(-1, 1, 0.5),
            z_range=(-10, 10, 1),
            x_length=10,
            y_length=6,
            z_length=8,
        ).rotate(0*DEGREES)
        curve = ax.plot(np.sin)
        xlab = ax.get_axis_labels("x-axis")
        ylab = ax.get_axis_labels("y")
        zlab = ax.get_axis_labels("z")
        self.add(ax, curve, xlab, ylab, zlab)
        
        self.set_camera_orientation(phi=-0.5, theta=-1.4)
    