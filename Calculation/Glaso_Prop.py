import math;

def Rs_Glaso(API, T, P, Pb) -> float:
    
    SG = 141.5/(API + 131.5);
    
    Pressure = P;
    if P > Pb:
        Pressure = Pb;
    
    P_Bubble = 10 ** (2.8869 - (14.1811 - (3.3093 * math.log(Pressure, 10)))**0.5);
    Glaso_Value = SG * (((API**0.989)/(T**0.172)) * P_Bubble**1.2255);
    
    return Glaso_Value;

