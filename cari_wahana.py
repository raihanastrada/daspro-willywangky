from load2 import Filename

def cari_wahana():
    found_session = False
    while (not found_session):
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
            jenis_umur = "Semua Umur"
        if (jenis_tinggi == 1):
            jenis_tinggi = "170"
        elif (jenis_tinggi == 2):
            jenis_tinggi = "0"
        
        count = 0
        print("Hasil Pencarian:")
        i = 0
        while True:
            if (Filename[1][i] != None):
                if (Filename[1][i][3]==jenis_umur and Filename[1][i][4]==jenis_tinggi):
                    print("{} | {} | {}".format(Filename[1][i][0],Filename[1][i][1],Filename[1][i][2]))
                    count += 1
                i+=1
            else:
                break

        if (count==0):
            print("Maaf, wahana tidak ditemukan")

        valid = False
        while (not valid):
            pilih = input("Apakah Anda ingin melanjutkan mencari? (Y/N): ")
            if (pilih == "Y"):
                valid = True
            elif (pilih == "N"):
                valid = True
                found_session = True
            else:
                print("Masukan salah, silakan ulangi!")
        
cari_wahana()
