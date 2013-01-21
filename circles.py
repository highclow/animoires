import cairo
import math
from shapes import Shape
from position import Position
from repeater import Repeater
from lineproperties import LineProperties


class Circles(Shape):

    def __init__(self, initialRadius, position, repeater, lineProperties):
        #Shape.__init__(self, position, repeater, lineProperties)
        self.initialRadius = initialRadius

    def initialShape(self, cr):
        self.drawInitialCircle(cr)

    def drawInitialCircle(self, cr):
        cr.arc(0, 0, self.initialRadius, 0, 2 * math.pi)
        cr.stroke()
