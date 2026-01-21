from __future__ import absolute_import

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")))

from src.rpmgauge import RpmGauge, GaugeColor

class TestRpmGauge(unittest.TestCase):
    def test_default_color_green(self):
        gauge = RpmGauge()
        self.assertEqual(GaugeColor.GREEN, gauge.get_color())

if __name__ == "__main__":
    unittest.main()

