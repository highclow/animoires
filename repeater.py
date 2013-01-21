import cairo


class Repeater:

    def __init__(
            self, numberRepetitions, translater=None,
            rotater=None, scaler=None):
        self.numberRepetitions = numberRepetitions
        self.translater = translater
        self.rotater = rotater
        self.scaler = scaler

    def repeat(self, cr, frame, time, lineProps, initialDrawer):
        for i in range(1, self.numberRepetitions + 1):
            cr.save()
            if (lineProps is not None):
                lineProps.setDrawingContext(cr, i, frame, time)
            if (self.translater is not None):
                (tX, tY) = self.translater(i, frame, time)
                cr.translate(tX, tY)
            if (self.rotater is not None):
                angle = self.rotater(i, frame, time)
                cr.rotate(angle)
            if (self.scaler is not None):
                lw = cr.get_line_width()
                (sX, sY) = self.scaler(i, frame, time)
                cr.scale(sX, sY)
                cr.set_line_width(lw / sX)
            initialDrawer(cr)
            cr.restore()
