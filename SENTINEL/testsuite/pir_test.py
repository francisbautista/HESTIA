#!/usr/bin/env python
"""
Testing for Pir package
"""
import unittest
import site

site.addsitedir('..')
from lib.pir import MotionDetector


class TestPir(unittest.TestCase):
    """
    Test for the Pir class
    """
    @classmethod
    def setUpClass(cls):
        """
        Initialize Motiondetector class
        """
        cls.pir = MotionDetector()

    def test_movement_detected(self):
        """
        Test method pir.movement_detected()
        """
        self.assertFalse(self.pir.movement_detected())


if __name__ == '__main__':
    unittest.main()
