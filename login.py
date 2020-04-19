from load2 import Filename
import Obfuscator



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
    un = input("Masukkan username: ")
    pw = Obfuscator.obs(input("Masukkan password: "))
    login = False
    for i in range(200):
        try:
            if (Filename[0][i][3]==un and Filename[0][i][4]==pw):
                user_birth = Filename[0][i][1]
                user_height = Filename[0][i][2]
                user_saldo = Filename[0][i][6]
                login = True
                break
        except:
            login = False
    if (login == True):
        if Filename[0][i][5] == 'admin':
            print('Selamat datang, Admin!')
            admin = True
        else:
            print("Selamat bermain,",un,"!")
            admin = False
    else:
        print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    return admin,un,user_birth,user_height,user_saldo

# CEK FUNGSI
admin,un,user_birth,user_height,user_saldo = login()

