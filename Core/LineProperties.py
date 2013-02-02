import cairo


class LineProperties:

    def __init__(self, initialRGB, initialLW, changer=None):
        self.initialRGB = initialRGB
        self.initialLW = initialLW
        self.changer = changer

    def setDrawingContext(self, cr, value=None):
        if (self.changer is not None) and (value is not None):
            (rgb, lw) = self.changer(self.initialRGB, \
                self.initialLW, value)
        else:
            (rgb, lw) = (self.initialRGB, self.initialLW)
        cr.set_source_rgb(rgb[0], rgb[1], rgb[2])
        cr.set_line_width(lw)


def defaultLineProperties():
    return LineProperties((0, 0, 0), 1.0)
