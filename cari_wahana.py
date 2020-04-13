from load2 import Filename

def cari_wahana():
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
    
    count = 0
    print("Hasil Pencarian:")
    for i in range(len(Filename[1])):
        if (Filename[1][i][3]==jenis_umur and Filename[1][i][4]==jenis_tinggi):
            print("{} | {} | {}".format(Filename[1][i][0],Filename[1][i][1],Filename[1][i][2]))
            count += 1
    if (count==0):
        print("Maaf, wahana tidak ditemukan")
        
cari_wahana()
