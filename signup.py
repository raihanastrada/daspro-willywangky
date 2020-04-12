import obfuscator
from load import Filename

'''
File[0] = 'user.csv'        # input('Masukkan nama File User: ')
File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
File[6] = 'kritiksaran.csv'    
'''
Filename = Filename


def alphacheck(user_input):
    cek = True
    for i in user_input:
        chr = ord(i)
        if not ((48 <= chr <= 57) or (65 <= chr <= 90) or (97 <= chr <= 122)):
            cek = False
            break
    return cek


def ucheck(user_input, array, col):
    existing = False
    for i in range(len(array)):
        if array[i][col] == user_input:
            existing = True
            break
    return existing


def signup():
    Nama = input("Masukkan nama pemain: ")
    Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
    Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
    Username = input("Masukkan username pemain: ")
    while alphacheck(Username) == False or ucheck(Username, Filename[0], 'Username') == True:
        if alphacheck(Username) == False:
            print('Error, please input alphanumeric for username!')
            Username = input("Masukkan username pemain: ")
        if ucheck(Username, Filename[0], 'Username') == True:
            print("Username sudah terdaftar")
            Username = input("Masukkan username pemain: ")
    Password = input("Masukkan password pemain: ")
    while alphacheck(Password) == False:
        print('Error, please input alphanumeric for password!')
        Password = input("Masukkan password pemain: ")
    Role = 'Pemain'
    x = input("Apakah admin? Jawab hanya dengan y/n. ")
    if x == 'y':
        Role = 'Admin'
    else:
        Role = 'Pemain'
    Saldo = None
    Filename[0].append({
        'Nama': Nama,
        'Tanggal_Lahir': Tanggal_Lahir,
        'Tinggi_Badan': Tinggi_Badan,
        'Username': Username,
        'Password': obfuscator.obs(Password)
    })
    print(Filename[0])


signup()
