import cairo
from transformations import IdentityTransformation


class Repeater:

    pass


class TransformationRepeater:

    def __init__(self, numberRepetitions,
            transformation=IdentityTransformation(),
            indexChanger=lambda x, y: x):
        self.numberRepetitions = numberRepetitions
        self.transformation = transformation
        self.indexChanger = indexChanger

    def repeat(self, cr, time, initialDrawer):
        for i in range(1, self.numberRepetitions + 1):
            if (self.indexChanger is not None):
                i = self.indexChanger(i, time)
            cr.save()
            self.transformation.transform(cr, i)
            initialDrawer(cr)
            cr.restore()


class MultiRepeater:

    def __init__(self, repeaters):
        self.repeaters = repeaters

    def repeat(self, cr, time, initialDrawer):
        for r in repeaters:
            r.repeat(cr, time, initialDrawer)


def defaultRepeater():
    return TransformationRepeater(1)
