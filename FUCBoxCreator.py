import maya.mel as mel
import pymel.core as pm

def FUCBoxCreator():
    try:
        pm.select('FUC_Sphere')
        pm.delete()
    except:
        pass

    try:
        pm.select('FUC_Box')
        pm.delete()
    except:
        pass

    pm.polyCube(name = 'FUC_Box')
    mel.eval('setAttr "FUC_Box.overrideEnabled" 1;')
    mel.eval('setAttr "FUC_Box.overrideShading" 0;')
