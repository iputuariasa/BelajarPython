# ** kwargs
#  untuk memungkinkan sebuah fungsi menerima sejumlah argumen kata kunci (keyword arguments) yang tidak ditentukan jumlahnya.

# **kwargs akan menangkap semua argumen kata kunci tambahan yang dikirimkan ke fungsi tersebut dalam bentuk dictionary.

def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"Halo saya {nama} tinggi {tinggi} dan berat {berat}")

fungsi(nama="Arik", tinggi=173, berat=61)

def math(*args,**kwargs):
    output = 0
    if kwargs['operator'] == "tambah":
        for angka in args:
            output += angka
    
    elif kwargs['operator'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
    
    else:
        print("Operator tidak ada !")

    return output

HASIL = math(1,2,3,4,operator="tambah")
print(f"Hasil Tambah = {HASIL}")

HASIL = math(1,2,3,4,operator="kali")
print(f"Hasil Kali = {HASIL}")