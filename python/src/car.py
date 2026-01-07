from __future__ import absolute_import

from src.engine import Engine

class CarColor(object):
    BLACK = 1
    RED = 2
    BLUE = 3

class CarState(object):
    OFF = 1
    ON = 2
    DRIVING = 3

class Car(object):
    def __init__(self):
        """Construct the car"""
        self.engine = Engine()

        self.license_plate = ""
        self.mileage = 0.0

        self.color = CarColor.BLACK
        self.state = CarState.OFF

    def start(self):
        if not self.engine.start():
            raise ValueError('Broken valve.')

        self.mileage = 0.0
        with open('milage.txt', 'r') as f:
            self.mileage = float(f.read())

        self.state = CarState.ON

    def stop(self):
        self.engine.stop()
        self.state = CarState.OFF

    def drive(self):
        if self.state is CarState.ON:
            self.state = CarState.DRIVING

    def brake(self):
        if self.state is CarState.DRIVING:
            self.state = CarState.ON

    def get_mileage(self):
        return self.mileage

    def set_license_plate(self, license_plate):
        if not license_plate:
            raise ValueError('license plate cannot be empty.')
        else:
            self.license_plate = license_plate

    def add_mile(self):
        if self.state is CarState.DRIVING:
            self.mileage = self.mileage + 1.0

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def get_license_plate(self):
        return self.license_plate

    def add_kilometers(self, kilometers):
        self.mileage = self.mileage + (1.609344 * kilometers)

