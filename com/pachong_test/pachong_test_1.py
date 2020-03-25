import urllib.request as request
import urllib.parse as parse
import socket
import urllib.error

# get请求
def pachong_def(url_name):
    response = request.urlopen(url_name)
#    url_neirong = response.read().decode('gbk') # read()可以获取返回内容
    url_neirong_code =str(response.getcode()) # getcode()查看返回码
    url_neirong_head = str(response.getheaders()) # getheaders()查看返回头部
    url_neirong_server = str(response.getheader('Server')) # 查看后端服务器
    with open(r"C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\pachong.log","w") as pachong:
        pachong.writelines(url_neirong_code+'\n')
        pachong.writelines(url_neirong_head+'\n')
        pachong.writelines(url_neirong_server+'\n')
        pachong.close()
    
    
#pachong_def("https://www.163.com/")   

# post请求

def pachong_def_post(url_name):
    
    # 先将字典转换成字符串，再将字符串转换成bytes
    data = bytes(parse.urlencode({'word': 'hello'}),encoding = 'UTF-8')
    
    response = request.urlopen(url_name,data=data)
    print(response.read()) # 根据结果可以返现form中有hello world
    
#pachong_def_post("http://httpbin.org/post")
    
# 设置timeout参数，配合异常使用，当网站get超过指定时间，就跳过，并抛出异常
# 注意引入urllib.error
# URLError: <urlopen error _ssl.c:1059: The handshake operation timed out>
def pachong_timeout():
    try:
        response1 = request.urlopen("https://facebook.com/",timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance (e.reason,socket.timeout):
            print("超时！")
        else:
            print(response1.read())
#pachong_timeout()
            
# request

def pachong_request(url_add):
    dict = {'name':'doudou'}
    data = bytes(parse.urlencode(dict),encoding = 'utf-8')
    req = request.Request(url = url_add,data = data,method='POST')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))
    
pachong_request('http://httpbin.org/post')
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    