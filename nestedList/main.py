# BELAJAR NESTED LIST (LIST BERSARANG)

#contoh penggunaan nested list
peserta_0 = ["Dimas",19,"Laki-laki"]
peserta_1 = ["Bayu",21,"Laki-laki"]
peserta_2 = ["Sekar",20,"Perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]
for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")
