import matplotlib.pyplot as plt;

def addGraphFunc(func):
    def wrapper(title, xLabel, yLabel, xValue, yValue):
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