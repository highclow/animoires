import math
from gi.repository import Gtk, Gdk
from animation import Animation
from gui import Window
from shapes import Shape, InitialShapeFactory
from lineproperties import LineProperties
from transformations import Translation, Rotation, \
    Scale, Composition, TranslaterFactory, \
    RotaterFactory, ScalerFactory
from repeaters import TransformationRepeater, MultiRepeater


def animFactory(width, height, duration, frameRate):
    animation = Animation(width, height, duration, frameRate)

    frequency = 0.5
    amplitude = 5

    nbRep = 50
    initRad = 10

    sX = 1.0
    sY = 1.0

    lp = LineProperties((0, 0, 0), 1.0)

    isf = InitialShapeFactory()
    tf = TranslaterFactory()
    rf = RotaterFactory()
    sf = ScalerFactory()

    t1 = Translation(tf.infiniteSegmentBounce(frequency,
        amplitude, math.pi / 2))
    t2 = Translation(tf.infiniteCircle((0, 0), frequency, 1, (0, 20)))
    t3 = Translation(tf.infiniteCircle((0, 0), frequency, -1, (0, 20)))

    r1 = Rotation(rf.regularFrequencyRotation(frequency))
    tr1 = Composition([t1, r1])
    s1 = Scale(sf.arithmeticScale(sX, sY))
    rp1 = TransformationRepeater(100, s1)

    te1 = Shape((500, 500), isf.getEllipse(5, (1.0, 1.0)),
        repeater=rp1)
    te2 = Shape((500, 500), isf.getEllipse(7, (1.1, 1.0)),
        transformation=t2, repeater=rp1)
    tr1 = Shape((500, 500), isf.getRectangle(10, 10),
        repeater=rp1)

    r2 = Rotation(rf.regularFrequencyRotation(1.0 / 240))
    rp2 = TransformationRepeater(240, r2)
    l1 = Shape((500, 500), isf.getLine(400, 0),
        repeater=rp2)
    l2 = Shape((500, 500), isf.getLine(400, 0),
        transformation=t2, repeater=rp2)
    l3 = Shape((500, 500), isf.getLine(400, 0),
        transformation=t3, repeater=rp2)
    #animation.addMovShape(te1)
    #animation.addMovShape(te2)
    #animation.addMovShape(tr1)
    animation.addMovShape(l1)
    animation.addMovShape(l2)
    animation.addMovShape(l3)

    return animation


def main():
    width = 1000
    height = 1000
    duration = 2
    frameRate = 25
    animation = animFactory(width, height, duration, frameRate)
    app = Window(animation)
    Gtk.main()

if __name__ == "__main__":
    main()
