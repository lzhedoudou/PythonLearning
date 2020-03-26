# 爬一个猫眼电影排行榜

import requests
import re


def pachong_maoyan(url):
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36' }
    list_film = []
    for i in range(0,100,10):
        response = requests.get(url.format(i),headers=headers)
        find_paihangbang = re.compile(r'''<i class="board-index board-index-\d*">(\d*)</i>[\d\D]*?<p class="name"><a href="/films/\d*" title="(.*?)" data-act="boarditem-click" data-val="{movieId:\d+}">.*?</a></p>\n\s+<p class="star">\n\s+(.*?)\n\s+</p>\n\s*<p class="releasetime">(.*?)</p>''')
        my_paihangbang = find_paihangbang.findall(response.text)
        response.encoding='utf-8' # 设置编码，防止乱码
        for x in my_paihangbang:
            list_film.append(x)
     # bingo 写入文件
    if response.status_code == 200:
        with open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong.log",'w') as f:
            for y in list_film:
                for a in y:
                    f.write(a+'\n')
            f.close()

pachong_maoyan("https://maoyan.com/board/4?offset={}")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    