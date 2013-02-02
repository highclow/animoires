import math
import cairo


class Transformation(object):

    pass


class IdentityTransformation(Transformation):

    def __init__(self):
        pass

    def transform(self, cr, value):
        pass


class Translation(Transformation):

    def __init__(self, translater):
        self.translater = translater

    def transform(self, cr, value):
        (tX, tY) = self.translater(value)
        cr.translate(tX, tY)


class Rotation(Transformation):

    def __init__(self, rotater):
        self.rotater = rotater

    def transform(self, cr, value):
        angle = self.rotater(value)
        cr.rotate(angle)


class Scale(Transformation):

    def __init__(self, scaler):
        self.scaler = scaler

    def transform(self, cr, value):
        lw = cr.get_line_width()
        (sX, sY) = self.scaler(value)
        cr.scale(sX, sY)
        cr.set_line_width(lw / max(sX, sY))


class Composition(Transformation):

    def __init__(self, transformationList):
        self.transformationList = transformationList

    def transform(self, cr, value):
        for t in self.transformationList:
            t.transform(cr, value)


class TranslaterFactory():

    def infiniteSegmentBounce(self, frequency, amplitude, theta=0):
        return lambda value: (lambda dist=amplitude * (2 * math.asin(
            math.sin(2 * math.pi * frequency * value)) / math.pi):
            (math.cos(theta) * dist, math.sin(theta) * dist))()

    def infiniteCircle(self, frequency, (initX, initY), (cX, cY), direction=1.0):
        return lambda value: (lambda dx=(initX - cX), dy = (initY - cY):
            (lambda r=math.sqrt((dx ** 2) + (dy ** 2)), pi2=(2 * math.pi):
            (lambda cAngle=(direction * pi2 * frequency * value),
                iAngleX=(dx / r), iAngleY=(dy / r):
                (lambda rx=(r * math.cos(cAngle + iAngleX) - dx),
                    ry=(r * math.sin(cAngle + iAngleY) - dy):
                    (rx, ry)))))()()()()

    def infiniteDirection(self, amplitude, theta=0):
        return lambda value: (lambda dist=amplitude * value:
            (math.cos(theta) * dist, math.sin(theta) * dist))()


class RotaterFactory():
    def regularFrequencyRotation(self, frequency, direction=1):
        return lambda value: direction * 2 * math.pi * frequency * value


class ScalerFactory():
    def arithmeticScale(self, (progX, progY)):
        return lambda value: (1.0 + (progX * value), 1.0 + (progY * value))


def defaultTransformation():
    return IdentityTransformation()
