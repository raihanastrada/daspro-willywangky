from load2 import Filename

def best_wahana():
    arrWahana = Filename[1] # inisiasi array wahana
    arrBeli = Filename[2] # inisiasi array pembelian
    n = 0
    while (arrWahana[n] != None): # Menghitung banyak baris file wahana
        n += 1
    count = [[0 for j in range (3)] for i in range (n-1)] # Membuat array baru untuk total tiket per wahana
    for i in range (1,n):
        count[i-1] = [0,arrWahana[i][0],arrWahana[i][1]] # [0] = ID wahana ; [1] = nama wahana
        j = 0
        while (arrBeli[j] != None): # menghitung jumlah tiket wahana dari file pembelian tiket
            if (arrBeli[j][2] == arrWahana[i][0]):
                count[i-1][0] += int(arrBeli[j][3])
            j += 1
    
    for i1 in range(n-2): # mengurutkan array berdasarkan total penjualan tiket (besar ke kecil)
        for i2 in range(i1+1,n-1):
            if (count[i1][0] <= count[i2][0]):
                temp = count[i2]
                count[i2] = count[i1]
                count[i1] = temp
    
    for i in range (3): # menampilkan ranking wahana berdasarkan tiket
        print("{} | {} | {} | {}".format(i+1,count[i][1],count[i][2],count[i][0]))
    

best_wahana()