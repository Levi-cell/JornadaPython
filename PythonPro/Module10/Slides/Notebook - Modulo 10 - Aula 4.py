# pip install kivy[full]

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class Grid(Widget):
    pass

class PythonProApp(App):
    def build(self):

        return Builder.load_file('PythonPro.kv')

PythonProApp().run()
