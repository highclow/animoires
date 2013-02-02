from Core.Animation import Animation
from Core.Shapes import InitialShapeFactory
from Core.Transformations import TranslaterFactory, \
    RotaterFactory, ScalerFactory
from AnimationBasesFactory import AnimationBasesFactory
import animoire_1


class AnimationFactory(object):

    def __init__(self):
        animationBasesFactory = AnimationBasesFactory()
        initialShapeFactory = InitialShapeFactory()
        translaterFactory = TranslaterFactory()
        rotaterFactory = RotaterFactory()
        scalerFactory = ScalerFactory()

        self.animations = {
            'animoire_1':animoire_1.getAnimation(
                animationBasesFactory,
                initialShapeFactory,
                translaterFactory,
                rotaterFactory)
        }

    def getAnimation(self, animationName):
        if animationName in self.animations:
            return  self.animations[animationName]
        else:
            return None


