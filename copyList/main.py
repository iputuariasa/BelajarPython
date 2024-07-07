# BELAJAR COPY LIST

a = ["Bima", "Guna", "Sakti"]
b = a

# dengan ini tidak akan mengcopy list
print(f"a = {a}")
print(f"b = {b}")

# ubah data b
b[1] = "Yudha"      # ini akan mengubah a dan b karena id address nya sama
print(f"a = {a}")
print(f"b = {b}")

# Cek id address
print("a = "+hex(id(a)))
print("b = "+hex(id(b)))

# Cara mengcopy data agar id address nya beda yaitu dengan .copy()
c = b.copy()        # akan mengubah id address nya

print("a = "+hex(id(a)))
print("b = "+hex(id(b)))
print("c = "+hex(id(c)))

c[1] = "Dinda"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")