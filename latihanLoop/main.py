#LATIHAN LOOPING

sisi = 11
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        print(" "*spasi,"*"*count)
        count += 1
        spasi -= 1
    
    else:
        count += 1
        continue
    
    if count > sisi:
        break

count = sisi - 2
spasi = 1

# Bagian bawah dari belah ketupat
while True:
    if count % 2:
        print(" " * spasi, "*" * count)
        count -= 1
        spasi += 1
    else:
        count -= 1
        continue
    
    if count <= 0:
        break