import math
from AbstractShape import AbstractShape
from Core.Transformations.Translations import Translation
from ..LineProperties import defaultLineProperties
from ..Repeaters import defaultRepeater


class Ellipse(AbstractShape):

    def __init__(self, initialPosition, radius, (scaleX, scaleY),
            lineProps=defaultLineProperties(),
            transformation=Translation(),
            repeater=defaultRepeater()):
        AbstractShape.__init__(self, initialPosition,
            lineProps, transformation, repeater)
        self.radius = radius
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.pi2 = 2 * math.pi

    def drawInitialShape(self, cr):
        cr.save()
        cr.scale(self.scaleX, self.scaleY)
        cr.arc(0, 0, self.radius, 0, self.pi2)
        cr.stroke()
        cr.restore()