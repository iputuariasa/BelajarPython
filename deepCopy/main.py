# BELAJAR DEEP COPY

# nested list ketika ingin menduplikat tidak bida menggunakan .copy seperti biasanya harus menggunakan deepcopy agar id address list di dalam list nya ikut terganti tidak sama lagi, ketika menggunakan .copy biasanya hanya akan mengganti id address list paling luar saja list yang di dalamnya tidak terganti id address nya

data_0 = [1,2]
data_1 = [3,4]

data = [data_0,data_1]
print(f"Data = {data}")

#ketika menggunakan .copy()
data_copy = data.copy()
print(f"Id Address data asli = {hex(id(data))}")
print(f"Id Address data copy = {hex(id(data_copy))}")
print("data pertama")
print(f"Id Address data asli = {hex(id(data[0]))}")         #id address nya sama
print(f"Id Address data copy = {hex(id(data_copy[0]))}\n")    #id address nya sama

# ketika id address sama ketika melakukan perubahan data akan mempengaruhi yang lainnya
# maka dari itu harus menggunakan deepcopy untuk mengganti id address sampai masuk ke dalam list

from copy import deepcopy
data_deepcopy = deepcopy(data)
print(f"Id Address data asli = {hex(id(data))}")
print(f"Id Address data copy = {hex(id(data_copy))}")
print(f"Id Address data deepcopy = {hex(id(data_deepcopy))}")

print("data pertama")
print(f"Id Address data asli = {hex(id(data[0]))}")         #id address nya sama
print(f"Id Address data copy = {hex(id(data_copy[0]))}")    #id address nya sama
print(f"Id Address data deepcopy = {hex(id(data_deepcopy[0]))}") # id assress nya berubah

data_deepcopy[0][0] = 30
print(f"Data = {data}")
print(f"Data copy = {data_copy}")
print(f"Data deepcopy = {data_deepcopy}")