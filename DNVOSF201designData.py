# DNVOSF201 code check design data
from Preprocess import*

SMYS = 450E3                                 # specified minimum yield strength, KPa
fD = 0.8                                     # design factor for equivalent stress check
riserType.DNVOSF201F0 = 0.003                # out of roundness
riserType.DNVOSF201Fytemp = 14.4E3 #KPa      # derating value for yield stress,KPa
riserType.DNVOSF201Fu = 14.4E3 #KPa          # derating value for ultimate stress,KPa
riserType.DNVOSF201Pmin = 0                  # minmimum internal pressure 
SafetyClass = 'low'
manufacturingProcess = 'smls'

'''safety class resistance factor'''
SafetyClass = ['low','normal','high']
if SafetyClass =='low':
    riserType.DNVOSF201GammaSC = 1.04
elif SafetyClass =='normal':
    riserType.DNVOSF201GammaSC = 1.14
else:
    riserType.DNVOSF201GammaSC = 1.26
print(riserType.DNVOSF201GammaSC)

'''material resistance factor'''
riserType.DNVOSF201GammaM = 1.15

'''fabrication factor'''
if manufacturingProcess == 'smls':
    riserType.DNVOSF201GammaAlphaFab = 1.00
elif manufacturingProcess == 'UOE':
    riserType.DNVOSF201GammaAlphaFab = 0.85
else:
    riserType.DNVOSF201GammaAlphaFab = 0.925
print(riserType.DNVOSF201GammaAlphaFab)

''' usage factor for WSD combined loadong'''
if SafetyClass =='low':
    riserType.DNVOSF201GammaEta = 1.04
elif SafetyClass =='normal':
    riserType.DNVOSF201GammaEta = 1.14
else:
    riserType.DNVOSF201GammaEta = 1.26
print(riserType.DNVOSF201GammaEta)

''' functional and environmental load effect factors'''
riserType.DNVOSF201GammaF = 1.1
riserType.DNVOSF201GammaE = 1.3

'''condition load effect factor'''
riserType.DNVOSF201GammaC = 1.0  