#Belajar String Width Alignment

nama = "I Putu Ariasa"
makanan = "Bakso Ayam"
satuan = 1
harga = 17000

#string standar
print("STRING STANDAR".center(60,"="))

print(f"Halo, {nama} berikut daftar belanja kamu \nMakanan : {makanan}\nJumlah Porsi : {satuan}\nTotal Harga : {harga}\n\nTerimakasih\n\n")

#string kutip 3
print("STRING KUTIP TIGA".center(60,"="))
print(f"""Halo, {nama} berikut ini daftar belanja kamu
Makanan         : {makanan}
Jumlah Porsi    : {satuan} porsi
Total Harga     : Rp.{harga:,}

Terimakasih
""")