# 构造函数
class my_test_8(list):
    
    def __init__(self):
        print('这就是构造函数')
        
    
    def my_yield(self):
        list_1 = [[1,2,3],[4,5,6],[7,8,9]]
        for i in list_1:
            print(i)
    def my_yield_1(self,list_x):
        for a in list_x:
            for b in a:
                yield b
    
            
            
            
        

rst = my_test_8()
rst.my_yield()

list_2 = [[1,2,3],[4,5,6],[7,8,9]]

def for_yield(list_x):
    for i in rst.my_yield_1(list_x):
        print(i)
        
for_yield(list_2)

print(list(rst.my_yield_1(list_2)))

