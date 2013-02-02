import cairo


class PngDrawer(object):

    def __init__(self, animation):
        self.animation = animation

    def fillWhiteBackground(self, cr, width, height):
        cr.save()
        pat = cairo.SolidPattern(1.0, 1.0, 1.0)
        cr.rectangle(0, 0, width, height)
        cr.set_source(pat)
        cr.fill()
        cr.restore()

    def drawPng(self, fileName, time):
        if time < self.animation.duration:
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                self.animation.width, self.animation.height)
            cr = cairo.Context(surface)
            self.fillWhiteBackground(cr,
                self.animation.width, self.animation.height)
            self.animation.draw(cr, time)  # Draw the image
            surface.write_to_png(fileName)  # Output to PNG

    def drawAnimationPngs(self, dirName):
        for frame in range(self.animation.nbFrames):
            fileName = self.getPngFileName(dirName, frame)
            time = frame / self.animation.frameRate
            self.drawPng(fileName, time)

    def getPngFileName(self, dirName, frame):
        return dirName + "/" + format(frame, self.animation.frameFormat) + ".png"
            
