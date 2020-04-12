import csv

def tambah_wahana():
    with open('wahana.csv','r') as read:
        csv_reader = csv.DictReader(read) 

        with open('wahana.csv','a',newline='') as write:
            fieldnames = ['ID_Wahana','Nama_Wahana','Harga_Tiket','Batasan_Umur','Batasan_Tinggi']
            csv_writer = csv.DictWriter(write,fieldnames=fieldnames)
            print("Masukkan Informasi Wahana yang ditambahkan: ")
            id = input("Masukkan ID Wahana: ")
            nama = input("Masukkan Nama Wahana: ")
            harga = input("Masukkan Harga Tiket: ")
            umur = input("Batasan Umur: ")
            tinggi = input("Batasan Tinggi Badan: ")

            #Diasumsikan semua masukan valid
            csv_writer.writerow({
                'ID_Wahana' : id,
                'Nama_Wahana' : nama,
                'Harga_Tiket' : harga,
                'Batasan_Umur' : umur,
                'Batasan_Tinggi' : tinggi
            }) 

            print("Info wahana telah ditambahkan!")

def replace():
    with open('wahana.csv','r') as read:
        csv_reader = csv.DictReader(read)
        print("Ketik ID Wahana yang ingin anda ganti: ")
        ID = input()
        valid = False
        while (not valid):
            for row in csv_reader:
                if (row['ID_Wahana']==ID):
                    valid = True
                    print("Berikut info wahana yang ingin anda ubah: ")
                    print(row['ID_Wahana'])
                    print(row['Nama_Wahana'])
                    print(row['Harga_Tiket'])
                    print(row['Batasan_Umur'])
                    print(row['Batasan_Tinggi']+'\n')
                    break
            if (not valid):
                print("Data tidak ada, silakan ulangi lagi")
                ID = input()
        with open('wahana.csv','w',newline='') as write:
            fieldnames = ['ID_Wahana','Nama_Wahana','Harga_Tiket','Batasan_Umur','Batasan_Tinggi']
            csv_writer = csv.DictWriter(write,fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in csv_reader:
                if (row['ID_Wahana']!=ID):
                    csv_writer.writerow(row)
        
        with open('wahana.csv','a',newline='') as append:
            replace = csv.DictWriter(append,fieldnames=fieldnames)
            print("Silakan isi data baru tentang wahana ini: ")
            id = input("Masukkan ID Wahana: ")
            nama = input("Masukkan Nama Wahana: ")
            harga = input("Masukkan Harga Tiket: ")
            umur = input("Batasan Umur: ")
            tinggi = input("Batasan Tinggi Badan: ")
            replace.writerow({
                'ID_Wahana' : id,
                'Nama_Wahana' : nama,
                'Harga_Tiket' : harga,
                'Batasan_Umur' : umur,
                'Batasan_Tinggi' : tinggi
            })


replace()
