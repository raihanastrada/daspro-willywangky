import time
import csv
from load2 import Filename

def riwayat_wahana():
    """
    date = time.localtime()
    day = date.tm_mday
    if (day < 10):
        day = "0"+str(day)
    month = date.tm_mon
    if (month < 10):
        month = "0"+str(month)
    year = date.tm_year
    """
    ID = input("Masukkan ID Wahana: ")
    count = 0
    for i in range(len(Filename[3])):
        if (Filename[3][i][2]==ID):
            tanggal = Filename[3][i][1]
            user = Filename[3][i][0]
            tiket = Filename[3][i][3]
            print("{} | {} | {}".format(tanggal,user,tiket))
            count += 1
    if (count == 0):
        print("Riwayat tidak ditemukan")
        
riwayat_wahana()