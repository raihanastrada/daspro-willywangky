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
        """
                elif (ord(Filename[6][i1][2][0]) == ord(Filename[6][i2][2][0])):
                    j = 1
                    banding = False
                    while ((j < 6) or (not banding)):
                        if (ord(Filename[6][i1][2][j]) == ord(Filename[6][i2][2][j])):
                            j += 1
                        elif (ord(Filename[6][i1][2][j]) < ord(Filename[6][i2][2][j])):
                            temp = Filename[6][i2]
                            Filename[6][i2] = Filename[6][i1]
                            Filename[6][i1] = temp
                            banding = True
                    temp = Filename[6][i2]
                    Filename[6][i2] = Filename[6][i1]
                    Filename[6][i1] = temp
        """
        
        
        """
        min_urut = Filename[6][1][2]
        list_kritik = ['' for i in range (100)]
        for i in range(1,len(Filename[6])):
            for k in range(1,len(Filename[6])):
                ID = Filename[6][k][2]
                if (i == 0):
                    if (ord(ID[0])<ord(min_urut[0])):
                        min_urut = ID
                    elif (ord(ID[0])==ord(min_urut[0])):
                        j = 1
                        banding = False
                        while ((j < 7) or (not banding)):
                            if (ord(ID[j])==ord(min_urut[j])):
                                j += 1
                            elif (ord(ID[j])<ord(min_urut[j])):
                                min_urut = ID
                                banding = True
                            else:
                                min_urut = min_urut
                                banding = True
                else:
                    if (ID > list_kritik[i-1]):
                        min_urut = ID 
                    if (ord(ID[0])<ord(min_urut[0]) and ID != list_kritik[i-1]):
                        min_urut = ID
                    elif (ord(ID[0])==ord(min_urut[0]) and ID != list_kritik[i-1]):
                        j = 1
                        banding = False
                        while ((j < 6) or (not banding)):
                            if (ord(ID[j])==ord(min_urut[j])):
                                j += 1
                            elif (ord(ID[j])<ord(min_urut[j])):
                                min_urut = ID
                                banding = True
                            else:
                                min_urut = min_urut
                                banding = True
            list_kritik[i-1] = min_urut
        print(list_kritik[i])
                

"""
"""
            for j in range (len(ID)):
                if (ord(ID[j]))
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
"""
lihat_laporan()
