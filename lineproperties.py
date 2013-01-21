import cairo


class LineProperties:

    def __init__(self, initialRGB, initialLW, changer=None):
        self.initialRGB = initialRGB
        self.initialLW = initialLW
        self.changer = changer

    def setInitialDrawingContext(self, cr):
        cr.set_source_rgb(self.initialRGB[0], \
            self.initialRGB[1], self.initialRGB[2])
        cr.set_line_width(self.initialLW)

    def setDrawingContext(self, cr, repNumber, frame, time):
        if self.changer is not None:
            (rgb, lw) = self.changer(self.initialRGB, \
                self.initialLW, repNumber, frame, time)
        else:
            (rgb, lw) = (self.initialRGB, self.initialLW)
        cr.set_source_rgb(rgb[0], rgb[1], rgb[2])
        cr.set_line_width(lw)
