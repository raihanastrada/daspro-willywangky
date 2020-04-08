def load():
    fileuser =[]
    filewahana =[]
    filepembelian =[]
    filepenggunaan=[]
    filekepemilikan =[]
    filerefund =[]
    kritiksaran =[]
    
    file_user = input("Masukkan nama File User: ")
    file_wahana = input("Masukkan nama File Wahana:")
    file_pembelian = input("Masukkan nama File Pembelian Tiket: ")
    file_penggunaan = input("Masukkan nama File Penggunaan Tiket: ")
    file_kepemilikan = input("Masukkan nama File Kepemilikan Tiket: ")
    file_refund = input("Masukkan nama File Refund Tiket: ")
    file_kritiksaran = input("Masukkan nama File Kritik dan Saran: ")
    with open(file_user , 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter =',')
        for row in read:
            fileuser.append(row)
    with open(file_wahana, 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter=',')
        for row in read:
            filewahana.append(row)
    with open(file_pembelian, 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter=',')
        for row in read:
            filewahana.append(row)
    with open(file_pembelian, 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter=',')
        for row in read:
            filepembelian.append(row)
    with open(file_penggunaan, 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter=',')
        for row in read:
            filepenggunaan.append(row)
    with open(file_kepemilikan, 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter=',')
        for row in read:
            filekepemilikan.append(row)
    with open(file_refund, 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter=',')
        for row in read:
            filerefund.append(row)
    with open(file_kritiksaran, 'r') as csv_file:
        read = csv.DictReader(csv_file, delimiter=',')
        for row in read:
            kritiksaran.append(row)
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
    
    return fileuser, filewahana, filepembelian, filepenggunaan, filekepemilikan, filerefund, kritiksaran



