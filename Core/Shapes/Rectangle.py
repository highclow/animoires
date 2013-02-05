from AbstractShape import AbstractShape


class Rectangle(AbstractShape):

    def __init__(self, initialPosition, (width, height),
            lineProps=defaultLineProperties(),
            transformation=Translation(),
            repeater=defaultRepeater()):
        AbstractShape.__init__(self, initialPosition,
            lineProps, transformation, repeater)
        self.width = width
        self.height = height

    def drawInitialShape(self, cr):
        cr.save()
        cr.translate(-self.width / 2, -self.height / 2),
        cr.rectangle(0, 0, self.width, self.height)
        cr.stroke()
        cr.restore()