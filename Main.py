import pymel.core as pm
import FUCBoxCreator
import FUCSphereCreator
import ChangeDrawOverride as changer

from functools import partial

def MakePrimitive(s) :
    BOX = 1
    SPHERE = 2

    if s == BOX:
        FUCBoxCreator.FUCBoxCreator()
    elif s == SPHERE:
        FUCSphereCreator.FUCSphereCreator()

with pm.window(title='Collider Edit'):
    with pm.columnLayout(adjustableColumn = True):
        pm.text(label = 'Primitive')
        rdoGrp = pm.radioButtonGrp(numberOfRadioButtons = 2,
        label = 'Box or Sphere    ',
        labelArray2 = ['Box', 'Sphere'])

        pm.separator(style = 'none')

        selectNum = rdoGrp.getSelect()
        pm.button(label = 'create', c = 'MakePrimitive(selectNum)')

        pm.separator(style = 'none')

        pm.columnLayout( adjustableColumn = False)

        pm.text(label = '表示切替')

        pm.button(label = 'シェーディング', c = 'changer.ChangeShadingMode(selectNum, True)')
        pm.button(label = 'ワイヤ', c = 'changer.ChangeShadingMode(selectNum, False)')
        pm.button(label = '非表示', c = 'changer.ChangeVisibility(selectNum, False)')
        pm.button(label = '表示', c = 'changer.ChangeVisibility(selectNum, True)')
