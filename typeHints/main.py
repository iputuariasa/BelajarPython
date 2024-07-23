# TYPE HINTS DALAM FUNCTION
# digunakan untuk menginformasikan argument pada function itu inputnya type datanya apa agar mempermudah kita ketika bingung fungsi ini inputnya apa ketika program nya sudah besar

# (argument:int) -> int | maksudnya yaitu argument ini inputnya int dan return nya int
import string

def pangkat_sepuluh(argument:int) -> int:
    hasil = 10**argument
    return hasil

HASIL = pangkat_sepuluh(2)
print(HASIL)

# jika tidak memiliki return maka -> nilai nilainya None
def display(argument:string):
    print(argument)

display("Arik")