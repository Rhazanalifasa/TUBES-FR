import math;
def MiuWBeggs(T: float) -> float:
    
    return math.exp(1.003 - (1.479 * (10 ** -2) * T) + (1.982 * (10 ** -5) * T ** 2));