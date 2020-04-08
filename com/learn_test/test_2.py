# 编写一个名为 collatz()的函数，它有一个名为 number 的参数。如果参数是偶数，
# 那么 collatz()就打印出 number // 2， 并返回该值。如果 number 是奇数， collatz()就打
# 印并返回 3 * number + 1

# 然后编写一个程序， 让用户输入一个整数， 并不断对这个数调用 collatz()， 直
# 到函数返回值１（令人惊奇的是， 这个序列对于任何整数都有效， 利用这个序列，
# 你迟早会得到 1！ 既使数学家也不能确定为什么。 你的程序在研究所谓的“Collatz
# 序列”，它有时候被称为“最简单的、 不可能的数学问题”）。

def collatz(number):
    if number % 2 == 0:
        rst = number // 2
        print(rst)
    else:
        rst = 3 * number + 1
        print(rst)
    return rst



def input_num():
    try:
        num = int(input("请输入一个整数！"))
        while True:
            num = collatz(num) # 给num重新赋值！
            if num == 1:
                break
    except ValueError:
        print("需要输入的是一个整数！")
#input_num()



# 编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所
# 有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。例如，将
# 前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。但你的函数应
# 该能够处理传递给它的任何列表。



def str_list(list_1):
    list_1[-1] = 'and ' + list_1[-1]
    return str(spam).replace("'","").replace("[","").replace("]","")
spam = ['apples', 'bananas', 'tofu', 'cats','body','haha']
#print(str_list(spam))

#假定有一个列表的列表， 内层列表的每个值都是包含一个字符的字符串， 像这样：
#grid = [['.', '.', '.', '.', '.', '.'],
#       ['.', 'O', 'O', '.', '.', '.'],
#       ['O', 'O', 'O', 'O', '.', '.'],
#       ['O', 'O', 'O', 'O', 'O', '.'],
#       ['.', 'O', 'O', 'O', 'O', 'O'],
#       ['O', 'O', 'O', 'O', 'O', '.'],
#       ['O', 'O', 'O', 'O', '.', '.'],
#       ['.', 'O', 'O', '.', '.', '.'],
#       ['.', '.', '.', '.', '.', '.']]
#你可以认为 grid[x][y]是一幅“图” 在 x、 y 坐标处的字符， 该图由文本字符组
#成。 原点(0, 0)在左上角， 向右 x 坐标增加， 向下 y 坐标增加。
#复制前面的网格值， 编写代码用它打印出图像

def zifu_wangtu(list_1):
    for i in range(len(list_1[0])):
        for a in grid:
            for b in a[i]:
                print(b,end='')
        print("")
        
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
#zifu_wangtu(grid)

# 你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字
# 典。其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物
# 品。例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}意味着玩
# 家有 1 条绳索、 6 个火把、 42 枚金币等。

dict1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(dictx):
    print("Inventory:")
    Total_number_of_items = 0
    for a,b in dictx.items():
        print(a,b)
        Total_number_of_items += b
    print("Total number of items: {}".format(Total_number_of_items))
#displayInventory(dict1)
    
# 写一个名为 addToInventory(inventory, addedItems)的函数， 其中 inventory 参数
# 是一个字典， 表示玩家的物品清单（像前面项目一样）， addedItems 参数是一个列表，
# 就像 dragonLoot。
# addToInventory()函数应该返回一个字典， 表示更新过的物品清单。请注意， 列
# 表可以包含多个同样的项。你的代码看起来可能像这样：

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','元宝','元宝']
def addToInventory(inventory, addedItems):
    for a in dragonLoot:
        rst = inventory.get(a)
        if rst != None:
            inventory[a] += 1
        else:
            inventory.setdefault(a,1)
    print(inventory)

#addToInventory(inv,dragonLoot)
    
# 编写一个名为 printTable()的函数， 它接受字符串的列表的列表，将它显示在组
# 织良好的表格中， 每列右对齐。假定所有内层列表都包含同样数目的字符串。例如，
# 该值可能看起来像这样：
    
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
    


        


    

  


























    

