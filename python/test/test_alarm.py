from __future__ import absolute_import

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")))

from src.alarm import Alarm

class TestAlarm(unittest.TestCase):
    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        
        alarm.check()
        
        self.assertFalse(alarm.is_alarm_on())

if __name__ == "__main__":
    unittest.main()

