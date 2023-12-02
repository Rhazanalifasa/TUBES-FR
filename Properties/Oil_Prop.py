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





