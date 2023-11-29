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
from pyfiglet import figlet_format;
import colorama;

colorama.init();
title = figlet_format("PVT Calculator");
print(colorama.Fore.RED + title); print(colorama.Style.RESET_ALL);
def showMenu():
    print(colorama.Fore.GREEN + "[1]", colorama.Fore.CYAN + "PVT Calculator");
    print(colorama.Fore.GREEN + "[2]", colorama.Fore.CYAN + "Graphics");
    print(colorama.Fore.GREEN + "[3]", colorama.Fore.CYAN + "PVT Table");
    print(colorama.Fore.GREEN + "[4]", colorama.Fore.CYAN + "EXIT");
    print(colorama.Style.RESET_ALL);

    
# THE FUNCTIONS BELOW IS TEMPORARY
def mainLoop():
    while True:
        showMenu();
        userInput = int(input("Enter your choice: "));
        if userInput == 1:
            enterCalculatorSection();
        elif userInput == 2:
            enterGraphicsSection();
        elif userInput == 3:
            enterTableSection();
        elif userInput == 4:
            print(colorama.Fore.YELLOW + "Thanks for using this shit. Bye then!");
            break;
        else:
            print("Invalid input!");
            
    return 0;


def enterGraphicsSection():
    print("This is graphics section\n");


def enterCalculatorSection():
    print("This is calculator section\n");


def enterTableSection():
    print("This is table section\n");

# MAIN LOOPING
if __name__ == '__main__':
    mainLoop();
    