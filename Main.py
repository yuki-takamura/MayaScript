import pymel.core as pm
import FUCBoxCreator
import FUCSphereCreator

def MakePrimitive(s) :
    if s == 1:
        FUCBoxCreator.FUCBoxCreator()
    elif s == 2:
        FUCSphereCreator.FUCSphereCreator()

with pm.window(title='controller sampler UI'):
    with pm.columnLayout(adjustableColumn = True):
        pm.text(label = 'radio button')
        rdoGrp = pm.radioButtonGrp(numberOfRadioButtons = 2,
        label = 'Box or Sphere',
        labelArray2 = ['Box', 'Sphere'])

        pm.separator(style = 'none')

        pm.button(label = 'create', c = 'MakePrimitive(rdoGrp.getSelect())')
