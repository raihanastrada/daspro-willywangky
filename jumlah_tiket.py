from load2 import Filename

def jumlah_tiket():
    username = input("Masukkan username: ")
    print("Riwayat:")
    i = 0
    found = False
    while (Filename[4][i] != None):
        if (Filename[4][i][0] == username):
            ID = Filename[4][i][1]
            for j in range (1000):
                if (ID == Filename[1][j][0]):
                    wahana = Filename[1][j][1]
                    break
            jumlah = Filename[4][i][2]
            print("{} | {} | {}".format(ID,wahana,jumlah))
            found = True
        i += 1
    if (not found): #Data kosong
        print("Data tidak ditemukan!")

jumlah_tiket()
    