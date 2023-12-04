import matplotlib.pyplot as plt;
import colorama;
from pyfiglet import figlet_format;

colorama.init();
def showVisualOption():
    print(colorama.Fore.RED + "[1]", colorama.Fore.YELLOW + "Pressure & Gas FVF             ", colorama.Fore.RED + "[7]", colorama.Fore.YELLOW + "Pressure & Gas Density")
    print(colorama.Fore.RED + "[2]", colorama.Fore.YELLOW + "Pressure & Water FVF           ", colorama.Fore.RED + "[8]", colorama.Fore.YELLOW + "Pressure & Gas-Water Ratio")
    print(colorama.Fore.RED + "[3]", colorama.Fore.YELLOW + "Pressure & Water Viscocity     ", colorama.Fore.RED + "[9]", colorama.Fore.YELLOW + "Pressure & Water Isothermal Compressibility")
    print(colorama.Fore.RED + "[4]", colorama.Fore.YELLOW + "Pressure & Gas Viscocity       ", colorama.Fore.RED + "[10]", colorama.Fore.YELLOW + "Pressure & Oil FVF")
    print(colorama.Fore.RED + "[5]", colorama.Fore.YELLOW + "Pressure & GOR                 ", colorama.Fore.RED + "[11]", colorama.Fore.YELLOW + "Pressure & Z Factor")
    print(colorama.Fore.RED + "[6]", colorama.Fore.YELLOW + "Pressure & Oil Density         ", colorama.Fore.RED + "[12]", colorama.Fore.YELLOW + "Pressure & Oil Viscocity")
    print(colorama.Fore.YELLOW + "[13]", colorama.Fore.RED+ "EXIT", '\n'); 

    
def initiateGraph():
    from tools import calculator;
    data = calculator.properties_data;
    
    title = figlet_format("Graphics");
    print(colorama.Fore.LIGHTGREEN_EX + title); print(colorama.Style.RESET_ALL);
    while True:
        showVisualOption();
        userInput = int(input(colorama.Fore.LIGHTBLUE_EX + "Choose the parameter: "));
        if userInput == 1:
            makeGraph("Pressure & Gas FVF", "Pressure", "Gas FVF", data['P (psia)'], data['Bg (RB/MSCF)'])
        elif userInput == 2:
            makeGraph("Pressure & Water FVF", "Pressure", "Water FVF", data["P (psia)"], data['Bw (RB/STB)'])
        elif userInput == 3:
            makeGraph("Pressure & Water Viscocity", "Pressure", "Water Viscocity", data["P (psia)"], data['Brine Viscocity (cP)'])
        elif userInput == 4:
            makeGraph("Pressure & Gas Viscocity", "Pressure", "Gas Viscocity", data["P (psia)"], data['Gas Viscocity (cP)'])
        elif userInput == 5:
            makeGraph("Pressure & GOR", "Pressure", "GOR", data["P (psia)"], data['Rs (MSCF/STB)']);
        elif userInput == 6:
            makeGraph("Pressure & Oil Density", "Pressure", "Oil Density", data["P (psia)"], data['Oil Density (lbm/cf)']);
        elif userInput == 7:
            makeGraph("Pressure & Gas Density", "Pressure", "Gas Density", data["P (psia)"], data['Gas Density (lbm/cf)']);
        elif userInput == 8:
            makeGraph("Pressure & Gas-Water Ratio", "Pressure", "Gas-Water Ratio", data["P (psia)"], data['Rsw (SCF/STB)']);
        elif userInput == 9:
            makeGraph("Pressure & Water Isothermal Compressibility", "Pressure", "Water Isothermal Compressibility", data["P (psia)"], data['Cw (microsip)']);
        elif userInput == 10:
            makeGraph("Pressure & Oil FVF", "Pressure", "Oil FVF", data["P (psia)"], data['Bo (RB/STB)']);
        elif userInput == 11:
            makeGraph("Pressure & Z Factor", "Pressure", "Z Factor", data["P (psia)"], data['Z (vol/vol)']);
        elif userInput == 12:
            makeGraph("Pressure & Oil Viscocity", "Pressure", "Oil Viscocity", data["P (psia)"], data['Oil Viscocity (cP)'])
        elif userInput == 13:
            print(colorama.Fore.GREEN + "Bye Then!\n\n");
            break;

def makeGraph(title:str, xLabel:str, yLabel:str, xParam:list, yParam:list):
    
    plt.style.use('fast');
    plt.title(title);
    plt.xlabel(xLabel);
    plt.ylabel(yLabel);
    plt.plot(xParam, yParam);
    plt.grid(True);
    # plt.legend()
    plt.show()