import cProfile
import pstats
import math
import cairo
from gi.repository import Gtk, Gdk
from Printers.PngDrawer import PngDrawer
from Printers.VideoMaker import VideoMaker


from Animations.AnimationFactory import AnimationFactory
from Printers.Gui import Window

def main():
    fileName = "test.mp4"
    animationFactory = AnimationFactory()
    animation = animationFactory.getAnimation('animoire_1')
    if animation is not None:
        videoMaker = VideoMaker()
        videoMaker.makeClean(animation, fileName)
    else:
        print 'Couldn''t generate animation ...'

if __name__ == "__main__":
    main()
    #cProfile.run('main()')
