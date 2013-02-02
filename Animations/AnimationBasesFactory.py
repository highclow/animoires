from Core.Animation import Animation


class AnimationBasesFactory(object):
    def __init__(self):
        self.animationBases = {
            '640x360-1s-25fps':Animation(640, 360, 1, 25.0),
            '640x360-5s-25fps':Animation(640, 360, 5, 25.0),
            '640x360-20s-25fps':Animation(854, 480, 20, 25.0),
            '854x480-5s-25fps':Animation(854, 480, 5, 25.0),
            '854x480-20s-25fps':Animation(854, 480, 20, 25.0),
            '1280x720-5s-25fps':Animation(1280, 720, 5, 25.0),
            '1280x720-20s-25fps':Animation(1280, 720, 20, 25.0),
            '1920x1080-5s-25fps':Animation(1920, 1080, 5, 25.0),
            '1920x1080-20s-25fps':Animation(1920, 1080, 20, 25.0)
        }

    def getAnimationBase(self, animationBaseName):
        if animationBaseName in self.animationBases:
            return  self.animationBases[animationBaseName]
        else:
            return None