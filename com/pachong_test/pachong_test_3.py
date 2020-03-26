import requests
import urllib3
from requests.auth import HTTPBasicAuth

# 验证post

def pachong_test_post(url):
    data = {'name':'doudou'}
    
    # 上传文件
    files = {'file':open("C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong_wenjian\\31.png",'rb')}
#    response = requests.post(url,data)
    response = requests.post(url,files=files)
    # 各种方法
    print(response.text)
#    print(response.status_code)
#    print(response.url)
#    print(response.cookies)
#    print(response.history)
    
    
    
#pachong_test_post("https://httpbin.org/post")
    
# 可以使用cookies保持登录状态
    
def pachong_test_cookie(url):
    headers={'Cookie':'_zap=c157a44f-e9b5-471e-94a4-dc72e0973e9b; d_c0="ABAXtNjB6xCPTh534dLVuZg8d0CEXTYFYfo=|1583479305"; _ga=GA1.2.1163923813.1583479308; _xsrf=smOvC48P7YxxwKP4YjQYciLhcFQ946iF; tst=r; _gid=GA1.2.326551742.1585115227; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1585115226,1585119099,1585188843,1585188863; capsion_ticket="2|1:0|10:1585188953|14:capsion_ticket|44:NDA1NzI1OGYzNDdhNDE3ODhlZDU5MmVkNTcyYWYyZmU=|391484181c627359e196c4270c4c99711888a71abd925e57762e6c14da97a646"; z_c0="2|1:0|10:1585188957|4:z_c0|92:Mi4xR0JHS0FnQUFBQUFBRUJlMDJNSHJFQ1lBQUFCZ0FsVk5YVjVwWHdCT1dxb3c4ZDdBY25LaG5nOXJRSTVpTzhjd2p3|9b0957dd88cd886730f167cdf35b02bf6dcea8ad84bad56da3a9f49a168b11c2"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585188988; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1585188990|1585188842',
            'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'}
    response = requests.get(url,headers = headers)
    # 根据输出结果可以看到，确实借用浏览器的cookie成功登录了
    print(response.text)
#pachong_test_cookie("https://www.zhihu.com")
    
# 测试12306-原12306证书问题
def pachong_test_12306(url):
    urllib3.disable_warnings() # 忽略证书警告
    response = requests.get(url,verify=False) # 设置不验证证书
    print(response.status_code)

#pachong_test_12306("https://www.12306.cn/")
    

# 爬取代理
def pachong_test_taobao_daili(url):
    proxy = {'http':'182.149.83.194:9999'}
    response = requests.get(url,proxies=proxy,timeout=0.01)# 设置超时时间
    print(response.text)

#pachong_test_taobao_daili("https://www.taobao.com/")
    

# 认证
    
def pachong_test_passwd(url):
    # 需要先导入库
    response = requests.get(url,auth=HTTPBasicAuth('l1541','Asd@1234567890'))
    print(response.status_code)

#pachong_test_passwd("？？？没有测试的地址啊")
    





























