import math

def Bg(P , T , Z ):
    Bg = 0.00502 * (Z * (T + 460) / P) * 1000
    
    return Bg

def RhoG(SG , P , T , Z ):
    R = 10.73
    Ma = SG * 28.97
    RhoG = (P * Ma) / (Z * R * (T + 460))
    
    return RhoG

def MiuG(SG , T , RhoG):
    Ma = SG * 28.97
    K = ((9.4 + (0.02 * Ma)) * (T + 460) ** 1.5) / (209 + (19 * Ma) + (T + 460))
    X = 3.5 + (986 / (T + 460)) + (0.01 * Ma)
    Y = 2.4 - (0.2 * X)
    MiuG = (10 ** -4) * K * (math.exp(X * (RhoG / 62.4)) ** Y)
    
    return MiuG

def Cg(Tpr , Ppr , Z , Ppc):
    A1 = 0.31506237
    A2 = -1.0467099
    A3 = -0.5783272
    A4 = 0.53530771
    A5 = -0.61232032
    A6 = -0.1048813
    A7 = 0.68157001
    A8 = 0.68446549
    T1 = A1 + (A2 / Tpr) + (A3 / (Tpr ** 3))
    T2 = A4 + (A5 / Tpr)
    T3 = A5 * A6 / Tpr
    T4 = A7 / (Tpr ** 3)
    T5 = 0.27 * Ppr / Tpr
    Rhor = 0.27 * Ppr / (Z * Tpr)
    dhozperrhor = T1 + (2 * T2 * Rhor) + (5 * T3 * Rhor ** 4) + (2 * T4 * Rhor * ((1 + A8 * Rhor ** 2) - (A8 ** 2 * Rhor ** 4)) * math.exp(-A8 * Rhor ** 2))
    Cpr = (1 / Ppr) - ((0.27 / (Z ** 2) * Tpr) * (dhozperrhor / (1 + (Rhor * dhozperrhor / Z))))
    Cg = Cpr / Ppc
    
    return Cg

def Gas_Miu(temp, rhogas, sg):
    import numpy as np

    if temp > 100 and temp < 340:
        temp = temp + 459.67
        Mg = 28.97 * sg
        rhogas_lee = rhogas * 0.0160185 
        K = ((0.00094 + 2E-06)*(temp**1.5)) / (209 + 19*Mg + temp)
        x = 3.5 + (986 / temp) + (0.01 * Mg)
        y = 2.4 - 0.2*x  
        viscogas = K * np.exp(x * (rhogas_lee**y))
    
    else:
        viscogas = np.nan
    return viscogas

def Gas_Compressibility(T_pr, P_pr, rho_pr, z, P_pc):
    import numpy as np

    a1 = 0.3265; a2 = -1.0700; a3 = -0.5339; a4 = 0.01569; a5 = -0.05165; a6 = 0.5475
    a7 = -0.7361; a8 = 0.1844; a9 = 0.1056; a10 = 0.6134; a11 = 0.7210

    do = ((a1 + (a2/T_pr) + (a3/T_pr**3) +(a4/T_pr**4) + (a5/T_pr**5)) * rho_pr) + \
        (2 * ((a6 + (a7/T_pr) + (a8/T_pr**2))) * rho_pr**2) - \
        (5 * a9 * (((a7/T_pr) + (a8/T_pr**2))) * rho_pr**4) + (1 + (a11 * rho_pr**2) - (a11 * rho_pr**2)**2) \
        * ((2 * a10 * rho_pr / T_pr**3)*np.exp(-a11 * rho_pr**2))

    c_pr_analytical = (1 / P_pr) - ((0.27 / (z**2 * T_pr)) * (do / (1 + ((rho_pr / z) * do))))
    cgas_analytical = c_pr_analytical / P_pc
    
    return(cgas_analytical);
