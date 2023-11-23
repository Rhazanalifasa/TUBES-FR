import math



def F_rho_r(Ppr, Tpr, Rho_r) :
    A1 = 0.3265
    A2 = -1.07
    A3 = -0.5339
    A4 = 0.01569
    A5 = -0.05165
    A6 = 0.5475
    A7 = -0.7361
    A8 = 0.1844
    A9 = 0.1056
    A10 = 0.6134
    A11 = 0.721
    R1 = A1 + A2 / Tpr + A3 / (Tpr ** 3) + A4 / (Tpr ** 4) + A5 / (Tpr ** 5)
    R2 = 0.27 * Ppr / Tpr
    R3 = A6 + A7 / Tpr + A8 / Tpr ** 2
    R4 = A9 * (A7 / Tpr + A8 / Tpr ** 2)
    R5 = A10 / Tpr ** 3
    F_rho_r = (R1 * Rho_r - R2) / Rho_r + R3 * Rho_r ** 2 - R4 * Rho_r ** 5 + R5 * (1 + A11 * Rho_r ** 2) * Rho_r ** 2 * math.exp(-A11 * Rho_r ** 2,) + 1
    return F_rho_r

def df_rho_r(Ppr , Tpr , rho ):
    df_rho_r = (F_rho_r(Ppr, Tpr, rho + 0.001) - F_rho_r(Ppr, Tpr, rho)) / 0.001
    return df_rho_r

def Z_DAK(Tpr, Ppr ):
    galat = 999
    rho1 = 0.27 * Ppr / (0.5 * Tpr)
    while galat > 0.0000000001:
        rho2 = rho1 - F_rho_r(Ppr, Tpr, rho1) / df_rho_r(Ppr, Tpr, rho1)
        galat = abs(rho2 - rho1)
        rho1 = rho2
    Z_DAK = 0.27 * Ppr / (rho1 * Tpr)
    return


def Fy(Tpr, Ppr, Yt ): 
    T = 1 / Tpr
    return (-0.062156 * Ppr * T * math.exp(-1.2 * (1 - T) ** 2) + ((Yt + Yt ** 2 + Yt ** 3 + Yt ** 4) / (1 - Yt) ** 4) - (14.76 * T - 9.76 * T ** 2 + 4.58 * T ** 3) * Yt ** 2 + (90.7 * T - 242.2 * T ** 2 + 42.4 * T ** 3) * Yt ** (2.18 + 2.82 * T))


def Z_hy(Tpr, Ppr):
    MaxIter = 150
    g_iter = 0.000000000001
    ybefore = 0
    Yt = 0.01
    DZ = 0.0001
    T = 1 / Tpr
    i = 0
    while(Yt - ybefore) > g_iter and i < MaxIter:
        ybefore = Yt
        Yt = Yt - (Fy(Tpr, Ppr, Yt) * DZ / (Fy(Tpr, Ppr, Yt + DZ) - Fy(Tpr, Ppr, Yt)))
        i = i + 1
    return ((0.06125 * Ppr * T) / Yt) * math.exp(-1.2 * (1 - T) ** 2)

def Z_Beggs(Tpr , Ppr ):

    A = 1.39 * (Tpr - 0.92) ** 0.5 - 0.36 * Tpr - 0.101
    B = (0.62 - 0.23 * Tpr) * Ppr + ((0.066 / (Tpr - 0.86)) - 0.037) * Ppr ** 2 + 0.32 / (10 ** 9 * (Tpr - 1)) * Ppr ** 6
    C = 0.132 - 0.32 * math.log(Tpr)
    D = 10**(0.3016 - 0.49 * Tpr + 0.1825 * Tpr ** 2)
    return A + ((1 - A) / math.exp(B)) + C * Ppr ** D