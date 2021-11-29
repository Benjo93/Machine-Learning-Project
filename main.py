from __future__ import print_function

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

#Camera Functionality
from google.cloud import vision
from google.cloud.vision_v1 import types
import os
import io
import cv2

credential_path = "nodal-isotope-333317-71fcbccc05ee.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

class MainLayout(BoxLayout):
    pass


class MLProjectApp(App):
    def build(self):

        # Change the background color.
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        # Change window size.
        Window.size = (450, 800)

        #Google Vision
        self.client = vision.ImageAnnotatorClient()
        self.detectedText = ''
        #opencv2
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/33.0)

        return MainLayout()

    def on_press_button(self, function):

        if function == "Menu":
            print('Menu Button Function')

        if function == "Speak":
            print('Text-to-speech function')

        if function == "Read":
            print('Camera text extraction function')
            self.detectedText = self.detect_text('images/live.png')
            self.root.ids.textLabel.text = self.detectedText

    def update(self, dt):
        ret, frame = self.capture.read()

        file = 'images/live.png'
        cv2.imwrite( file,frame)
        
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.root.ids.img1.texture = texture1

    def detect_text(self, path):
        #Detects text in the file.
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = self.client.text_detection(image=image)
        texts = response.text_annotations
        string = ''

        for text in texts:
            string+=' ' + text.description
        print(string)
        return string

if __name__ == '__main__':
    MLProjectApp().run()
    os.remove("images/live.png")
    cv2.destroyAllWindows()