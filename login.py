import csv
import Obfuscator

import csv
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

    
def login():
    admin = False
    un = input("Masukkan username: ")
    pw = input("Masukkan password: ")
    login = False
    admin == False
    for i in range (len(Filename[0])):
        if Filename[0][i]['Username'] == un and Filename[0][i]["Password"] == pw:
            user = Filename[0][i]['Nama']
            login = True
            default_User = i
            break
    if Filename[0][i]['Role'] == "Admin":
        admin = True
    if (login == True):
        print("Selamat bermain, {}!".format(user))
        return default_User
    else:
        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")

user_id = login()

def isAdmin(id):
    adm = False
    if Filename[0][id]['Role'] == 'Admin':
        adm == True
    return adm

admin = isAdmin(user_id)
