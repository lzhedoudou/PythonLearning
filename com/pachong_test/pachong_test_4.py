import requests
from bs4 import BeautifulSoup

def bs4_test_zhihu(url):
#    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36'}
#    html = requests.get(url,headers=headers)
#    print(html.text)

    
    with open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong.log",'r',encoding='utf-8') as f:
        rst = f.read()
        f.close()
        
    soup = BeautifulSoup(rst,'lxml')
    print(soup.p)
    with open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong_1.log",'w',encoding='utf-8') as f:
        rst = f.write(soup.prettify())
        f.close() 
    
bs4_test_zhihu("https://movie.douban.com/top250")