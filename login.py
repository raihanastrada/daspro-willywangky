import csv
csvfile = open('user.csv', newline='')
filelogin= csv.reader(csvfile)

data = [row for row in filelogin]

col_nama = [x[0] for x in data]
col_uname = [x[3] for x in data]
col_pw = [x[4] for x in data]

un = input("Masukkan username: ")
pw = input("Masukkan password: ")

login = False
if un in col_uname:
    for i in range(0, len(col_uname)):   
        if col_uname[i]== un and col_pw[i] == pw:
            login = True
            print("Selamat bermain, {}!").format(col_nama[i])
else:
    print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
