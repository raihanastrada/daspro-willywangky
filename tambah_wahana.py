def tambah_wahana():
    with open('wahana.csv','r') as read:
        csv_reader = csv.DictReader(read)

        with open('wahana.csv','a',newline='') as write:
            csv_writer = csv.DictWriter(write)
            print("Masukkan Informasi Wahana yang ditambahkan: ")
            id = input("Masukkan ID Wahana: ")
            nama = input("Masukkan Nama Wahana")
            harga = input("Masukkan Harga Tiket")
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