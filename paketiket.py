from load import Filename
from login import username, user_birth, user_height, user_saldo
'''
File[0] = 'user.csv'        # input('Masukkan nama File User: ')
File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
File[6] = 'kritiksaran.csv'    
'''

def main():
    arrTiket = Filename[4]
    arrPenggunaan = Filename[3]
    arrPembelian = Filename[2]
    arrUser = Filename[0]
    wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jml_tiket = int(input("Masukkan tiket yang digunakan: "))
    valid = False
    i = 0
    while not(valid) and i < 1000 : # searching kepemilikan tiket dari user
        if arrTiket[i][0] == username and arrTiket[i][1] == wahana: 
            if int(arrTiket[i][2]) >= jml_tiket:
                valid = True
                arrTiket[i][2] = int(arrTiket[i][2]) - jml_tiket # mengurangi jumlah tiket pada array kepemilikan
                break
            else:
                print("Maaf tiket anda kurang! Silakan membeli tiket lagi.")
                break
        else:
            i += 1 # next element
    if valid: # jika user memiliki tiket yang cukup
        print("Terima kasih telah bermain.")
        for i in range(1000):
            if arrPenggunaan[i] == None:
                arrPenggunaan[i] = [username, tanggal, wahana, jml_tiket] # menambahkan data ke file penggunaan tiket
                break
    else:
        print("Tiket Anda tidak valid dalam sistem kami")

main()
