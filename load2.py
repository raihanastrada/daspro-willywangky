import csv

def load():
    sizeus = 200  # ukuran maksimal array user
    sizeelse = 1000  # ukuran maksimal array lain
    Auser = [None for j in range(sizeus)]  # template array user dengan ukuran sizeus
    Aelse1 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse2 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse3 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse4 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse5 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse6 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Filename = [Auser, Aelse1, Aelse2, Aelse3, Aelse4, Aelse5, Aelse6]
    File = ['' for i in range(7)]
    File[0] = 'user.csv'  # input('Masukkan nama File User: ')
    File[1] = 'wahana.csv'  # input('Masukkan nama File Daftar Wahana: ')
    File[2] = 'pembelian.csv'  # input('Masukkan nama File Pembelian Tiket: ')
    File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = 'tiket.csv'  # input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = 'refund.csv'  # input('Masukkan nama File Refund Tiket: ')
    File[6] = 'kritiksaran.csv'  # input('Masukkan nama File Kritik dan Saran: ')
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
print(Filename)