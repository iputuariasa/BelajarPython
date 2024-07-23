# *args dalam function
# untuk memungkinkan sebuah fungsi menerima sejumlah argumen yang tidak ditentukan jumlahnya.
'''
    Kapan Menggunakan *args?
    - Ketika kita tidak tahu berapa banyak argumen yang akan diberikan kepada fungsi.
    - Saat ingin membuat fungsi yang fleksibel dan dapat menerima berbagai jumlah argumen.
'''
def tambah(*args):
    output = 0
    for i in args:
        output += i
    return output

HASIL = tambah(1,2,3,4)
print(f"Hasil = {HASIL}")

def cetak_semua(*data):
    for name in data:
        print(name)

cetak_semua("Jeruk", "Apel", "Pisang", "Mangga", "Anggur")