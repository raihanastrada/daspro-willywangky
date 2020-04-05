import csv

with open('user.csv', 'r') as csvread:
    csv_reader = csv.DictReader(csvread)

    with open('user.csv', 'a', newline='') as csvwrite:
        fieldnames = ['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password']
        filesignup = csv.DictWriter(csvwrite, fieldnames=fieldnames)
        Nama = input("Masukkan nama pemain: ")
        Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYY): ")
        Tinggi_Badan = input("Masukkan tinggi badan (cm): ")
        Username = input("Masukkan username pemain: ")
        Password = input("Masukkan password pemain: ")

        valid = True
        for row in csv_reader:
            val_un = row['Username']
            if (val_un == Username):
                print("Username sudah terdaftar")
                valid = False
                break
        if (valid == True):
            filesignup.writerow({
                'Nama' : Nama ,
                'Tanggal_Lahir' : Tanggal_Lahir ,
                'Tinggi_Badan' : Tinggi_Badan , 
                'Username' : Username , 
                'Password' : Password
                })


    
