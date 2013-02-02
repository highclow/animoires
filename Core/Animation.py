class Animation:

    def __init__(self, width, height, duration, frameRate, movingShapes=[]):
        self.width = width
        self.height = height
        self.duration = duration
        self.frameRate = frameRate
        self.nbFrames = int(duration * frameRate)
        self.frameFormat = format(len(str(self.nbFrames)), "02d") + "d"
        self.movingShapes = movingShapes

    def getAnimationCenter(self):
        return (self.width / 2.0, self.height / 2.0)

    def addmovingShape(self, movingShape):
        self.movingShapes.append(movingShape)

    def draw(self, cr, time):
        for movingShape in self.movingShapes:
            cr.save()
            movingShape.draw(cr, time)
            cr.restore()
