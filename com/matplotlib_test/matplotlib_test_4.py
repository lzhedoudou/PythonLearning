# 自建数据画图
from matplotlib import pyplot as plt
import pandas as pd # 处理数据

# x = [1,2,3,4,5,6,7,8,9]
# y = [2,5,4,2,7,8,4,1,6] # 第一组数据
# z = [7,5,3,2,5,7,8,9,2] # 第二组数据
# o = [3,4,6,1,5,2,4,5,7] # 第三组数据
# plt.plot(x,y,label = 'x and y')
# plt.plot(x,z,label = 'x and z')
# plt.plot(x,o,label = 'x and o')
# plt.title("this is duibi")
# plt.legend()
# plt.show()

# 读取外部数据-csv
rst1 = pd.read_csv("C:\\Users\\Dou\\Desktop\\Python\\plt_test_1.csv")
print(type(rst1)) # 数据类型DataFrame
print(rst1)
print('------',rst1.col_2.iloc[9],rst1.col_3.iloc[9],'------')
plt.xlabel("col_2",color = 'red')
plt.ylabel("col_3")
plt.plot(rst1.col_2,rst1.col_3)
plt.legend()
plt.show()
