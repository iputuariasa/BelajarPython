# LATIHAN APLIKASI KONVERSI SUHU

# CELSIUS
# print("============CELCIUS============")
# celsius = float(input("Masukkan Angka : "))

# print("Suhu Celsius : ", celsius, "C")

# # REAMUR
# reamur = (4/5)*celsius
# print("Suhu Celsius dalam Reamur: ", reamur, "R")

# # FAHRENHEIT
# fahrenheit = ((9/5)*celsius)+32
# print("Suhu Celsius dalam Fahrenheit: ", fahrenheit, "F")

# # KELVIN
# kelvin = celsius + 273
# print("Suhu Celsius dalam Kelvin: ", kelvin, "K")

# print("============REAMUR============")
# reamur = float(input("Masukkan Nilai : "))
# print("Suhu Reamur : ", reamur, "R")

# # CELSIUS
# celsius = (5/4)*reamur
# print("Suhu Reamur dalam Celsius: ", celsius, "C")

# # FAHRENHEIT
# fahrenheit = ((9/4)*reamur)+32
# print("Suhu Reamur dalam Fahrenheit: ", fahrenheit, "F")

# # KELVIN
# kelvin = ((5/4)*reamur)+273
# print("Suhu Reamur dalam Kelvin: ", kelvin, "K")

# #FAHRENHEIT
# print("============FAHRENHEIT============")
# fahrenheit = float(input("Masukkan Nilai : "))
# print("Suhu Fahrenheit : ", fahrenheit, "F")

# # CELSIUS
# celsius = 5/9*(fahrenheit-32)
# print("Suhu Fahrenheit dalam Celsius: ", celsius, "C")

# # REAMUR
# reamur = 4/9*(fahrenheit-32)
# print("Suhu Fahrenheit dalam Reamur: ", reamur, "R")

# # KELVIN
# kelvin = (5/9*(fahrenheit-32))+273
# print("Suhu Fahrenheit dalam Kelvin: ", kelvin, "K")

print("============KELVIN============")
kelvin = float(input("Masukkan Nilai : "))
print("Suhu Kelvin : ", kelvin, "K")

# CELSIUS
celsius = kelvin - 273
print("Suhu Kelvin dalam Celsius: ", celsius, "C")

# REAMUR
reamur = 4/5*(kelvin-273)
print("Suhu Kelvin dalam Reamur: ", reamur, "R")

# FAHRENHEIT
fahrenheit = (9/5*(kelvin-273))+32
print("Suhu Kelvin dalam Fahrenheit: ", fahrenheit, "F")
