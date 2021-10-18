from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label


class MLProjectApp(App):
    def build(self):

        layout = BoxLayout(padding=[10, 20, 10, 10], orientation='vertical')

        btn_top = Button(text="Button top", background_color=[0.5, 0.5, 0.5, 1.0])
        layout.add_widget(btn_top)

        btn_bot = Button(text="Button bot", background_color=[0.8, 0.8, 0.8, 1.0])
        layout.add_widget(btn_bot)

        layout.add_widget(Button())

        return layout

    def on_press_button(self):
        print('You pressed the button')


MLProjectApp().run()
