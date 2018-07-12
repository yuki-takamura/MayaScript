import pymel.core as pm
import MakePrimitive as maker
import ChangeDrawOverride as changer

from functools import partial

with pm.window(title='Collider Edit'):
    with pm.columnLayout(adjustableColumn = True):
        pm.text(label = 'Primitive')
        rdoGrp = pm.radioButtonGrp(numberOfRadioButtons = 2,
        label = 'Box or Sphere    ',
        labelArray2 = ['Box', 'Sphere'])

        pm.separator(style = 'none')

        pm.button(label = 'create', c = 'maker.MakePrimitive(rdoGrp.getSelect())')

        pm.separator(style = 'none')

        pm.columnLayout(adjustableColumn = False)

        pm.text(label = '表示切替')

        pm.button(label = 'シェーディング', c = 'changer.ChangeShadingMode(rdoGrp.getSelect(), True)')
        pm.button(label = 'ワイヤ', c = 'changer.ChangeShadingMode(rdoGrp.getSelect(), False)')
        pm.button(label = '非表示', c = 'changer.ChangeVisibility(rdoGrp.getSelect(), False)')
        pm.button(label = '表示', c = 'changer.ChangeVisibility(rdoGrp.getSelect(), True)')
