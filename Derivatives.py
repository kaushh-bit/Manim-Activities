from manim import *
import numpy as np

class Derivatives(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 5, 1], 
            y_range=[-1, 30, 5],
            x_length=7,
            y_length=7,
            tips=False,
            axis_config={"include_numbers": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        def f(x):
            return x**2
        graph = axes.plot(f, color=BLUE)

        self.add(axes, labels)
        self.play(Write(graph))

        #x and x+h 
        x0 = 1
        y0 = f(x0)
        h = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]
        dot_x1 = Dot(axes.c2p(x0, f(x0)), color=WHITE) #c2p - coordinate to point
        
        self.add (dot_x1)

        #initial h
        dot_x2 = Dot(axes.c2p(x0 + h[0], f(x0 + h[0])), color=WHITE)
        line = Line(dot_x1.get_center(), dot_x2.get_center()).set_color(ORANGE)
        line = line.scale(1.5, about_point=line.get_center())

        self.add (dot_x2)
        self.play (Write(line))

        #slope unedited
        slope_value = ((f(x0 + h[0])) - y0)/((x0 + h[0]) - x0)
        slope = Text(f"Slope = {slope_value:.2f}", font_size=36).to_corner(UR).shift(DOWN)
        h_value = Text(f"h = {h[0]:.2f}", font_size=20).next_to(dot_x2, RIGHT)
        self.play(Write(slope), Write(h_value))

        #as h -> 0
        scaler = 2
        for i in h:
            x1 = x0 + i
            y1 = f(x1)
            dot_x2_updated = Dot(axes.c2p(x1, y1), color=WHITE)        

            start = dot_x1.get_center()
            end = dot_x2_updated.get_center()
            direction = end - start
            unit_vector = direction / np.linalg.norm(direction)
            length = 5  # fixed line length
            line_updated = Line(
                start - unit_vector * length / 3,
                start + unit_vector * length,
                color=ORANGE
            )

            self.play (
                Transform (dot_x2, dot_x2_updated),
                Transform (line, line_updated),
                run_time = 0.5
            ) 
            
            self.add(line_updated.copy().set_opacity(0.3).set_stroke(width=1))

            #slope
            slope_value = (y1 - y0)/(x1 - x0)
            slope_updated = Text(f"Slope = {slope_value:.2f}", font_size=36).to_corner(UR).shift(DOWN)
            h_value_updated = Text(f"h = {i:.2f}", font_size=20).next_to(dot_x2, RIGHT)
            self.play(
                Transform(slope, slope_updated),
                Transform(h_value, h_value_updated),
                )
       
        self.wait (3)