from load2 import Filename
from login import un

'''
File[0] = 'user.csv'        # input('Masukkan nama File User: ')
File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
File[6] = 'kritiksaran.csv'    
'''


def kritik_saran(un):
    # Proses memasukkan kritik dan saran
    ID_Wahana = input("Masukkan ID Wahana: ")
    Tanggal_Kritik = input("Masukkan tanggal pelaporan: ")
    Username = un #un = username awal, di login
    Isi_Kritik = input("Kritik/saran Anda: ")

    for i in range (1000):
        if (Filename[6][i] == None):
            Filename[6][i] = [Username,Tanggal_Kritik,ID_Wahana,Isi_Kritik]
            break
    print("")
    print("Kritik dan saran Anda kami terima.")
    return Filename

    
kritik_saran(un)
print(Filename[6])