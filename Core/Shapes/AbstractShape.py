import math
from Core.Transformations.Translations import Translation
from ..LineProperties import defaultLineProperties
from ..Repeaters import defaultRepeater


class AbstractShape(object):

    def __init__(self, (initialX, initialY),
            lineProps=defaultLineProperties(),
            transformation=Translation(),
            repeater=defaultRepeater()):
        self.initialX = initialX
        self.initialY = initialY
        self.lineProps = lineProps
        self.transformation = transformation
        self.repeater = repeater   

    def drawInitialShape(self, cr):
        pass

    def draw(self, cr, time):
        cr.translate(self.initialX, self.initialY)
        self.lineProps.setDrawingContext(cr)
        self.transformation.transform(cr, time)
        self.repeater.repeat(cr, time, self.drawInitialShape)