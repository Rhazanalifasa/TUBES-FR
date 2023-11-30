import math

def log(x):
    return (math.log(x,10) / math.log(10,10))

def exp(x):
    return math.exp(x)

def Rs_VB(API, T, P, Tsep, Psep, Pb, Pressure): # Gas Oil Ratio
    SG = 141.5 / (API + 131.5)
    if P > Pb:
        Pressure = Pb
    else:
        Pressure = P
    if API <= 30:
        C1 = 0.0362
        C2 = 1.0937
        C3 = 25.724
    else:
        C1 = 0.0178
        C2 = 1.187
        C3 = 23.931

    SG1 = SG * (1 + (5.912 * 0.00001 * API * Tsep * (log(Psep / 114.7) / log(10))))
    Rs_VB = C1 * SG1 * (Pressure ** C2) * exp(C3 * (API / (T + 460)))
    return Rs_VB