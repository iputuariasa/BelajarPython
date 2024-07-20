# MULTI KEY & NESTING DICTIONARY

import datetime

mahasiswa1 = {
    'nama' : 'I Putu Arik Arnawa',
    'nim' : '190030278',
    'sks' : 134,
    'beasiswa' : True,
    'masuk' : datetime.datetime(2019,4,29)
}

mahasiswa2 = {
    'nama' : 'Ni Kadek Sekar Jagat',
    'nim' : '190038732',
    'sks' : 100,
    'beasiswa' : False,
    'masuk' : datetime.datetime(2019,3,12)
}

mahasiswa3 = {
    'nama' : 'Tony Kurniawan',
    'nim' : '190041427',
    'sks' : 144,
    'beasiswa' : False,
    'masuk' : datetime.datetime(2019,5,30)
}

data_mahasiswa = {
    'MHS278' : mahasiswa1,
    'MHS732' : mahasiswa2,
    'MHS427' : mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<20} {'NIM':<9} {'SKS':<3} {'BEASISWA':<9} {'MASUK':<10}")
print('-'*60)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    MASUK = data_mahasiswa[KEY]['masuk'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<20} {NIM:<9} {SKS:<3} {BEASISWA:^9} {MASUK:<10}")