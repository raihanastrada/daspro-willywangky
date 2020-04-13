import csv

def save(ArrayToSave):
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
                File[i] = input('Masukkan nama File',Name[i])
                Error[i] = False
                try:
                    open(File[i])
                except:
                    Error[i] == True
    if (Error.count(True) == 0):
        for i in range(7):
            with open(File[i],'w') as savedfiles:
                Fieldnames = [['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password'],
                              ['ID_Wahana','Nama_Wahana','Harga_Tiket','Batasan_Umur','Batasan_Tinggi'],
                              ['Username','Tanggal_Pembelian','ID_Wahana','Jumlah_Tiket'],
                              ['Username','Tanggal_Penggunaan','ID_Wahana','Jumlah_Tiket'],
                              ['Username','ID_Wahana','Jumlah_Tiket'],
                              ['Username','Tanggal_Refund','ID_Wahana','Jumlah_Tiket'],
                              ['Username','Tanggal_Kritik','ID_Wahana','Isi_Kritik']]
                csv_writer = csv.DictWriter(savedfiles,fieldnames=Fieldnames[i],delimiter=',')
                csv_writer.writeheader()
                for j in ArrayToSave[i]:
                    csv_writer.writerow(j)
        print('Success!')
