from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
import random
from kivy.uix.button import Button

Window.clearcolor = (38 / 255.0, 101 / 255.0, 189 / 255.0, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        self.canvas.add(Color(rgb=(colorR / 255.0, colorG / 255.0, colorB / 255.0)))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):
    def build(self):
        rootWindow = Widget()
        self.painter = PaintWindow()
        clearBtn = Button(text='Clear Screen')
        clearBtn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearBtn)

        return rootWindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


PaintApp().run()
