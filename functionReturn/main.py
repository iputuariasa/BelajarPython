# FUNCTION DENGAN RETURN

# function kuadrat
def kuadrat(x):
    hasil = x**2
    return hasil

hasil_kuadrat = kuadrat(5)
print(hasil_kuadrat)

# function tambah
def fungsi_tambah(angka_1,angka_2):
    return angka_1 + angka_2

hasil_tambah = fungsi_tambah(10,12)
print(hasil_tambah)

# function banyak return
def operasi_aritmatika(angka1,angka2):
    tambah = angka1+angka2
    kurang = angka1-angka2
    kali = angka1*angka2
    bagi = angka1/angka2
    return tambah,kurang,kali,bagi

ta,ku,ka,ba = operasi_aritmatika(9,3)
print(f"Hasil Tambah = {ta}")
print(f"Hasil Kurang = {ku}")
print(f"Hasil Kali = {ka}")
print(f"Hasil Bagi = {ba}")