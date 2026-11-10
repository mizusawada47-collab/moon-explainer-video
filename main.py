
from manim import *

class MoonExplainer(Scene):
    def construct(self):
        self.camera.background_color = "#080D1B"

        # INTRODUCTION
        title = Text(
            "WHY DOES THE MOON CHANGE SHAPE?",
            font_size=32,
            color=WHITE
        )
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # INTRODUCTION TO THE MOON
        earth = Circle(
            radius=0.65,
            color=BLUE,
            fill_opacity=1
        ).move_to(ORIGIN)

        moon = Circle(
            radius=0.22,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1
        ).move_to(RIGHT * 3)

        orbit = Circle(
            radius=3,
            color=GRAY,
            stroke_opacity=0.5
        )

        earth_label = Text("EARTH", font_size=22).next_to(earth, DOWN)
        moon_label = Text("MOON", font_size=20).next_to(moon, UP)

        self.play(Create(orbit))
        self.play(FadeIn(earth), Write(earth_label))
        self.play(FadeIn(moon), Write(moon_label))
        self.wait(2)

        # EXPLANATION
        explanation = Text(
            "The Moon does not actually change shape.",
            font_size=27,
            color=YELLOW
        ).to_edge(DOWN)

        self.play(Write(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

        # SUN
        sun = Circle(
            radius=0.55,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1
        ).move_to(LEFT * 5)

        sun_label = Text(
            "SUN",
            font_size=22,
            color=YELLOW
        ).next_to(sun, DOWN)

        self.play(FadeIn(sun), Write(sun_label))

        explanation2 = Text(
            "The Sun illuminates one half of the Moon.",
            font_size=26,
            color=WHITE
        ).to_edge(DOWN)

        self.play(Write(explanation2))
        self.wait(3)
        self.play(FadeOut(explanation2))

        # MOON ORBIT
        self.play(
            MoveAlongPath(
                moon,
                Circle(radius=3).shift(ORIGIN)
            ),
            run_time=8,
            rate_func=linear
        )

        self.play(FadeOut(moon_label))

        # MOON PHASES
        self.play(
            FadeOut(orbit),
            FadeOut(earth),
            FadeOut(earth_label),
            FadeOut(sun),
            FadeOut(sun_label),
            FadeOut(moon)
        )

        heading = Text(
            "THE 4 MAIN MOON PHASES",
            font_size=34,
            color=YELLOW
        ).to_edge(UP)

        self.play(Write(heading))

        phases = [
            ("NEW MOON", 0),
            ("FIRST QUARTER", 1),
            ("FULL MOON", 2),
            ("LAST QUARTER", 3)
        ]

        positions = [
            LEFT * 4.5,
            LEFT * 1.5,
            RIGHT * 1.5,
            RIGHT * 4.5
        ]

        for (name, phase), position in zip(phases, positions):
            disc = Circle(
                radius=0.48,
                color=WHITE,
                fill_color=WHITE,
                fill_opacity=1
            ).move_to(position)

            label = Text(
                name,
                font_size=17,
                color=WHITE
            ).next_to(disc, DOWN, buff=0.3)

            if phase == 0:
                disc.set_fill(GRAY, opacity=0.3)

            if phase == 1:
                shadow = Circle(
                    radius=0.48,
                    color=BLACK,
                    fill_color=BLACK,
                    fill_opacity=1
                ).move_to(position + RIGHT * 0.24)
                self.add(disc, shadow)
            elif phase == 3:
                shadow = Circle(
                    radius=0.48,
                    color=BLACK,
                    fill_color=BLACK,
                    fill_opacity=1
                ).move_to(position + LEFT * 0.24)
                self.add(disc, shadow)
            else:
                self.add(disc)

            self.play(Write(label))
            self.wait(1)

        self.wait(3)

        # CONCLUSION
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        conclusion = Text(
            "The Moon changes appearance because\nwe see different portions of its sunlit side!",
            font_size=27,
            color=YELLOW,
            line_spacing=1.4
        )

        self.play(Write(conclusion))
        self.wait(4)
        self.play(FadeOut(conclusion))
