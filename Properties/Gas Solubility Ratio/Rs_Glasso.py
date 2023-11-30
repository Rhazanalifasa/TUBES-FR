import math
def log(x):
    return (math.log(x,10) / math.log(10,10))

def Rs_Glaso(API , T , P , Pb ): # Gas-Oil Ratio
    SG = 141.5 / (API + 131.5) 
    if P > Pb:
        Pressure = Pb
    else:
        Pressure = P
    Pbubble = 10 ** (2.8869 - (14.1811 - (3.3093 * log(Pressure))) ** 0.5)
    Rs_Glaso = SG * ((((API ** 0.989) / ((T) ** 0.172)) * Pbubble) ** 1.2255)
    
    return Rs_Glaso