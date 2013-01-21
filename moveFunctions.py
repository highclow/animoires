import math


def periodicTriangle(frequency, amplitude,
        direction, frame, time):
    if direction == "V":
        return (0.0, amplitude * (2 * math.asin(
            math.sin(2 * math.pi * frequency * time)) / math.pi))
    else:
        return (amplitude * (2 * math.asin(
            math.sin(2 * math.pi * frequency * time)) / math.pi), 0.0)


def circle((cX, cY), frequency, direction,
        (initX, initY), frame, time):
    r = math.sqrt(((cX - initX) ** 2) + ((cY - initY) ** 2))
    iAngleX = 2 * math.pi * ((initX - cX) / r)
    iAngleY = 2 * math.pi * ((initY - cY) / r)
    print iAngleX
    print iAngleY
    if direction == "H":
        print (2 * math.pi * frequency * time) + iAngleX
        rx = cX + (r * math.cos((2 * math.pi * frequency * time) + iAngleX))
        ry = cY + (r * math.sin((2 * math.pi * frequency * time) + iAngleY))
        return (rx, ry)
    else:
        rx = cX + (r * math.cos(-2 * math.pi * frequency * time))
        ry = cY + (r * math.sin(-2 * math.pi * frequency * time))
        return (rx, ry)


def arithmeticRep(progX, progY, repNumber, frame, time):
    return (progX * repNumber, progY * repNumber)
