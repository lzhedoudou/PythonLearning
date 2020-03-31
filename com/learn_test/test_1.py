# 做一个猜数字的test

import random
import logging


def caizi():
    number_1 = random.randint(1,100) # 生成1-100的数字
    logging.basicConfig(level = logging.DEBUG,format ='%(asctime)s  %(levelname)s  %(message)s')
    logging.debug('start')
    
    try:
        while True:
            my_input = int(input("请输入你猜测的数字"))
            rst_num = my_input - number_1
            if rst_num > 10 and rst_num < 20 :
                print("输入的有点大了!")
                logging.debug
            elif rst_num < -10 and rst_num > -20:
                print("输入的有点小了!")
            elif rst_num > 10 :
                print("输入的tai大了!")
            elif rst_num < -10:
                print("输入的tai小了!")   
            elif rst_num > 5 :
                print("有点大 非常接近了!")
            elif rst_num < -5:
                print("有点小 非常接近了!")    
            if rst_num == 0:
#                raise Exception("谜底揭晓了ahha！生成的数字是{}".format(number_1))
                print("谜底揭晓，生成的数字是{}".format(number_1))
                break
    except ValueError:
        print("输入的字符错误，需要输入一个数字！")
#    except Exception as err:
#        print(str(err))
caizi()
        

    
        