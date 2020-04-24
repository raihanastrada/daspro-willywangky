from load2 import Filename
from login import un

'''
File[0] = 'user.csv'        # input('Masukkan nama File User: ')
File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
File[6] = 'kritiksaran.csv' # input('Masukkan nama File Kritik Saran: ')
File[7] = 'kehilangan.csv'  # input('Masukkan nama File Kehilangan: ')  
'''
def kehilangan():
    arrHilang = Filename[7]
    arrTiket = Filename[4]
    input_un = input("Masukkan username: ")
    tanggal_hilang = input("Masukkan tanggal kehilangan: ")
    wahana = input("ID wahana: ")
    jml_tiket_hilang = int(input("Jumlah tiket yang dihilangkan: "))
    i = 0
    empty = False
    while not(empty) and i < 1000:
        if arrHilang[i] == None:  # mencari line kosong untuk di write
            arrHilang[i] = [input_un, wahana, tanggal_hilang, jml_tiket_hilang]
            print("Laporan kehilangan tiket Anda telah direkam.") # proses searching data di file tiket.csv
            empty = True
        else:
            i = i + 1
            
    tiket_found = False
    j = 0
    while not(tiket_found) and j < 1000:     
        if arrTiket[j][0] == input_un and arrTiket[j][1] == wahana:
            # mengganti kolom kepemilikan tiket, dengan anggapan user pasti memiliki tiket dan jumlahnya valid
            arrTiket[j][2] = int(arrTiket[i][2]) - jml_tiket_hilang
            found_tiket = True
        else:
            j = j + 1
    Filename[7] = arrHilang
    Filename[4] = arrTiket

    return Filename
    



