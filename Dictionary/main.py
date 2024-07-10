# Pengenalan Dictionary

# list -> array, mengakses dengan menggunakan index
# dictionary (dict) -> associative array, mengakses menggunakan identifier atau key

data_list = ['Bobon', 'Bambang', 'Wayu']
print(data_list[1])

data_dict = {
    'nama1' : 'Bobon',
    'nama2' : 'Bambang',
    'nama3' : 'Wayu',
    'number' : 100,
    'status' : True,
    'list' : data_list
}

print(data_dict['nama1'])
print(data_dict['number'])
print(data_dict['status'])
print(data_dict['list'])