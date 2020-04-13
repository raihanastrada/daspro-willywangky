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

def lihat_laporan():
    if (len(Filename[6]) == 0):
        print("Tidak terdapat kritik dan saran") 
    
    else :
        # Mengurutkan berdasarkan ID Wahana
        for i1 in range(len(Filename[6])):
            for i2 in range(len(Filename[6])):
                if Filename[6][i1]['ID_Wahana'] < Filename[6][i2]['ID_Wahana']:
                    temp = Filename[6][i2]
                    Filename[6][i2] = Filename[6][i1]
                    Filename[6][i1] = temp

        # Menuliskan Kritik dan Saran
        print("Kritik dan Saran:")
        for i in range(len(Filename[6])):
            print(Filename[6][i]['ID_Wahana'],'|', Filename[6][i]['Tanggal_Kritik'],'|', Filename[6][i]['Username'],'|', Filename[6][i]['Isi_Kritik'])
            