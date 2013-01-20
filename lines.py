import cairo
import math
from position import Position
from repeater import Repeater
from lineproperties import LineProperties

class Lines:

    def __init__(self, initialLength, position, repeater, lineProperties):
        self.initialLength = initialLength
        self.position = position
        self.repeater = repeater
        self.lineProperties = lineProperties

    def draw(self, cr, frame, time):
        self.position.move(cr, frame, time)
        self.lineProperties.setInitialDrawingContext(cr)
        self.repeater.repeat(cr, frame, time, self.lineProperties, self.drawInitialLine)
        
    def drawInitialLine(self, cr):
        cr.move_to(0,0)
        cr.line_to(self.initialLength, 0)
        cr.stroke()