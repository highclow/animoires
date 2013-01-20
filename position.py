import cairo

class Position:
    def __init__(self, initialPosition, translater=None):
        self.initialPosition = initialPosition
        self.translater = translater

    def move(self, cr, frame, time):
        if (self.translater is not None):
            (cX, cY) = self.translater(None, frame, time)
        else:
        	(cX, cY) = (0, 0)
        cr.translate(cX + self.initialPosition[0], cY + self.initialPosition[1])