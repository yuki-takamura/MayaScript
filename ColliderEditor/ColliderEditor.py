import pymel.core as pm
import maya.mel as mel
import MakePrimitive as maker
import ChangeDrawOverride as changer
import DeleteFUC as dFUC

from functools import partial

with pm.window(title='ColliderEditor') as editorWin:
    with pm.columnLayout(adjustableColumn = False):
        pm.text(label = 'Primitive', fn = 'boldLabelFont')
        rdoGrp = pm.radioButtonGrp(numberOfRadioButtons = 2,
        labelArray2 = ['Box', 'Sphere'],
        on1 = 'maker.MakePrimitive(rdoGrp.getSelect())',
        on2 = 'maker.MakePrimitive(rdoGrp.getSelect())')

        pm.separator(style = 'none')
        pm.text(label = '')
        pm.button(label = 'Delete', c = 'dFUC.DeleteFUC(),')

        pm.separator(style = 'none')
        pm.text(label = '')

        pm.columnLayout(adjustableColumn = False)

        pm.text(label = 'Change View Mode', fn = 'boldLabelFont')

        pm.checkBox(label = 'Wireframe or Shading',
        onc = 'changer.ChangeShadingMode(rdoGrp.getSelect(), True)',
        ofc = 'changer.ChangeShadingMode(rdoGrp.getSelect(), False)')

        pm.checkBox(label = 'View',
        v = True,
        onc = 'changer.ChangeVisibility(rdoGrp.getSelect(), True)',
        ofc = 'changer.ChangeVisibility(rdoGrp.getSelect(), False)')

        pm.separator(style = 'none')
        pm.text(label = '')
        pm.button(label = 'Close', c = 'editorWin.delete()')
