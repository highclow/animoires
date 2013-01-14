from gi.repository import Gtk, Gdk
from animation import Animation
from gui import Window
from circles import Circles
from ellipses import Ellipses
from moveFunctions import movBackAndForth

def initAnim(anim):
    c1 = Circles((0,0,0), 1.0, (300, 300), (None, movBackAndForth), 50, lambda x : x *  5)
    
    e1 = Ellipses((0,0,0), 1.0, (300, 300), (None, None), (1.0, 0.9), 50, lambda x : x *  5)

    c2 = Circles((0,0,0), 1.0, (300, 300), (movBackAndForth, None), 50, lambda x : x *  5)

    anim.addMovShape(e1)
    anim.addMovShape(c1)
    anim.addMovShape(c2)

def main():
    
    frameRate = 25;

    animation = Animation()
    app = Window()

    animation.init(app.darea, frameRate)
    app.initAnimation(animation)

    initAnim(animation)

    Gtk.main()
        
        
if __name__ == "__main__":    
    main()