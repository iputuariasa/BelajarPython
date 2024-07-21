# LATIHAN DICTIONARY
import datetime
import os
import string
import random

#  Template Produk
product_template = {
    'name' : 'name',
    'price' : '0',
    'stock' : 0,
    'expired' : datetime.datetime(1111,11,1)
}

data_product = {}

while True:
    os.system("clear")
    print(f"{'SELAMAT DATANG':^60}")
    print(f"{'INPUT DATA PRODUK':^60}")
    print("-"*60)

    product = dict.fromkeys(product_template.keys())
    product['name'] = input('Masukkan Nama Produk : ')
    product['price'] = int(input('Masukkan Harga Produk : '))
    product['stock'] = int(input('Masukkan Stok Produk : '))
    EXPIRED_YEAR = int(input('Tahun Kadaluwarsa (YYYY): '))
    EXPIRED_MONTH = int(input('Bulan Kadaluwarsa (1-12): '))
    EXPIRED_DAY = int(input('Tanggal Kadaluwarsa (1-31): '))
    product['expired'] = datetime.datetime(EXPIRED_YEAR,EXPIRED_MONTH,EXPIRED_DAY)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_product.update({KEY:product})

    print("\n")
    print("-"*60)
    print(f"{'KEY':<7} {'NAMA':<13} {'HARGA':<15} {'KADALUWARSA':<12}")
    print("-"*60)

    for product in data_product:
        KEY = product
        NAME = data_product[KEY]['name']
        PRICE = data_product[KEY]['price']
        STOCK = data_product[KEY]['stock']
        EXPIRED = data_product[KEY]['expired'].strftime("%x")

        DISPLAY_PRICE = f"{PRICE:,}"
        print(f"{KEY:<7} {NAME:<13} Rp.{DISPLAY_PRICE:<15} {EXPIRED:<12}")
    
    is_done = input('\nApakah Ingin Input Lagi (y/n): ')
    if is_done == "n":
        break

print("\nProgram Selesai")