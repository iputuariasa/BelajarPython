# LOOPING DICTIONARY

friends = {
    "ari" : "I Putu Arik Arnawa",
    "yuyu" : "Arip Yuyun Yanti",
    "bye" : "Bayu Guna Artha",
    'bos' : "Bosip Ramadan"
}

# Looping biasa
for friend in friends:
    print(friend)   # ini akan menampilkan key nya saja

# Looping keys
friend = friends.keys() # mengambil key nya saja dimasukkan ke variabel friend
print(f"\n{friend}")

for key in friends.keys():
    print(f"Key : {key}") # ini akan menampilkan key nya saja

# Looping Value
friend = friends.values()
print(f"\n{friend}")    # mengambil value dictionary dimasukkan ke variabel friend

for value in friends.values():
    print(f"Value : {value}")   # ini akan menampilkan value dari dictionary

# Looping Items
friend = friends.items()
print(f"\n{friend}")    # ini akan mengambil berpasangan key dan value dalam bentuk tuple

for item in friends.items():
    print(f"Item : {item}") #ini akan menampilkan key dan value dalam bentuk tuple

for key,value in friends.items():
    print(f"Key : {key}, Value : {value}")  # bisa saja seperti ini untuk menampilkan data keduanya (key & value)