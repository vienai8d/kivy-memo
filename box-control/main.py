import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.vector import Vector
from kivy.clock import Clock

FPS = 30
SPEED = 20
BOX_SIZE = (50, 50)
BOX_COLOR = Color(0.4, 0.7, 0.4) 


class MainApp(App):

    v_x = 0.0
    v_y = 0.0

    def left(self, instance):
        self.v_x = -0.5

    def right(self, instance):
        self.v_x = 0.5

    def up(self, instance):
        self.v_y = 0.5

    def down(self, instance):
        self.v_y = -0.5
    
    def stop_x(self, instance):
        self.v_x = 0.0

    def stop_y(self, instance):
        self.v_y = 0.0

    def build(self):

        layout = FloatLayout(size=Window.size)
        box = Rectangle(pos=layout.center, size=BOX_SIZE)
        btn_l = Button(text='L', size_hint=(0.1, 0.1), pos_hint={'x': 0, 'center_y': 0.5},
                       on_press=self.left, on_release=self.stop_x)
        btn_r = Button(text='R', size_hint=(0.1, 0.1), pos_hint={'right': 1, 'center_y': 0.5},
                       on_press=self.right, on_release=self.stop_x)
        btn_u = Button(text='U', size_hint=(0.1, 0.1), pos_hint={'center_x': 0.5, 'top': 1},
                       on_press=self.up, on_release=self.stop_y)
        btn_d = Button(text='D', size_hint=(0.1, 0.1), pos_hint={'center_x': 0.5, 'y': 0},
                       on_press=self.down, on_release=self.stop_y)
        layout.canvas.add(BOX_COLOR)
        layout.canvas.add(box)
        layout.add_widget(btn_l)
        layout.add_widget(btn_r)
        layout.add_widget(btn_u)
        layout.add_widget(btn_d)

        def update(dt):
            v = Vector(self.v_x, self.v_y) * SPEED
            box.pos = v + box.pos

        Clock.schedule_interval(update, 1.0/FPS)

        return layout

if __name__ == '__main__':
    MainApp().run()
