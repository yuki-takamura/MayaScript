import pymel.core as pm
import maya.mel as mel
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

        buttonName = 'create'
        createEvent = 'maker.MakePrimitive(rdoGrp.getSelect()),'
        createEvent += 'pm.disable(buttonName)'

        if rdoGrp.getSelect() != 0:
            pm.button(buttonName, label = 'create', c = createEvent)
        pm.disable(buttonName)

        pm.separator(style = 'none')

        pm.columnLayout(adjustableColumn = False)

        pm.text(label = '表示切替')

        pm.button(label = 'シェーディング', c = 'changer.ChangeShadingMode(rdoGrp.getSelect(), True)')
        pm.button(label = 'ワイヤ', c = 'changer.ChangeShadingMode(rdoGrp.getSelect(), False)')
        pm.button(label = '非表示', c = 'changer.ChangeVisibility(rdoGrp.getSelect(), False)')
        pm.button(label = '表示', c = 'changer.ChangeVisibility(rdoGrp.getSelect(), True)')

        pm.separator()

        #pm.text(label = 'バウンディングスフィア')
        #sld = pm.floatSliderGrp(label = '半径')
