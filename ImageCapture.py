import cv2
import os
from picamera2 import Picamera2
import time
import requests
import json
from datetime import datetime


image_prefix = 'pi_'
image_suffix = '.jpg'
ImgOutput = "./pi"
key = 'resolutionValue'
url = 'http://localhost:5000/getResolution'
print (url)
myResponse = requests.get(url)

resolution = '1920*1080'
if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    resolution = jData[key]
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()
print(resolution)
resValues = resolution.split('*')
IMG_SIZE=100
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (int(resValues[0]), int(resValues[1]))}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)
#picam2.start_preview(Preview.QTGL)
picam2.start()

def capture_image(filename):
    #time.sleep(10)
    picam2.capture_file(ImgOutput + "/" + filename)
    #picam2.stop_()

now = datetime.now()
date_time = now.strftime("%Y_%m_%d_%H:%M:%S")
filename = image_prefix + date_time + image_suffix
capture_image(filename)
