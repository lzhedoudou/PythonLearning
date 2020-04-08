dict1 ={'name':'doudou','age':18}
print(dict1)
list1 = [1]
key_new = 'why'
new_list = dict(zip(key_new,list1))
dict1.update(new_list)
print(dict1)