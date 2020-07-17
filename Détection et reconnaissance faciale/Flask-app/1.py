from PIL import Image 
from keras.applications.mobilenet import preprocess_input
import base64 
from io import BytesIO 
import json 
import random 
import keras
import cv2 
from keras.models import load_model 
import numpy as np 
threshold = 0.70  
font = cv2.FONT_HERSHEY_SIMPLEX
from flask import Flask, render_template, Response
import time
import cv2 
from flask import Flask, render_template, Response, request

app = Flask(__name__)


@app.route('/')
def index():
    """home page."""
    return render_template('index.html')


@app.route('/stream')
def stream():
    """Video streaming home page."""
    return render_template('stream.html')

model = keras.models.load_model('face3.h5',compile=False)                                                                                                                


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

def face_extractor(img):
    faces = face_cascade.detectMultiScale(img, 1.3, 5) 
    if faces is (): 
        return None 

    for (x,y,w,h) in faces: 
        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cropped_face = img[y:y+h, x:x+w] 
     
    return cropped_face 
print(" * Loading Keras model...") 


def gen():
    """Video streaming generator function."""
    video_capture = cv2.VideoCapture(0)

    # Read until video is completed
    while True:
        _, frame = video_capture.read()
        face = face_extractor(frame)
        if type(face) is np.ndarray:
            face = cv2.resize(face, (224, 224))
            im = Image.fromarray(face, 'RGB')
            img_array = np.array(im)
            img_array_expanded_dims = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array_expanded_dims)
            pred = model.predict(img_array)
            prediction = np.argmax(pred[0])

            probabilityValue = np.amax(pred)
            if probabilityValue > threshold:

                if prediction == 0:
                    name = 'autre :'
                elif prediction == 1:
                    name = 'jihed :'
                elif prediction == 2:
                    name = 'younes :'
                # cv2.putText(frame,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                # cv2.putText(frame, name+str(round(probabilityValue*100,2) )+"%", (50, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
                text = "{}: {:.2f}%".format(name, probabilityValue * 100)
                faces = face_cascade.detectMultiScale(frame, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    # cropped_face = img[y:y+h, x:x+w]
                    cv2.rectangle(frame, (x-2,y-2), (x+w, y-30), (0,255,0), cv2.FILLED)
                    cv2.putText(frame, text, ((x+5, y-5)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        #cv2.imshow('Video', frame)
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
