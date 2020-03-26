# 使用requests
import requests
import re
import time

def get_url_test(url):
    rst = requests.get(url)
#    print(rst) # 返回状态码
#    print(rst.status_code)
#    print(rst.cookies)
#    print(rst.text.encode('utf-8'))
    print(rst.text)

#get_url_test("https://httpbin.org/get")

# 在get中附加参数

def get_params(url):
    data = {'name':'doudou','age':'22','sex':'girl'}
    rst = requests.get(url,params=data) # 利用params提供参数
    print(rst.text)
    print("-" * 20)
    print(rst.json()) # 结果虽然是str类型的，但是是json格式的，需要使用json格式

#get_params("https://httpbin.org/get")
# 通过输出结果可以看到URL变成了 url": "https://httpbin.org/get?name=doudou&age=22&sex=girl

# 知乎抓取-成功！
# 将热点问题写入文件
def pachong_zhuhu_1(url):
    # 需要使用headers伪装成浏览器，否则爬不下来
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36' }
    rst = requests.get(url,headers=headers)
    find_tittle = re.compile(r'Card-.*?Title.*?>(.*?)</a>') 
#    print(rst.text)
    print("-" * 20)
    rst_tittle = find_tittle.findall(rst.text)
    with open("C:\\Users\\Dou\\Desktop\\Python\\Jupyter\\pachong.log",'a')as tx:
        for i in rst_tittle:
            tx.write(i+'\n')
            print(i)
        tx.close()

#pachong_zhuhu_1("https://www.zhihu.com/explore") # 知乎发现首页

# 抓取二进制文件，视频、音频、图片等
        
def pachong_erjinzhi(url):
    rst = requests.get(url)
#    print(rst.text) # 这是乱码
#    print("-" * 20)
#    print(rst.content) # 这个都是十六进制数字
    # 可以想办法把图片文件直接保存下来
    with open("C:\\Users\\Dou\\Desktop\\Python\\Jupyter\\pachong_wenjian\\favicon.ico","wb") as f:
        f.write(rst.content)
        f.close()

#pachong_erjinzhi("https://static.zhihu.com/static/favicon.ico")

# 爬个知乎图片-成功！ 哈哈哈哈哈
def pachong_zhuhu_tupian(url):
    # 需要使用headers伪装成浏览器，否则爬不下来
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36' }
    rst = requests.get(url,headers=headers)
#    print(rst.text)
    # 先把图片的地址爬下来
    find_tittle_1 = re.compile(r'noscript><img\ssrc="(https:.*?)"\sdata-caption') 
    find_tittle_2 = re.compile(r'noscript><img\ssrc="(https:.*?)"\sdata-rawwidth') 
    print("-" * 20)
    rst_tittle_1 = find_tittle_1.findall(rst.text) # 得到了图片的地址
#    rst_tittle_2 = find_tittle_2.findall(rst.text) # 得到了图片的地址
#    rst_tittle = rst_tittle_1 + rst_tittle_2
#    print(rst_tittle)
    
    for i_url,i in zip(rst_tittle_1,range(len(rst_tittle_1))):
        rst_tupian = requests.get(i_url)
        print(i_url)
        with open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong_wenjian\\{}.png".format(i+1),'wb') as f:
            f.write(rst_tupian.content)
            f.close()
        time.sleep(1)
            
pachong_zhuhu_tupian("https://www.zhihu.com/question/320087117/answer/873752166") # 知乎发现首页
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    
    
    
    
    

    
    
    
    