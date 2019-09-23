import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.vector import Vector
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from random import random

FPS = 30
SPEED = 20
BOX_SIZE = (50, 50)
BOX_COLOR = Color(0.4, 0.7, 0.4) 
LINE_COLOR = Color(0.9, 0.5, 0.8)
MAX_LEN_LINE_POINTS = 1000

class MainApp(App):

    def build(self):
        layout = FloatLayout(size=Window.size)
        box = Rectangle(pos=layout.center, size=BOX_SIZE)
        line = Line(points=list(layout.center))
        layout.canvas.add(BOX_COLOR)
        layout.canvas.add(box)
        layout.canvas.add(LINE_COLOR)
        layout.canvas.add(line)

        def update(dt):
            v_x = random() - 0.5
            v_y = random() - 0.5
            v = Vector(v_x, v_y) * SPEED
            box.pos = v + box.pos
            center = Vector(box.size) / 2 + box.pos
            line.points += list(center)

            if len(line.points) > MAX_LEN_LINE_POINTS:
                line.points.pop(0)
                line.points.pop(0)

        Clock.schedule_interval(update, 1.0/FPS)
        return layout

if __name__ == '__main__':
    MainApp().run()
