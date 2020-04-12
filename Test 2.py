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

Filename = Filename
un = input("Masukkan username: ")
pw = Obfuscator.obs(input("Masukkan password: "))

login = False
for i in range(len(Filename[0])):
    if (Filename[0][i]['Username']==un and Filename[0][i]['Password']==pw):
        login = True
        break
if (login == True):
    print("Selamat bermain,",un,"!")
else:
    print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
