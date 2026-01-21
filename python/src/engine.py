import random

class Type(object):
    STRAIGHT = 1
    V6 = 2
    BOXER = 3
    ROTARY = 4

class FuelType(object):
    DIESEL = 1
    PETROL = 2
    GASOLINE = 3
    ELECTRICAL = 4

class Engine(object):
    def __init__(self):
        """Construct the engine"""
        self.type = Type.V6
        self.torque = 0.0
        self.fuel_type = FuelType.PETROL
        self.power = 0.0
        self.is_running = False

    def start(self):
        self.is_running = True
        return True

    def stop(self):
        self.is_running = False

    def get_torque(self):
        return self.torque

    def get_power(self):
        return self.power

    def get_type(self):
        return self.type

    def get_fuel_type(self):
        return self.fuel_type

    def is_running(self):
        return self.is_running

    @staticmethod
    def get_temperature():
        return 6 * random.random() * random.random()

class DieselEngine(Engine):
    def __init__(self, cc=None, engine_type=None):
        super(DieselEngine, self).__init__()
        if cc is not None:
            self.cc = cc
        if engine_type is not None:
            self.type = engine_type