import csv

def load():
    Filename = [[[' ' for k in range (7)] for j in range (100)] for i in range (7)]
    File = ['' for i in range(7)]
    File[0] = 'user.csv'        # input('Masukkan nama File User: ')
    File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
    File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
    File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
    File[6] = 'kritiksaran.csv'
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            with open(File[i], 'r') as csv_file:
                read = csv.reader(csv_file, delimiter=',')
                j = 0
                for row in read:
                    Filename[i][j]=row
                    j += 1
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
    if (Error.count(True) == 0):
        print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return Filename

Filename = load()
print(Filename[6])