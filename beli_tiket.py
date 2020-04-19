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

Filename = Filename
user_id = user_id
admin = admin
'''



## ALGORITMA BELI TIKET
def umurvalid(now, birth):  # DD/MM/YYYY
    hari_lahir = int(birth[0:2])
    bulan_lahir = int(birth[3:5])
    tahun_lahir = int(birth[6:10])
    hari_now = int(now[0:2])
    bulan_now = int(now[3:5])
    tahun_now = int(now[6:10])
    valid = False
    if (tahun_now - tahun_lahir) > 17:
        valid = True
    else: # tahun_now - tahun_lahir <= 17
        if tahun_now - tahun_lahir == 17:
            if bulan_lahir > bulan_now:
                valid = True
            else: 
                if bulan_lahir == bulan_now:
                    if hari_lahir > hari_now:
                        valid = True
                    else:
                        valid = False
                else:
                    valid = False
        else:
            valid = False
    if valid:
       return 'Dewasa' # anggapan lebih tua dari batas umur 17
    else:
        return "Anak" # anggapan anak - anak

def beli_tiket():
    wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jml_tiket = int(input("Masukkan tiket yang dibeli: "))
    arrUser = Filename[0]
    arrWahana = Filename[1]
    arrBeli = Filename[2]
    arrTiket = Filename[4]
    i = 0
    harga_tiket = 0
    found = False
    while not(found) and i < 201: # panjang array statis 200 line dengan 1 line header
        if arrWahana[i][0] == wahana:
            wahana_id = i
            found = True
            harga_tiket = harga_tiket + (jml_tiket * int(arrWahana[wahana_id][2])) # menentukan harga tiket yang di beli
            break
        else:
            i = i + 1 
    if found :
        if (umurvalid(str(tanggal), str(user_birth)) == str(arrWahana[wahana_id][3]) or str(arrWahana[wahana_id][3]) == "Semua Umur") and user_height > arrWahana[wahana_id][4]:
            if harga_tiket < int(user_saldo):
                for i in range (1000): # jumlah baris pada array
                   if arrBeli[i] == None: # mengecek baris kosong awal dari array yang sudah tersedia
                       arrBeli[i] = [username, tanggal, wahana, jml_tiket] # mengisi baris kosong dengan data yang diinput
                       break
                
                j = 0
                while (arrUser[j] != None):
                    if (arrUser[j][3] == username):
                        arrUser[j][6] = int(arrUser[j][6]) - harga_tiket # mengurangi nilai saldo pada array user
                        break
                    else:
                        j = j + 1
                
                for i in range (1000): # melihat array file tiket.csv
                    if arrTiket[i] == None: # mengecek apakah user sudah memiliki tiket di wahana tsb
                        arrTiket[i] = [username, wahana, jml_tiket]
                        break
                    else:
                        if arrTiket[i][0] == username and arrTiket[i][1] == wahana: # mengecek apakah user sudah punya tiket
                            arrTiket[i][2] = int(arrTiket[i][2]) + jml_tiket # menambahkan jumlah tiket ke file yang sudah ada
                            break
            else:
                print("Saldo Anda tidak cukup")
                print("Silakan mengisi saldo Anda")
        else:
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
    else:
        print("Wahana tidak ditemukan!")

beli_tiket()
print(Filename[0])
print(Filename[1])
print(Filename[2])
print(Filename[4])

