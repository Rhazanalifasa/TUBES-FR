from math import exp

def newton_raphson(f, x):
	tolerance = 1e-12
	'''
	xi+1 = xi - f(xi)/f'(xi)
	iterate until
	abs(f(xi)) < tolerance 
	'''
	f_prime = (f(x+1e-6)-f(x))/1e-6
	x1 = x - f(x)/f_prime

	if abs(f(x)) < tolerance:
		return x
	else:
		return newton_raphson(f,x1)

def Z(Ppr, Tpr, Y):
	t = 1/Tpr
	return ((0.06125*Ppr*t)/Y)*exp(-1.2*(1-t)**2)

def hall_yarborough(Ppr, Tpr):
	t = 1/Tpr
	X1 = -0.06125*Ppr*t*exp(-1.2*(1-t)**2)
	X2 = 14.76*t - 9.76*(t**2) + 4.58*(t**3)
	X3 = 90.7*t - 242.2*(t**2) + 42.4*(t**3)
	X4 = 2.18 + 2.82*t
	return lambda Y: X1 + ((Y + (Y**2) + (Y**3) + (Y**4))/((1-Y)**3)) - (X2*Y**2) + (X3*(Y**X4))

def Sutton_Correlation_Ppc(Yg): # untuk Ppc, akurat utk 0.57 < Yg < 1.68
	return 756.8 - 131.07*Yg - 3.6*Yg**2

def Sutton_Correlation_Tpc(Yg): # untuk Tpc, akurat utk 0.57 < Yg < 1.68
	return 169.2 + 349.5*Yg - 74*Yg**2
# ========================= #
# INPUT #
P_res = 5300
T_res = 100
Yg = 0.78

# Ppr = P_res/Sutton_Correlation_Ppc(Yg)
# Tpr = T_res/Sutton_Correlation_Tpc(Yg)

Ppr = 2.5
Tpr = 2.5

x0 = 0.001 # initial x buat root-finding newton-raphson

f = hall_yarborough(Ppr, Tpr) # sama aja f = lambda Y: ...
Y_estimate = newton_raphson(f, x0)

# print("Kasus:")
# # print(f"P reservoir: {P_res} psia")
# # print(f"T reservoir: {T_res} °R")
# # print(f"Gas Specific Gravity (Yg): {Yg} ")
# # print("* Sutton corr untuk Ppc dan Tpc")
# print(f"Ppr = {Ppr}")
# print(f"Tpr = {Tpr}")
# print("* Newton-Raphson untuk root-finding")
# print("* Hall-Yarborough method untuk Z-Factor")
# print("==========")
# print("Hasil:")
# print(f"Y_estimate: {Y_estimate}")
# print(f"Z: {Z(Ppr = Ppr, Tpr = Tpr, Y = Y_estimate)} ")
