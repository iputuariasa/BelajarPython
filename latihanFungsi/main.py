# LATIHAN FUNCTION
# MENGHITUNG LUAS & KELILING PERSEGI PANJANG
import os

def header():
    os.system("clear")
    print(f"{'PROGRAM MENGHITUNG LUAS':^50}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^50}")
    print("-"*50)

def input_user():
    panjang = float(input("Masukkan Nilai Panjang : "))
    lebar = float(input("Masukkan Nilai Lebar : "))
    return panjang,lebar

def hitung_luas(panjang, lebar):
    return panjang*lebar

def hitung_keliling(panjang, lebar):
    return 2*(panjang+lebar)

def display(mesage, value):
    print(f"Hasil Perhitungan {mesage} = {value}")

while True:
    header()
    PANJANG,LEBAR = input_user()
    menu = int(input("Pilih untuk menghitung 1. Luas | 2. Keliling (1/2) : "))
    if menu == 1:
        LUAS = hitung_luas(PANJANG,LEBAR)
        display("Luas", LUAS)
    elif menu == 2:
        KELILING = hitung_keliling(PANJANG,LEBAR)
        display("Keliling", KELILING)
    else:
        print("Menu Tidak Tersedia")

    is_go = input ("\nApakah Ingin Hitung Lagi (y/n) : ")
    if is_go == "n":
        break

print("Program Selesai")