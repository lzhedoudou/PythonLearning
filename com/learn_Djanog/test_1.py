# 斐波那契数列

import socket

def fbnqsl(num):
    list_rst = [0,1]
    for i in range(num-2):
        list_rst.append(list_rst[-2]+list_rst[-1])
    return list_rst

def print_fbnqsl(num):
    for i,rst in enumerate(fbnqsl(num)):
        print("序号{}，结果{}".format(i+1,rst))
#print_fbnqsl(10)
    

# 测试变成的参数
        
# 字典模式        
def bccs(**args):
    print(args)
    
#if __name__ == '__main__':
#    bccs(a = 'this',b = 'is')


#import socket
#import datetime
#
#host = '192.168.151.251'
#port = 65345
#
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.bind((host,port))
#s.listen(1)
#
#while True:
#    conn,addr=s.accept()
#    print('Client %s connnected!' % str(addr))
#    dt = datetime.datetime.now()
#    message = 'Current time is ' + str(dt)
#    conn.send(message.encode('utf8'))
#    print("Sent:",message)
#    conn.close
    
def conn_socket_tcp():
    host = '192.168.151.251'
    port = 65345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    print("Connect {}:{} OK".format(host,port))
    data = s.recv(1024)
    print("Received: ",data)
    s.close()
#conn_socket_tcp()
    
def conn_socket_udp():
    host = '192.168.151.251'
    port = 65345
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    data = 'hello! UDP !!!'
    s.sendto(data.encode('utf-8'),(host,port))

    s.close()

conn_socket_udp()
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    