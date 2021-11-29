from __future__ import print_function

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

from gtts import gTTS

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

        return MainLayout()

    def on_press_button(self, function):

        if function == "Menu":
            print('Menu Button Function')

        if function == "Speak":
            print('Text-to-speech function')
            self.text_to_speech()

        if function == "Read":
            print('Camera text extraction function')

class CamApp(App):

    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        cv2.imshow("CV2 Image", frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

client = vision.ImageAnnotatorClient()
def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

<<<<<<< Updated upstream
    for text in texts:
        string+=' ' + text.description
    return string
=======
        for text in texts:
            string += ' ' + text.description
        print(string)
        return string
>>>>>>> Stashed changes

    def text_to_speech(self):
        text_to_read = self.detectedText
        text_result = gTTS(text=text_to_read, lang='en', slow=False)
        text_result.save("text_result.mp3")
        os.system("start text_result.mp3")


if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()