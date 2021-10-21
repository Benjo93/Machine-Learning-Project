from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class MainLayout(BoxLayout):
    pass


class MLProjectApp(App):
    def build(self):

        # Change the background color.
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        # Change window size
        Window.size = (450, 800)

        return MainLayout()

    def on_press_button(self, function):

        if (function == "Menu"):
            print('Menu Button Function')

        if (function == "Speak"):
            print('Text-to-speech function')

        if (function == "Read"):
            print('Camera text extraction function')

MLProjectApp().run()
