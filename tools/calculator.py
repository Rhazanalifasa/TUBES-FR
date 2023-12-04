from pyfiglet import figlet_format;
import colorama;
import pandas as pd;
from typing import *;

# Ganti Pemilihan korelasi dengan hanya memasukkan pilihan dalam angka
colorama.init();
def showTittle():
    
    title = figlet_format("Calculator");
    print(colorama.Fore.MAGENTA + title); print(colorama.Style.RESET_ALL);
    
#### User Input Data ####
PropertiesData = dict();

##### Calculator MAINLOOP #####
def calculatorLoop():
    calculateCriticalProperties(userInput); print("\n")
    calculateGasProperties(userInput); print("\n")
    calculateOilProperties(userInput); print('\n')
    calculateBrineProperties(userInput); print('\n')
    initiateTable();

# Input the required data
showTittle()
userInput = float(input(colorama.Fore.LIGHTCYAN_EX + "Enter the pressure value (psi): ")); print("\n");

print(colorama.Fore.LIGHTRED_EX + "========= Critical Properties Input =========")
corr = input("Enter the correlation name [Sutton/Misc Standing/Condensate Standing]: ").lower();
gas_SG = float(input("Enter gas specific gravity: "));
temperature = float(input("Enter the temperature (F): "))
M_CO2 = float(input("Enter CO2 mol: "));
M_H2S = float(input("Enter H2S mol: "));
M_N2 = float(input("Enter N2 mol: "));

print(colorama.Fore.LIGHTBLUE_EX + "========= Brine Properties Input =========")
BrinePropList = list();
TDS = float(input("Enter Total Dissolve Solid Value (ppm): "));
corr_brine = input("Enter the correlation for MiuW [Beggs/McChain]: ").lower();

print(colorama.Fore.LIGHTGREEN_EX + "========= Oil Properties Input =========")
OilPropList = list();
Oil_API = float(input("Enter the oil API: "));
corr_Rho = int(input("Enter the correlation for Rho ([1] Standard\t[2] Standing): "));
Rsb = float(input("Enter the GOR at Bubble point pressure(at PVT data) (scf/STB): "))
    
##### PROPERTIES #####x
from Properties import Critical_Prop;
def calculateCriticalProperties(pressure:float):
    # Input requirement
    global corr 
    global gas_SG 
    global temperature
    global M_CO2 
    global M_H2S 
    global M_N2 
    
    # CRITICAL PROPERTIES
    print('\n', colorama.Fore.LIGHTRED_EX + "=========== Critical Properties ==========");
    Ppc_Value = Critical_Prop.Ppc_(gas_SG, corr); 
    print(f"Ppc            : {Ppc_Value} psia");
    Tpc_Value = Critical_Prop.Tpc_(gas_SG, corr); 
    print(f"Tpc            : {Tpc_Value} Rankine");
    
    Tpcz_Value = Critical_Prop.Tpcz(Tpc_Value, M_CO2, M_H2S, M_N2); 
    print(f"Tpcz Value     : {Tpcz_Value}");
    Ppcz_Value = Critical_Prop.Ppcz(Ppc_Value, M_CO2, M_H2S, M_N2); 
    print(f"Ppcz Value     : {Ppcz_Value} ");
    
    Tpr_Value = Critical_Prop.Tpr(temperature, Tpc_Value); 
    print(f"Tpr Value      : {Tpr_Value}");
    Ppr_Value = Critical_Prop.Ppr(pressure, Ppc_Value); 
    print(f"Ppr Value      : {Ppr_Value}");
    
    # Insert user input to PropertiesData
    gas_SG = gas_SG;
    temperature = temperature;
    PropertiesData["Gas Molecule"] = [M_CO2, M_H2S, M_N2];
    PropertiesData["Critical Value"] = [Ppc_Value, Tpc_Value, Ppcz_Value, Tpcz_Value, Ppr_Value, Tpr_Value, corr];


from Properties import Gas_Prop; 
from Properties import Z_Fact;
def calculateGasProperties(pressure:float):
    # GAS PROPERTIES    
    print(colorama.Fore.YELLOW + " ========== Gas PVT Correlation ==========");
    GasPropList = list();
    f = Z_Fact.hall_yarborough(PropertiesData["Critical Value"][4], PropertiesData["Critical Value"][5]);
    Y_estimate = Z_Fact.newton_raphson(f, x=0.25);
    Z_Value = Z_Fact.Z(PropertiesData["Critical Value"][4], PropertiesData["Critical Value"][5], Y_estimate); 
    print(f"Z Value             : {Z_Value}");
    
    Bg_Value = Gas_Prop.Bg(pressure, temperature, Z_Value); 
    print(f"Bg_Value            : {Bg_Value}"); GasPropList.append(Bg_Value);
    
    RhoG_Value = Gas_Prop.RhoG(gas_SG, pressure, temperature, Z_Value); 
    print(f"RhoG Value          : {RhoG_Value}"); GasPropList.append(RhoG_Value);
    
    MiuG_Value = Gas_Prop.MiuG(gas_SG, temperature, RhoG_Value); 
    print(f"MiuG Value          : {MiuG_Value}"); GasPropList.append(MiuG_Value);
    
    Cg_Value = Gas_Prop.Cg(PropertiesData["Critical Value"][5], PropertiesData["Critical Value"][4], Z_Value, PropertiesData["Critical Value"][0]); 
    print(f"Cg Value            : {Cg_Value}");
    
    PropertiesData["Gas Properties"] = GasPropList;
    

from Properties import Brine_Prop;
def calculateBrineProperties(pressure:float):
    
    global BrinePropList 
    global TDS 
    global corr_brine

    # BRINE PROPERTIES
    print('\n', colorama.Fore.LIGHTBLUE_EX + "========== Brine PVT Correlation ==========");
    Bw_Value = Brine_Prop.BW(pressure, temperature); 
    print(f"Water FVF                 : {Bw_Value} RB/STB"); BrinePropList.append(Bw_Value);
    
    Pbubble_water = Brine_Prop.Water_Pbubble(temperature); 
    print(f"Bubble Point Pressure     : {Pbubble_water} psia");
    
    Rsw_Value = Brine_Prop.RSW(pressure, temperature, TDS); 
    print(f"Solution Gas-Water Ratio  : {Rsw_Value} scf/STB"); BrinePropList.append(Rsw_Value);
    
    RhoW_Value = Brine_Prop.RhoW(TDS, Bw_Value); BrinePropList.append(RhoW_Value);
    print(f"Water Density             : {RhoW_Value} g/cc"); 
    
    MiuW_Value = Brine_Prop.MiuW(pressure, temperature, TDS, corr_brine); 
    print(f"Water Viscocity           : {MiuW_Value} cP"); BrinePropList.append(MiuW_Value);
    
    Cw_Value = Brine_Prop.CW(pressure, temperature); 
    print(f"Isothermal Compressibility: {Cw_Value} microsip"); BrinePropList.append(Cw_Value);
    
    PropertiesData["Brine Properties"] = BrinePropList;


from Properties import Oil_Prop;
def calculateOilProperties(pressure:float):
    # Input Required Data
    global OilPropList
    global Oil_API
    global corr_Rho 
    global Rsb 
    
    # OIL PROPERTIES
    print('\n', colorama.Fore.LIGHTGREEN_EX + "========== Oil PVT Correlation ==========");
    # Calculate Pb
    Pb_Value = Oil_Prop.Oil_Pbubble(Rsb, gas_SG, Oil_API, temperature);
    print(f"Bubble Point Pressure        : {Pb_Value} psi ({condition(pressure, Pb_Value)})"); 
    
    # Calculate Isothermal Oil Compressibility
    Co_Value = Oil_Prop.Oil_Compressibility(pressure, Pb_Value, temperature, Oil_API, Rsb, gas_SG);
    print(f"Isothermal Compressibility   : {Co_Value} microsip"); 
    OilPropList.append(Co_Value);
    
    # Calculate Solution Gas-Oil Ratio
    Rs_Value = Oil_Prop.Rs_Standing(Oil_API, temperature, pressure, Pb_Value);
    print(f"Gas-Oil Ratio                : {Rs_Value} scf/STB"); 
    OilPropList.append(Rs_Value);
    
    # Calculate Oil FVF
    Bo_Value = Oil_Prop.Oil_FVF(Pb_Value, Oil_API, Rsb, gas_SG, temperature, pressure);
    print(f"Oil FVF                      : {Bo_Value} RB/STB"); 
    OilPropList.append(Bo_Value);
    
    # Calculate Oil Density
    if corr_Rho == 1:
        RhoO_Value = Oil_Prop.Rho_Standard(Bo_Value, gas_SG, Rs_Value, Oil_API); 
    elif corr_Rho == 2:
        RhoO_Value = Oil_Prop.Rho_Standing(Co_Value, pressure, Pb_Value, Oil_API, gas_SG, temperature, Rs_Value);
    print(f"Oil Density                  : {RhoO_Value} g/cc");
    OilPropList.append(RhoO_Value);
    
    # Calculate Oil Viscocity
    Miu_Value = Oil_Prop.oil_mu(pressure, Pb_Value, gas_SG, Oil_API, temperature, Rs_Value);
    print(f"Oil Viscocity                : {Miu_Value} cP"); 
    OilPropList.append(Miu_Value);

    Miu_od_Value = Oil_Prop.Miu_DO(Oil_API, temperature);
    print(f"Dead-Oil Viscocity           : {Miu_od_Value} cP");
    
    PropertiesData["Oil Properties"] = OilPropList;
    PropertiesData["Bubble Point Pressure"] = Pb_Value;
    PropertiesData["Oil API"] = Oil_API;
    
    
##### CONDITION #####
def condition(pressure:float, Pb:float) -> str:
    if pressure > Pb:
        return "Undersaturated";
    else:
        return 'Saturated'
    

##### Initiating Table ##### 
from tools import table;
properties_data = {
    'P (psia)': [],
    'Bo (RB/STB)': [], # Oil
    'Rs (MSCF/STB)': [], # Oil
    'Bg (RB/MSCF)': [], # Gas
    'Bw (RB/STB)': [], # Brine
    'Rsw (SCF/STB)': [], # Brine
    'Cw (microsip)': [], # Brine
    'Co (microsip)': [], # Oil
    # 'Cg (microsip)': [], # Gas
    'Conditions': [], 
    'Z (vol/vol)': [], 
    'P (psia)': [],
    'Oil Density (lbm/cf)': [], 
    'Gas Density (lbm/cf)': [],
    'Brine Dencity (lbm/cf)': [],
    'Oil Viscocity (cP)': [],
    'Gas Viscocity (cP)': [],
    'Brine Viscocity (cP)': []
}

def initiateTable():
    

    pressureList = [4500, 4387.8675, 4275.735, 4163.6025, 4051.47, 3939.3375, 3827.205, 3715.0725, 3602.94, 3490.8075, 3378.675, 3266.5425, 3154.41, 3042.2775, 2930.145, 2818.0125, 2705.88, 2593.7475, 2481.615, 2369.4825, 2257.35, 2145.2175, 2033.085, 1920.9525, 1808.82, 1696.6875, 1584.555, 1472.4225, 1360.29, 1248.1575, 1136.025, 1023.8925, 911.76, 799.6275, 687.495, 575.3625, 463.23, 351.0975, 238.965, 126.8325, 14.7]
    for pressure in pressureList:
        properties_data["P (psia)"].append(pressure);
        
        Pb_Value = Oil_Prop.Oil_Pbubble(Rsb, gas_SG, Oil_API, temperature);
        Bo_ = Oil_Prop.Oil_FVF(Pb_Value, Oil_API, Rsb, gas_SG, temperature, pressure);
        properties_data['Bo (RB/STB)'].append(Bo_);
        
        Rs_ = Oil_Prop.Rs_Standing(Oil_API, temperature, pressure, Pb_Value);
        properties_data['Rs (MSCF/STB)'].append(Rs_);
        
        Ppc_Value = Critical_Prop.Ppc_(gas_SG, corr);
        Tpc_Value = Critical_Prop.Tpc_(gas_SG, corr);
        Tpr_Value = Critical_Prop.Tpr(temperature, Tpc_Value); 
        Ppr_Value = Critical_Prop.Ppr(pressure, Ppc_Value);
        f = Z_Fact.hall_yarborough(Ppr_Value, Tpr_Value);
        Y_estimate = Z_Fact.newton_raphson(f, x=0.25); 
        Z_Value = Z_Fact.Z(Ppr_Value, Tpr_Value, Y_estimate);
        properties_data['Z (vol/vol)'].append(Z_Value);
        
        Bg_ = Gas_Prop.Bg(pressure, temperature, Z_Value);
        properties_data['Bg (RB/MSCF)'].append(Bg_);
        
        Bw_ = Brine_Prop.BW(pressure, temperature);
        properties_data['Bw (RB/STB)'].append(Bw_);
        
        Rsw_ = Brine_Prop.RSW(pressure, temperature, TDS);
        properties_data['Rsw (SCF/STB)'].append(Rsw_);
        
        Cw_ = Brine_Prop.CW(pressure, temperature);
        properties_data["Cw (microsip)"].append(Cw_);
        
        Co_ = Oil_Prop.Oil_Compressibility(pressure, Pb_Value, temperature, Oil_API, Rsb, gas_SG);
        properties_data["Co (microsip)"].append(Co_);
        
        # Cg_ = Gas_Prop.Cg(Tpr_Value, Ppr_Value, Z_Value, Ppc_Value);
        # properties_data["Cg (microsip)"].append(Cg_); 
        
        Conditions_ = condition(pressure, Pb_Value);
        properties_data['Conditions'].append(Conditions_);
        
        Co_ = Oil_Prop.Oil_Compressibility(pressure, Pb_Value, temperature, Oil_API, Rsb, gas_SG);
        if corr_Rho == 1:
            RhoO_Value = Oil_Prop.Rho_Standard(Bo_, gas_SG, Rs_, Oil_API); 
        elif corr_Rho == 2:
            RhoO_Value = Oil_Prop.Rho_Standing(Co_, pressure, Pb_Value, Oil_API, gas_SG, temperature, Rs_);
        properties_data['Oil Density (lbm/cf)'].append(RhoO_Value);
        
        Gas_Den = Gas_Prop.RhoG(gas_SG, pressure, temperature, Z_Value); 
        properties_data['Gas Density (lbm/cf)'].append(Gas_Den);
        
        Brine_Den = Brine_Prop.RhoW(TDS, Bw_);
        properties_data['Brine Dencity (lbm/cf)'].append(Brine_Den);
        
        Oil_Viscos = Oil_Prop.Oil_Miu(pressure, Pb_Value, gas_SG, Oil_API, temperature, Rs_);
        properties_data['Oil Viscocity (cP)'].append(Oil_Viscos);
        
        Gas_Viscos = Gas_Prop.Gas_Miu(temperature, Gas_Den, gas_SG);
        properties_data['Gas Viscocity (cP)'].append(Gas_Viscos);
        
        Brine_Viscos = Brine_Prop.MiuW(pressure, temperature, TDS, corr_brine);
        properties_data['Brine Viscocity (cP)'].append(Brine_Viscos);
        

    return properties_data;
        