class GaugeColor(object):
    GREEN = 1
    BLUE = 2
    RED = 3

class RpmGauge(object):
    def __init__(self):
        self.rpm = 0

    def set_rpm(self, rpm):
        """
        Provide the rpm to the RpmGauge:
        :param rpm 0 - 10000.
        """
        if rpm < 0:
            self.rpm = 0
        elif rpm <= 9999:
            self.rpm = rpm
        else:
            self.rpm = 10000

    def get_color(self):
        """
        Determine the color of the gauge.
        :returns GaugeColor  Red: 6000 >= rpm
                             Blue: 4000 <= rpm < 6000
                             Green: 0 <= rpm < 4000
        """
        color = GaugeColor.GREEN
        if self.rpm >= 6000:
            color = GaugeColor.RED
        elif self.rpm >= 4000:
            color = GaugeColor.BLUE

        return color

    def get_rpm(self):
        """
        Retrieves the rpm
        :return: rpm
        """
        return self.rpm
