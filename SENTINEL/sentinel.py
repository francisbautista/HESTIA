#!/usr/bin/python
#  TODO: Use Gammu for SMS enabling on serial pin

import RPi.GPIO as GPIO
import time, io, sys, select
from datetime import datetime


from picamera import PiCamera, PiCameraCircularIO
from time import sleep

camera = PiCamera()
camera.resolution = (1280, 720)
camera.sensor_mode=4
stream = PiCameraCircularIO(camera, seconds=30)
camera.start_recording(stream, format='h264', quality=20)
GPIO.setmode(GPIO.BOARD)            #Set GPIO to pin numbering
pir = 8                             #Assign pin 8 to PIR
led = 10                            #Assign pin 10 to LED
GPIO.setup(pir, GPIO.IN)            #Setup GPIO pin PIR as input
GPIO.setup(led, GPIO.OUT)   


def main():
      
            #Setup GPIO pin for LED as output
    print ("Sensor initializing . . .")
    time.sleep(2)                       #Give sensor time to startup
    print ("Active")
    print ("Press Ctrl+c to end program")

    try:
        while True:
            camera.wait_recording(1)
            if GPIO.input(pir) == True:      #If PIR pin goes high, motion is detected
                print ("Motion Detected!")
                time.sleep(5)
                if GPIO.input(pir) == True:
                    print ("A lot of motion detected! Recording video.")        
                    capture_video()
                print ("Resetting")                 
            GPIO.output(led, False)          #Turn off LED
        time.sleep(0.1)

    except KeyboardInterrupt:           #Ctrl+c
        pass                              #Do nothing, continue to finally
            
    finally:
        GPIO.output(led, False)           #Turn off LED in case left on
        GPIO.cleanup()                    #reset all GPIO
        print ("Program ended")

def capture_video():
    GPIO.output(led, True)
    now = datetime.now().time()
    now = now.strftime("%H:%M:%S")

    camera.wait_recording(30)
    capture_image()    
    stream.copy_to(now + 'motion.h264')
    GPIO.output(led, False)  

def capture_image():
    now = datetime.now().time()
    now = now.strftime("%H:%M:%S")

    # camera.brightness = 50
    # camera.sharpness = 50
    # camera.saturation = -75
    # camera.ISO = 1200
    # camera.shutter_speed = 2000000
    camera.capture(now + 'image.jpg', use_video_port=True)
  
if __name__== "__main__":
  main()