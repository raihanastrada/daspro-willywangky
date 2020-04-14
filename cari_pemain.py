import csv
from load2 import Filename

def cari_pemain():
    found_session = False
    while (not found_session):
        found = False
        un_search = input("Masukkan username: ")
        for i in range(len(Filename[0])):
            if (Filename[0][i][3]==un_search):
                print("Nama Pemain: ",Filename[0][i][0])
                print("Tinggi Pemain: ",Filename[0][i][2])
                print("Tanggal Lahir Pemain: ",Filename[0][i][1])
                found = True
                break
        if (not found):
            print("Pemain tidak ditemukan")
        print()
        valid = False
        while (not valid):
            pilih = input("Apakah Anda ingin melanjutkan mencari? (Y/N): ")
            if (pilih == "Y"):
                valid = True
            elif (pilih == "N"):
                valid = True
                found_session = True
            else:
                print("Masukaan salah, silakan ulangi!")

cari_pemain()