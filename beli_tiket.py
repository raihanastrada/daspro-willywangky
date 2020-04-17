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

## ALGORITMA BELI TIKET
def umur(now, birth):  # DD/MM/YYYY
    hari_lahir = int(birth[0:2])
    bulan_lahir = int(birth[3:5])
    tahun_lahir = int(birth[6:10])
    hari_now = int(now[0:2])
    bulan_now = int(now[3:5])
    tahun_now = int(now[6:10])
    days = 0
    while tahun_now > tahun_lahir and days == 0:
        days += abs(tahun_now - tahun_lahir)*365 - abs(bulan_now - bulan_lahir)*30 - abs(hari_now - hari_lahir)
    return days / 365
    

def beli_tiket():
    wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jml_tiket = int(input("Masukkan tiket yang dibeli: "))
    arrUser = Filename[0]
    arrWahana = Filename[1]
    arrBeli = Filename[2]
    i = 0
    found = False
    while not(found) and i < len(arrWahana):
        if arrWahana[i]["ID_Wahana"] == wahana:
            wahana_id = i
            found = True
            break
        else:
            i = i + 1 
    if found :
        if umur(str(tanggal), str(arrUser[user_id]['Tanggal_Lahir'])) > int(arrWahana[wahana_id]['Batasan_Umur']) or arrUser[user_id]['Tinggi_Badan'] >arrWahana[wahana_id]["Batasan_Tinggi"]:
            if int(jml_tiket * arrWahana[wahana_id]["Harga_Tiket"]) < int(arrUser[user_id]["Saldo"]):
                arrBeli.append({
                    'Username': arrUser[user_id]['Username'],
                    'Tanggal_Pembelian': tanggal,
                    'ID_Wahana': wahana,
                    'Jumlah_Tiket': jml_tiket,
                })
                print(arrBeli)
            else:
                print("Saldo Anda tidak cukup")
                print("Silakan mengisi saldo Anda")
        else:
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
    else:
        print("Wahana tidak ditemukan!")

umur()
#beli_tiket()

