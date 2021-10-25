from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window


class MainLayout(BoxLayout):
    pass


class MLProjectApp(App):
    def build(self):

        # Change the background color.
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        # Change window size.
        Window.size = (450, 800)

        return MainLayout()

    def on_press_button(self, function):

        if function == "Menu":
            print('Menu Button Function')

        if function == "Speak":
            print('Text-to-speech function')

        if function == "Read":
            print('Camera text extraction function')


MLProjectApp().run()


# Take a picture with device camera and store it in the root directory.
class CameraExample(App):

    def build(self):

        # Get camera feed.
        self.camera = Camera(play=True)
        self.camera.resolution = (800, 800)

        take_picture = Button(text="Take Picture")
        take_picture.size_hint = (0.5, 0.2)
        take_picture.pos_hint = {'x': 0.25, 'y': 0.25}
        take_picture.bind(on_press=self.take_picture)

        layout = BoxLayout()
        layout.add_widget(self.camera)
        layout.add_widget(take_picture)
        return layout

    def take_picture(self, *args):
        print("Picture Taken")
        self.camera.export_to_png("./camera_test.png")


# CameraExample().run()
