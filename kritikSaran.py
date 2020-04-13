from load2 import Filename

'''
File[0] = 'user.csv'        # input('Masukkan nama File User: ')
File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
File[6] = 'kritiksaran.csv'    
'''
Filename = Filename

def kritik_saran():
    # Proses memasukkan kritik dan saran
    ID_Wahana = input("Masukkan ID Wahana: ")
    Tanggal_Kritik = input("Masukkan tanggal pelaporan: ")
    Username = un #un = username awal, di login
    Isi_Kritik = input("Kritik/saran Anda: ")

    temp = [ID_Wahana,Tanggal_Kritik,Username,Isi_Kritik]
    Filename[6].append(temp)
    print("")
    print("Kritik dan saran Anda kami terima.")
