import OrcFxAPI as Orc
from DNVOSF201designData import*
import pandas as pd
import numpy as np

# identifies the basecase file and key objects within it
model = Orc.model('basecase.dat')  
line = model['riser']
vessel = model['FPSO']
riserType = model[line.LineType[0]] # assume that the first section line type is the pipe line type

# load allowable limits 
maxTensionLimit = 260                                   # kN
minTensionLimit = 0                                     # kN

# DNVOSF201 allowable stress limit
riserType.DNVOSF201Fy = (SMYS - riserType.DNVOSF201Fytemp)*riserType.DNVOSF201GammaAlphaFab
stressLimit = fD*riserType.DNVOSF201Fy/1000 # in MPa, derived automatically from the OrcaFlex model

# obtain results from orcaflex
model.CalculateStatics()                                                     # perform static calculation
topTension = line.StaticResult('Effective Tension', OrcFxAPI.oeEndA)         # tension at topside
bottomTension = line.StaticResult('Effective Tension', OrcFxAPI.oeTouchdown) # tension at touchdown 
lineTension = (line.RangeGraph('Effective Tension', OrcFxAPI.pnStaticState)).Mean # tension from top to bottom
minLineTension = min(lineTension)
topBendMoment = line.StaticResult('Bend Moment', OrcFxAPI.oeEndA)
codeCheck_DNVOSF201_LRFD = (line.RangeGraph('DNV OS F201 LRFD', OrcFxAPI.pnStaticState)).Mean
maxcombinedload = max(codeCheck_DNVOSF201_LRFD)
maxVonMisesstress = (line.RangeGraph('Max von Mises Stress', OrcFxAPI.pnStaticState)).Mean

# checks results against the allowable limit
def toptensionlimit():
    if topTension <= maxTensionLimit:
        return 'pass'
    else:
        return 'fail'
toptensionlimit()

def minLineTensionlimit():
    if minLineTension >= minTensionLimit:
        return 'pass'
    else:
        return 'fail'
minLineTensionlimit()

def max_combinedload_unity_check():
    if maxcombinedload <= 1.0:   # APIRP1111 combined load unity check due to axial load,bending and external pressure
        return 'pass'
    else:
        return 'fail'
max_combinedload_unity_check()

def codestress_check():
    if maxVonMisesstress/1000 <= stressLimit:
        return 'pass'
    else:
        return 'fail'
codestress_check()

# write out results
data = pd.DataFrame({'topTension[kN]': [[topTension,toptensionlimit()]]
                     'bottomTension[kN]': [[bottomTension]],
                     'minLineTension[kN]': [[minLineTension, minLineTensionlimit()]],
                     'topBendMoment[kNm]': [[topBendMoment]],
                     'maxcombinedload[kNm]':[[maxcombinedload,max_combinedload_unity_check()]],
                     'maxVonMisesstress[MPa]':[[maxVonMisesstress],codestress_check()]] })
print(data)