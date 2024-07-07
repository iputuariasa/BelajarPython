# BELAJAR MANIPULASI LIST 2

data_angka = [2,4,5,1,0,2,3,9,4,1,8,9]
data  = ["Bayu", "Guna", "Bima", "Sakti"]
print(f"Data Angka = \n{data_angka}")
print(f"Data List = \n{data}")

# Mencari jumlah data di list (count)
jumlah_2 = data_angka.count(2)
print(f"Jumlah angka 2 = {jumlah_2}")

# Mengampil posisi data (index)
index_bima = data.index("Bima")
print(f"Posisi Index Bima = {index_bima}")

# Mengurutkan data list (sort)
print(f"Data Angka sebelum diurutkan = \n{data_angka}")
data_angka.sort()
print(f"Data Angka setelah diurutkan = \n{data_angka}")

print(f"Data list sebelum diurutkan = {data}")
data.sort()
print(f"Data list setelah diurutkan = \n{data}")

# Membalik urutan list
data_angka.reverse()
print(f"Data angka setelah dibalik = \n{data_angka}")

data.reverse()
print(f"Data list setelah dibalik = \n{data}")