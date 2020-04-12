def cari_wahana():
    with open('wahana.csv','r') as read:
        csv_reader = csv.DictReader(read)
        print("Jenis batasan umur:")
        print("1. Anak-anak (<17 tahun)")
        print("2. Dewasa (>=17 tahun)")
        print("3. Semua umur")
        print()
        print("Jenis batasan tinggi badan:")
        print("1. Lebih dari 170 cm")
        print("2. Tanpa batasan")
        print()
        jenis_umur = int(input("Batasan umur pemain: "))
        jenis_tinggi = int(input("Batasan tinggi badan: "))
        if (jenis_umur == 1):
            jenis_umur = "Anak"
        elif (jenis_umur == 2):
            jenis_umur = "Dewasa"
        elif (jenis_umur == 3):
            jenis_umur = "Semua"
        if (jenis_tinggi == 1):
            jenis_tinggi = "Atas 170"
        elif (jenis_tinggi == 2):
            jenis_tinggi = "Tidak ada"
        i = 0
        print("Hasil Pencarian:")
        for row in csv_reader:
            if (row['Batasan_Umur']==jenis_umur and row['Batasan_Tinggi']==jenis_tinggi):
                print("{} | {} | {}".format(row['ID_Wahana'],row['Nama_Wahana'],row['Harga_Tiket']))
                i += 1
        if (i==0):
            print("Maaf, wahana tidak ditemukan")

"""
cari_wahana()
"""