def Miu_DO(API, T):
    Z = 3.0324 - (0.02023 * API)
    Y = 10 ** Z
    X = Y * (T ** (-1.163))
    Miu_DO = (10 ** X) - 1
    return Miu_DO

def Miu(Rs, API , T):
    A = 10.715 * (Rs + 100) ** -0.515
    B = 5.44 * (Rs + 150) ** -0.338
    Miu = A * (Miu_DO(API, T)) ** B
    return Miu

def Miu_VB(P , Pb , Rs , API , T ):
    A = -3.9 * (10** -5) * P - 5
    m = 2.6 * (P** 1.187) * 10 ** A
    Miu_VB = Miu(Rs, API, T) * ((P / Pb) ** m)
    return Miu_VB

print(Miu_VB(1,2,3,4,5))