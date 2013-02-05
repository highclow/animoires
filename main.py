import cProfile
import pstats
import math
import cairo
from gi.repository import Gtk, Gdk
from Controllers.PngDrawer import PngDrawer
from Controllers.VideoMaker import VideoMaker
from Animations.AnimationFactory import AnimationFactory

from Controllers.JsonPrinter import JsonPrinter
from Controllers.Marshaller import Marshaller


def main():
    videoFileName = "test.mp4"
    jsonFileName = "test.json"
    anmFileName = "test.anm"

    animationFactory = AnimationFactory()
    animation = animationFactory.getAnimation('test2')
    if animation is not None:
        #videoMaker = VideoMaker()
        #videoMaker.makeClean(animation, videoFileName)
        jsonPrinter = JsonPrinter()
        jsonPrinter.printObject(animation, jsonFileName)
    else:
        print 'Couldn''t generate animation ...'

if __name__ == "__main__":
    main()
    #cProfile.run('main()')
