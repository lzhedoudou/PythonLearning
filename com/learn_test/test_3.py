#-*- coding : utf-8 -*-
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import csv
import pandas

url = 'https://baike.baidu.com/item/%E7%9C%81%E4%BC%9A/2089891?fr=aladdin'
headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36' }
response = requests.get(url,headers = headers)
response.encoding='utf-8'
soup = BeautifulSoup(response.text,'lxml')
# 使用css
rst = soup.select('td div a ') # 还是用css样式比较好 直接出来了
csv_path = 'C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\test.csv'
list_rst = []
list_rst_new = []
for a in rst:
    if len(a.string) > 1 and '/' not in a.string:
        list_rst.append(a.string)
# 这里再拆分一下列表
for i in range(0,len(list_rst),2):
#    print(i) # 输出的结果是 0 2 4 6 8。。。。。。
    list_rst_new.append(list_rst[i:i+2])


with open (csv_path,'w',newline='') as f: # 使用newline参数否则有多余换行
    writer = csv.writer(f)
    writer.writerow(['省份','省会'])
    writer.writerows(list_rst_new)
    f.close()
#print(list_rst_new)

df = pandas.read_csv(csv_path,encoding='gbk',index_col='sdf')
print(df)
    
    
    
    
    
    
    














    
    
