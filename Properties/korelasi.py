Function Rs_Glaso(API As Double, T As Double, P As Double, Pb As Double) As Double
Dim SG As Double
SG = 141.5 / (API + 131.5)
Dim Pressure As Double
If P > Pb Then
Pressure = Pb
Else
Pressure = P
End If
Dim Pbubble As Double
Pbubble = 10 ^ (2.8869 - (14.1811 - (3.3093 * Logx(Pressure))) ^ 0.5)
Rs_Glaso = SG * ((((API ^ 0.989) / ((T) ^ 0.172)) * Pbubble) ^ 1.2255)

Function Rs_Standing(API As Double, T As Double, P As Double, Pb As Double) As Double
Dim SG As Double
SG = 141.5 / (API + 131.5)
Dim Pressure As Double
If P > Pb Then
Pressure = Pb
Else
Pressure = P
End If
Rs_Standing = SG * (((Pressure / 18.2) + 1.4) * 10 ^ ((0.0125 * API) - 0.00091 * (T))) ^ 1.2048
End Function

Function Rs_VB(API As Double, T As Double, P As Double, Tsep As Double, Psep As Double, Pb As Double) As Double
Dim SG As Double
SG = 141.5 / (API + 131.5)
Dim C1, C2, C3, SG1, Pressure As Double
If P > Pb Then
Pressure = Pb
Else
Pressure = P
End If
If API <= 30 Then
C1 = 0.0362
C2 = 1.0937
C3 = 25.724
Else
C1 = 0.0178
C2 = 1.187
C3 = 23.931
End If
SG1 = SG * (1 + (5.912 * 0.00001 * API * Tsep * (Logx(Psep / 114.7) / Log(10))))
Rs_VB = C1 * SG1 * (Pressure ^ C2) * Exp(C3 * (API / (T + 460)))
End Function