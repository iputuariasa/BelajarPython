#BELAJAR IF DAN ELSE

# 1. IF INLINE
# belajar = str(input("Apakah kamu belajar hari ini(yes/no) ? : "))
# if belajar=="yes" : print("Wahh Kamu Rajin Banget!!")
# print("Program Berakhir Terimakasih")

# 2. IF INDENTATION
# belajar = str(input("Apakah kamu belajar hari ini(yes/no) : "))
# if belajar=="yes":
#     print("Wahh Kamu Rajin Banget!")
#     print("Semoga Kamu Jadi Orang Sukses Kedepannya!")
# print("Akhir Program Terimakasih")

# 3. ELSE STATEMENT
# belajar = str(input("Apakah kamu belajar hari ini(yes/no) : "))
# if belajar=="yes":
#     print("Wahh Kamu Rajin Banget!")
# else:
#     print("Wah Kamu Jangan Malas Belajar!")
# print("Akhir Program Terimakasih")

# 4. Elif
print("CEK JADWAL".center(50,"="))

hari = str(input("Masukkan Hari : "))
if hari=="senin":
    print(f"""Mata Kuliah Kamu :
          1. Komputer Jaringan
          2. Bahasa Inggris I""")
elif hari=="rabu":
    print(f"""Mata Kuliah Kamu :
          1. Pendidikan Agama
          2. Pemrograman Web""")
elif hari=="jumat":
    print(f"""Mata Kuliah Kamu :
          1. Olahraga
          2. Kalkulus""")
else:
    print("Tidak ada matakuliah hari ini!")
print("Program Selesai")