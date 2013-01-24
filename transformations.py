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

    def infiniteSegmentBounce(self, frequency, amplitude, theta):
        return lambda value: (lambda dist=amplitude * (2 * math.asin(
            math.sin(2 * math.pi * frequency * value)) / math.pi):
            (math.cos(theta) * dist, math.sin(theta) * dist))()

    def infiniteCircle(self, (cX, cY), frequency, direction, (initX, initY)):
        return lambda value: (lambda r=math.sqrt(
            ((cX - initX) ** 2) + ((cY - initY) ** 2)):
            (lambda iAngleX=2 * math.pi * ((initX - cX) / r),
                iAngleY=2 * math.pi * ((initY - cY) / r):
                (lambda rx=cX + (r * math.cos(
                    (direction * 2 * math.pi * frequency * value) + iAngleX)),
                ry=cY + (r * math.sin(
                    (direction * 2 * math.pi * frequency * value) + iAngleY)):
                (rx, ry))))()()()

    def infiniteDirection(self, amplitude, theta):
        return lambda value: (lambda dist=amplitude * value:
            (math.cos(theta) * dist, math.sin(theta) * dist))()


class RotaterFactory():
    def regularFrequencyRotation(self, frequency):
        return lambda value: 2 * math.pi * frequency * value


class ScalerFactory():
    def arithmeticScale(self, progX, progY):
        return lambda value: (1.0 + (progX * value), 1.0 + (progY * value))


def defaultTransformation():
    return IdentityTransformation()
