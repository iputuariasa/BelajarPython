# LATIHAN DICTIONARY

import datetime
import os

# template mahasiswa
template_mahasiswa = {
    'nama' : 'nama',
    'nim' : '000000000',
    'sks_lulus' : 0,
    'lahir' :  datetime.datetime(1111,11,1)
}

data_mahasiswa = {}


while True:
    os.system("clear")

    print(f"{'SELAMAT DATANG MAHASISWA BARU':^60}")
    print(f"{'INPUT DATA MAHASISWA':^60}")
    print("-"*60)

    mahasiswa = dict.fromkeys(template_mahasiswa.keys())
    mahasiswa['nama'] = input("Masukkan Nama Mahasiswa : ")
    mahasiswa['nim'] = input("Masukkan NIM Mahasiswa : ")
    mahasiswa['sks_lulus'] = int(input("Masukkan SKS Lulus : "))
    TAHUN_LAHIR = int(input("Masukkan Tahun Lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Masukkan Bulan Lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Masukkan Tanggal Lahir (1-31) : "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    len_mahasiswa = len(data_mahasiswa)+1
    data_mahasiswa.update({'MHS'+str(len_mahasiswa).zfill(3):mahasiswa})
    print("\n")
    print("-"*60)
    print(f"{'KEY':<6} {'NAMA':<15} {'NIM':<9} {'SKS LULUS':<12} {'LAHIR':<10}")
    print("-"*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS_LULUS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<15} {NIM:<9} {SKS_LULUS:^12} {LAHIR:<10}")
    
    is_done = input("\nIngin Input Lagi (y/n): ")
    if is_done == "n":
        break

print("\nProgram Selesai")