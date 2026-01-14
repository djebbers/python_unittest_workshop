from __future__ import absolute_import

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")))

from src.car import Car, CarColor

class TestCar(unittest.TestCase):
    def test_get_milage__new_car_has_zero_mileage(self):
        car = Car()
        car.set_license_plate("30-UTW-87")
        car.set_color(CarColor.RED)

        mileage = car.get_mileage()

        self.assertAlmostEqual(mileage, 0.0)

    def test_car_drives_2_miles_mileage_increased_with_2(self):
        car = Car()
        car.set_license_plate("30-UTW-87")
        car.set_color(CarColor.RED)
        car.start()
        car.drive()
        car.add_mile()
        car.add_mile()

        mileage = car.get_mileage()

        self.assertAlmostEqual(mileage, 2.0)

    def test_new_car_has_color_black(self):
        car = Car()
        car.set_license_plate("30-UTW-87")

        color = car.get_color()

        self.assertEqual(color, CarColor.BLACK)

    def test_color_change_color_is_red(self):
        car = Car()
        car.set_license_plate("30-UTW-87")
        car.set_color(CarColor.RED)

        color = car.get_color()

        self.assertEqual(color, CarColor.RED)

    def test_car_different_license_plate(self):
        car = Car()
        car.set_color(CarColor.RED)
        car.set_license_plate("30-BAO-43")

        license_plate = car.get_license_plate()

        self.assertEqual(license_plate, "30-BAO-43")

if __name__ == "__main__":
    unittest.main()