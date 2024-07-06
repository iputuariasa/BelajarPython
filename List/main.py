#BELAJAR LIST

#list => kumpulan data (numbers, strings, boolean)

#list numbers
list_number = [1,4,2,5,6,7]
print(list_number)

#list string
list_string = ["Andi","Bayu","Putra","Artadi"]
print(list_string)

#list boolean
list_boolean = [True, False, False, True]
print(list_boolean)

#list campuran
list_campuran = ["Totong", 5, True]
print(list_campuran)

#list alternatif dengan range
list_range = range(0,10,2) #range(start, stop, step)
print(list(list_range))

#list dengan for
list_for = list(i**2 for i in range(0,10))
print(list_for)

#list dengan for if
list_for_if = list(i for i in range(0,10) if i != 5)
print(list_for_if)

#list for if mancari bilanganb ganjil
list_for_if_ganjil = list(i for i in range(0,10) if i % 2 != 0)
print(list_for_if_ganjil)

#list for if mancari bilanganb genap
list_for_if_ganjil = list(i for i in range(0,10) if i % 2 == 0)
print(list_for_if_ganjil)