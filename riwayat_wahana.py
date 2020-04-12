import time
import csv

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

    with open('riwayat.csv','r') as read:
        csv_reader = csv.DictReader(read,delimiter=',')
        id = input("Masukkan ID Wahana: ")
        for row in csv_reader:
            if (row['ID_Wahana']==id):
                print("{} | {} | {}".format(row['Tanggal'],row['Username'],row['Jumlah_Tiket']))

riwayat_wahana()