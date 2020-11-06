from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0, 0, 1, 1)


class KivyApp(App):
    def build(self):
        label = Label(text="Hello! I am Vedant Nichal", font_size='40sp', bold=True,
                      color=(1, 0, 0, 1),
                      italic=True)
        return label


KivyApp().run()
