#Imports
import csv
import Obfuscator # Download file obfuscator.py dulu.
from load2 import Filename
from save import save

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

def exit():
    print('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?',end=' ')
    choice = input()
    while not (choice == 'Y' or choice == 'y' or choice == 'N' or choice == 'n'):
        print('Input error!')
        print('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?', end=' ')
        choice = input()
    if choice == 'Y' or choice == 'y':
        save()
    sys.exit()

exit()