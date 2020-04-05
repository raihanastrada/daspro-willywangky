import csv
csvfile = open('user.csv', newline='')
filesignup = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
filelogin = csv.reader(csvfile)

Nama = input("Masukkan nama pemain: ")
Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
Username = input("Masukkan username pemain: ")
Password = input("Masukkan password pemain: ")
if Username in filelogin:
    print("Username sudah terdaftar")
else:
    filesignup.writerow([Nama, Tanggal_Lahir, Tinggi_Badan, Username, Password])


    
