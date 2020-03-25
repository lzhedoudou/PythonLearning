# 使用requests
import requests
import re

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

# 知乎抓取
def pachong_zhuhu_1(url):
    # 需要使用headers伪装成浏览器，否则爬不下来
    headers={'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36' }
    rst = requests.get(url,headers=headers)
#    find_tittle = re.compile(r'data-za-detail-view-id="\w*">(.*)</a>') 
    print(rst.text)
    print("-" * 20)
#    rst_tittle = find_tittle.findall(rst.text)
#    print(rst_tittle)

#pachong_zhuhu_1("https://www.zhihu.com/explore") # 知乎发现首页
    
def zhengze_test():
    text = '''
    class="ExploreSpecialCard-contentList"><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19900873#NewsSpecial-SubModule-1225924012863750144" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">疫情之下的春招</a><a class="ExploreSpecialCard-contentTitle" href="/question/367880979" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">疫情对2020春招有什么影响？ </a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19900873#NewsSpecial-SubModule-1225925525153239040" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">2020 行业趋势</a><a class="ExploreSpecialCard-contentTitle" href="/answer/1073034894" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">应届生想做运营类工作，该进什么样的公司？</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19900873#NewsSpecial-SubModule-1225926839149371392" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">简历&amp;面试干货</a><a class="ExploreSpecialCard-contentTitle" href="/answer/1073080156" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">大学生参加校招，怎样制作一份出色的简历？</a></div></div></div><div class="ExploreSpecialCard ExploreHomePage-specialCard">
    '''
    my_find = re.compile(r'<a class="ExploreSpecialCard-contentTitle" href="/answer/1073034894" target="blank" rel="noopener noreferrer" data-za-detail-view-id="\d+">(.*)</a>')
    rst_find = my_find.findall(text)
    print(rst_find)
    
zhengze_test()
    

    
    
    
    
    

    
    
    
    