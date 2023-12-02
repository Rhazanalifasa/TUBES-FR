from pyfiglet import figlet_format;
import colorama;
import sys;
sys.path.append('C:\\Tubes FR\\TUBES-FR\\');

colorama.init();
def showTittle():
    
    title = figlet_format("Calculator");
    print(colorama.Fore.MAGENTA + title); print(colorama.Style.RESET_ALL);

##### Calculator MAINLOOP #####
def calculatorLoop():
    
    showTittle();
    userInput = float(input(colorama.Fore.LIGHTCYAN_EX + "Enter the pressure value: ")); print("\n");
    print(colorama.Fore.YELLOW + f"CONDITION: {determineConditions(userInput)}"); print(colorama.Style.RESET_ALL);
    calculateCriticalProperties(userInput);
    
    
##### PROPERTIES #####
from Properties.Critical_prop import *;
def calculateCriticalProperties(pressure:float):
    # Input the required data
    corr = input(colorama.Fore.WHITE + "Enter the correlation name: ");
    gas_SG = float(input("Enter gas specific gravity: "));
    temperature = float(input("Enter the temperature: "))
    M_CO2 = float(input("Enter CO2 mol: "));
    M_H2S = float(input("Enter H2S mol: "));
    M_N2 = float(input("Enter N2 mol: "));
    
    # CRITICAL PROPERTIES
    print(colorama.Fore.LIGHTRED_EX, "\n");
    Ppc_Value = Ppc_(gas_SG, corr); print(f"Ppc: {Ppc_Value} PSIA");
    Tpc_Value = Tpc_(gas_SG, corr); print(f"Tpc: {Tpc_Value} Rankine");
    
    Tpcz_Value = Tpcz(Tpc_Value, M_CO2, M_H2S, M_N2); print(f"Tpcz Value: {Tpcz_Value}");
    Ppcz_Value = Ppcz(Ppc_Value, M_CO2, M_H2S, M_N2); print(f"Ppcz Value: {Ppcz_Value} ");
    
    Tpr_Value = Tpr(temperature, Tpc_Value); print(f"Tpr Value: {Tpr_Value}");
    Ppr_Value = Ppr(pressure, Ppc_Value); print(f"Ppr Value: {Ppr_Value}\n");

from Properties import Gas_Prop
def calculateGasProperties(pressure:float):
    # Input the required data
    print("Input required properties.")
    P = float(input("Enter pressure(psia): "))
    T = float(input("Enter temperature(Fahrenheit): "))
    Z = float(input("Enter compressibility factor(Z): "))
    
def determineConditions(pressure:float) -> str:
    if pressure > 3000:
        return 'Undersaturated'
    else:
        return 'Saturated'
    

#brine formation volume factor#
from Properties import Brine_Prop;

def calculateBW(pressure : float, temperature : float):
    # Input the required data
    temperature = float(input("Enter the temperature: "))
    pressure = float(input("Enter the pressure: "))
    corr = input("Enter the corr: [Free/Sat]").lower()
    
    BW = Brine_Prop.BW(pressure, temperature, corr) ; print(f"BW_{corr}: {BW} RB/STB");

    
def calculateCSIsothermal(pressure: float, temperature: float, TDS: float, BW: float):
    # Input the required data
    temperature = float(input("Enter the temperature: "))
    pressure = float(input("Enter the pressure: "))
    TDS = float(input("Enter the TDS: "))
    
    CW = Brine_Prop.CW(pressure, temperature) ; print(f"CW: {CW} 1/PSI");
    RSW = Brine_Prop.RSW(pressure, temperature, TDS) ; print(f"RSW: {RSW} SCF/STB");
    Rhow = Brine_Prop.RhoW(TDS,BW) ; print(f"Rho: {Rhow} LBM/SCF");
    
    
def Miuw(pressure: float, temperature: float, TDS: float):
    # Input the required data
    temperature = float(input("Enter the temperature: "))
    pressure = float(input("Enter the pressure: "))
    TDS = float(input("Enter the TDS: "))
    corr = input("Enter the corr: [McCain/Beggs]").lower()
    
    Miuw = Brine_Prop.miuw(pressure, temperature, TDS, corr) ; print(f"Miuw_{corr}: {Miuw} CP");
    



    
    
    
# from Properties.Brine_Formation_Volume_Factor import *;
# def calculateBWsat(pressure, temperature):

#oil
from Properties.Oil_Prop import *;
def calculateOilProperties():
    Bo  = float(input("Enter formation volume factor(sfc/stb): "));
    SGg = float(input("Enter Spesific Gravity gas: "));
    Rs  = float(input("Enter Solution Gas Oil Ratio: "));
    API = float(input("Enter API: "));
    Co  = float(input("Enter : "));
    P   = float(input("Enter Pressure: "));
    Pb  = float(input("Enter: "));
    T   = float(input("Enter: "));
    Tsep   = float(input("Enter: "));
    Psep   = float(input("Enter: "));
    
    
    #Oil Properties
    Rho_Standard_Value  = Rho_Standard(Bo , SGg , Rs , API)
    Rho_Standing_Value  = Rho_Standing(Co, P, Pb , API, SGg, T, Rs)
    Bo_Standing_Value   = Bo_Standing(SGg , API , T)
    Rs_Glaso_Value      = Rs_Glaso(API, T , P , Pb)
    Rs_Standing_Value   = Rs_Standing(API, T, P, Pb)
    Rs_VB_Value         = Rs_VB(API, T, P, Tsep, Psep, Pb)
    Miu_DP_Value         = Miu_DO(API, T)
    Miu_BR_sat_Value       =MiuBRsat(API, T, Rs)
    Miu_BR_unsat_Value      =MiuBRunsat(API, T,Rs,P,Pb)


