"""
Package for interfacing with Raspberry PI PIR motion sensor.
"""
from gpiozero import MotionSensor


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
                print ("LOG: Motion Detected!")
                time.sleep(5)
                if self.pir.motion_detected:
                    return bool(self.pir.motion_detected)
                print ("LOG: PIR Resetting")