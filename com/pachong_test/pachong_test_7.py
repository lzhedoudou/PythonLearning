# 爬一个游民众评评分试试
# 游民这个页面看到的是经过渲染后的，所以request请求的数据和html解析看到的不一样的
import requests
from bs4 import BeautifulSoup

def pachong_youmin_test(url):
    '''
    爬一个游民评分页面看看
    '''
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36'}
    html = (requests.get(url)).text
#    print(html)
    soup = BeautifulSoup(html,'lxml')
    with open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong.log",'w') as f:
        f.write(str(soup.prettify))
        f.close()
    
pachong_youmin_test("https://ku.gamersky.com/sp/1751-0-2020-0-0-0.html?sort=20")