# TIPE DATA

# Tipe Data Basic
# integer
data_integer = 11
print("Data : ", data_integer)
print("-Bertipe : ", type(data_integer))

# float
data_float = 26.6
print("Data : ", data_float)
print("-Bertipe : ", type(data_float))

# string
data_string = "Yanto"
print("Data : ", data_string)
print("-Bertipe : ", type(data_string))

# boolean
data_bool = True
print("Data : ", data_bool)
print("-Bertipe : ", type(data_bool))

# Tipe Data Khusus
# bilangan kompleks
data_complex = complex(5,6)
print("Data : ", data_complex)
print("-Bertipe : ", type(data_complex))

# tipe data bahasa C
# import dahulu dari C
from ctypes import c_double, c_char
data_double = c_double(26.87)
print("Data : ", data_double)
print("-Bertype : ", type(data_double))