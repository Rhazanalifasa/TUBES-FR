def BWSat(P: float, T: float) -> float:

    A1 = 0.9911 + ((6.35 * 10 ** -5) * T) + ((8.5 * 10 ** -7) * T ** 2)
    A2 = (-1.093 * 10 ** -6) + ((-3.497 * 10 ** -9) * T) + ((4.57 * 10 ** -12) * T ** 2)
    A3 = (-5 * 10 ** -11) + ((6.429 * 10 ** -13) * T) + ((-1.43 * 10 ** -15) * T ** 2)
    
    return A1 + (A2 * P) + (A3 * P ** 2);