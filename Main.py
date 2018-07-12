import pymel.core as pm
import FUCBoxCreator
import FUCSphereCreator

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

        pm.button(label = 'create', c = 'MakePrimitive(rdoGrp.getSelect())')
