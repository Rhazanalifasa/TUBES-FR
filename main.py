from Graphics.visual import *;

number = [i for i in range(100)];
cubicNum = list(map(lambda x: x**3, number));

cubic_graphic(number, cubicNum, "Grafik Bilangan Kubik", "Bilangan", "Bilangan Kubik");
    