import string
list1 = [i for i in range(10)]
list2 = ['this','is','a','test','ha','la']
print(list1)
del(list1[2])
print(list1)
list2.remove('ha')
print(list2)

str1 = 'this is my test and i want to be an xxx'
list3 = str1.split()
print(list3)

list3.extend(list1)
print(list3)
print(list3.index('and'))

print((44,))

print('how are {}'.format('you'))

print(string.digits)
print(string.ascii_letters)

print('hahah'.center(25))

# translate

table1 = str.maketrans('ha','no')
table2 = str.maketrans('cry','lau')
text1 = 'this is my test haha  and no one want to cry'
rst = text1.translate(table1)
print(rst)

text2 = 'this is my test haha  and no one want to cry'
print(text2.replace('test','test1'))

list4 = [0,1]
for i in range(10):
    list4.append(list4[-1] + list4[-2])
    
print(list4)
    
    
    
    
    
    
    
    
    
    
    
    
    