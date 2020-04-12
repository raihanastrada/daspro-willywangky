import csv
import Obfuscator
from load2 import Filename

Filename = Filename

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
    for i in range(len(b)):
        if b[i]['Username'] == a:
            Exist = True
            break
    return Exist


with open('user2.csv', 'r') as csvread:
    csv_reader = csv.DictReader(csvread)
    with open('user2.csv', 'a', newline='') as csvwrite:
        fieldnames = ['Nama', 'Tanggal_Lahir', 'Tinggi_Badan', 'Username', 'Password']
        Nama = input("Masukkan nama pemain: ")
        Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
        Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
        Username = input("Masukkan username pemain: ")
        while (alphacheck(Username,'username') == False) or (ucheck(Username,Filename[0]) == True):
            if (alphacheck(Username,'username') == False):
                print('Error, please input alphanumeric for username!')
                Username = input("Masukkan username pemain: ")
            if (ucheck(Username,Filename[0]) == True):
                print("Username sudah terdaftar")
                Username = input("Masukkan username pemain: ")

        Password = input("Masukkan password pemain: ")
        while (alphacheck(Password,'password') == False):
            print('Error, please input alphanumeric for password!')
            Password = input("Masukkan password pemain: ")

        Filename[0].append({
            'Nama': Nama,
            'Tanggal_Lahir': Tanggal_Lahir,
            'Tinggi_Badan': Tinggi_Badan,
            'Username': Username,
            'Password': Obfuscator.obs(Password)
        })

# CEK Fungsi
print(Filename[0])