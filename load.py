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
    File[0] = input('Masukkan nama File User: ')
    File[1] = input('Masukkan nama File Daftar Wahana: ')
    File[2] = input('Masukkan nama File Pembelian Tiket: ')
    File[3] = input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = input('Masukkan nama File Refund Tiket: ')
    File[6] = input('Masukkan nama File Kritik dan Saran: ')
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            with open(File[i], 'r') as csv_file:
                read = csv.DictReader(csv_file, delimiter=',')
                for row in read:
                    Filename[i].append(row)
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
    if (Error.count(True) == 0):
        print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return fileuser, filewahana, filepembelian, filepenggunaan, filekepemilikan, filerefund, kritiksaran