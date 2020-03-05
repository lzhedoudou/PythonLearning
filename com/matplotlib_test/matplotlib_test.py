# 用matplotlib进行可视化展示
from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,7,5,4,1,2,3,5]
x2 = [1,2,3,4,5,6,7,8,9,10]
y2 = [6,4,3,7,3,1,8,9,1,8] # 第二条线
plt.title("Date and Money!\nthis is a test",) # 定义标题 并且有一个副标题 换行
plt.legend() # 为不同的线条定义不同的颜色
plt.xlabel("Day") # 定义x轴标签
plt.ylabel("Money") # 定义y轴标签
plt.plot(x,y,label='test_a') # 画图,第一条线
plt.plot(x2,y2,label='test_b') # 画图，第二条线
plt.show() # 展示图形