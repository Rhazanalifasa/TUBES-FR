import math
#Oil Formation Volume Factor (Bo)
def Bo_Standing(SGg , API , T, Rs): # Saturated
    SG = 141.5 / (131.5 + API);
    Bo_Standing_ = 0.9759 + 0.00012 * (Rs * ((SGg/SG)**0.5) + 1.25 * (T-460)) **1.2;
    
    return Bo_Standing_;

def Bo_Glaso(Rs, SGg, SGo, T):
    Bob = (Rs(SGg/SGo)**0.526) + 0.968*(T-460)
    A = -6.58511 + 2.91329 * math.log(math.log(Bob)) - 0.27683*((math.log(math.log(Bob)))**2)
    Bo_Glaso = 1.0 + (10**A);
    
    return Bo_Glaso;
  
def Oil_FVF(P_bubble, api, Rsb, sg2, temp2, pressure2):
    """
    Calculate Oil FVF
    * Above bubble-point pressure
      For range: unspecified
      (Vazquez and Beggs, 1980)
    * At and bubble-point pressure
      For range: unspecified
      (Levitan and Murtha, 1999)
    """

    import numpy as np
    so = 141.5 / (api + 131.5)
    Bo_bubble = 1 + ((0.0005 * Rsb) * ((sg2 / so)**0.25)) + ((0.0004*(temp2- 60)) / (so * sg2)) # temp in def F

    if pressure2 < P_bubble: # use Vazquez-Beggs
        if api <= 30: 
          c1 = 0.0362
          c2 = 1.0937
          c3 = 25.7240
          c4 = 4.677E-4
          c5 = 1.751E-5
          c6 = -1.811E-8
          
        if api > 30:
          c1 = 0.0178
          c2 = 1.187
          c3 = 23.9310
          c4 = 4.670E-4
          c5 = 1.100E-5
          c6 = 1.337E-9
          
        Rsc = (pressure2**c2) * c1 * sg2 * np.exp((c3 * api) / (temp2 + 459.67))
        Bo = 1 + (c4 * Rsc) + (c5 * (temp2 - 60) * (api / sg2)) + (c6 * Rsc *(temp2 - 60) * (api / sg2)) # temp in deg F
    
    if pressure2 == P_bubble:
        Bo = Bo_bubble
    if pressure2 > P_bubble:
        coil = ((5 * Rsb) + (17.2 * temp2) - (1180 * sg2) + (12.61 * api) - 1433) / (1E+05 * pressure2)
        Bo = Bo_bubble * np.exp(coil * (P_bubble - pressure2))
    if P_bubble != P_bubble:
        Bo = np.nan  

    return Bo

#Gas Solubility
def Rs_Glaso(API , T , P,  Pb): # Gas-Oil Ratio
    SG = 141.5 / (API + 131.5) 
    if P > Pb:
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

#Bubble-Point Pressure (Pb) *takutnya salah
def Oil_Pbubble(Rsb, sg2, api, temp2):
  """
  Calculate Oil Bubble-Point Pressure
  For range: 20 < Rsb (scf/STB) < 2,070; 0.56 < sg < 1.18; 16 < api < 58; 70 < temp (°F) < 295 (err=0.7%)
  (Vazquez and Beggs, 1980)
  """
  import numpy as np

  if Rsb > 20 and Rsb < 2070 and sg2 > 0.56 and sg2 < 1.18 and api > 16 and api < 58 and temp2 > 70 and temp2 < 295:
    # c1, c2, c3 coefficient from Vazquez-Beggs
    if api <=30:
      c1 = 0.0362
      c2 = 1.0937
      c3 = 25.7240
    if api > 30:
      c1 = 0.0178
      c2 = 1.187
      c3 = 23.9310

    P_bubble = (Rsb / (c1 * sg2 * np.exp((c3 * api)/(temp2 + 459.67))))**(1 / c2) # convert temp to Rankine
  else:
    P_bubble = np.nan
  return P_bubble

#Oil Density 
def exp(x):
    return math.exp(x)

def Rho_Standard(Bo , SGg , Rs , API):
    SG = 141.5 / (131.5 + API)
    Rho_Std = ((62.4 * SG) + (0.0136 * Rs * SGg)) / Bo
    return Rho_Std

def Rho_Standing(Co, P, Pb , API, SGg, T, Rs): #Temperatur yang digunakan masih belum pasti rankine atau bukan
    SG = 141.5 / (131.5 + API)
    Rho_Oil = ((62.4 * SG) + (0.0136 * Rs * SGg)) / (0.972 + (0.000147 * ((Rs * ((SGg / SG) ** 0.5)) + (1.25 * T)) ** 1.175)) 
    if P > Pb:
        Rho_Stand = Rho_Oil * exp(Co * (P - Pb))
        return Rho_Stand
    else:
        Rho_Stand = Rho_Oil
        return Rho_Stand
# print(Rho_Standing(1,2,3,44,5,6,7))

#Oil Viscosity 
def Oil_Miu(pressure2, P_bubble, sg2, api, temp2, Rs):
  """
  Calculate Oil Viscosity
  * Below and at bubble-point pressure
    For range: 0 < p (psia) < 5,250; range sg unspecified; 16 < api < 58; 70 < temp (°F) < 295; 20 < Rs (scf/STB) < 2,070 (err=1.83%)
    (Beggs and Robinson, 1975; Chew and Connally, 1959)
  * Above bubble-point pressure
    For range: 126 < p (psia) < 9,500; 0.511 < sg < 1.351; 15.3 < api < 59.5; range temp unspecified; 9.3 < Rs (scf/STB) < 2199 (err=7.54%)
    (Vazquez and Beggs, 1980)
  """
  # Calculate viscosity of oil
  import numpy as np

  mu_oil_array = []

  if pressure2 <= P_bubble:
    # validity check
    if pressure2 < 5250 and api > 16 and api < 58 and temp2 > 70 and temp2 < 295 and Rs > 20 and Rs < 2070:
      if api <=30:
        c1 = 0.0362
        c2 = 1.0937
        c3 = 25.7240
      if api > 30:
        c1 = 0.0178
        c2 = 1.187
        c3 = 23.9310

      # use Beggs and Robinson
      # valid for: 0 < pressure < 5250 psig, 70 < temp < 295 F, 20 < Rs < 2070 scf/STB, 16 < api < 58 API 
      x = (temp2**(-1.163)) * np.exp(6.9824 - (0.04658 * api))
      mu_dead_oil = 10**x - 1
      a = 10.715 * ((Rs + 100)**(-0.515))
      b = 5.44 * ((Rs + 150)**(-0.338))
      mu_live_oil = a * (mu_dead_oil**b)
    else:
      mu_live_oil = np.nan

  if pressure2 > P_bubble:
    # validity check
    # 126 < p (psia) < 9,500; 0.511 < sg < 1.351; 15.3 < api < 59.5; range temp unspecified; 9.3 < Rs (scf/STB) < 2199
    if pressure2 > 126 and pressure2 < 9500 and sg2 > 0.511 and sg2 < 1.351 and api > 15.3 and api < 59.5 and Rs > 9.3 and Rs < 2199: 
      if api <=30:
        c1 = 0.0362
        c2 = 1.0937
        c3 = 25.7240
      if api > 30:
        c1 = 0.0178
        c2 = 1.187
        c3 = 23.9310

      # use Vazquez and Beggs
      # valid for: 126 < pressure < 9500 psig, 9.3 < Rs < 2199 scf/STB, 15.3 < api < 59.5 API, 0.511 < sg < 1.351 

      # compute oil viscosity at bubblepoint first
      x_bubble = (temp2**(-1.163)) * np.exp(6.9824 - (0.04658 * api))
      mu_dead_oil_bubble = 10**x_bubble - 1
      
      a_bubble = 10.715 * ((Rs + 100)**(-0.515))
      b_bubble = 5.44 * ((Rs + 150)**(-0.338))
      
      mu_live_oil_bubble = a_bubble * (mu_dead_oil_bubble**b_bubble)

      m = 2.6 * (pressure2**1.187) * np.exp(-11.513 - (8.98E-05 * pressure2))
      mu_live_oil = mu_live_oil_bubble * ((pressure2 / P_bubble)**m)

    else:
      mu_live_oil = np.nan

  if P_bubble != P_bubble:
    mu_live_oil = np.nan

  return mu_live_oil

#Beda codingan untuk oil viscosity
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
    
    return MiuBR;

def MiuBRunsat(API, T,Rs,P,Pb):
    #unsaturated
    #MIU VB
    A = -3.9 * (10 ** -5) * P - 5
    m = 2.6 * (P ** 1.187) * 10 ** A
    Miu_BRunsat = MiuBRsat(Rs, API, T) * ((P / Pb) ** m)
    
    return Miu_BRunsat;

#Isothermal Compressibility Coefficient of Oil (Co)
def Oil_Compressibility(pressure2, P_bubble, temp2, api, Rsb, sg2):
    """
    Calculate Oil Isothermal Compressibility
    * Below bubble-point pressure
      For range: unspecified
      (McCain, 1988)
    * Above and at bubble-point pressure
      For range: unspecified
      (Vazquez and Beggs, 1980)
    """
    import numpy as np
    from math import e

    # oil isothermal compressibility
    if pressure2 < P_bubble:
        # use McCain
        ln_coil = -7.573 - (1.45 * np.log(pressure2)) - (0.383 * np.log(P_bubble)) + (1.402 * np.log(temp2)) + (0.256 * np.log(api)) + (0.449 * np.log(Rsb))  
        coil = np.exp(ln_coil)
    if pressure2 >= P_bubble:
        # use Vazquez-Beggs
        coil = ((5 * Rsb) + (17.2 * temp2) - (1180 * sg2) + (12.61 * api) - 1433) / (1E+05 * pressure2)

    if P_bubble != P_bubble:
        coil = np.nan

    return coil