#OPERASI KOMPARASI
    # Untuk membandingkan nilai, setiap hasil komperasi menghasilkan nilai boolean

# OPERASI KOMPARASI : >, <, >=, <=, ==, !=, is, is not

# Operator komparasi lebih besar dari 
print('=====Lebih Besar Dari (>)=====')
a = 5
b = 6
hasil = a > 7
print('a > 7 = ', hasil)
hasil = a > 3
print('a > 3 = ', hasil)
hasil = a > 5
print('a > 5 = ', hasil)

print('=====Kurang Dari (<)=====')
hasil = a < 7
print('a < 7 = ', hasil)
hasil = a < 3
print('a < 3 = ', hasil)
hasil = a < 5
print('a < 5 = ', hasil)

print('=====Lebih Besar Sama Dengan (>=)=====')
hasil = a >= 7
print('a >= 7 = ', hasil)
hasil = a >= 3
print('a >= 3 = ', hasil)
hasil = a >= 5
print('a >= 5 = ', hasil)

print('=====Kurang Dari Sama Dengan (<=)=====')
hasil = a <= 7
print('a <= 7 = ', hasil)
hasil = a <= 3
print('a <= 3 = ', hasil)
hasil = a <= 5
print('a <= 5 = ', hasil)

print('===== Sama Dengan (==)=====')
hasil = a == 5
print('a == 5 = ', hasil)
hasil = a == 6
print('a == 6 = ', hasil)

print('===== Tidak Sama Dengan (!=)=====')
hasil = a != 5
print('a != 5 = ', hasil)
hasil = a != 6
print('a != 6 = ', hasil)

# Komparasi Object Identity
    # membandingkan nilai id atau object
print('===== Sama (is)=====')
x = 2
y = 3
hasil = x is y
print('Nilai x = ', x, ' id = ', hex(id(x)))
print('Nilai y = ', y, ' id = ', hex(id(y)))
print('Hasil x is y = ', hasil)

print('===== Tidak Sama (is not)=====')
x = 2
y = 3
hasil = x is not y
print('Nilai x = ', x, ' id = ', hex(id(x)))
print('Nilai y = ', y, ' id = ', hex(id(y)))
print('Hasil x is not y = ', hasil)