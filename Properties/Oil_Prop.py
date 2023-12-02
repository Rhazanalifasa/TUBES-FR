import math
#Oil Formation Volume Factor (Bo)
def Bo_(SGg , API , T, Rs, SGo, corr:str): # Saturated
    if corr.lower() == 'standing':
      SG = 141.5 / (131.5 + API)
      Bo_Standing = 0.9759 + 0.00012 * (Rs*((SGg/SG)**0.5) + 1.25(T-460))**1.2
      return Bo_Standing;
    elif corr.lower() == 'glaso':
      Bob = (Rs(SGg/SGo)**0.526) + 0.968*(T-460)
      A = -6.58511 + 2.91329 * math.log(math.log(Bob)) - 0.27683*((math.log(math.log(Bob)))**2)
      Bo_Glaso = 1.0 + (10**A);
      return Bo_Glaso;

def Bo_Glaso(Rs, SGg, SGo, T):
    Bob = (Rs(SGg/SGo)**0.526) + 0.968*(T-460)
    A = -6.58511 + 2.91329 * math.log(math.log(Bob)) - 0.27683*((math.log(math.log(Bob)))**2)
    Bo_Glaso = 1.0 + (10**A);
    
    return Bo_Glaso;

#Gas Solubility
def Rs_(API , T , P, corr:str, Pb): # Gas-Oil Ratio
    if corr.lower() == 'glaso':
      SG = 141.5 / (API + 131.5) 
      if P > Pb:
          Pressure = Pb
      else:
          Pressure = P
        
      Pbubble = 10 ** (2.8869 - (14.1811 - (3.3093 * math.log(Pressure))) ** 0.5)
      Rs_Glaso = SG * ((((API ** 0.989) / ((T) ** 0.172)) * Pbubble) ** 1.2255)   
      return Rs_Glaso
    elif corr.lower() == 'vb':
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

      SG1 = SG * (1 + (5.912 * 0.00001 * API * Tsep * (math.log(Psep / 114.7) / math.log(10))))
      Rs_VB = C1 * SG1 * (Pressure ** C2) * exp(C3 * (API / (T + 460)))
      return Rs_VB
    elif corr.lower() == 'standing':
      SG = 141.5 / (API + 131.5)
      if P > Pb :
          Pressure = Pb
      else:
          Pressure = P
      Rs_Standing = SG * (((Pressure / 18.2) + 1.4) * 10 ** ((0.0125 * API) - 0.00091 * (T))) ** 1.2048
      return Rs_Standing

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

    SG1 = SG * (1 + (5.912 * 0.00001 * API * Tsep * (math.log(Psep / 114.7) / math.log(10))))
    Rs_VB = C1 * SG1 * (Pressure ** C2) * exp(C3 * (API / (T + 460)))
    
    return Rs_VB

def Rs_Standing(API, T, P, Pb): 
    SG = 141.5 / (API + 131.5)
    if P > Pb :
        Pressure = Pb
    else:
        Pressure = P
    Rs_Standing = SG * (((Pressure / 18.2) + 1.4) * 10 ** ((0.0125 * API) - 0.00091 * (T))) ** 1.2048
    
    return Rs_Standing

#Bubble-Point Pressure (Pb) *takutnya salah
def oil_pbubble(Rsb, sg2, api, temp2):
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
def oil_mu(pressure2, P_bubble, sg2, api, temp2, Rs):
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
def CO_VB(API, T, Pb, Tsep, Psep, P, SGg):
    Rsb = Rs_VB(API, T, Pb, Tsep, Psep, Pb) #Rs_VBDari sebelumnya
    SG1 = SGg * (1 + (5.912 / 100000) * API * Tsep * (math.log(math.log(Psep / 114.7)) / math.log(math.log(10)))) #SGg ada di bagian sebelumnya, TSEP DAN PSEP INPUTAN.
    if P > Pb:
        Co_VB = (-1433 + 5 * Rsb + 17.2 * T - 1.18 * SG1 + 12.61 * API) / (100000 * P) #P ada di sebelumnya
    else:
        Co_VB = math.exp(-7.573 - 1.45 * math.log(P) / math.log(math.exp(1)) - 0.383 * math.log(Pb) / math.log(math.exp(1)) + 1.402 * math.log(T) / math.log(math.exp(1)) + 0.256 * math.log(API) / math.log(math.exp(1)) + 0.449 * math.log(Rsb) / math.log(math.exp(1)))
        
    return (Co_VB);