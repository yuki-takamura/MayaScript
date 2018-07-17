import maya.mel as mel
import pymel.core as pm
import maya.cmds as cmds

def FUCSphereCreator():
    pos = [0, 0, 0]
    thisR = 1

    try:
        pm.select('FUC_Sphere')
        pos = cmds.objectCenter('FUC_Sphere')
        thisR = pm.getAttr('FUC_Sphere' + '.sx')
        pm.delete()
    except:
        pass

    try:
        pm.select('FUC_Box')
        pos = cmds.objectCenter('FUC_Box', gl = True)
        w = pm.getAttr('FUC_Box' + '.sx')
        h = pm.getAttr('FUC_Box' + '.sy')
        d = pm.getAttr('FUC_Box' + '.sz')
        thisR = (w + h + d) / 3
        pm.delete()
    except:
        pass

    pm.polySphere(name = 'FUC_Sphere', r = 1)
    pm.move(pos)
    pm.scale(thisR, thisR, thisR)
    mel.eval('setAttr "FUC_Sphere.overrideEnabled" 1;')
    mel.eval('setAttr "FUC_Sphere.overrideShading" 0;')
