from __future__ import print_function
from google.cloud import vision
from google.cloud.vision_v1 import types
import os
import io
import cv2
from PIL import Image

credential_path = "nodal-isotope-333317-71fcbccc05ee.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

client = vision.ImageAnnotatorClient()
def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

    for text in texts:
        string+=' ' + text.description
    return string


cap = cv2.VideoCapture(0)
count = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    file = 'live.png'
    cv2.imwrite( file,frame)

    # print OCR text
    print(count)
    count+=1
    print(detect_text(file))

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()