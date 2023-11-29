def Tc_NG(SG) :
    Tc_NG = 168 + 325 * SG - 12.5 * SG ** 2
    return Tc_NG 

def Tc_GC(SG): 
    Tc_GC = 187 + 330 * SG - 71.5 * SG ** 2
    return Tc_GC

def Pc_NG(SG):
    Pc_NG = 677 + 15 * SG - 37.5 * SG ** 2
    return Pc_NG 

def Pc_GC(SG):
    Pc_GC = 706 - 51.7 * SG - 11.1 * SG ** 2
    return Pc_GC 

def Tpcz(Tpc , CO2 , H2S , N2 ):
    Tpcz = Tpc - (80 * CO2) + (130 * H2S) - (250 * N2)
    return Tpcz 

def Ppcz(Ppc , CO2 , H2S , N2 ):
    Ppcz = Ppc + (440 * CO2) + (600 * H2S) - (170 * N2)
    return Ppcz 

def Tpr(T , Tc ): 
    Tpr = (T + 460) / Tc
    return Tpr

def Ppr(P , Pc ):
    Ppr = P / Pc
    return Ppr

