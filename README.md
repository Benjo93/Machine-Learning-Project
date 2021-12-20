# Machine-Learning-Project
## TTS Mobile App 

# Introduction:
The importance of Artificial Intelligence is not hidden to anyone these days. It’s fascinating the way Artificial Intelligence has become involved in our lives and we encounter it in our daily lives without even realizing it. From aiding in avoiding traffic, offering movies or music recommendations, voice-controlled personal digital assistants, the famous self-driving cars and vehicles, instant translation of machines, and many other predictive capabilities are just some applications of the forms Artificial Intelligence has taken up today. AI makes our lives more efficient every day. AI empowers many programs and services that help us do everyday things such as connecting with friends, using an email program, or using a ride-share service.
In this project, we have used the power of AI for making life easier for those patients who have difficulty in reading their medicine labels or prescriptions due to small fonts. Our team has developed a mobile app that uses the camera of a smartphone to scan the text of a medical prescription bottle or some other product items and reads out the text. This application is a good example of how AI technology is useful in our everyday lives.

Part one (Building the App):
The TTS Mobile App was developed using a python mobile app building package called kivy. The components were broken down into two modules, namely the text-to-speech module and the camera-module. The two modules act independently such that the camera captures an image, extracts the text data, and then passes that data to the TTS module to output the result.
main.py – file that contains all the python code required to run the project. This includes the kivy, text-to-speech, and google vision libraries required to run the app. 
mlproject.kv – layout file that defines the structure of the app and communicates the user interaction to the main process. 

![image](https://user-images.githubusercontent.com/13397606/146822399-9281866c-85d2-45e3-9296-fd40be66dd25.png)

Part 2 (Extract text from image):
	Text extraction was implemented using google vision libraries and opencv in Python. This works in two independent functions. First, opencv will open a connection with the webcam atached to the computer, or the 1st camera attached to the device, and then save the image as a file. The opencv image is then converted into a kivy texture and applied to the camera widget at the bottom of the app screen. A button is then pressed to allow google vision to analyze the last live photo for text and display it in the label above.
 
![ML App Pic](https://user-images.githubusercontent.com/13397606/146821767-8d221e0e-0dad-4ef0-8eeb-6b16d96847d3.png)

Part 3 (Turn text to speech):
Text-to-speech was implemented using the gTTS python library. This library contains functions to convert an input text into an audio file that can then be saved to the user’s device. 
 
 

![MLProject App Concept](https://user-images.githubusercontent.com/13397606/146821897-7c70be2e-4179-495e-b23a-12d900434e9b.png)

