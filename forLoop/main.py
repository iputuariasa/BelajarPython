#BELAJAR PERULANGAN FOR LOOP

print("FOR LOOP".center(50,"="))

#menggunakan List
numbers_list = [0,5,3,4,7,8]

for i in numbers_list:
    print(f"Angka {i}")
print("Akhir program 1".center(50,"-")+"\n")

#menggunakan range
for i in range(1,10): #jika ingin mulai dari 0 cukup tuliskan angka yang di belakang saja (5)
    print(f"Angka {i}")
print("Akhir program 2".center(50,"-")+"\n")
