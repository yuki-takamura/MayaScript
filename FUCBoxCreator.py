import maya.mel as mel
import pymel.core as pm

def FUCBoxCreator():
    pm.polyCube(name = 'FUC_Box')
    mel.eval('setAttr "FUC_Box.overrideEnabled" 1;')
    mel.eval('setAttr "FUC_Box.overrideShading" 0;')
