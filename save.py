#Imports
import csv
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

def save():
    File = ['' for i in range(7)]
    File[0] = input('Masukkan nama File User: ')
    File[1] = input('Masukkan nama File Daftar Wahana: ')
    File[2] = input('Masukkan nama File Pembelian Tiket: ')
    File[3] = input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = input('Masukkan nama File Refund Tiket: ')
    File[6] = input('Masukkan nama File Kritik dan Saran: ')
    Name = ['User: ','Daftar Wahana: ','Pembelian Tiket: ','Penggunaan Tiket: ','Kepemilikan Tiket: ','Refund Tiket: ','Kritik dan Saran: ']
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            open(File[i])
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
            while Error[i] == True:
                File[i] = input('Masukkan nama File ' + Name[i])
                Error[i] = False
                try:
                    open(File[i])
                except:
                    Error[i] == True
    if (Error.count(True) == 0):
        for i in range(7):
            with open(File[i],'w',newline='') as savedfiles:
                csv_writer = csv.writer(savedfiles,delimiter=',')
                for j in range(201):
                    try:
                        if Filename[i][j] != None:
                            csv_writer.writerow(Filename[i][j])
                    except:
                        break
        print('Success!')
