import math
import cairo
import sys


#class Transformation(object):
#
#    pass
#
#
class IdentityTransformation(object):

    def __init__(self):
        pass

    def transform(self, cr, value):
        pass


class Translation(object):

    def __init__(self, translater):
        self.translater = translater

    def transform(self, cr, value):
        (tX, tY) = self.translater(value)
        cr.translate(tX, tY)


class Rotation(object):

    def __init__(self, rotater):
        self.rotater = rotater

    def transform(self, cr, value):
        angle = self.rotater(value)
        cr.rotate(angle)


class Scale(object):

    def __init__(self, scaler):
        self.scaler = scaler

    def transform(self, cr, value):
        lw = cr.get_line_width()
        (sX, sY) = self.scaler(value)
        cr.scale(sX, sY)
        cr.set_line_width(lw / max(sX, sY))


class Composition(object):

    def __init__(self, transformationList):
        self.transformationList = transformationList

    def transform(self, cr, value):
        for t in self.transformationList:
            t.transform(cr, value)


class TranslaterFactory(object):

    def infiniteSegmentBounce(self, frequency, amplitude, theta=0):
        return lambda value: (lambda dist=amplitude * (2 * math.asin(
            math.sin(2 * math.pi * frequency * value)) / math.pi):
            (math.cos(theta) * dist, math.sin(theta) * dist))()

    def infiniteCircle(self, frequency, (initX, initY), (cX, cY), direction=1):
        d = math.copysign(1, direction)
        dx = (initX - cX)
        dy = (initY - cY)
        r = math.sqrt((dx ** 2) + (dy ** 2))
        signeAngle = math.copysign(1, math.asin(dy / r))
        iAngle = signeAngle * math.acos(dx / r)
        return lambda value: (lambda
            cAngle=(d * 2 * math.pi * frequency * value):
            (lambda rx=(r * math.cos(cAngle + iAngle) - dx),
                ry=(r * math.sin(cAngle + iAngle) - dy):
                (rx, ry)))()()

    def infiniteDirection(self, amplitude, theta=0):
        return lambda value: (lambda dist=amplitude * value:
            (math.cos(theta) * dist, math.sin(theta) * dist))()


class RotaterFactory(object):
    def regularFrequencyRotation(self, frequency, direction=1):
        d = math.copysign(1, direction)
        return lambda value: d * 2 * math.pi * frequency * value


class ScalerFactory(object):
    def arithmeticScale(self, (progX, progY)):
        return lambda value: (1.0 + (progX * value), 1.0 + (progY * value))


def defaultTransformation():
    return IdentityTransformation()
