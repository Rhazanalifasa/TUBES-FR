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

