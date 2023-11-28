import matplotlib.pyplot as plt;
# import pandas as pd;

def initiate(xLabel:str, yLabel:str, title:str):
    fig, ax = plt.subplots();
    ax.set_title(title);
    ax.set_xlabel(xLabel);
    ax.set_ylabel(yLabel);

def showGraphic():
    plt.legend();
    plt.grid(True);
    plt.show();
    
def cubic_graphic(x:list, y:list, title:str, xLabel:str, yLabel:str):
    initiate(xLabel, yLabel, title);
    plt.plot(x, y);
    showGraphic();