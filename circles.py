﻿import cairo
import math
from position import Position
from repeater import Repeater
from lineproperties import LineProperties

class Circles:

    def __init__(self, initialRadius, position, repeater, lineProperties):
        self.initialRadius = initialRadius
        self.position = position
        self.repeater = repeater
        self.lineProperties = lineProperties

    def draw(self, cr, frame, time):
        self.position.move(cr, frame, time)
        self.lineProperties.setInitialDrawingContext(cr)
        self.repeater.repeat(cr, frame, time, self.lineProperties, self.drawInitialCircle)
        
    def drawInitialCircle(self, cr):
        cr.arc(0, 0, self.initialRadius, 0, 2*math.pi)
        cr.stroke()