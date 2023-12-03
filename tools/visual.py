import numpy as np
import matplotlib.pyplot as plt;
import colorama;
from pyfiglet import figlet_format;

colorama.init();
def showVisualTitle():
    title = figlet_format("Graphics");
    print(colorama.Fore.LIGHTGREEN_EX + title); print(colorama.Style.RESET_ALL);
    
    print(colorama.Fore.RED + "[1]", colorama.Fore.YELLOW + "Pressure & Gas FVF\t\t", colorama.Fore.RED + "[6]", colorama.Fore.YELLOW + "Pressure & Gas Density")
    print(colorama.Fore.RED + "[2]", colorama.Fore.YELLOW + "Pressure & Water FVF\t\t", colorama.Fore.RED + "[7]", colorama.Fore.YELLOW + "Pressure & Gas-Water Ratio")
    print(colorama.Fore.RED + "[3]", colorama.Fore.YELLOW + "Pressure & Water Viscocity\t\t", colorama.Fore.RED + "[8]", colorama.Fore.YELLOW + "Pressure & Water Isothermal Compressibility")

def addGraphFunc(func):
    def wrapper(title, xLabel, yLabel, xValue, yValue):
        showVisualTitle();
        func(title, xLabel, yLabel, xValue, yValue);
        plt.style.use('fast');
        plt.grid(True);
        plt.show();
        
    return wrapper;
        
@addGraphFunc
def createGraph(title, xLabel, yLabel, xValue, yValue):
    plt.title(title);
    plt.xlabel(xLabel);
    plt.ylabel(yLabel);
    plt.plot(xValue, yValue);
    plt.show()
# NOT FINISHED YET!