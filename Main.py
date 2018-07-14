import pymel.core as pm
import maya.mel as mel
import MakePrimitive as maker
import ChangeDrawOverride as changer

from functools import partial

with pm.window(title='コライダ エディタ') as editorWin:
    with pm.columnLayout(adjustableColumn = False):
        pm.text(label = 'プリミティブ')
        rdoGrp = pm.radioButtonGrp(numberOfRadioButtons = 2,
        labelArray2 = ['Box', 'Sphere'],
        on1 = 'maker.MakePrimitive(rdoGrp.getSelect())',
        on2 = 'maker.MakePrimitive(rdoGrp.getSelect())')

        pm.separator(style = 'none')
        pm.separator(style = 'none')
        pm.text(label = '')

        pm.columnLayout(adjustableColumn = False)

        pm.text(label = '表示切替')

        pm.checkBox(label = 'ワイヤ / シェーディング',
        onc = 'changer.ChangeShadingMode(rdoGrp.getSelect(), True)',
        ofc = 'changer.ChangeShadingMode(rdoGrp.getSelect(), False)')

        pm.checkBox(label = '可視',
        v = True,
        onc = 'changer.ChangeVisibility(rdoGrp.getSelect(), True)',
        ofc = 'changer.ChangeVisibility(rdoGrp.getSelect(), False)')

        pm.separator()

        pm.button(label = '閉じる', c = 'editorWin.delete()')
