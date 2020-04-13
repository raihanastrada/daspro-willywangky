import Obfuscator
from load2 import Filename

# NOTE

# File[0] = 'user.csv'
# File[1] = 'wahana.csv'
# File[2] = 'pembelian.csv'
# File[3] = 'penggunaan.csv'
# File[4] = 'tiket.csv'
# File[5] = 'refund.csv'
# File[6] = 'kritiksaran.csv'

# Initiation
Filename = Filename

def signup():
    # Local Function
    def alphacheck(a):
        cek = True
        for i in a:
            chr = ord(i)
            if not ((48 <= chr <= 57) or (65 <= chr <= 90) or (97 <= chr <= 122)):
                cek = False
                break
        return cek

    def ucheck(a,b):
        Exist = False
        for i in range(201):
            try:
                if b[i][3] == a:
                    Exist = True
                    break
            except:
                Exist = False
        return Exist

    # Function Algorithm
    N = 200
    fieldnames = ['Nama', 'Tanggal_Lahir', 'Tinggi_Badan', 'Username', 'Password']
    Nama = input("Masukkan nama pemain: ")
    Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
    Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
    Username = input("Masukkan username pemain: ")
    while (alphacheck(Username) == False) or (ucheck(Username,Filename[0]) == True):
        if (alphacheck(Username) == False):
            print('Error, please input alphanumeric for username!')
            Username = input("Masukkan username pemain: ")
        if (ucheck(Username,Filename[0]) == True):
            print("Username sudah terdaftar")
            Username = input("Masukkan username pemain: ")

    Password = input("Masukkan password pemain: ")
    while (alphacheck(Password) == False):
        print('Error, please input alphanumeric for password!')
        Password = input("Masukkan password pemain: ")

    for i in range (N):
        if Filename[0][i] == None:
            Filename[0][i] = [Nama, Tanggal_Lahir,Tinggi_Badan,Username,Obfuscator.obs(Password),'user',0]
            break
    return Filename

# CEK Fungsi
signup()