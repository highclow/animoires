import cairo
import math
from drawable import Drawable
from movable import Movable

class Ellipses(Drawable, Movable):

    def __init__(self, rgb, lineWidth, center, movers, (sx, sy) , numRep, radisuChanger):
        Drawable.__init__(self, rgb, lineWidth)
        Movable.__init__(self, center, movers)
        self.sx = sx
        self.sy = sy
        self.isx = 1 / sx
        self.isy = 1 / sy
        self.numRep = numRep
        self.radisuChanger = radisuChanger

    def draw(self, cr):
        for i in range(1, self.numRep + 1):
            cr.scale(self.sx, self.sy);
            cr.arc(0, 0, self.radisuChanger(i), 0, 2*math.pi)
            cr.scale(self.isx, self.isy)
            cr.stroke()