import matplotlib.pyplot as plt
import numpy as np
import cv2

import os
import random
from glob import glob
from keras import preprocessing

class_names = ['BANANA', 'APPLE', 'ORANGE', 'CARROT']

# get the reference to the webcam
camera = cv2.VideoCapture(0)
camera_height = 500
raw_frames_type_1 = []
raw_frames_type_2 = []
raw_frames_type_3 = []
raw_frames_type_4 = []

while (True):
    # read a new frame
    _, frame = camera.read()

    # flip the frame
    frame = cv2.flip(frame, 1)

    # rescaling camera output
    aspect = frame.shape[1] / float(frame.shape[0])
    res = int(aspect * camera_height)  # landscape orientation - wide image
    frame = cv2.resize(frame, (res, camera_height))

    # add rectangle
    cv2.rectangle(frame, (300, 75), (650, 425), (0, 255, 0), 2)

    #  show the frame
    cv2.imshow("Capturing frames", frame)

    key = cv2.waitKey(1)

    # quit camera if 'q' key is pressed
    if key & 0xFF == ord("q"):
        break
    elif key & 0xFF == ord("1"):
        # save the frame
        raw_frames_type_1.append(frame)
        print('1 key pressed - saved TYPE_1 frame')
    elif key & 0xFF == ord("2"):
        # save the frame
        raw_frames_type_2.append(frame)
        print('2 key pressed - Saved TYPE_2 frame')
    elif key & 0xFF == ord("3"):
        # save the frame
        raw_frames_type_3.append(frame)
        print('3 key pressed - Saved TYPE_3 frame')
    elif key & 0xFF == ord("4"):
        # save the frame
        raw_frames_type_4.append(frame)
        print('4 key pressed - Saved TYPE_4 frame')

camera.release()
cv2.destroyAllWindows()

#for croppig images
save_width = 400
save_height = 400

for i in range(1, 5):
    name = '/home/mrkushalsharma/Desktop/data/images_type_{}'.format(i)
    os.makedirs(name, exist_ok=True)

#saving images in local directory
for i, frame in enumerate(raw_frames_type_1):
    roi = frame[75 + 2:425 - 2, 300 + 2:650 - 2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('/home/mrkushalsharma/Desktop/data/images_type_1/{}.png'.format(i), cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_type_2):
    roi = frame[75 + 2:425 - 2, 300 + 2:650 - 2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('/home/mrkushalsharma/Desktop/data/images_type_2/{}.png'.format(i), cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_type_3):
    roi = frame[75 + 2:425 - 2, 300 + 2:650 - 2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('/home/mrkushalsharma/Desktop/data/images_type_3/{}.png'.format(i), cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

for i, frame in enumerate(raw_frames_type_4):
    roi = frame[75 + 2:425 - 2, 300 + 2:650 - 2]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (save_width, save_height))
    cv2.imwrite('/home/mrkushalsharma/Desktop/data/images_type_4/{}.png'.format(i), cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))


    #/home/mrkushalsharma/Desktop/data/images_type_2/{}.png'