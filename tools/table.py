from tabulate import tabulate;
import numpy as np;

headers = ["Name", "Age", "Sex"];
rows = np.array([["John", "Afdinal"], [12, 20], ["Male", "Male"]]);

print(tabulate(rows, headers, tablefmt='fancy_grid', showindex='always'));