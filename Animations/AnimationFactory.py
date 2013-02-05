from Core.Animation import Animation
from Core.Transformations.Transformations import ScalerFactory
from AnimationBaseFactory import AnimationBaseFactory
#import animoire_1
#import animoire_2
import animoire_3


class AnimationFactory(object):

    def __init__(self):
        animationBaseFactory = AnimationBaseFactory()
        #initialShapeFactory = InitialShapeFactory()
        #translaterFactory = TranslaterFactory()
        #rotaterFactory = RotaterFactory()
        scalerFactory = ScalerFactory()
        self.animations = {
            #'test1': animoire_1.getAnimation(
            #    animationBaseFactory,
            #    initialShapeFactory,
            #    translaterFactory,
            #    rotaterFactory),
            #'test2': animoire_2.getAnimation(
            #    animationBaseFactory,
            #    initialShapeFactory,
            #    translaterFactory,
            #    rotaterFactory,
            #    scalerFactory)
            'test3': animoire_3.getAnimation(
                animationBaseFactory,
                scalerFactory)
        }

    def getAnimation(self, animationName):
        if animationName in self.animations:
            return  self.animations[animationName]
        else:
            return None
