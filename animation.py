class Animation:

    def __init__(self, width, height, duration, frameRate):
        self.width = width
        self.height = height
        self.duration = duration
        self.frameRate = frameRate
        self.frameFrequency = 1.0 / frameRate
        self.movShapes = []

    def addMovShape(self, movShape):
        self.movShapes.append(movShape)

    def draw(self, cr, time):
        for movShape in self.movShapes:
            cr.save()
            movShape.draw(cr, time)
            cr.restore()
