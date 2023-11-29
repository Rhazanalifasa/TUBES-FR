import sys
sys.path.append('C:\\Users\\daffa\\OneDrive\\Documents\\TUBADAG FR\\Tubes\\')

from Calculation.Bo_Standing import Bo_Standing;

def calculate_Bo_Standing():
    ST = float(input("Enter Separator Temperature:  ")) #Separator Temperature(Tsep)
    BPP = float(input("Enter Bubble Point Pressure:  ")) #Bubble Point Pressure
    SP = float(input("Enter Separator Pressure:  ")) #Separator Pressure(Psep)
    OA = float(input("Enter Oil API Gravity:  ")) #Oil API Gravity
    Bo_Standing_Value = Bo_Standing(0.77, OA, ST)
    
    print(Bo_Standing_Value)

# print(Rs_VB)

while True:
    menu = input('masukkan data: \n1.Reservoir Data\n2.Oil Data\n3.Impurities\n4.Brine Data\nSelesai\npilih Nomor:')
    corelation = input("Enter Corelation: ")
    try:
        if menu == '1':
            print("Reservoir Data")
        elif menu == '2':
            print("\nOil Data")
            calculate_Bo_Standing()
        elif menu == '3':
            print("\nImpurities")
            CO2 = float(input("Enter CO2 Percentage:  %")) #CO2
            H2S = float(input("Enter H2S Percentage:  %")) #H2S
            N2 = float(input("Enter N2 Percentage:  %")) #N2
        elif menu == '4':
            print("\nBrine Data")
            TDS = float(input("Enter TDS Percentage:  ")) #Total Dissolved Solid
        elif menu == 'selesai':
            print()
            break
    except:
        print('Tolong pilih sesuai nomor yang diberikan')
