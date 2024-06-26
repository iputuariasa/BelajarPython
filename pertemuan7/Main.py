# MENGAMPIL INPUT DATA DARI USER

data = input("Masukkan Data : ")

# semua data yang di inputkan user bertype data string
print("Data : ", data, ", Bertype : ", type(data))

# untuk mengambil bertype data numerik (int/float), maka harus dicasting
angka = int(input("Masukkan Angka : "))
angka = float(input("Masukkan Angka : "))

print("Data : ", angka, " , Bertype : ", type(angka))

# khusus untuk mengambil data boolean harus di casting ke integer dahulu kemudian di casting ke boolean
biner = bool(int(input("Masukkan Biner : ")))

print("Data : ", biner, " , Bertype : ", type(biner))