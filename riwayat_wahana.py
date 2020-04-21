import time
import csv
from load2 import Filename

def riwayat_wahana():
    ID = input("Masukkan ID Wahana: ")
    count = 0
    for i in range(1000):
        if (Filename[3][i]!=None):
            if (Filename[3][i][2]==ID):
                tanggal = Filename[3][i][1]
                user = Filename[3][i][0]
                tiket = Filename[3][i][3]
                print("{} | {} | {}".format(tanggal,user,tiket))
                count += 1
        else:
            break
    if (count == 0):
        print("Riwayat tidak ditemukan")
        
riwayat_wahana()