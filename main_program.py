import csv
import Obfuscator

def load():
    sizeus = 200  # ukuran maksimal array user
    sizeelse = 1000  # ukuran maksimal array lain
    Auser = [None for j in range(sizeus)]  # template array user dengan ukuran sizeus
    Aelse1 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse2 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse3 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse4 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse5 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Aelse6 = [None for j in range(sizeelse)] # template array lain dengan ukuran else
    Filename = [Auser, Aelse1, Aelse2, Aelse3, Aelse4, Aelse5, Aelse6]
    File = ['' for i in range(7)]
    File[0] = input('Masukkan nama File User: ')
    File[1] = input('Masukkan nama File Daftar Wahana: ')
    File[2] = input('Masukkan nama File Pembelian Tiket: ')
    File[3] = input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = input('Masukkan nama File Refund Tiket: ')
    File[6] = input('Masukkan nama File Kritik dan Saran: ')
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            with open(File[i], 'r') as csv_file:
                read = csv.reader(csv_file, delimiter=',')
                j = 0
                for row in read:
                    Filename[i][j]=row
                    j += 1
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
    if (Error.count(True) == 0):
        print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return Filename


'''
File[0] = 'user.csv'        # input('Masukkan nama File User: ')
File[1] = 'wahana.csv'      # input('Masukkan nama File Daftar Wahana: ')
File[2] = 'pembelian.csv'   # input('Masukkan nama File Pembelian Tiket: ')
File[3] = 'penggunaan.csv'  # input('Masukkan nama File Penggunaan Tiket: ')
File[4] = 'tiket.csv'       # input('Masukkan nama File Kepemilikan Tiket: ')
File[5] = 'refund.csv'      # input('Masukkan nama File Refund Tiket: ')
File[6] = 'kritiksaran.csv'    
'''
def login():
    login = False
    while (not login):
        un = input("Masukkan username: ")
        pw = Obfuscator.obs(input("Masukkan password: "))        
        for i in range(200):
            if (Filename[0][i] != None):
                if (Filename[0][i][3]==un and Filename[0][i][4]==pw):
                    login = True
                    break
            else:
                break
        if (login == True):
            print("Selamat bermain,",un,"!")
        else:
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    if (un=="ADMIN"):
        admin = True
    else:
        admin = False

    print()
    return admin,un

def signup():
    # Local Function
    def alphacheck(a):
        cek = True
        for i in a:
            chr = ord(i)
            if not ((48 <= chr <= 57) or (65 <= chr <= 90) or (97 <= chr <= 122)):
                cek = False
                break
        return cek

    def ucheck(a,b):
        Exist = False
        for i in range(201):
            try:
                if b[i][3] == a:
                    Exist = True
                    break
            except:
                Exist = False
        return Exist

    # Function Algorithm
    Nama = input("Masukkan nama pemain: ")
    Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
    Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
    Username = input("Masukkan username pemain: ")
    while (alphacheck(Username) == False) or (ucheck(Username,Filename[0]) == True):
        if (alphacheck(Username) == False):
            print('Error, please input alphanumeric for username!')
            Username = input("Masukkan username pemain: ")
        if (ucheck(Username,Filename[0]) == True):
            print("Username sudah terdaftar")
            Username = input("Masukkan username pemain: ")

    Password = input("Masukkan password pemain: ")
    while (alphacheck(Password) == False):
        print('Error, please input alphanumeric for password!')
        Password = input("Masukkan password pemain: ")

    for i in range (200):
        if (Filename[0][i] == None):
            Filename[0][i] = [Nama, Tanggal_Lahir,Tinggi_Badan,Username,Obfuscator.obs(Password),'user',0]
            break
    return Filename


def cari_pemain():
    found_session = False
    while (not found_session):
        found = False
        un_search = input("Masukkan username: ")
        if (un_search != "ADMIN"):
            for i in range(200):
                if (Filename[0][i] != None):
                    if (Filename[0][i][3]==un_search):
                        print("Nama Pemain: ",Filename[0][i][0])
                        print("Tinggi Pemain: ",Filename[0][i][2])
                        print("Tanggal Lahir Pemain: ",Filename[0][i][1])
                        found = True
                        break
                else:
                    break
        if (not found):
            print("Pemain tidak ditemukan")
        print()
        valid = False
        while (not valid):
            pilih = input("Apakah Anda ingin melanjutkan mencari? (Y/N): ")
            if (pilih == "Y"):
                valid = True
            elif (pilih == "N"):
                valid = True
                found_session = True
            else:
                print("Masukaan salah, silakan ulangi!")


def tambah_wahana():
    id = input("Masukkan ID Wahana: ")
    nama = input("Masukkan Nama Wahana: ")
    harga = input("Masukkan Harga Tiket: ")
    umur = input("Batasan Umur: ")
    tinggi = input("Batasan Tinggi Badan: ")
    wahana = [id,nama,harga,umur,tinggi]
    for i in range (1000):
        if (Filename[1][i] == None):
            Filename[1][i] = wahana
            break
    return Filename

def riwayat_wahana():
    ID = input("Masukkan ID Wahana: ")
    count = 0
    for i in range(1000):
        if (Filename[3][i]!=None):
            if (Filename[3][i][2]==ID):
                tanggal = Filename[3][i][1]
                user = Filename[3][i][0]
                tiket = Filename[3][i][3]
                print("{} | {} | {}".format(tanggal,user,tiket))
                count += 1
        else:
            break
    if (count == 0):
        print("Riwayat tidak ditemukan")


def lihat_laporan():
    if (Filename[6][1]==None):
        print("Tidak terdapat kritik dan saran") 
    
    else :
        count = 0
        while (Filename[6][count] != None):
            count += 1
        for i1 in range(1,count-1):
            for i2 in range(i1+1,count):
                if (ord(Filename[6][i1][2][0]) > ord(Filename[6][i2][2][0])):
                    temp = Filename[6][i2]
                    Filename[6][i2] = Filename[6][i1]
                    Filename[6][i1] = temp
                elif (ord(Filename[6][i1][2][0]) == ord(Filename[6][i2][2][0])):
                    if (ord(Filename[6][i1][2][1]) > ord(Filename[6][i2][2][1])):
                        temp = Filename[6][i2]
                        Filename[6][i2] = Filename[6][i1]
                        Filename[6][i1] = temp
                    elif (ord(Filename[6][i1][2][1]) == ord(Filename[6][i2][2][1])):
                        if (ord(Filename[6][i1][2][2]) > ord(Filename[6][i2][2][2])):
                            temp = Filename[6][i2]
                            Filename[6][i2] = Filename[6][i1]
                            Filename[6][i1] = temp
                        elif (ord(Filename[6][i1][2][2]) == ord(Filename[6][i2][2][2])):
                            continue

        j = 1
        while (Filename[6][j] != None):
            print("{} | {} | {} | {}".format(Filename[6][j][2],Filename[6][j][1],Filename[6][j][0],Filename[6][j][3]))
            j += 1


def topup():
    found = False
    while (not found):
        un = input("Masukkan username: ")
        saldo = int(input("Masukkan saldo yang di top-up: "))
        for i in range(200):
            if (Filename[0][i] != None):
                if (Filename[0][i][3] == un):
                    Filename[0][i][6] = int(Filename[0][i][6]) + saldo
                    print()
                    found = True
                    print("Top-up berhasil. Saldo Willy Wangky bertambah menjadi Rp{},00".format(Filename[0][i][6]))
                    break
            else:
                break
        if (not found):
            print("Data yang anda masukkan salah! Silakan masukkan ulang.")
    return Filename

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

## ALGORITMA BELI TIKET
def umurvalid(now, birth):  # DD/MM/YYYY
    hari_lahir = int(birth[0:2])
    print(hari_lahir)
    bulan_lahir = int(birth[3:5])
    print(bulan_lahir)
    tahun_lahir = int(birth[6:10])
    print(tahun_lahir)
    hari_now = int(now[0:2])
    bulan_now = int(now[3:5])
    tahun_now = int(now[6:10])
    if (tahun_now - tahun_lahir) > 17:
        dewasa = True
    else: # tahun_now - tahun_lahir <= 17
        if (tahun_now - tahun_lahir == 17):
            if (bulan_lahir > bulan_now):
                dewasa = True
            elif (bulan_lahir == bulan_now):
                if (hari_lahir >= hari_now):
                    dewasa = True
                else:
                    dewasa = False
            else:
                dewasa = False
        else:
            dewasa = False
    if (dewasa):
        return 'Dewasa' # anggapan lebih tua dari batas umur 17
    else:
        return "Anak" # anggapan anak - anak

def beli_tiket(username):
    wahana = input("Masukkan ID wahana: ")
    tanggal = input("Masukkan tanggal hari ini: ")
    jml_tiket = int(input("Masukkan tiket yang dibeli: "))
    arrUser = Filename[0]
    arrWahana = Filename[1]
    arrBeli = Filename[2]
    arrTiket = Filename[4]
    i = 0
    found = False
    while (not found and arrWahana[i] != None): # panjang array statis 200 line dengan 1 line header
        if (arrWahana[i][0] == wahana):
            wahana_id = i
            found = True
            harga_tiket = jml_tiket * int(arrWahana[wahana_id][2]) # menentukan harga tiket yang di beli
            break
        else:
            i = i + 1 
    if (found) :
        if ((umurvalid(str(tanggal), str(user_birth)) == str(arrWahana[wahana_id][3]) or str(arrWahana[wahana_id][3]) == "Semua Umur") and int(user_height) > int(arrWahana[wahana_id][4])):
            if (int(harga_tiket) < int(user_saldo)):
                for i in range (1000): # jumlah baris pada array
                   if (arrBeli[i] == None): # mengecek baris kosong awal dari array yang sudah tersedia
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
                    if (arrTiket[i] == None): # mengecek apakah user sudah memiliki tiket di wahana tsb
                        arrTiket[i] = [username, wahana, jml_tiket]
                        break
                    else:
                        if (arrTiket[i][0] == username and arrTiket[i][1] == wahana): # mengecek apakah user sudah punya tiket
                            arrTiket[i][2] = int(arrTiket[i][2]) + jml_tiket # menambahkan jumlah tiket ke file yang sudah ada
                            break
            else:
                print("Saldo Anda tidak cukup")
                print("Silakan mengisi saldo Anda")
        else:
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        Filename[0] = arrUser
        Filename[1] = arrWahana
        Filename[2] = arrBeli
        Filename[4] = arrTiket

    else:
        print("Wahana tidak ditemukan!")

    return Filename

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

def save():
    File = ['' for i in range(7)]
    File[0] = input('Masukkan nama File User: ')
    File[1] = input('Masukkan nama File Daftar Wahana: ')
    File[2] = input('Masukkan nama File Pembelian Tiket: ')
    File[3] = input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = input('Masukkan nama File Refund Tiket: ')
    File[6] = input('Masukkan nama File Kritik dan Saran: ')
    Name = ['User: ','Daftar Wahana: ','Pembelian Tiket: ','Penggunaan Tiket: ','Kepemilikan Tiket: ','Refund Tiket: ','Kritik dan Saran: ']
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            open(File[i])
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
            while (Error[i] == True):
                File[i] = input('Masukkan nama File ' + Name[i])
                Error[i] = False
                try:
                    open(File[i])
                except:
                    Error[i] == True
    if (Error.count(True) == 0):
        for i in range(7):
            with open(File[i],'w',newline='') as savedfiles:
                csv_writer = csv.writer(savedfiles,delimiter=',')
                for j in range(1000):
                    try:
                        if (Filename[i][j] != None):
                            csv_writer.writerow(Filename[i][j])
                    except:
                        break
        print('Success!')

"""
---------------------------------------------------------------------------------------------------------
"""

session1 = True
session2 = True

print("Selamat Datang di Willy Wangky, 'Not Just A Chocolate Factory'")
print("Untuk memulai silakan masukkan (load) data-data terlebih dahulu")
print()
Filename = load()
print()

while (session1):
    print("Willy Wangky, Dunia Bermain Impian Anda!")
    print("Silakan Login terlebih dahulu")
    print()
    admin,un = login()
    while (session2):
        if (admin):
            print("Silakan pilih opsi di bawah ini:")
            print("1. Signup")
            print("2. Cari Pemain")
            print("3. Lihat Kritik dan Saran")
            print("4. Tambah Wahana Baru")
            print("5. Top Up Saldo Pemain")
            print("6. Lihat Riwayat Wahana")
            print("7. Lihat Jumlah Tiket Pemain")
            print("8. Save")
            print("9. Exit")
            print()
            pilih = int(input())
            if (pilih == 1):
                signup()
            elif (pilih == 2):
                cari_pemain()
            elif (pilih == 3):
                lihat_laporan()
            elif (pilih == 4):
                tambah_wahana()
            elif (pilih == 5):
                topup()
            elif (pilih == 6):
                riwayat_wahana()
            elif (pilih == 7):
                jumlah_tiket()
            elif (pilih == 8):
                save()
        if (not admin):
            print("Silakan pilih opsi di bawah ini:")
            print("1. Cari Wahana")
            print("2. Beli Tiket")
            print("3. Pakai Tiket")
            print("4. Refund")
            print("5. Kritik Saran")
            print("6. Save")
            print("7. Exit")
            print()
            pilih = int(input())
            if (pilih == 1):
                cari_wahana()
            elif (pilih == 2):
                beli_tiket(un)
            elif (pilih == 3):
                refund(un)
            elif (pilih == 4):
                kritik_saran(un)
            elif (pilih == 5):
                save()
            """
            elif (pilih == 6):
                exit()
            """    


"""
tambah = 0
data_wahana = [[None for j in range (6)] for i in range (30)] 
valid = True
tambah_wahana(data_wahana,tambah)
print(data_wahana)
tambah += 1
print("Info wahana telah ditambahkan!")
"""
"""
riwayat_wahana()
"""