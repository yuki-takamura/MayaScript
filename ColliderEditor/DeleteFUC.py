import pymel.core as pm

def DeleteFUC():
    try:
        pm.select('FUC_Sphere')
        pm.delete()
    except:
        pass

    try:
        pm.select('FUC_Box')
        pm.delete()
    except:
        pass
