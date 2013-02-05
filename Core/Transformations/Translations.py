import math
import cairo
import sys


class Translation(object):

    def __init__(self, step=0, angle=0):
        self.step = step
        self.angle = angle
        self.cos = math.cos(angle)
        self.sin = math.sin(angle)

    def getTranslation(self, value):
        dist = self.step * value
        tX =  self.cos * dist
        tY =  self.sin * dist
        return (tX, tY)

    def transform(self, cr, value):
        (tX, tY) = self.getTranslation(value)
        cr.translate(tX, tY)


class SegmentBackAndForth(Translation):

    def __init__(self, frequency, amplitude, angle=0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.angle = angle
        self.cos = math.cos(angle)
        self.sin = math.sin(angle)

    def getTranslation(self, value):
        dist = self.amplitude * (2 * math.asin(
            math.sin(2 * math.pi * frequency * value)) / math.pi)
        tX =  self.cos * dist
        tY =  self.sin * dist
        return (tX, tY)


class Circle(Translation):

    def __init__(self, frequency,
        (initialX, initialY),
        (centerX, centerY),
        direction=1):
        # Initial parameters
        self.frequency = frequency
        self.initialX = initialX
        self.initialY = initialY
        self.centerX = centerX
        self.centery = centerY
        self.direction = direction

        #Calculated parameters
        self.dX = initialX - centerX
        self.dY = initialY - centerY
        self.radius = math.sqrt((self.dX ** 2) + (self.dY ** 2))
        self.signeAngle = math.copysign(1, math.asin(self.dY / self.radius))
        self.initialAngle = signeAngle * math.acos(self.dX / self.radius)
        self.d = math.copysign(1, direction)

    def getTranslation(self, value):
        angle= self.d * 2 * math.pi * self.frequency * value
        tX = self.radius * math.cos(angle + self.initialAngle) - self.dX
        ty = self.radius * math.sin(angle + self.initialAngle) - self.dY
        return (tX, tY)
