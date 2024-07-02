# BELAJAR PASS, CONTINUE, BREAK

#PASS
print("PASS".center(50,"-"))
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass    # tidak akan dieksekusi dijalankan hanya dummy
    print(angka)
print("Akhir Program \n")

#CONTINUE
print("CONTINUE".center(50,"-"))

angka = 0
print(f"Angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}")
    if angka == 3:
        print("nice")
        continue # akan membuat loop loncat ke step selanjutnya yaitu ke while perintah dibawahnya tidak akan di eksekusi
    print("Whatsapp")
print("Akhir Program\n")

#BREAK
print("BREAK".center(50,"-"))

angka = 0
while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}")

    if angka == 3:
        print("nice")
        break   #akan langsung mengakhiri loop
    print("whatsapp")
print("Akhir program\n")

angka = 0
angka_count = int(input("Masukkan angka : "))

while True:
    angka += 1
    print(f"Count angka -> {angka}")

    if angka == angka_count:
        break
print("Akhir Program\n")