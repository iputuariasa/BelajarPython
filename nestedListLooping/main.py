# BELAJAR LOOPING NESTED LIST 7 ENUMERATE

numbers = [2,5,7,1,4,3]
print(f"Data Number : {numbers}")

# for loop
print("\nFOR LOOP")
for a in numbers:
    print(f"Angka : {a}")

# FOR LOOP AND RANGE
print("\nFOR LOOP AND RANGE")
panjang_data = len(numbers)

for i in range(panjang_data):
    print(f"Angka : {numbers[i]}")

# WHILE LOOP    
print("\nWHILE LOOP")
i = 0

while i < panjang_data:
    print(f"Angka : {numbers[i]}")
    i += 1

# LIST COMPREHENSION
print("\nLIST COMPREHENSION")
[print(f"Angka : {i}") for i in numbers]

# ENUMERATE
print("\nENUMERATE")
for index, data in enumerate(numbers):
    print(f"Index {index}, Angka : {data}")