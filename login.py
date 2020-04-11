import csv
import Obfuscator

with open('user.csv','r') as read:
    csv_reader = csv.DictReader(read)
    un = input("Masukkan username: ")
    pw = Obfuscator.obs(input("Masukkan password: "))

    login = False
    for row in csv_reader:
        if (row['Username']==un and row['Password']==pw):
            user = row['Nama']
            login = True
            break
    if (login == True):
        print("Selamat bermain, {}!".format(user))
    else:
        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")