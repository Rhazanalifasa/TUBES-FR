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

#Bo Standing
def Bo_Standing(SGg , API , T): # Saturated
    SG = 141.5 / (131.5 + API)
    Bo_Standing = 0.9759 + (0.00012 * ((((SGg / SG) ** 0.5)) + (1.25 * (T-460))) ** 1.2)
    return Bo_Standing

#Rs Glaso
import math
def log(x):
    return (math.log(x,10) / math.log(10,10))

def Rs_Glaso(API , T , P , Pb ): # Gas-Oil Ratio
    SG = 141.5 / (API + 131.5) 
    if P > Pb:
        Pressure = Pb
    else:
        Pressure = P
    Pbubble = 10 ** (2.8869 - (14.1811 - (3.3093 * log(Pressure))) ** 0.5)
    Rs_Glaso = SG * ((((API ** 0.989) / ((T) ** 0.172)) * Pbubble) ** 1.2255)
    
    return Rs_Glaso

#Rs Vb
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

#Miu_VB
def Miu_VB(P , Pb , Rs , API , T ):
    A = -3.9 * (10** -5) * P - 5
    m = 2.6 * (P** 1.187) * 10 ** A
    Miu_VB = Miu(Rs, API, T) * ((P / Pb) ** m)
    return Miu_VB

def Miu(Rs, API , T):
    A = 10.715 * (Rs + 100) ** -0.515
    B = 5.44 * (Rs + 150) ** -0.338
    Miu = A * (Miu_DO(API, T)) ** B
    return Miu