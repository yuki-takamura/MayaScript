import FUCBoxCreator
import FUCSphereCreator

def MakePrimitive(s) :
    BOX = 1
    SPHERE = 2

    if s == BOX:
        FUCBoxCreator.FUCBoxCreator()
    elif s == SPHERE:
        FUCSphereCreator.FUCSphereCreator()
