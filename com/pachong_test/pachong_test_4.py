import requests
from bs4 import BeautifulSoup

def bs4_test_zhihu(url):
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36'}
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    
    # 电影标签的全部信息
    rst_all = soup.find_all('div',class_='item')
    # 排名
    rst_em = soup.find_all('em',class_="") # 注意这个底杠 然后需要迭代出来
    # 电影名称
    rst_name = soup.find_all('span',class_='title')
    # 电影相关信息
    rst_p = soup.find_all('p',class_='')
    # 电影评分
    rst_span_rating_num = soup.find_all('span',class_='rating_num')
    # 一句短评
    rst_span_inq = soup.find_all('span',class_='inq')
#    for em,p,span_rating_num,span_inq in zip(rst_em,rst_p,rst_span_rating_num,rst_span_inq):
#        print(em.text,p.text.replace(" ",""),span_rating_num.text+'\n',span_inq.text.replace(" ",""))
#    for i in rst_all:
#        print(i.text.replace(" ","").replace("\n",""))
    for i in rst_name:
        print(i.text.replace(" ","").replace("\n",""))


#    with open("C:\\Users\\Dou\\Desktop\\Python\\Jupyter\\Jupyter\\\\pachong.log",'w',encoding='utf-8') as f:
#        f.write(soup.prettify())
#        f.close()
#    print(soup.p.string) # 这样就可以快速输出字符
#    print(type(soup))
#    print(type(soup.prettify())) # 以标准字符格式缩进，结果是str类型
#    print(soup.head.string)
#    print(soup.a.string)
#    print(soup.a.name)
#    print("-" * 20)
#    print(soup.a.attrs)
#    print(soup.a.attrs['class'])
#    print("-" * 20)
#    print(soup.body.a)
#    print("-" * 20)
#    print(soup.find_all('span')[5].string) # 这就可以定位了
#    print("-" * 20)
#    print(soup.find_all(name = 'span',attrs={'class':'other'}))
#    for i,b in zip(soup.select('span'),soup.select('p')):
#        print(i.get_text())
#        print(b.get_text())
#    print(soup.)
    
bs4_test_zhihu("https://movie.douban.com/top250")