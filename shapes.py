import cairo
import math
from position import Position
from repeater import Repeater
from lineproperties import LineProperties


class Shape(object):

    def __init__(self, position, repeater, lineProperties, initialShape):
        self.position = position
        self.repeater = repeater
        self.lineProperties = lineProperties
        self.initialShape = initialShape

    def draw(self, cr, frame, time):
        self.position.move(cr, frame, time)
        self.lineProperties.setInitialDrawingContext(cr)
        self.repeater.repeat(cr, frame, time,
            self.lineProperties, self.initialShape)


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
        return lambda cr: (cr.arc(0, 0, initialRadius, 0, 2 * math.pi), cr.stroke())

    def getEllipse(self, initialRadius, (initalScaleX, initalScaleY)):
        return lambda cr: (cr.save(), cr.scale(initalScaleX, initalScaleY),
            cr.arc(0, 0, initialRadius, 0, 2 * math.pi), cr.stroke(), cr.restore())
