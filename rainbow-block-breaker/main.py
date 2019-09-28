import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.vector import Vector
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from random import random

FPS = 60
BLOCK_SIZE = 100
BLOCK_NUM_H = 3
BALL_SIZE = 50
DEFAULT_SPEED = 15

class Block(Rectangle):

    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color

    @property
    def x(self):
        return self.pos[0] + self.r

    @property
    def y(self):
        return self.pos[1] + self.r

    @property
    def r(self):
        return self.size[0] / 2

class Ball(Ellipse):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.v = Vector(random() * DEFAULT_SPEED, -1 * DEFAULT_SPEED)

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
        self.pos = self.v + self.pos
    
    def reflect(self):
        if abs(self.v.x) > abs(self.v.y):
            self.reflect_x()
        else:
            self.reflect_y()

    def reflect_x(self):
        self.v = self.v * (-1, 1)

    def reflect_y(self):
        self.v = self.v * (1, -1)


class MainApp(App):

    def build(self):
        layout = FloatLayout(size=Window.size)
        
        layout_w = Window.size[0]
        layout_h = Window.size[1]
        block_num_w_lim = int(layout_w / BLOCK_SIZE)
        block_num_h_lim = int(layout_h / BLOCK_SIZE)

        block_list = []
        for j in range(block_num_h_lim - BLOCK_NUM_H, block_num_h_lim):
            for i in range(0, block_num_w_lim):
                block = Block(pos=(i * BLOCK_SIZE, j * BLOCK_SIZE),
                              size=(BLOCK_SIZE, BLOCK_SIZE),
                              color=Color(i/block_num_w_lim, j/block_num_h_lim, 1.0, mode='hsv'))
                layout.canvas.add(block.color)
                layout.canvas.add(block)
                block_list.append(block)

        ball_list = []
        ball = Ball(pos=layout.center, size=(BALL_SIZE, BALL_SIZE))
        ball_list.append(ball)
        layout.canvas.add(Color(1, 1, 1))
        layout.canvas.add(ball)

        distance2_for_collision = (BLOCK_SIZE / 2) ** 2 + (BALL_SIZE / 2) ** 2

        def update(dt):
            for ball in ball_list:
                ball.move()
                if ball.y < 0 or ball.y > layout_h:
                    ball.reflect_y()
                elif ball.x < 0 or ball.x > layout_w:
                    ball.reflect_x()

                for block in block_list:
                    distance2 = (ball.x - block.x) ** 2 + (ball.y - block.y) **2
                    if distance2 < distance2_for_collision:
                        layout.canvas.remove(block)
                        block_list.remove(block)
                        ball.reflect()
                        ball1 = Ball(pos=block.pos, size=(BALL_SIZE, BALL_SIZE))
                        ball2 = Ball(pos=block.pos, size=(BALL_SIZE, BALL_SIZE))
                        ball_list.append(ball1)
                        ball_list.append(ball2)
                        layout.canvas.add(block.color)
                        layout.canvas.add(ball1)
                        layout.canvas.add(ball2)
                        break

        Clock.schedule_interval(update, 1.0/FPS)
        return layout

if __name__ == '__main__':
    MainApp().run()
