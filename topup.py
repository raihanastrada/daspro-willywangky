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

def topup():
    un = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo yang di top-up: "))

    for i in range(len(Filename[0])):
        if (Filename[0][i]['Username'] == un):
            Filename[0][i]['Saldo'] = int(Filename[0][i]['Saldo']) + saldo
            print("")
            print("Top-up berhasil. Saldo Willy Wangky bertambah menjadi",Filename[0][i]['Saldo'])
            break