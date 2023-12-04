import subprocess;

library_to_install = ["pandas", "pyfiglet", "colorama", "numpy", "openpyxl", "matplotlib"];

print("\n========== WARNING!! ==========\n");
print("To run the Python code, you have to install these modules: ")
with open('requirements.txt', 'r') as file:
    count = 1
    for line in file:
        line = line.rstrip();
        print(f"{count}. {line}");
        count+=1;
        
print("\nThis section will install the required modules automatically. Install the modules? \n[1] yes     [2] no     [3] I already have it")
isInstallModule = int(input("\nEnter your choice: "));
if isInstallModule == 1:
    for module in library_to_install:
        subprocess.check_call(["python", "-m", "pip", "install", module]);
        
    from pyfiglet import figlet_format;
    import colorama;
    colorama.init();
elif isInstallModule == 3:
    
    print("Make sure you have installing all modules above");
    from pyfiglet import figlet_format;
    import colorama;
    colorama.init();
elif isInstallModule == 2:
    print("\nThe code will not be executed to avoid errors occurring when running the code ...");



oilProperties = {
    # property: correlations
    "Bo_Sat": "Standing",
    "Bo_Und": "",
    "Rs": ["Glasso", "Vasquez-Beggs"],
    "Rho": ["Standard", "Standing"],
    "Miu": [],
    "Co": "Vasquez-Beggs"
}
gasProperties = {
    # property: correlations
    "Tpc": ["Sutton", "NG", "Condensate"], 
    "Ppc": ["Sutton", "NG", "Condensate"],
    "Tpr": None,
    "Ppr": None,
    "Tpcz": None,
    "Ppcz": None,
    "MiuG": None,
    "Cg": "Standard",
    "Bg": "Hawlert-Packard",
    "Z-Fact": ["Dranchuk-AbuKassem", "Hall-Yarborough", "Beggs"]
}
brineProperties = {
    # property: correlation
    "Bw": ["Free", "Saturated"],
    "MiuW": ["Mc Chain", "Beggs"],
    "Cw": []
}

######### Initiate Menu ##########
def showMainMenu(count):
    if count == 0:
        print(colorama.Fore.GREEN + "[1]", colorama.Fore.CYAN + "START");
        print(colorama.Fore.GREEN + "[2]", colorama.Fore.CYAN + "EXIT");
        print(colorama.Style.RESET_ALL);
    else:
        print(colorama.Fore.GREEN + "[1]", colorama.Fore.CYAN + "PVT Calculator");
        print(colorama.Fore.GREEN + "[2]", colorama.Fore.CYAN + "Graphics");
        print(colorama.Fore.GREEN + "[3]", colorama.Fore.CYAN + "PVT Table");
        print(colorama.Fore.GREEN + "[4]", colorama.Fore.CYAN + "EXIT");
        print(colorama.Style.RESET_ALL);

    
# THE FUNCTIONS BELOW IS TEMPORARY
def mainLoop():
    count = 0
    while True:
        showMainMenu(count);
        userInput = int(input("Enter your choice: "));
        if count != 0:
            if userInput == 1:
                from tools import calculator
                calculator.calculatorLoop();
                count+=1;
            elif userInput == 2:
                from tools import visual
                visual.initiateGraph();
                count+=1;
            elif userInput == 3:
                from tools import table
                table.openExcelApp();
                count+=1;
            elif userInput == 4:
                bye = figlet_format("BYE!", font = "banner3-D"); print(colorama.Fore.CYAN + bye);
                print(colorama.Fore.GREEN + "\nThanks for using this code. Bye then!");
                break;
            else:
                invalid = figlet_format("Invalid input!", font = "banner3-D"); print(colorama.Fore.RED + invalid);
        elif count == 0:
            if userInput == 1:
                from tools import calculator
                calculator.calculatorLoop();
                count+=1;
            elif userInput == 2:
                bye = figlet_format("BYE!", font = "banner3-D"); print(colorama.Fore.CYAN + bye);
                print(colorama.Fore.GREEN + "\nThanks for using this code. Bye then!");
                break;
            else:
                invalid = figlet_format("Invalid input!", font = "banner3-D"); print(colorama.Fore.RED + invalid);
            
    return 0;
    

# MAIN LOOPING
if __name__ == '__main__':
    if isInstallModule == 1 or isInstallModule == 3:
        title = figlet_format("PVT Calculator");
        print(colorama.Fore.RED + title); print(colorama.Style.RESET_ALL);
        mainLoop();
    else:
        print("Make sure you have installing all modules above");
    