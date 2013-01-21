import cairo
import math
from shapes import Shape
from position import Position
from repeater import Repeater
from lineproperties import LineProperties


class Ellipses(Shape):

    def __init__(self, initialRadius, (initalScaleX, initalScaleY),
            position, repeater, lineProperties):
        Shape.__init__(self, position, repeater, lineProperties, self.initialEllipse)
        self.initialRadius = initialRadius
        self.initalScaleX = initalScaleX
        self.initalScaleY = initalScaleY

    def initialEllipse(self, cr):
        cr.save()
        cr.scale(self.initalScaleX, self.initalScaleY)
        cr.arc(0, 0, self.initialRadius, 0, 2 * math.pi)
        cr.stroke()
        cr.restore()
