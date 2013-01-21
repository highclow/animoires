import math


def arithmeticScale(progX, progY, repNumber, frame, time):
    sX = 1.0 + (progX * repNumber)
    sY = 1.0 + (progY * repNumber)
    return (sX, sY)
