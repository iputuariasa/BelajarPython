##Belajar String

title = "BELAJAR STRING".center(50,"=")
print(title)

# Menggabungkan string
namaDepan = "Ucup"
namaBelakang = "Libaba"
namaLengkap = namaDepan  + " " + namaBelakang
print("Nama Lengkap : " + namaLengkap)

# Menghitung panjang string
print("Panjang String Nama Lengkap = " + str(len(namaLengkap)))

# Mengecek apakah ada char didalam string (in)
nama = "Ucup"
status = nama in namaLengkap
print("Apakah kata " + nama + " ada di " + namaLengkap + " = " + str(status))

# Mengecek apakah tidak ada char didalam string (not in)
nama = "Ucup"
status = nama not in namaLengkap
print("Apakah Benar Tidak Ada Kata " + nama + " di Kalimat " + namaLengkap + " = " + str(status))

# Mengulang String
print("Ucup Ketawa " + "wk"*20)

# Mengambil Data dari String
nama = namaLengkap[0:4]
print("Ambil Nama Lengkap dari index[0-3] = " + nama)

# Mencari Item paling Kecil (min)
print("Item paling kecil dari kalimat " + namaLengkap + " adalah = " + min(namaLengkap))

# Mencari Item paling Besar (max)
print("Item paling besar dari kalimat " + namaLengkap + " adalah = " + max(namaLengkap))