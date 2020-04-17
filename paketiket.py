from load import Filename
from login import user_id, admin
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
user_id = user_id
admin = admin

def pakai():
    arrPenggunaan = Filename[3]
    arrPembelian = Filename[2]
    arrUser = Filename[0]
    wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jml_tiket = input("Masukkan tiket yang digunakan: ")
    valid = False
    i = 0
    while not(valid) and i < len(arrPembelian):
        if arrPenggunaan[i]['Username'] == arrUser[user_id]['Username'] and arrPembelian[i]["ID_Wahana"] == wahana and arrPembelian[i]['Jumlah_Tiket'] <= jml_tiket:
            valid = True
    if valid:
        print("Terima kasih telah bermain.")
        arrPenggunaan.append({
            'Username': arrUser[user_id]['Username'],
            'Tanggal_Penggunaan': tanggal,
            'ID_Wahana': wahana,
            'Jumlah_Tiket': jml_tiket,
        })
    
    else:
        print("Tiket Anda tidak valid dalam sistem kami")

main()