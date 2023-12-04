from pyfiglet import figlet_format;
import colorama;
colorama.init();

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

warn = figlet_format("WARNING!", font = "banner3-D");
print('\n', colorama.Fore.YELLOW + warn);
print(colorama.Fore.WHITE + "To run the Python code, you need this 3rd module: ")
with open('requirements.txt', 'r') as file:
    count = 1
    for line in file:
        line = line.rstrip();
        print(f"{count}. {line}");
        count+=1;
isKeepGoing = input("\nKeep going? [yes/no] "); print('\n');

######### Initiate Menu ##########
def showMainMenu():
    print(colorama.Fore.GREEN + "[1]", colorama.Fore.CYAN + "PVT Calculator");
    print(colorama.Fore.GREEN + "[2]", colorama.Fore.CYAN + "Graphics");
    print(colorama.Fore.GREEN + "[3]", colorama.Fore.CYAN + "PVT Table");
    print(colorama.Fore.GREEN + "[4]", colorama.Fore.CYAN + "EXIT");
    print(colorama.Style.RESET_ALL);

    
# THE FUNCTIONS BELOW IS TEMPORARY
def mainLoop():
    while True:
        showMainMenu();
        userInput = int(input("Enter your choice: "));
        if userInput == 1:
            from tools import calculator
            calculator.calculatorLoop();
        elif userInput == 2:
            from tools import visual
            visual.initiateGraph();
        elif userInput == 3:
            from tools import table
            table.openExcelApp();
        elif userInput == 4:
            print(colorama.Fore.GREEN + "Thanks for using this code. Bye then!");
            break;
        else:
            print("Invalid input!");
            
    return 0;
    

# MAIN LOOPING
if __name__ == '__main__':
    if isKeepGoing == 'yes':
        title = figlet_format("PVT Calculator");
        print(colorama.Fore.RED + title); print(colorama.Style.RESET_ALL);
        mainLoop();
    else:
        print(colorama.Fore.GREEN + "Make sure you have installing all module above");
    