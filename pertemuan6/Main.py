# CASTING TIPE DATA
    # MENGUBAH DARI TIPE DATA SATU KE TIPE DATA LAINNYA

# INTEGER
print("==========INTEGER==========")
data_int = 10
print("Data Integer: ", data_int, " bertipe : ", type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int)
print("Data Float : ", data_float, " bertipe : ", type(data_float))
print("Data String : ", data_string, " bertipe : ", type(data_string))
print("Data Boolean: ", data_bool, " bertipe : ", type(data_bool))

# FLOAT
print("==========FLOAT==========")
data_float = 7.8
print("Data Float: ", data_float, " bertipe : ", type(data_float))

data_int = int(data_float) # Akan dibulatkan ke bawah
data_string = str(data_float)
data_bool = bool(data_float) # Selain nilainya 0 bernilai True
print("Data Integer : ", data_int, " bertipe : ", type(data_int))
print("Data String : ", data_string, " bertipe : ", type(data_string))
print("Data Boolean: ", data_bool, " bertipe : ", type(data_bool))

# BOOLEAN
print("==========BOOLEAN==========")
data_bool = False
print("Data Boolean: ", data_bool, " bertipe : ", type(data_bool))

data_int = int(data_bool) # Bernilai 1 jika True, bernilai 0 jika False
data_string = str(data_bool)
data_float = float(data_bool) # Bernilai 1.0 jika True, bernilai 0.0 jika False
print("Data Integer : ", data_int, " bertipe : ", type(data_int))
print("Data String : ", data_string, " bertipe : ", type(data_string))
print("Data Float: ", data_float, " bertipe : ", type(data_float))

# STRING
print("==========STRING==========")
data_str = ""
print("Data String: ", data_str, " bertipe : ", type(data_str))

data_int = int(data_str) # nilai str harus angka misalkan "10"
data_bool = bool(data_str) # bernilai False jika str kosong
data_float = float(data_str) # nilai str harus angka misalkan "10"
print("Data Integer : ", data_int, " bertipe : ", type(data_int))
print("Data Boolean : ", data_bool, " bertipe : ", type(data_bool))
print("Data Float: ", data_float, " bertipe : ", type(data_float))