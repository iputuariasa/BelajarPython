#FORMAT STRING

print("FORMAT STRING".center(60,"="))

#String Teks
nama = "I Putu Ariasa"
umur = 10
# print("Halo, nama saya " + nama + " umur saya " + umur) hal ini tidak bisa dilakukan tidak bisa menggunakan + untuk menggabungkan string dengan number

print(f"Halo Nama Saya {nama}, saya berumur {umur} tahun saat ini") #kita bisa menggabungkan string dengan number menggunakan format string

#Boolean
status = True
print(f"Hari ini Hujan : {status}")

#Number
angka1 = 20
angka2 = 5.5

print(f"Penjumlahan dari {angka1} + {angka2} = {angka1+angka2}")

#menambahkan jumlah angka dibelakang koma
print(f"Angka 2 = {angka2:.2f}")

#memberikan tanda koma pada number
print(f"Total Harga Bakso : Rp.{12000:,}")

#menampilkan landing zero (akan menambahkan angka 0 diawal number sebanyak yang ditentukan)
nis = 326726
print(f"{nama} nis anda adalah : {nis:09}")

#memformat persentase
print(f"Halo, {nama} nilai total pencapaian kamu adalah : {0.855:.1%}")
