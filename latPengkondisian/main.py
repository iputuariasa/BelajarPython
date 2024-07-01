# LATIHAN PENGKONDISIAN 

print("KALKULATOR SEDERHANA".center(50,"="))

angka1 = float(input("Masukkan angka pertama : "))
angka2 = float(input("Masukkan angka kedua : "))
operator = str(input("Pilih operator (+,-,/,*) : \n"))
print("HASIL".center(50,"-"))

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil dari : {angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil dari : {angka1} - {angka2} = {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasil dari : {angka1} / {angka2} = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil dari : {angka1} * {angka2} = {hasil}")
else:
    print("Operator salah")