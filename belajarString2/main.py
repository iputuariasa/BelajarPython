# Belajar string method

print("BELAJAR STRING METHOD".center(60,"="))

kalimat = "DAUN pun BERGUGURAN"
numberStr = "1674876"
listStr = ["ari", "nata", "beje", "sutejo"]

print("Kalimat Normal : " + kalimat)
print("Method UPPER : " + kalimat.upper()) #membuat kalimat kapital
print("Method LOWER : " + kalimat.lower()) #membuat kalimat huruf kecil
print("Methot TITLE : " + kalimat.title()) #membuat kalimat hutuf kapital di awal kata
print("Method Capitalize : " + kalimat.capitalize()) #membuat kalimat huruf kapital di awal kalimat
print("Method lstrip : " + kalimat.lstrip()) #menghapus space di sebalah kiri
print("Method rstrip : " + kalimat.rstrip()) #menghapus spece di sebelah kanan
print("Method Center : " + kalimat.center(50,"-")) #membuat kalimat di posisi tengah
print("Method ljust : " + kalimat.ljust(50,"-")) #membuat kalimat rata kiri
print("Method rjust : " + kalimat.rjust(50,"-")) #membuat kalimat rata kanan
print("Method Replace : " + kalimat.replace("BERGUGURAN", "TUMBUH")) #menggantikan kalimat yang lama dengan yang baru
print("Method Count : " + str(kalimat.count("DAUN"))) # menghitung berapa banyak kata/kalimat "DAUN" di dalam kalimat
print("Method andswith : " + str(kalimat.endswith("BERGUGURAN"))) #mengecek ada tidak kata "BERGUGURAN" di akhir kalimat (True/False)
print("Method find : " + str(kalimat.find("pun"))) # mencari posisi string di mulai dari index ke-0
print("Method zfill : " + numberStr.zfill(9)) #menambahkan 0 pada sebelah kiri berdasarkan jumlah lebar yang ditentukan
print('Method join : ' + ", ".join(listStr)) #menggabungkan string dari list dan memisahkannnya dengan tanda koma ","
print('Method split : ' + str(kalimat.split())) #memisahkan string yang hasilnya berupa list