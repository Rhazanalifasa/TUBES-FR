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

