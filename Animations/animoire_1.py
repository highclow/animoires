from Core.Animation import Animation
from Core.Shapes import Shape
from Core.LineProperties import LineProperties
from Core.Transformations import Translation, Rotation
from Core.Repeaters import TransformationRepeater

def getAnimation(animationBasesFactory, initialShapeFactory,
        translaterFactory, rotaterFactory):

    # Get animation base
    #animationBaseName = '1280x720-20s-25fps'
    animationBaseName = '1280x720-20s-25fps'
    animation = animationBasesFactory.getAnimationBase(animationBaseName)
    if animation is None:
        return None

    animationCenter = animation.getAnimationCenter()

    # Line From (shape.InitialPosition)
    # To (shape.InitialPosition) + (x, y)
    x = animation.width * 0.75
    y = 0
    line = initialShapeFactory.getLine(x, y)

    # Line properties
    linesColor = (0, 0, 0)  # black
    lineWidth = 1.5
    lineProperties = LineProperties(linesColor, lineWidth)

    # Star using Lines repeater
    # Rotation repeater using line
    # Regularly rotate nbLines times around (shape.InitialPosition)
    nbLines = 240
    rotation = Rotation(rotaterFactory.regularFrequencyRotation(1.0 / nbLines))
    rotationRepeater = TransformationRepeater(nbLines, rotation)

    # Shape 1 : Star Not moving
    # Centered
    initialPosition1 = animationCenter
    shape1 = Shape(initialPosition1, line, lineProperties,
        repeater=rotationRepeater)

    # Shape 2 : Star moving along a circle
    # Rotation around center clockwise
    # Starting (center) + (0, -20)
    initialPosition2 = (animationCenter[0] + 20, animationCenter[1])
    frequency2 = 0.05
    rotationCenter2 = animationCenter
    circleTranlation = Translation(translaterFactory.infiniteCircle(
        frequency2, initialPosition2, rotationCenter2))
    shape2 = Shape(initialPosition2, line, lineProperties,
        transformation=circleTranlation, repeater=rotationRepeater)

    # Shape 3 : Star moving along a circle
    # Rotation around shape.InitialPosi anti-clockwise
    # Starting (center) + (0, -20)
    initialPosition3 = (animationCenter[0] - 20, animationCenter[1])
    frequency3 = 0.05
    rotationCenter3 = animationCenter
    direction3 = -1
    circleTranlationInv = Translation(translaterFactory.infiniteCircle(
        frequency3, initialPosition3, rotationCenter3, direction3))
    shape3 = Shape(initialPosition3, line, lineProperties,
        transformation=circleTranlationInv, repeater=rotationRepeater)
  
    # Animation using Shapes 1, 2 and 3
    animation.addmovingShape(shape1)
    animation.addmovingShape(shape2)
    animation.addmovingShape(shape3)

    return animation
