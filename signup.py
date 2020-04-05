import csv

with open('user.csv', 'r') as csvread:
    csv_reader = csv.DictReader(csvread)

    with open('user.csv', 'w', newline='') as csvwrite:
        fieldnames = ['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password']
        filesignup = csv.DictWriter(csvwrite, fieldnames=fieldnames)
        filesignup.writeheader()
        Nama = input("Masukkan nama pemain: ")
        Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
        Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
        Username = input("Masukkan username pemain: ")
        Password = input("Masukkan password pemain: ")
        if Username in csv_reader:
            print("Username sudah terdaftar")
        else:
            filesignup.writerow({'Nama' : Nama , 'Tanggal_Lahir' : Tanggal_Lahir ,
            'Tinggi_Badan' : Tinggi_Badan , 'Username' : Username , 'Password' : Password})


    
