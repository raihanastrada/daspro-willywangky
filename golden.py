from load2 import Filename

def upgrade():
    username = input("Masukkan username yang ingin di-upgrade: ")
    arrUser = Filename[0]
    biaya = 200000
    i = 0
    while (arrUser[i] != None):
        if (arrUser[i][3] == username):
            saldo = int(arrUser[i][6])
            saldo -= biaya
            if (saldo < 0):
                print("Saldo tidak mencukupi untuk upgrade! Silakan isi saldo terlebih dahulu")
            else: # saldo >= 0
                arrUser[i][5] = "Golden"
                arrUser[i][6] = saldo
                print("Akun telah di-upgrade")
            break
        i += 1
    Filename[0] = arrUser

    return Filename

upgrade()
print(Filename[0])