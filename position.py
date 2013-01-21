import math
import cairo


class Position:
    def __init__(self, initialPosition, translater=None):
        self.initialPosition = initialPosition
        self.translater = translater

    def move(self, cr, frame, time):
        if (self.translater is not None):
            (cX, cY) = self.translater(frame, time)
        else:
            (cX, cY) = (0, 0)
        cr.translate(cX + self.initialPosition[0],
            cY + self.initialPosition[1])

class PositionTranslaterFactory():

    def regularLinePath(self, frequency, amplitude, theta):
        return lambda frame, time: (lambda dist = amplitude * (2 * math.asin(
            math.sin(2 * math.pi * frequency * time)) / math.pi):
            (math.cos(theta) * dist, math.sin(theta) * dist))()


    def regularCirclePath(self, (cX, cY), frequency, direction, (initX, initY)):
        return lambda frame,  time: (lambda r = math.sqrt(((cX - initX) ** 2) + ((cY - initY) ** 2)),
            iAngleX = 2 * math.pi * ((initX - cX) / r),
            iAngleY = 2 * math.pi * ((initY - cY) / r),
            rx = cX + direction * (r * math.cos((2 * math.pi * frequency * time) + iAngleX)),
            ry = cY + direction * (r * math.sin((2 * math.pi * frequency * time) + iAngleY)):
            (rx, ry))()