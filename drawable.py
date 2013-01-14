import cairo

class Drawable(object):

    def __init__(self, (r, g, b), lineWidth):
        self.r = r
        self.g = g
        self.b = b
        self.lineWidth = lineWidth

    def setDrawingContext(self, cr):
        cr.set_source_rgb(self.r, self.g, self.b)
        cr.set_line_width(self.lineWidth)