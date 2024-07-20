# COPY AND POP DICTIONARY

teman_teman = {
    "ari" : "I Putu Arik Arnawa",
    "yuyu" : "Arip Yuyun Yanti",
    "bye" : "Bayu Guna Artha",
    'bos' : "Bosip Ramadan"
}

# Copy
# dengan menggunakan copy ketika mengubah data tidak akan mengubah data lainnya seperti kita menggunakan
# friends = teman_teman
friends = teman_teman.copy()
teman_teman["ari"] = "Arik Ayuni"
print(f"Data teman_teman : {teman_teman}\n")
print(f"Data friends : {friends}\n")

#POP
# mengambil data dari dictionary data yang diambil akan hilang pada dictionary, menggunakan key
dataArik = friends.pop("ari")
print(f"Data ari : {dataArik}\n")
print(f"Data friends : {friends}\n") #data ari yang ada pada dict friend hilang

#POPITEM
# mengambil data terakhir dari dictionary data yang diambil akan hilang pada dictionary
dataTerakhir = friends.popitem()
print(f"Data terakhir : {dataTerakhir}\n")
print(f"Data friends : {friends}\n") #data terakhir yang ada pada dict friend hilang
