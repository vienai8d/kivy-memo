import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse
from kivy.vector import Vector
from kivy.clock import Clock

FPS = 60
BALL_SIZE = (50, 50)
GRAVITY = 30 / FPS
LIFT = 1.5 * GRAVITY 

class Ball(Ellipse):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.v = Vector(0, 0)
        self.hovering = False

    @property
    def x(self):
        return self.pos[0] + self.r

    @property
    def y(self):
        return self.pos[1] + self.r

    @property
    def r(self):
        return self.size[0] / 2
    
    def hover(self, isinstance):
        self.hovering = True
    
    def fall(self, isinstance):
        self.hovering = False

    def move(self):
        self.v.y += LIFT if self.hovering else -GRAVITY
        self.pos = self.v +self.pos

    def reset(self, pos):
        self.v = Vector(0, 0)
        self.pos = pos


class MainApp(App):

    def build(self):
        layout = FloatLayout(size=Window.size)
        ball = Ball(pos=layout.center, size=BALL_SIZE)
        bottun = Button(text='hover!', size_hint=(0.1, 0.1), pos_hint={'x': 0, 'y': 0},
                        on_press=ball.hover, on_release=ball.fall)
        layout.canvas.add(ball)
        layout.add_widget(bottun)

        def update(dt):
            ball.move()
            if ball.y < 0 or ball.y > layout.height:
                ball.reset(layout.center)

        Clock.schedule_interval(update, 1.0/FPS)

        return layout

if __name__ == '__main__':
    MainApp().run()
