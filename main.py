from gi.repository import Gtk, Gdk
from animation import Animation
from gui import Window
from position import Position
from repeater import Repeater
from lineproperties import LineProperties
from circles import Circles
from ellipses import Ellipses
from lines import Lines
from moveFunctions import periodicTriangle, circle, arithmeticRep
from repeatFunctions import arithmeticScale

def animFactory(width, height, frameRate):
    animation = Animation(width, height, frameRate)

    frequency = 0.5
    amplitude = 10
    movBF = lambda n, f, t : periodicTriangle(frequency, amplitude, "H", n, f, t)
    movBFM = lambda n, f, t : periodicTriangle(frequency, -amplitude, "H", n, f, t)

    center = (300, 300)
    movC = lambda i, f, t : circle(center, frequency, "H", i, f, t)
    movCM = lambda i, f, t : circle(center, frequency, "A", i, f, t)

    progX1 = 0.0
    progY1 = 5.0
    arithScale1 = lambda i, f, t : arithmeticScale(progX1, progY1, i, f, t)

    arithRep1 = lambda i, f, t : arithmeticRep(progX1, progY1, i, f, t)

    progX2 = 1.4
    progY2 = 1.0
    arithScale2 = lambda i, f, t : arithmeticScale(progX2, progY2, i, f, t)

    nbRep = 50
    initRad = 5

    lp = LineProperties((0,0,0), 2.0)

    pc1 = Position((330, 300), movBFM)
    rpc1 = Repeater(nbRep, scaler=arithScale1)
    c1 = Circles(initRad, pc1, rpc1, lp)

    pc2 = Position((270, 300), movBF)
    rpc2 = Repeater(nbRep, translater=arithRep1, scaler=arithScale1)
    c2 = Circles(initRad, pc2, rpc2, lp)

    pe1 = Position((300, 300))
    rpe1 = Repeater(nbRep, scaler=arithScale2)
    e1 = Ellipses(initRad, (1.0, 1.0), pe1, rpe1, lp)


    pl1 = Position((100, 100))
    rpl1 = Repeater(70, translater=arithRep1)
    l1 = Lines(400, pl1, rpl1, lp)

    animation.addMovShape(e1)
    #animation.addMovShape(c1)
    #animation.addMovShape(c2)
    animation.addMovShape(l1)

    return animation

def main():
    width = 1000
    height = 1000
    frameRate = 25;
    animation = animFactory(width, height, frameRate)
    app = Window(animation)
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()