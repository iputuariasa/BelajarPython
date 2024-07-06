#BELAJAR MANIPULASI LIST

data = ["Bayu", "Guna", "Fajar"]
print(f"Data List : {data}")

# Mengambil data list
data_0 = data[0]
print(f"Data Pertama(index-0) : {data_0}")

data_terakhir = data[-1]
print(f"Data Terakhir : {data_terakhir}")

# Menghitung panjang data list
panjang_data = len(data)
print(f"Panjang Data List : {panjang_data}")

# Menambahkan data list
data.insert(1,"Eka")
print(f"Data Tambahan : {data}")

# Menambahkan data paling akhir
data.append("Sekar")
print(f"Data Tambah : {data}")

#Mengubah data list
data[0] = "Bima"
print(f"Data List Diubah : {data}")

# Menghapus Data List
data.remove("Bima")
print(f"Data Setelah diremove : {data}")

data.pop()
print(f"Data Setelah diremove : {data}")

# Menggabungkan list dengan list
print(f"Data List Sebelumnya : \n{data}")

data_baru = ["Rojak", "Denis"]
data.extend(data_baru)
print(f"Data Gabung : \n{data}")