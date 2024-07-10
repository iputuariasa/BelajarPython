# BELAJAR OPERATOR PADA DICTIONARY

data_dict = {
    "nama1" : "Bobon Santoso",
    "nama2" : "Willy Salim",
    "nama3" : "Kadek Kangin"
}

print(data_dict)

# Menghitung panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang data dictionary = {LENDICT}")

# Mengecek apakah key ada atau tidak pada dictionary
KEY = "nama1"
CHECKKEY = KEY in data_dict
print(f"apakah key {KEY} ada pada data_dict = {CHECKKEY}")

# READ => Mengakses value dengan get
print(f"Nama 1 : {data_dict.get("nama1")}")
print(f"Nama 6 : {data_dict.get("nama6")}")
print(f"Nama 7 : {data_dict.get("nama7","Key tidak ditemukan")}")

# UPDATE => meupdate data pada dictionary
# jika key ada akan mengubah data berdasarka  key yang ditentukan
data_dict.update({"nama1" : "Sandika Galih"})
print(data_dict)

#jika key tidak ada akan secara otomatis menambahkan data
data_dict.update({"nama4" : "Wahyudika Jaya Abadi"})
print(data_dict)

# DELETE => Menghapus data pada dictionary
del data_dict["nama2"]
print(data_dict)