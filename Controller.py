#UIの参考(実際には使わない)

import pymel.core as pm

with pm.window(title='controller sampler UI'):
    with pm.columnLayout(adjustableColumn = True):
        pm.text(label = 'radio button')
        rdoGrp = pm.radioButtonGrp(numberOfRadioButtons = 3,
        label = 'x/y/z',
        labelArray3 = ['x', 'y', 'z'])

        pm.separator(style = 'none')

        pm.text(label = 'check box')
        boxGrp = pm.checkBoxGrp(numberOfCheckBoxes = 3,
        label = 'box group',
        labelArray3 = ['X', 'Y', 'Z'])

        pm.separator()

        box1 = pm.checkBox(label = 'Check 1')
        box2 = pm.checkBox(label = 'Check 2')
        pm.button(label = 'print',
        c = 'print box1.getValue(), box2.getValue()')

        pm.text(label = 'float field')
        fField = pm.floatFieldGrp(numberOfFields = 1,
        label = 'some value')

        pm.separator()

        pm.text(label = 'slider')
        sld = pm.floatSliderGrp(label = 'slider')

        pm.separator()

        pm.text(label = 'text field')
        txt = pm.textFieldGrp(label = 'text field',
        pht = 'please input text...')

        pm.separator()

        cmdString = 'print '
        cmdString += 'rdoGrp.getSelect(),'
        cmdString += 'boxGrp.getValueArray4(),'
        cmdString += 'fField.getValue()[0],'
        cmdString += 'sld.getValue(),'
        cmdString += 'txt.getText(),'

        pm.button(label = 'print', c = cmdString)
