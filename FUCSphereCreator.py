import maya.mel as mel
import pymel.core as pm

def FUCSphereCreator():
    try:
        pm.select('FUC_Box')
        pm.delete()
    except:
        pass

    try:
        pm.select('FUC_Sphere')
        pm.delete()
    except:
        pass

    pm.polySphere(name = 'FUC_Sphere')
    mel.eval('setAttr "FUC_Sphere.overrideEnabled" 1;')
    mel.eval('setAttr "FUC_Sphere.overrideShading" 0;')
