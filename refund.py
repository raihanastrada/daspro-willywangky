from load2 import Filename
from login import un

def refund(username):
    id = input("Masukkan ID Wahana: ")
    tanggal = input("Masukkan tanggal refund: ") # now = masukkan tanggal saat ini
    tiket = int(input("Jumlah tiket yang ingin di-refund: "))
    
    found = False
    i1 = 0
    
    while (Filename[4][i1] != None): 
        if (Filename[4][i1][0] == username) and (Filename[4][i1][1] == id): # Mencari apakah pengguna memasukkan input yang valid di tiket.csv
            if (int(Filename[4][i1][2]) < tiket):
                break
            else :
                found = True
                Filename[4][i1][2] = int(Filename[4][i1][2]) - tiket # jml tiket di tiket.csv dikurangin

                i2 = 0
                while (Filename[1][i2] != None): # pencarian harga tiket suatu wahana untuk penghitungan refund
                    if (Filename[1][i2][0] == id) :
                        refunds = 0.75*(int(Filename[1][i2][2]))*tiket #menghitung uang yang dikembalikan
                        break
                    i2 += 1

                i3 = 0   
                while (Filename[0][i3] != None): # pencarian username di user csv untuk penambahan saldo
                    if (Filename[0][i3][3] == username):
                        Filename[0][i3][6] = int(Filename[0][i3][6]) + refunds # penambahan saldo di user.csv 
                        break
                    i3 += 1

                # pencatatan di refund.csv
                temp = [un,tanggal,id,tiket]
        
                for i in range(1000):
                    if (Filename[5][i] == None):
                        Filename[5][i] = temp #penulisan di array
                        break
            break
        i1 += 1

    if (found == True):
        print("Uang refund sudah kami berikan pada akun Anda.")
    else:
        print("Anda tidak memiliki tiket terkait.")

    return Filename

refund(un)
print(Filename[5])
print(Filename[0])