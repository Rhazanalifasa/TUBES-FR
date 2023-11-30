def Bo_Standing(SGg , API , T): # Saturated
    SG = 141.5 / (131.5 + API)
    Bo_Standing = 0.9759 + (0.00012 * ((((SGg / SG) ** 0.5)) + (1.25 * (T-460))) ** 1.2)
    
    return Bo_Standing
