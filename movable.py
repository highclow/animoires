import cairo

class Movable(object):
    def __init__(self, (ix, iy), (moveX, moveY)):
        self.ix = ix
        self.iy = iy
        self.cx = ix
        self.cy = iy
        self.moveX = moveX
        self.moveY = moveY

    def move(self, cr, t):
        if (self.moveX is not None):
            self.cx = self.moveX(i=self.ix, c=self.cx, t=t)
        if (self.moveY is not None):
            self.cy = self.moveY(i=self.iy, c=self.cy, t=t)
        cr.translate(self.cx, self.cy)
        