import cv2
import numpy as np
from PIL import Image 
from keras.applications.mobilenet import preprocess_input
from keras.models import load_model
import RPi.GPIO as GPIO
from time import sleep
led=8
ledw= 16
srm = 11
leds=36
frequence = 50
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(srm, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW,)
GPIO.output(leds,GPIO.HIGH)
def action_mecanique():
    pwm = GPIO.PWM(srm, frequence)
    pwm.start(7)
    sleep(0.2)
    pwm.ChangeDutyCycle(2)
    sleep(1.5)
    pwm.ChangeDutyCycle(7)
    sleep(0.2)
    del pwm 

prob = 0.70  
from keras.preprocessing import image 
model = load_model('/home/pi/fsmlogo.h5')
clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(0)  # Put here ID of your camera (/dev/videoN)
cv2.namedWindow('camera')
cv2.setMouseCallback('camera', onMouse)

# Read and process frames in loop
success, frame = cameraCapture.read()
run=False
while success and not clicked:
    cv2.waitKey(1)
    success, frame = cameraCapture.read()
    r = cv2.rectangle(frame, (30, 30), (390, 450), (255, 0, 0), 3)
    contour = frame[30:390, 30:450] 
    contour = cv2.resize(contour, (224, 224)) 
    im = Image.fromarray(contour, 'RGB') 
    img_array = np.array(im) 
    img_array_expanded_dims = np.expand_dims(img_array, axis=0) 
    img_array = preprocess_input(img_array_expanded_dims)
    pred = model.predict(img_array)
    prediction = np.argmax(pred[0]) 
    probabilityValue =np.amax(pred)
    if probabilityValue > prob:

        if prediction==0:
            name='autre :'
        elif prediction==1:
            name='fsm :'
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW,)
    GPIO.setup(ledw, GPIO.OUT, initial=GPIO.LOW)
    
    if prediction==1:
        GPIO.output(led,GPIO.HIGH)
        #print("on")
        while run==False:
            action_mecanique()
            run=True
    if prediction==0:
        GPIO.output(ledw, GPIO.HIGH)  
        #print("Worning")
        sleep(0.25)
        GPIO.output(ledw, GPIO.LOW)
        run=False    
    text = "{}: {:.2f}%".format(name, probabilityValue * 100)
    cv2.putText(frame,text, (50, 20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 1) 
    cv2.imshow('camera', frame)
GPIO.output(leds,GPIO.LOW)    
GPIO.cleanup((8,16,11,36))
cv2.destroyAllWindows()
cameraCapture.release()