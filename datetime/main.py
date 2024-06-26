# BELAJAR DATE AND TIME

import datetime as dt

print("APLIKASI MENGHITUNG UMUR".center(50,"="))

tanggal = int(input("Masukkan Tanggal Lahir\t : "))
bulan = int(input("Masukkan Bulan Lahir\t : "))
tahun = int(input("Masukkan Tahun Lahir\t : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal Lahir Anda\t : {tanggal_lahir}")

tanggal_sekarang = dt.date.today()
print(f"Tanggal Sekarang\t : {tanggal_sekarang}")

print("HASIL PENGHITUNGAN".center(50,"-"))
umur = tanggal_sekarang - tanggal_lahir     #untuk mencari selisih umur
umur_hari = umur.days                       #method untuk mengambil jumlah hari saja
umur_bulan = (umur_hari % 365) // 30        #rumus mencari bulan (umur hari dimodulus 365 hari hasilnya dibagi 30 hari)
umur_tahun = umur_hari // 365               #rumus mencari tahun
print(f"Anda Lahir Pada Hari\t : {tanggal_lahir:%A}") #untuk menampilkan hari (.%A)
print(f"Umur Anda Adalah\t : {umur_tahun} tahun, {umur_bulan} bulan")