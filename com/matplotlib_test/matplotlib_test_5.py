from matplotlib import pyplot as plt
import pandas as pd
# 从csv中读取世界人口增长图

rst1 = pd.read_csv("C:\\Users\\Dou\\Desktop\\Python\\person_number.csv")


# print(rst1)
China_filter = rst1.country == 'China' # 需要将单个国家数据筛选出来
China_data = rst1[China_filter]
print(China_data)
India_filter = rst1.country == 'India' # 需要将单个国家数据筛选出来
India_data = rst1[India_filter]
print(India_data)
USA_filter = rst1.country == 'USA' # 需要将单个国家数据筛选出来
USA_data = rst1[USA_filter]
print(USA_data)
plt.title("world people number")
plt.plot(China_data.year,China_data.number/10 ** 8,label = 'China') # 因为数值太大，在表中会以科学计数法显示，所以除以10的8次方
plt.plot(India_data.year,India_data.number/10 ** 8,label = 'India')
plt.plot(USA_data.year,USA_data.number/10 ** 8,label = 'USA')
plt.plot(China_data.year,China_data.number/China_data.number.iloc[0],label = 'China_increase')
plt.plot(India_data.year,India_data.number/India_data.number.iloc[0],label = 'India_increase')
plt.plot(USA_data.year,USA_data.number/USA_data.number.iloc[0],label = 'USA_increase')
plt.xlabel("year")
plt.ylabel("number")
plt.legend()
plt.show()

# 以上就是一个完整的画图
# 但是有的时候，有可能number数值本身比较低的情况下，虽然增长很快，但是从图里看起来很慢
# 所以以基数为1进行比较，就是以自己的第一条数据作为基准值进行比较增长幅度
# 也就是将number除以自己的第一个number

# 这样就能看出来 实际上印度的人口增长是最快的

