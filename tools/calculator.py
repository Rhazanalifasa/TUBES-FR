from pyfiglet import figlet_format;
import colorama;

# Ganti Pemilihan korelasi dengan hanya memasukkan pilihan dalam angka
colorama.init();
def showTittle():
    
    title = figlet_format("Calculator");
    print(colorama.Fore.MAGENTA + title); print(colorama.Style.RESET_ALL);
    
#### User Input Data ####
userInputData = dict();

##### Calculator MAINLOOP #####
def calculatorLoop():
    
    showTittle();
    userInput = float(input(colorama.Fore.LIGHTCYAN_EX + "Enter the pressure value: ")); print("\n");
    print(colorama.Fore.YELLOW + f"CONDITION: {determineConditions(userInput)}"); print(colorama.Style.RESET_ALL);
    calculateCriticalProperties(userInput);
    
    
##### PROPERTIES #####
def determineConditions(pressure:float) -> str:
    if pressure > 3000:
        return 'Undersaturated'
    else:
        return 'Saturated'

from Properties import Critical_Prop;
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
    Ppc_Value = Critical_Prop.Ppc_(gas_SG, corr); print(f"Ppc: {Ppc_Value} PSIA");
    Tpc_Value = Critical_Prop.Tpc_(gas_SG, corr); print(f"Tpc: {Tpc_Value} Rankine");
    
    Tpcz_Value = Critical_Prop.Tpcz(Tpc_Value, M_CO2, M_H2S, M_N2); print(f"Tpcz Value: {Tpcz_Value}");
    Ppcz_Value = Critical_Prop.Ppcz(Ppc_Value, M_CO2, M_H2S, M_N2); print(f"Ppcz Value: {Ppcz_Value} ");
    
    Tpr_Value = Critical_Prop.Tpr(temperature, Tpc_Value); print(f"Tpr Value: {Tpr_Value}");
    Ppr_Value = Critical_Prop.Ppr(pressure, Ppc_Value); print(f"Ppr Value: {Ppr_Value}\n");
    
    # Insert user input to userInputData
    userInputData["gas_SG"] = gas_SG;
    userInputData["temperature"] = temperature;
    userInputData["Gas Molecule"] = [M_CO2, M_H2S, M_N2];
    userInputData["Critical Value"] = [Ppc_Value, Tpc_Value, Ppcz_Value, Tpcz_Value, Ppr_Value, Tpr_Value];

from Properties import Gas_Prop; 
from Properties import Z_Fact;
def calculateGasProperties(pressure:float):
    # Input the required data
    P = float(input("Enter pressure(psia): "));
    T = float(input("Enter temperature(Fahrenheit): "));
    Z = float(input("Enter compressibility factor(Z): "));
    
    # GAS PROPERTIES
    Bg_Value = Gas_Prop.Bg(P, T, Z); print(f"Bg_Value: {Bg_Value}");
    RhoG_Value = Gas_Prop.RhoG(userInputData.get("gas_SG"), pressure, userInputData.get("temperature"), Z); print(f"RhoG Value: {RhoG_Value}");
    MiuG_Value = Gas_Prop.MiuG(userInputData.get("gas_SG"), T, RhoG_Value); print(f"MiuG Value: {MiuG_Value}");
    Cg_Value = Gas_Prop.Cg(userInputData["Critical Value"][5], userInputData["Critical Value"][4], Z, userInputData["Critical Value"][0]); print(f"Cg Value: {Cg_Value}");
    
    f = Z_Fact.hall_yarborough(userInputData["Critical Value"][4], userInputData["Critical Value"][5]);
    Y_estimate = Z_Fact.newton_raphson(f, x=0.25);
    Z_Fact.Z(userInputData["Critical Value"][4], userInputData["Critical Value"][5], Y_estimate);
        

from Properties import Brine_Prop;
def calculateBrineProperties(pressure:float):
    TDS = float(input("Enter Total Dissolve Solid Value: "));

    # BRINE PROPERTIES
    Bw_Value = Brine_Prop.BW(pressure, userInputData["temperature"]); print(f"Bw Value: {Bw_Value}");
    Rsw_Value = Brine_Prop.RSW(pressure, userInputData["temperature"], TDS); print(f"Rsw Value: {Rsw_Value}");
    RhoW_Value = Brine_Prop.RhoW(TDS, Bw_Value); print(f"RhoW Value: {RhoW_Value}");
    
    corr = input("Enter the correlation: ");
    MiuW_Value = Brine_Prop.MiuW(pressure, userInputData["temperature"], TDS, corr); print(f"MiuW Value: {MiuW_Value}");
    Cw_Value = Brine_Prop.CW(pressure, userInputData["temperature"]); print(f"Cw Value: {Cw_Value}");


from Properties import Oil_Prop;
def calculateOilProperties(pressure:float):
    # Input Required Data
    Oil_API = float(input("Enter the oil API: "));
    corr_Rs = input("Enter the correlation for Rs: ");
    corr_Bo = input("Enter the correlation for Bo: ");
    corr_Rho = input("Enter then correlation for Rho: ");
    SGo = 141.5/(Oil_API + 131.5);
    
    # OIL PROPERTIES
    Rs_Value = Oil_Prop.Rs_(Oil_API, userInputData["temperature"], pressure, corr_Rs, Pb=3000); print(f"Rs Value: {Rs_Value}")
    Bo_Value = Oil_Prop.Bo_(userInputData["gas_SG"], Oil_API, userInputData["temperature"], Rs_Value, SGo, corr_Bo); print(f"Bo Value = {Bo_Value}");
    
    if corr_Rho.lower() == 'standard':
        RhoO_Value = Oil_Prop.Rho_Standard(Bo_Value, userInputData["gas_SG"], Rs_Value, Oil_API); print(f"RhoO Value: {RhoO_Value}");
    elif corr_Rho.lower() == 'standing':
        RhoO_Value = Oil_Prop.Rho_Standing()