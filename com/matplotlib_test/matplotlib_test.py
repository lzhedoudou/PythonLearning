# 用matplotlib进行可视化展示-折线图
from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,7,5,4,1,2,3,5]
x2 = [1,2,3,4,5,6,7,8,9,10]
y2 = [6,4,3,7,3,1,8,9,1,8] # 第二条线
plt.title("Date and Money!\nthis is a test",) # 定义标题 并且有一个副标题 换行
# plt.legend() # 为不同的线条定义不同的颜色
plt.xlabel("Day") # 定义x轴标签
plt.ylabel("Money") # 定义y轴标签
plt.plot(x,y,label='test1111') # 画图,第一条线
plt.plot(x2,y2,label='test2222') # 画图，第二条线
plt.show() # 展示图形

# 柱状图
x11= ['name_a','name_b','name_c'] # x轴
y11 = [1,2,3] # y轴
x22= ['name_aa','name_bb','name_cc'] # x轴
y22 = [4,5,6] # y轴
plt.bar(x11,y11,label='test111',color='black') # 可以定义颜色
plt.bar(x22,y22,label='test111',color='c')
plt.xlabel("company") # 定义x轴名称
plt.ylabel("money")
plt.title("分公司盈利")
plt.legend() # 为不同的线条定义不同的颜色
plt.show() # 展示图形