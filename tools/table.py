import os;
import pandas as pd;
from openpyxl import load_workbook;
from pyfiglet import figlet_format;
import colorama;

colorama.init();
def showTableTittle():
    title = figlet_format("PVT Table");
    print(colorama.Fore.YELLOW + title); print(colorama.Style.RESET_ALL);

properties_data = {
    'P (psia)': [4500, 4387.8675, 4275.735, 4163.6025, 4051.47, 3939.3375, 3827.205, 3715.0725, 3602.94, 3490.8075, 3378.675, 3266.5425, 3154.41, 3042.2775, 2930.145, 2818.0125, 2705.88, 2593.7475, 2481.615, 2369.4825, 2257.35, 2145.2175, 2033.085, 1920.9525, 1808.82, 1696.6875, 1584.555, 1472.4225, 1360.29, 1248.1575, 1136.025, 1023.8925, 911.76, 799.6275, 687.495, 575.3625, 463.23, 351.0975, 238.965, 126.8325, 14.7],
    'Bo (RB/STB)': [12],
    'Rs (MSCF/STB)': [12],
    'Bg (RB/MSCF)': [1],
    'Bw (RB/STB)': [1],
    'Rsw (SCF/STB)': [1],
    'H2O in Gas': [1],
    'Conditions': [1],
    'Z (vol/vol)': [1],
    'P (psia)': [1],
    'Oil Density (lbm/cf)': [1],
    'Gas Density (lbm/cf)': [1],
    'Brine Dencity (lbm/cf)': [1],
    'Oil Viscocity (cP):': [1],
    'Gas Viscocity (cP)': [1],
    'Brine Viscocity (cP)': [1]
}

############ Properties Calculation ############
from Properties import Oil_Prop;
def Bo_Data():
    Oil_Prop.Bo_Standing()

df = pd.DataFrame(properties_data);
        
def openExcelApp():
    showTableTittle();
    excel_file_path = 'C:\\PVT_Table.xlsx';
    with pd.ExcelWriter(excel_file_path) as writer:
        df.to_excel(writer, sheet_name='PVT Table');
        
    userInput = input(colorama.Fore.CYAN + "Open Excel? [yes/no] ").lower();
    if userInput == 'yes':
        if os.path.exists(excel_file_path):
            workbook = load_workbook(excel_file_path);
            workbook.save(excel_file_path);
        
            try:
                os.system('start excel.exe "%s"' %excel_file_path);
                print(colorama.Fore.BLUE + "Successfully opened the file!\n");
            except:
                print(colorama.Fore.RED + "Something went wrong!\n");
        else:
            print(colorama.Fore.RED + "File not found!\n");
    elif userInput == 'no':
        print(colorama.Fore.LIGHTCYAN_EX + f"Good bye then!\nMake sure you check the .xlsx file in {excel_file_path}\n");
    else:
        print(colorama.Fore.RED + "Command not detected as a valid input! This session will be terminated to avoid errors\n");
