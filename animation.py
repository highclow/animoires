import gobject

class Animation:
    
    def __init__(self):
        self.stop = True
        self.darea = None
        self.frameRate = 25
        self.t = 0
        self.movShapes = []

    def init(self, darea, frameRate):
        self.darea = darea
        self.frameRate = frameRate

    def run(self):
        gobject.timeout_add(1000 / self.frameRate, self.changeFrame)

    def addMovShape(self, movShape):
        self.movShapes.append(movShape)

    def changeFrame(self):
        self.t = self.t + 1
        self.darea.queue_draw()
        return not self.stop

    def draw(self, cr):
        for movShape in self.movShapes:
            cr.save()
            movShape.setDrawingContext(cr)
            movShape.move(cr, self.t)
            movShape.draw(cr)
            cr.restore()