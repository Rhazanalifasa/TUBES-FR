def CW(P: float, T: float) -> float:
    C1 = 3.8546 - (0.000134 * P)
    C2 = -0.01052 + (4.77 * (10 ** -7) * P)
    C3 = (3.9267 * (10 ** -5)) - (8.8 * (10 ** -10) * P)
    
    return (C1 + (C2 * T) + (C3 * T ** 2)) * (10 ** -6);

def RSW(P: float, T: float, TDS: float) -> float:
    
    A = 2.12 + (3.45 * (10 ** -3) * T) - (3.59 * (10 ** -5) * T ** 2)
    B = 0.0107 - (5.26 * (10 ** -5) * T) + (1.48 * (10 ** -7) * T ** 2)
    C = (-8.75 * (10 ** -7)) + (3.9 * (10 ** -9) * T) - (1.02 * (10 ** -11) * T ** 2)
    Rswpure = A + (B * P) + (C * (P ** 2))
    SC = 1 - ((0.0753 - (0.000173 * T)) * TDS)
    
    return Rswpure * SC / 1000

def RhoW(TDS: float, BW: float) -> float:
    
    return (((TDS / 100) * 62.4) + 62.4) / BW;