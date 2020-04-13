import csv

def load():
    fileuser = []
    filewahana = []
    filepembelian = []
    filepenggunaan = []
    filekepemilikan = []
    filerefund = []
    filekritiksaran = []
    Filename = [fileuser,filewahana,filepembelian,filepembelian,filepenggunaan,filekepemilikan,filerefund,filekritiksaran]
    File = ['' for i in range(7)]
    File[0] = 'user.csv'        # input('Masukkan nama File User: ')
    File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
    File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
    File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
    File[6] = 'kritiksaran.csv' # input('Masukkan nama File Kritik dan Saran: ')
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            with open(File[i], 'r') as csv_file:
                read = csv.reader(csv_file, delimiter=',')
                for row in read:
                    Filename[i].append(row)
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
    if (Error.count(True) == 0):
        print() #print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return Filename

Filename = load()