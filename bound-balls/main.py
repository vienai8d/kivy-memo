import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse
from kivy.vector import Vector
from kivy.clock import Clock

from random import random

FPS = 60
SPEED = 20
BALL_SIZE = (50, 50)
BALL_NUM = 10

class Ball(Ellipse):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.v = Vector(random(), random())

    @property
    def x(self):
        return self.pos[0] + self.r

    @property
    def y(self):
        return self.pos[1] + self.r

    @property
    def r(self):
        return self.size[0] / 2
    
    def move(self):
        self.pos = self.v * SPEED + self.pos


class MainApp(App):

    def build(self):

        layout = FloatLayout(size=Window.size)
        ball_list = [Ball(pos=(random() * layout.width, random() * layout.height), size=BALL_SIZE)
                     for i in range(0, BALL_NUM)]
        for ball in ball_list:
            layout.canvas.add(ball)

        def update(dt):
            for ball in ball_list:
                if ball.x <= 0 or layout.width <= ball.x:
                    ball.v.x *= -1
                if ball.y <= 0 or layout.height <= ball.y:
                    ball.v.y *= -1
                ball.move()
        
        Clock.schedule_interval(update, 1.0/FPS)

        return layout

if __name__ == '__main__':
    MainApp().run()
