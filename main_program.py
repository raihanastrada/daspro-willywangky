import csv
import Obfuscator

def load():
    Filename = [[[' ' for k in range (7)] for j in range (100)] for i in range (7)]
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
        for i in range(100):
            if (Filename[0][i][3]==un and Filename[0][i][4]==pw):
                login = True
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
    N = 200
    fieldnames = ['Nama', 'Tanggal_Lahir', 'Tinggi_Badan', 'Username', 'Password']
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

    for i in range (N):
        if Filename[0][i] == None:
            Filename[0][i] = [Nama, Tanggal_Lahir,Tinggi_Badan,Username,Obfuscator.obs(Password),'user',0]
            break
    return Filename


def cari_pemain():
    found_session = False
    while (not found_session):
        found = False
        un_search = input("Masukkan username: ")
        if (un_search != "ADMIN"):
            for i in range(100):
                if (Filename[0][i][3]==un_search):
                    print("Nama Pemain: ",Filename[0][i][0])
                    print("Tinggi Pemain: ",Filename[0][i][2])
                    print("Tanggal Lahir Pemain: ",Filename[0][i][1])
                    found = True
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
    for i in range (100):
        if (Filename[1][i][0] == ' '):
            Filename[1][i] = wahana
            break
    return Filename

def riwayat_wahana():
    ID = input("Masukkan ID Wahana: ")
    count = 0
    for i in range(100):
        if (Filename[3][i][2]==ID):
            tanggal = Filename[3][i][1]
            user = Filename[3][i][0]
            tiket = Filename[3][i][3]
            print("{} | {} | {}".format(tanggal,user,tiket))
            count += 1
    if (count == 0):
        print("Riwayat tidak ditemukan")

def lihat_laporan():
    if (Filename[6][1]==[]):
        print("Tidak terdapat kritik dan saran") 
    
    else :
        count = 0
        while (Filename[6][count][0] != ' '):
            count += 1
        for i1 in range(1,count-1):
            for i2 in range(i1+1,count):
                if (ord(Filename[6][i1][2][0]) < ord(Filename[6][i2][2][0])):
                    temp = Filename[6][i2]
                    Filename[6][i2] = Filename[6][i1]
                    Filename[6][i1] = temp
                elif (ord(Filename[6][i1][2][0]) == ord(Filename[6][i2][2][0])):
                    if (ord(Filename[6][i1][2][1]) < ord(Filename[6][i2][2][1])):
                        temp = Filename[6][i2]
                        Filename[6][i2] = Filename[6][i1]
                        Filename[6][i1] = temp
                    elif (ord(Filename[6][i1][2][1]) == ord(Filename[6][i2][2][1])):
                        if (ord(Filename[6][i1][2][2]) < ord(Filename[6][i2][2][2])):
                            temp = Filename[6][i2]
                            Filename[6][i2] = Filename[6][i1]
                            Filename[6][i1] = temp
                        elif (ord(Filename[6][i1][2][2]) == ord(Filename[6][i2][2][2])):
                            continue

        j = 1
        while (Filename[6][j][0] != ' '):
            print("{} | {} | {} | {}".format(Filename[6][j][2],Filename[6][j][1],Filename[6][j][0],Filename[6][j][3]))
            j += 1

def topup():
    un = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo yang di top-up: "))

    for i in range(100):
        if (Filename[0][i][3] == un):
            Filename[0][i][6] = int(Filename[0][i][6]) + saldo
            print()
            print("Top-up berhasil. Saldo Willy Wangky bertambah menjadi Rp{},00".format(Filename[0][i][6]))
            break
    return Filename


"""
---------------------------------------------------------------------------------------------------------
"""
print("Selamat Datang di Willy Wangky, 'Not Just A Chocolate Factory'")
print("Untuk memulai silakan masukkan (load) data-data terlebih dahulu")
print()
Filename = load()
print()

print("Willy Wangky, Dunia Bermain Impian Anda!")
print("Masukkan Opsi Permainan:")
print("1. Log In")
print("2. Sign Up")
print()
pilih = int(input())
if (pilih == 1):
    admin,un = login()
    if (admin):
        print("Silakan pilih opsi di bawah ini:")
        print("1. Cari Pemain")
        print("2. Lihat Kritik dan Saran")
        print("3. Tambah Wahana Baru")
        print("4. Top Up Saldo Pemain")
        print("5. Lihat Riwayat Wahana")
        print("6. Lihat Jumlah Tiket Pemain")
        print("7. Save")
        print("8. Exit")
        print()
        pilih = int(input())
        if (pilih == 1):
            cari_pemain()
        elif (pilih == 2):
            lihat_laporan()
        elif (pilih == 3):
            tambah_wahana()
        elif (pilih == 4):
            topup()
        elif (pilih == 5):
            riwayat_wahana()
        #elif (pilihan == 6):
            


else:
    signup()

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
