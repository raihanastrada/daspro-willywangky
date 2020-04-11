import csv
import Obfuscator

def alphacheck(a,b):
    cek = True
    for i in a:
        chr = ord(i)
        if not ((48 <= chr <= 57) or (65 <= chr <= 90) or (97 <= chr <= 122)):
            cek = False
            break
    return cek

def ucheck(a,file):
    with open(file, 'r') as csvread:
        fl = csv.DictReader(csvread)
        exist = False
        for row in fl:
            val_un = row['Username']
            if (val_un == a):
                exist = True
                break
    return exist


with open('user.csv', 'r') as csvread:
    csv_reader = csv.DictReader(csvread)
    with open('user.csv', 'a', newline='') as csvwrite:
        fieldnames = ['Nama', 'Tanggal_Lahir', 'Tinggi_Badan', 'Username', 'Password']
        filesignup = csv.DictWriter(csvwrite, fieldnames=fieldnames)
        Nama = input("Masukkan nama pemain: ")
        Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
        Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
        Username = input("Masukkan username pemain: ")
        while (alphacheck(Username,'username') == False) or (ucheck(Username,'user.csv') == True):
            if (alphacheck(Username,'username') == False):
                print('Error, please input alphanumeric for username!')
                Username = input("Masukkan username pemain: ")
            if (ucheck(Username,'user.csv') == True):
                print("Username sudah terdaftar")
                Username = input("Masukkan username pemain: ")

        Password = input("Masukkan password pemain: ")
        while (alphacheck(Password,'password') == False):
            print('Error, please input alphanumeric for password!')
            Password = input("Masukkan password pemain: ")

        filesignup.writerow({
            'Nama': Nama,
            'Tanggal_Lahir': Tanggal_Lahir,
            'Tinggi_Badan': Tinggi_Badan,
            'Username': Username,
            'Password': Obfuscator.obs(Password)
        })