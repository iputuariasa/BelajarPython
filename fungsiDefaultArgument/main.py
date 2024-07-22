# FUNCTION DEFAULT ARGUMENT
# memberikan nilai default ketika argumen tidak diisi

#contoh 1
def sapa(nama = "Kamu"):
    print(f"Hello, {nama}!")

sapa()
sapa("Arik")

#contoh 2
def hitung_pangkat(angka = 2, pangkat = 3):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,2))
hasil = hitung_pangkat(pangkat=5, angka=3)
print(hasil)

#contoh 3
def input_angka(angka1 = 1, angka2 = 2, angka3 = 3, angka4 = 4):
    hasil = angka1+angka2+angka3+angka4
    return hasil

hasil = input_angka()
print(hasil)
hasil = input_angka(angka3=8)
print(hasil)