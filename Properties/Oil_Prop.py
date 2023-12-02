#rho standart
def Rho_Standard(Bo , SGg , Rs , API ):
    SG = 141.5 / (131.5 + API)
    Rho_Std = ((62.4 * SG) + (0.0136 * Rs * SGg)) / Bo
    return Rho_Std

#rho standing
import math
def exp(x):
    return math.exp(x)
def Rho_Standing(Co, P, Pb , API, SGg, T, Rs):
    SG = 141.5 / (131.5 + API)
    Rho_Oil = ((62.4 * SG) + (0.0136 * Rs * SGg)) / (0.972 + (0.000147 * ((Rs * ((SGg / SG) ** 0.5)) + (1.25 * T)) ** 1.175))
    if P > Pb:
        Rho_Stand = Rho_Oil * exp(Co * (P - Pb))
        return Rho_Stand
    else:
        Rho_Stand = Rho_Oil
        return Rho_Stand

from korelasi_OIL import Rs_Standing
#Bo Standing
def Bo_Standing(SGg , API , T, Rs): # Saturated
    SG = 141.5 / (131.5 + API)
    Bo_Standing = 0.9759 + 0.00012 * (Rs*((SGg/SG)**0.5) + 1.25(T-460))**1.2
    return Bo_Standing





import math
def Rs_Glaso(API, T , P , Pb):
    SG = 141.5 / (API + 131.5)
    if P > Pb :
        Pressure = Pb
    else:
        Pressure = P
        Pbubble = 10 ** (2.8869 - (14.1811 - (3.3093 * math.log(Pressure))) ** 0.5)
    Rs_Glaso = SG * ((((API ** 0.989) / ((T) ** 0.172)) * Pbubble) ** 1.2255)
    return Rs_Glaso
def Rs_Standing(API, T, P, Pb): 
    SG = 141.5 / (API + 131.5)
    if P > Pb :
        Pressure = Pb
    else:
        Pressure = P
    Rs_Standing = SG * (((Pressure / 18.2) + 1.4) * 10 ** ((0.0125 * API) - 0.00091 * (T))) ** 1.2048
    return Rs_Standing

def Rs_VB(API, T, P, Tsep, Psep, Pb):

    SG = 141.5 / (API + 131.5)
    if P > Pb :
        Pressure = Pb
    else:
        Pressure = P
        C1 = 0.0178
        C2 = 1.187
        C3 = 23.931
    if API <= 30:
        C1 = 0.0362
        C2 = 1.0937
        C3 = 25.724
    
    SG1 = SG * (1 + (5.912 * 0.00001 * API * Tsep * (math.log(Psep / 114.7) / math.log(10))))
    Rs_VB = C1 * SG1 * (Pressure ** C2) * math.exp(C3 * (API / (T + 460)))
    return Rs_VB



def Miu_DO(API, T):
    Z = 3.0324 - (0.02023 * API)
    Y = 10 ** Z
    X = Y * (T ** (-1.163))
    Miu_DO = (10 ** X) - 1
    return Miu_DO

def MiuBRsat(API, T, Rs):
    #saturated
    A = 10.715 * (Rs + 100) ** -0.515 #RS TERGANTUNG KORELASI YANG DIPAKAI
    B = 5.44 * (Rs + 150) ** -0.338
    MiuBR = A * (Miu_DO(API, T)) ** B
    return MiuBR

def MiuBRunsat(API, T,Rs,P,Pb):
    #unsaturated
    #MIU VB
    A = -3.9 * (10 ** -5) * P - 5
    m = 2.6 * (P ** 1.187) * 10 ** A
    Miu_BRunsat = MiuBRsat(Rs, API, T) * ((P / Pb) ** m)
    return Miu_BRunsat

