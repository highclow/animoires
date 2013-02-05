from AbstractShape import AbstractShape


class Line(AbstractShape):

    def __init__(self, initialPosition, (lengthX, lengthY),
            lineProps=defaultLineProperties(),
            transformation=Translation(),
            repeater=defaultRepeater()):
        AbstractShape.__init__(self, initialPosition,
            lineProps, transformation, repeater)
        self.lengthX = lengthX
        self.lengthY = lengthY

    def drawInitialShape(self, cr):
        cr.move_to(0, 0)
        cr.line_to(self.lengthX, self.lengthY)
        cr.stroke