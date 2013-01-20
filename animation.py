class Animation:
    
    def __init__(self, width, height, frameRate):
        self.frameRate = frameRate
        self.width = width
        self.height = height
        self.frameFrequency = 1.0 / frameRate
        self.movShapes = []

    def addMovShape(self, movShape):
        self.movShapes.append(movShape)

    def draw(self, cr, frame):
        time = frame * self.frameFrequency
        for movShape in self.movShapes:
            cr.save()
            movShape.draw(cr, frame, time)
            cr.restore()