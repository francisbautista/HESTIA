"""
Package for interfacing with Raspberry PI PIR motion sensor.
"""
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time

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
        return bool(self.pir.motion_detected)


pir = MotionDetector()

try:
    while True:
        if pir.movement_detected():
            print("hi")
        else:
            time.sleep(1)
except KeyboardInterrupt:
    del camera