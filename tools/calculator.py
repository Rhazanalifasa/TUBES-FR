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

from Properties.Gas_Prop import *;
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
from Properties.Brine_Formation_Volume_Factor import *;
# def calculateBWsat(pressure, temperature):

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
    
    #Oil Properties
    Rho_Standard_Value  = Rho_Standard(Bo , SGg , Rs , API)
    Rho_Standing_Value  = Rho_Standing(Co, P, Pb , API, SGg, T, Rs)
    Bo_Standing_Value   = Bo_Standing(SGg , API , T)


