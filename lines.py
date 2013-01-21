import cairo
import math
from shapes import Shape
from position import Position
from repeater import Repeater
from lineproperties import LineProperties


class Lines(Shape):

    def __init__(self, initialLength, position, repeater, lineProperties):
        Shape.__init__(self, position, repeater, lineProperties, self.initialLine)
        self.initialLength = initialLength

    def initialLine(self, cr):
        cr.move_to(0, 0)
        cr.line_to(self.initialLength, 0)
        cr.stroke()
