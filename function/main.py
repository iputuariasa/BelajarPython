# FUNCTION ARGUMENT

# function sapa
def sapa(name):
    print(f"Hello {name}!")

sapa('Arik')

# function tambah
def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(23,54)
tambah(1,1)

# function cetak list peserta
def cetak(peserta):
    peserta = peserta.copy()
    for data in peserta:
        print(f"Data Peserta : {data}")

anggota = ['Bayu', 'Eka', 'Wahyu']
cetak(anggota)