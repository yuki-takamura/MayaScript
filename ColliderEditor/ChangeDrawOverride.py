import maya.mel as mel

BOX = 1
SPHERE = 2

def ChangeShadingMode(obj, isShading):
    if isShading:
        if obj == BOX:
            mel.eval('setAttr "FUC_Box.overrideShading" 1;')
        elif obj == SPHERE:
            mel.eval('setAttr "FUC_Sphere.overrideShading" 1;')
    else:
        if obj == BOX:
            mel.eval('setAttr "FUC_Box.overrideShading" 0;')
        elif obj == SPHERE:
            mel.eval('setAttr "FUC_Sphere.overrideShading" 0')


def ChangeVisibility(obj, visible):
    if visible:
        if obj == BOX:
            mel.eval('setAttr "FUC_Box.overrideVisibility" 1;')
        elif obj == SPHERE:
            mel.eval('setAttr "FUC_Sphere.overrideVisibility" 1;')
    else:
        if obj == BOX:
            mel.eval('setAttr "FUC_Box.overrideVisibility" 0;')
        elif obj == SPHERE:
            mel.eval('setAttr "FUC_Sphere.overrideVisibility" 0;')
