from __future__ import absolute_import

from src.engine import Engine

class Alarm(object):
    def __init__(self, engine=None):
        self._low_temperature_threshold = 0
        self._high_temperature_threshold = 130
        self._is_alarm_on = False
        self._engine = engine or Engine()

    def check(self):
        temperature = self._engine.get_temperature()
        if temperature < self._low_temperature_threshold or temperature > self._high_temperature_threshold:
            self._is_alarm_on = True

    def is_alarm_on(self):
        return self._is_alarm_on