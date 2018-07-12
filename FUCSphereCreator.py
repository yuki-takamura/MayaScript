import maya.mel as mel
import pymel.core as pm

def FUCSphereCreator():
    pm.polySphere(name = 'FUC_Sphere')
    mel.eval('setAttr "FUC_Sphere.overrideEnabled" 1;')
    mel.eval('setAttr "FUC_Sphere.overrideShading" 0;')
