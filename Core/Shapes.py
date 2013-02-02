import math
from Transformations import defaultTransformation
from LineProperties import defaultLineProperties
from Repeaters import defaultRepeater


class Shape(object):

    def __init__(self, (initialX, initialY), initialShape,
            lineProps=defaultLineProperties(),
            transformation=defaultTransformation(),
            repeater=defaultRepeater()):
        self.initialX = initialX
        self.initialY = initialY
        self.initialShape = initialShape
        self.lineProps = lineProps
        self.transformation = transformation
        self.repeater = repeater

    def draw(self, cr, time):
        cr.translate(self.initialX, self.initialY)
        self.lineProps.setDrawingContext(cr)
        self.transformation.transform(cr, time)
        self.repeater.repeat(cr, time, self.initialShape)


class InitialShapeFactory:

    def getLine(self, initialX, initalY):
        return lambda cr: (cr.move_to(0, 0), cr.line_to(initialX, initalY),
            cr.stroke())

    def getRectangle(self, initialWidth, initialHeight):
        return lambda cr: (cr.save(),
            cr.translate(- initialWidth / 2, -initialHeight / 2),
            cr.rectangle(0, 0, initialWidth, initialHeight),
            cr.stroke(), cr.restore())

    def getCircle(self, initialRadius):
        return lambda cr: (cr.arc(0, 0, float(initialRadius), 0, 2 * math.pi),
            cr.stroke())

    def getEllipse(self, initialRadius, (initalScaleX, initalScaleY)):
        return lambda cr: (cr.save(), cr.scale(initalScaleX, initalScaleY),
            cr.arc(0, 0, initialRadius, 0, 2 * math.pi), cr.stroke(),
            cr.restore())
