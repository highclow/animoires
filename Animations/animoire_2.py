from Core.Animation import Animation
from Core.Shapes import Shape
from Core.LineProperties import LineProperties
from Core.Transformations import Translation, Rotation, Scale
from Core.Repeaters import TransformationRepeater


def getAnimation(animationBasesFactory, initialShapeFactory,
        translaterFactory, rotaterFactory, scalerFactory):

    # Get animation base
    #animationBaseName = '1280x720-20s-25fps'
    animationBaseName = '640x360-5s-25fps'
    animation = animationBasesFactory.getAnimationBase(animationBaseName)
    if animation is None:
        return None

    animationCenter = animation.getAnimationCenter()

    # Line From (shape.InitialPosition)
    # To (shape.InitialPosition) + (x, y)
    radius = 7
    ellispeScaleValues = (1.0, 1.0)
    ellipse = initialShapeFactory.getEllipse(radius, ellispeScaleValues)

    # Line properties
    linesColor = (0, 0, 0)  # black
    lineWidth = 1.5
    lineProperties = LineProperties(linesColor, lineWidth)

    # Star using Lines repeater
    # Rotation repeater using line
    # Regularly rotate nbLines times around (shape.InitialPosition)
    nbEllipses = 100
    arithScaleValues = (2.0, 1.2)
    arithScale = Scale(scalerFactory.arithmeticScale(arithScaleValues))
    scaleRepeater = TransformationRepeater(nbEllipses, arithScale)

    # Shape 1 : Concentric ellipses Not moving
    # Centered
    initialPosition1 = animationCenter
    shape1 = Shape(initialPosition1, ellipse, lineProperties,
        repeater=scaleRepeater)

    # Shape 2 : Star moving along a circle
    # Rotation around center clockwise
    # Starting (center) + (0, -20)
    initialPosition2 = (animationCenter[0] + 20, animationCenter[1])
    frequency2 = 0.2
    rotationCenter2 = animationCenter
    circleTranlation = Translation(translaterFactory.infiniteCircle(
        frequency2, initialPosition2, rotationCenter2))
    shape2 = Shape(initialPosition2, ellipse, lineProperties,
        transformation=circleTranlation, repeater=scaleRepeater)

    # Shape 3 : Star moving along a circle
    # Rotation around shape.InitialPosi anti-clockwise
    # Starting (center) + (0, -20)
    initialPosition3 = (animationCenter[0] - 20, animationCenter[1])
    frequency3 = 0.2
    rotationCenter3 = animationCenter
    direction3 = -1
    circleTranlationInv = Translation(translaterFactory.infiniteCircle(
        frequency3, initialPosition3, rotationCenter3, direction3))
    shape3 = Shape(initialPosition3, ellipse, lineProperties,
        transformation=circleTranlationInv, repeater=scaleRepeater)

    # Animation using Shapes 1, 2 and 3
    animation.addmovingShape(shape1)
    animation.addmovingShape(shape2)
    #animation.addmovingShape(shape3)

    return animation
