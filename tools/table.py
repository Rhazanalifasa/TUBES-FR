import os;
import pandas as pd;
from openpyxl import load_workbook;
from pyfiglet import figlet_format;
from tools import calculator
import colorama;

colorama.init();
def showTableTittle():
    title = figlet_format("PVT Table");
    print(colorama.Fore.YELLOW + title); print(colorama.Style.RESET_ALL);

       
############ Tabel Development ############        
def openExcelApp():
    showTableTittle();
    
    data = calculator.properties_data
    df = pd.DataFrame(data)
    
    current_directory = os.getcwd();
    excel_file = 'PVT_Table.xlsx';
    excel_file_path = os.path.join(current_directory, excel_file);
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

