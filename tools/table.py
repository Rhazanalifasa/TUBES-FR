import os;
import pandas as pd;
import numpy as np;
from openpyxl import load_workbook;
from pyfiglet import figlet_format;
import colorama;

colorama.init();
def showTableTittle():
    title = figlet_format("PVT Table");
    print(colorama.Fore.LIGHTYELLOW_EX + title); print(colorama.Style.RESET_ALL);

properties_data = {
    'P (psia)': [12],
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

df = pd.DataFrame(properties_data);
with pd.ExcelWriter('PVT_Table.xlsx') as writer:
    df.to_excel(writer, sheet_name='PVT Table');
        
def openExcelApp():
    showTableTittle();
    excel_file_path = 'C:\\Tubes FR\\TUBES-FR\\PVT_Table.xlsx';
    userInput = input(colorama.Fore.CYAN + "Open Excel? [yes/no]").lower();
    
    if userInput == 'yes':
        if os.path.exists(excel_file_path):
            workbook = load_workbook(excel_file_path);
            workbook.save(excel_file_path);
        
            try:
                os.system('start excel.exe "%s"' %excel_file_path);
                print(colorama.Fore.BLUE + "Successfully opened the file!\n");
            except:
                print(colorama.Fore.RED + "Something went wrong!\n")
        else:
            print(colorama.Fore.RED + "File not found!\n");
    else:
        print("Good bye then!\n");
