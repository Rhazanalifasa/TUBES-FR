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
    userInput = float(input(colorama.Fore.LIGHTCYAN_EX + "Enter the pressure value (psi): ")); print("\n");
    
    calculateCriticalProperties(userInput); print("\n")
    calculateGasProperties(userInput); print("\n")
    calculateOilProperties(userInput); print('\n')
    calculateBrineProperties(userInput); print('\n')
    
    
##### PROPERTIES #####
from Properties import Critical_Prop;
def calculateCriticalProperties(pressure:float):
    # Input the required data
    corr = input(colorama.Fore.WHITE + "Enter the correlation name [Sutton/Misc Standing/Condensate Standing]: ");
    gas_SG = float(input("Enter gas specific gravity: "));
    temperature = float(input("Enter the temperature (F): "))
    M_CO2 = float(input("Enter CO2 mol: "));
    M_H2S = float(input("Enter H2S mol: "));
    M_N2 = float(input("Enter N2 mol: "));
    
    # CRITICAL PROPERTIES
    print('\n', colorama.Fore.LIGHTRED_EX + "=========== Critical Properties ==========");
    Ppc_Value = Critical_Prop.Ppc_(gas_SG, corr); print(f"Ppc: {Ppc_Value} PSIA");
    Tpc_Value = Critical_Prop.Tpc_(gas_SG, corr); print(f"Tpc: {Tpc_Value} Rankine");
    
    Tpcz_Value = Critical_Prop.Tpcz(Tpc_Value, M_CO2, M_H2S, M_N2); print(f"Tpcz Value: {Tpcz_Value}");
    Ppcz_Value = Critical_Prop.Ppcz(Ppc_Value, M_CO2, M_H2S, M_N2); print(f"Ppcz Value: {Ppcz_Value} ");
    
    Tpr_Value = Critical_Prop.Tpr(temperature, Tpc_Value); print(f"Tpr Value: {Tpr_Value}");
    Ppr_Value = Critical_Prop.Ppr(pressure, Ppc_Value); print(f"Ppr Value: {Ppr_Value}");
    
    # Insert user input to userInputData
    userInputData["gas_SG"] = gas_SG;
    userInputData["temperature"] = temperature;
    userInputData["Gas Molecule"] = [M_CO2, M_H2S, M_N2];
    userInputData["Critical Value"] = [Ppc_Value, Tpc_Value, Ppcz_Value, Tpcz_Value, Ppr_Value, Tpr_Value];


from Properties import Gas_Prop; 
from Properties import Z_Fact;
def calculateGasProperties(pressure:float):
    # GAS PROPERTIES    
    print(colorama.Fore.YELLOW + " ========== Gas PVT Correlation ==========");
    f = Z_Fact.hall_yarborough(userInputData["Critical Value"][4], userInputData["Critical Value"][5]);
    Y_estimate = Z_Fact.newton_raphson(f, x=0.25);
    Z_Value = Z_Fact.Z(userInputData["Critical Value"][4], userInputData["Critical Value"][5], Y_estimate); print(f"Z Value: {Z_Value}");
    
    Bg_Value = Gas_Prop.Bg(pressure, userInputData["temperature"], Z_Value); print(f"Bg_Value: {Bg_Value}");
    RhoG_Value = Gas_Prop.RhoG(userInputData.get("gas_SG"), pressure, userInputData.get("temperature"), Z_Value); print(f"RhoG Value: {RhoG_Value}");
    MiuG_Value = Gas_Prop.MiuG(userInputData.get("gas_SG"), userInputData["temperature"], RhoG_Value); print(f"MiuG Value: {MiuG_Value}");
    Cg_Value = Gas_Prop.Cg(userInputData["Critical Value"][5], userInputData["Critical Value"][4], Z_Value, userInputData["Critical Value"][0]); print(f"Cg Value: {Cg_Value}");
        

from Properties import Brine_Prop;
def calculateBrineProperties(pressure:float):
    print(colorama.Fore.WHITE);
    TDS = float(input("Enter Total Dissolve Solid Value (ppm): "));
    corr = input("Enter the correlation for MiuW [Beggs/McChain]: ").lower();

    # BRINE PROPERTIES
    print('\n', colorama.Fore.LIGHTBLUE_EX + "========== Brine PVT Correlation ==========");
    Bw_Value = Brine_Prop.BW(pressure, userInputData["temperature"]); print(f"Water FVF: {Bw_Value} RB/STB");
    Pbubble_water = Brine_Prop.Water_Pbubble(userInputData["temperature"]); print(f"Bubble Point Pressure: {Pbubble_water} psia");
    Rsw_Value = Brine_Prop.RSW(pressure, userInputData["temperature"], TDS); print(f"Solution Gas-Water Ratio: {Rsw_Value} scf/STB");
    RhoW_Value = Brine_Prop.RhoW(TDS, Bw_Value); print(f"Water Density: {RhoW_Value} g/cc");
    MiuW_Value = Brine_Prop.MiuW(pressure, userInputData["temperature"], TDS, corr); print(f"Water Viscocity: {MiuW_Value} cP");
    Cw_Value = Brine_Prop.CW(pressure, userInputData["temperature"]); print(f"Isothermal Compressibility: {Cw_Value} microsip");


from Properties import Oil_Prop;
def calculateOilProperties(pressure:float):
    # Input Required Data
    print(colorama.Fore.WHITE);
    Oil_API = float(input("Enter the oil API: "));
    corr_Rs = input("Enter the correlation for Rs [Glaso/Standing]: ").lower();
    corr_Rho = input("Enter the correlation for Rho []: ");
    Rsb = float(input("Enter the GOR at Bubble point pressure(at PVT data) (scf/STB): "))
    
    # OIL PROPERTIES
    print('\n', colorama.Fore.LIGHTGREEN_EX + "========== Oil PVT Correlation ==========");
    # Calculate Pb
    Pb_Value = Oil_Prop.Oil_Pbubble(Rsb, userInputData["gas_SG"], Oil_API, userInputData["temperature"]);
    print(f"Bubble Point Pressure: {Pb_Value} psi ({condition(pressure, Pb_Value)})"); 
    
    # Calculate Isothermal Oil Compressibility
    Co_Value = Oil_Prop.Oil_Compressibility(pressure, Pb_Value, userInputData["temperature"], Oil_API, Rsb, userInputData["gas_SG"]);
    print(f"Isothermal Compressibility: {Co_Value} microsip");
    
    # Calculate Solution Gas-Oil Ratio
    if corr_Rs.lower() == 'glasso':
        Rs_Value = Oil_Prop.Rs_Glaso(Oil_API, userInputData["temperature"], pressure, Pb_Value);
    elif corr_Rs.lower() == 'standing':
        Rs_Value = Oil_Prop.Rs_Standing(Oil_API, userInputData["temperature"], pressure, Pb_Value);
    print(f"Gas-Oil Ratio: {Rs_Value} scf/STB");
    
    # Calculate Oil FVF
    Bo_Value = Oil_Prop.Oil_FVF(Pb_Value, Oil_API, Rsb, userInputData["gas_SG"], userInputData["temperature"], pressure);
    print(f"Oil FVF: {Bo_Value} RB/STB");
    
    # Calculate Oil Density
    if corr_Rho.lower() == 'standard':
        RhoO_Value = Oil_Prop.Rho_Standard(Bo_Value, userInputData["gas_SG"], Rs_Value, Oil_API); print(f"RhoO Value: {RhoO_Value}");
    elif corr_Rho.lower() == 'standing':
        RhoO_Value = Oil_Prop.Rho_Standing(Co_Value, pressure, Pb_Value, Oil_API, userInputData["gas_SG"], userInputData["temperature"], Rs_Value);
    print(f"Oil Density: {RhoO_Value} g/cc");
    
    # Calculate Oil Viscocity
    Miu_Value = Oil_Prop.oil_mu(pressure, Pb_Value, userInputData["gas_SG"], Oil_API, userInputData["temperature"], Rs_Value);
    print(f"Oil Viscocity: {Miu_Value} cP");

    Miu_od_Value = Oil_Prop.Miu_DO(Oil_API, userInputData["temperature"]);
    print(f"Dead-Oil Viscocity: {Miu_od_Value} cP");
    
##### CONDITION #####
def condition(pressure:float, Pb:float) -> str:
    if pressure > Pb:
        return "Undersaturated";
    else:
        return 'Saturated'