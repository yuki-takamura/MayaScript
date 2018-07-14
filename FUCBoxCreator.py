import maya.mel as mel
import pymel.core as pm
import maya.cmds as cmds

def FUCBoxCreator():
    pos = [0, 0, 0]
    thisW = 1
    thisH = 1
    thisD = 1

    try:
        pm.select('FUC_Box')
        pos = cmds.objectCenter('FUC_Box', gl = True)
        thisW = pm.getAttr('FUC_Box' + '.sx')
        thisH = pm.getAttr('FUC_Box' + '.sy')
        thisD = pm.getAttr('FUC_Box' + '.sz')
        pm.delete()
    except:
        pass

    try:
        pm.select('FUC_Sphere')
        pos = cmds.objectCenter('FUC_Sphere', gl = True)
        r = pm.getAttr('FUC_Sphere' + '.sx')
        thisW = r
        thisH = thisW
        thisD = thisW
        pm.delete()
    except:
        pass

    pm.polyCube(name = 'FUC_Box')
    pm.move(pos)
    pm.scale(thisW, thisH, thisD)
    mel.eval('setAttr "FUC_Box.overrideEnabled" 1;')
    mel.eval('setAttr "FUC_Box.overrideShading" 0;')
