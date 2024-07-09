# LATIHAN LIST

# INPUT DATABASE PRODUK SEDERHANA
print("UD. TOKO SERBAADA".center(55,"="),"\n")
print("Input Produk")
list_produk = []
while True:
    print("".center(55,"-"))
    nama_produk = str(input("Nama Produk : "))
    stok_produk = int(input("Stok Produk : "))

    produk_baru = [nama_produk,stok_produk]
    list_produk.append(produk_baru)

    status = input("\nInput Produk Lagi ?(y/n) : ")
    if status == "y":
        continue
    elif status == "n":
        break
    else:
        print("Perintah salah!\n")
        break
print("\n")
print("DATABASE PRODUK".center(55,"="))
print("No\t| Nama Produk \t\t| Stok")
print("".center(55,"-"))
for index, data in enumerate(list_produk):
    print(f"{index+1}\t| {data[0]}\t\t| {data[1]}")

print("\nPROGRAM SELESAI")