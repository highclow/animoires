import cProfile
import pstats
import math
import cairo
from gi.repository import Gtk, Gdk
from Animations.AnimationFactory import AnimationFactory
from Printers.Gui import Window

def main():
    animationFactory = AnimationFactory()
    animation = animationFactory.getAnimation('animoire_1')
    if animation is not None:
        app = Window(animation)
        Gtk.main()
    else:
        print 'Couldn''t generate animation ...'


if __name__ == "__main__":
    main()
    #cProfile.run('main()')
