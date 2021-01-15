"""
Package for interfacing with Raspberry PI PIR motion sensor.
"""
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time

GPIO.setup(4, GPIO.IN)    

class MotionDetector:  # pylint: disable=too-few-public-methods
    """
    Class to interfaces with Raspberry PI PIR motion sensor module
    """

    def __init__(self):
        self.pir = MotionSensor(4)

    def movement_detected(self):
        """
        Check if movement detected.
        :return: boolean
        """
        if self.pir.motion_detected:      #If PIR pin goes high, motion is detected
                print ("Motion Detected!")
                time.sleep(5)
                if self.pir.motion_detected:
                    sm.SendSMS(ALERT_MESSAGE)
                    print ("A lot of motion detected! Recording video.")        
                    return bool(self.pir.motion_detected)
                print ("Resetting")
        


pir = MotionDetector()

try:
    while True:
        if pir.movement_detected():
            print("hi")
        else:
            time.sleep(1)
except KeyboardInterrupt:
    del camera