import matplotlib.pyplot as plt;
import colorama;
from pyfiglet import figlet_format;

colorama.init();
def showVisualTitle():
    print(colorama.Fore.RED + "[1]", colorama.Fore.YELLOW + "Pressure & Gas FVF\t", colorama.Fore.RED + "[8]", colorama.Fore.YELLOW + "Pressure & Gas Density")
    print(colorama.Fore.RED + "[2]", colorama.Fore.YELLOW + "Pressure & Water FVF\t", colorama.Fore.RED + "[9]", colorama.Fore.YELLOW + "Pressure & Gas-Water Ratio")
    print(colorama.Fore.RED + "[3]", colorama.Fore.YELLOW + "Pressure & Water Viscocity\t", colorama.Fore.RED + "[10]", colorama.Fore.YELLOW + "Pressure & Water Isothermal Compressibility")
    print(colorama.Fore.RED + "[4]", colorama.Fore.YELLOW + "Pressure & Ppr\t", colorama.Fore.RED + "[11]", colorama.Fore.YELLOW + "Pressure & Oil FVF")
    print(colorama.Fore.RED + "[5]", colorama.Fore.YELLOW + "Pressure & GOR\t", colorama.Fore.RED + "[12]", colorama.Fore.YELLOW + "Pressure & Z Factor")
    print(colorama.Fore.RED + "[6]", colorama.Fore.YELLOW + "Pressure & Oil Density\t", colorama.Fore.RED + "[13]", colorama.Fore.YELLOW + "Pressure & Oil Viscocity")
    print(colorama.Fore.YELLOW + "[7]", colorama.Fore.RED+ "EXIT", '\n'); 

    

def initiateGraph():
    from tools import calculator;
    data = calculator.properties_data;
    
    title = figlet_format("Graphics");
    print(colorama.Fore.LIGHTGREEN_EX + title); print(colorama.Style.RESET_ALL);
    while True:
        showVisualTitle();
        userInput = int(input(colorama.Fore.LIGHTBLUE_EX + "Choose the parameter: "));
        if userInput == 1:
            makeGraph("Pressure & Gas FVF", "Pressure", "Gas FVF", data['P (psia)'], data['Bg (RB/MSCF)'])


def makeGraph(title:str, xLabel:str, yLabel:str, xParam:list, yParam:list):
    
    plt.style.use('fast');
    plt.title(title);
    plt.xlabel(xLabel);
    plt.ylabel(yLabel);
    plt.plot(xParam, yParam);
    plt.grid(True);
    # plt.legend()
    plt.show()