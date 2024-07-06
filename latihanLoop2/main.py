#BELAJAR LATIHAN LOOPING 2

sisi = 9
count = 1
spasi = int(sisi/2)
spasi2 = sisi

while True:
    if count % 2:
        print(" "*spasi,"*"*count,"-"*spasi2,"*"*count)
        count += 1
        spasi -= 1
        spasi2 -= 1
    
    else:
        count += 1
        spasi2 -= 1
        continue

    if count > sisi:
        break

#reset
count = count-2
spasi = 1
spasi2 = 2

while True:
    if count % 2:
        print(" "*spasi,"*"*count,"-"*spasi2,"*"*count)
        count -= 1
        spasi += 1
        spasi2 += 1
    
    else:
        count -= 1
        spasi2 += 1
        continue

    if count == 0:
        break