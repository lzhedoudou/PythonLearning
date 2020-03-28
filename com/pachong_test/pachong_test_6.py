# 先爬一个微博
# 我的主页
import requests
from bs4 import BeautifulSoup

def pachong_youmin_test(url):
    '''
    爬一个自己的微博
    '''
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36'}
    response = requests.get(url)
    response.encoding = 'gbk'
    html = response.text
#    print(html)
    soup = BeautifulSoup(html,'lxml')
    print(soup.prettify)
#    with open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong.log",'w') as f:
#        f.write(str(soup.prettify))
#        f.close()
    
pachong_youmin_test("https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__20&id=1005052807453641&script_uri=/2807453641/profile&feed_type=0&pre_page=1&domain_op=100505&__rnd=1585299693228")