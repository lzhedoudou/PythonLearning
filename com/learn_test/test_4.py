# 项目： 生成随机的测验试卷文件
import random
import pandas
import csv

# 读取爬取的省份和省会信息
csv_path = 'C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\test.csv'
with open(csv_path,'r') as f:
    rst = csv.reader(f)
    next(rst) # 这个是用来不要第一行的
    dict_new = {}
    for i in rst:
        dict_new[i[0]]=i[1]
    print(dict_new)
    f.close()
# 以上内容已创建出来了一个字典
    
