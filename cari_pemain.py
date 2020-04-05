import csv
def cari_pemain():
    with open('user.csv', 'r') as read:
        csv_reader = csv.DictReader(read)
        un_search = input("Masukkan username: ")

        found = False
        for row in csv_reader:
             if(row['Username'] == un_search):
                 found = True
                 data = row
                 break
        if (found == True):
            nama = row["Nama"]
            tgl = row["Tanggal_Lahir"]
            tinggi = row["Tinggi_Badan"]

            print("Nama pemain: " + nama)
            print("Tinggi badan pemain: " + str(tinggi))
            print("Tanggal lahir pemain: " + str(tgl))
        else:
            print("Maaf, pemain tidak ditemukan di database kami!")
