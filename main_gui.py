import cProfile
import pstats
import math
import cairo
import jsonpickle
from gi.repository import Gtk, Gdk
from Core.Animation import Animation
from Animations.AnimationFactory import AnimationFactory
from Controllers.Gui import Window


def main():
    animationFactory = AnimationFactory()
    animation = animationFactory.getAnimation('test3')
    #f = open('test.json')
    #json_str = f.read()
    #animation = jsonpickle.decode(json_str)

    if (isinstance(animation, Animation) and
        animation is not None):
        app = Window(animation)
        Gtk.main()
    else:
        print 'Couldn''t generate animation ...'


if __name__ == "__main__":
    main()
    #cProfile.run('main()')
