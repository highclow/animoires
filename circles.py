import cairo
import math
from drawable import Drawable
from movable import Movable

class Circles(Drawable, Movable):

    def __init__(self, rgb, lineWidth, center, movers, numRep, radisuChanger):
        Drawable.__init__(self, rgb, lineWidth)
        Movable.__init__(self, center, movers)
        self.numRep = numRep
        self.radisuChanger = radisuChanger

    def draw(self, cr):
        for i in range(1, self.numRep + 1):
            cr.arc(0, 0, self.radisuChanger(i), 0, 2*math.pi)
            cr.stroke()