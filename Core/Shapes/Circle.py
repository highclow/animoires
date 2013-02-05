import math
from AbstractShape import AbstractShape


class Circle(AbstractShape):

    def __init__(self, initialPosition, radius,
            lineProps=defaultLineProperties(),
            transformation=Translation(),
            repeater=defaultRepeater()):
        AbstractShape.__init__(self, initialPosition,
            lineProps, transformation, repeater)
        self.radius = radius
        self.pi2 = 2 * math.pi

    def drawInitialShape(self, cr):
        cr.arc(0, 0, float(self.radius), 0, self.pi2)
        cr.stroke()