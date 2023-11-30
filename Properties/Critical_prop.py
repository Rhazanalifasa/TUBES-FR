#Ppc
def Ppc_(gas_SG, corr):
	if corr == "Sutton":
		return 756.8 - 131.07*gas_SG - 3.6*(gas_SG**2)

	elif corr == "Misc Standing":
		return 677 + 15*gas_SG - 37.5*(gas_SG**2)

	elif corr == "Condensate Standing":
		return 706 - 51.7*gas_SG - 11.1*(gas_SG**2)

# Tpc
def Tpc_(gas_SG, corr):
	if corr == "Sutton":
		return 169.2 + 349.5*gas_SG - 74*(gas_SG**2)

	elif corr == "Misc Standing":
		return 168 + 325*gas_SG - 12.5*(gas_SG**2)

	elif corr == "Condensate Standing":
		return 187 + 330*gas_SG - 71.5*(gas_SG**2) 

def Tpcz(Tpc , CO2 , H2S , N2 ):
    Tpcz = Tpc - (80 * CO2) + (130 * H2S) - (250 * N2)
    return Tpcz 

def Ppcz(Ppc , CO2 , H2S , N2 ):
    Ppcz = Ppc + (440 * CO2) + (600 * H2S) - (170 * N2)
    return Ppcz 

def Tpr(T , Tc ): 
    Tpr = (T + 460) / Tc
    return Tpr

def Ppr(P , Pc ):
    Ppr = P / Pc
    return Ppr

