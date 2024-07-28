immutable_var = 1, 2, 'zdes', 'svet'
print(immutable_var)
#immutable_var [2] = 'éroor'
#Кортеж создан не изменяемым это отличает его от списка. При этом он занимает меньше места и
# в нём можно хранить информацию, которую мы не хотим менять.
mutable_list = ([1, 2, 3, "chernika", "öleg" ])
mutable_list [3] = "klubnika"
print(mutable_list)