def Rho_Standard(Bo , SGg , Rs , API ):
    SG = 141.5 / (131.5 + API)
    Rho_Std = ((62.4 * SG) + (0.0136 * Rs * SGg)) / Bo
    return Rho_Std
print(Rho_Standard(1,2,3,4))