import numpy as np
import matplotlib.pyplot as plt;
import colorama;
from pyfiglet import figlet_format;

colorama.init();
def showVisualTitle():
    title = figlet_format("Graphics");
    print(colorama.Fore.LIGHTGREEN_EX + title); print(colorama.Style.RESET_ALL);

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
sumbu_x = np.arange (0,5000,1)
createGraph("Oil density",sumbu_x,'range yLabel',)