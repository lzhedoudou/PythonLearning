# 读取csv列表
from matplotlib import pyplot as plt
import numpy as np

x,y = np.loadtxt("C:\\Users\\Dou\\Desktop\\Python\\plt_test_1.csv",
                 delimiter=',',unpack=True)
plt.plot(x,y,label = 'csv')
plt.xlabel("x")
plt.ylabel("y")
plt.title("this is from csv")
plt.legend()
plt.show()