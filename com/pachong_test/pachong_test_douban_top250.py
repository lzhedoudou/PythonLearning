# 爬一个douban电影排行榜

import requests
import re


def pachong_douban(url):
    '''
    爬虫豆瓣排行榜top250
    '''
    # 定义一个空的列表，放最后的结果
    list_film = []
    
    # 伪装浏览器
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36' }      
    
    for i in range(0,226,25):
        # 请求网页
        response = requests.get(url.format(i),headers=headers)
    
        # 正则表达式匹配出需要的信息
        find_paihangbang = re.compile(r'<em class="">(\d+?)</em>[\d\D]*?<span class="title">(.*?)</span>[\d\D]*?<span class="other">/(.*?)</span>[\d\D]*?<p class="">\n\s*([\d\D]*?)\n\s*([\d\D]*?)\n\s*?</p>[\d\D]*?<span class="rating_num" property="v:average">(.*?)</span>[\d\D]*?<span>(.*?)</span>[\d\D]*?<span class="inq">(.*?)</span>')
    
        # 结果搞出来
        my_paihangbang = find_paihangbang.findall(response.text.replace(r"&nbsp;","").replace(r"<br>",''))# 这里替换一下讨厌的&nbsp;
        
        response.encoding='utf-8' # 设置编码，防止乱码
        for x in my_paihangbang:
            list_film.append(x)
     # bingo 写入文件
    if response.status_code == 200:
        with open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong.log",'w',encoding='utf-8') as f:
            for y in list_film:
                for a in y:
                    f.write(a+'\n')
            f.close()

pachong_douban("https://movie.douban.com/top250?start={}&filter=")
