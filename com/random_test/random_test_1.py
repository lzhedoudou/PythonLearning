# 模拟骰子大小
import random as rd
def guize():
    shaizi_1 = rd.choice([i for i in range(1,7)])
    shaizi_2 = rd.choice([i for i in range(1,7)])
    shaizi_3 = rd.choice([i for i in range(1,7)])
    rst1 = shaizi_1 + shaizi_2 + shaizi_3
    dianshu_guize = 0
    if shaizi_1 == shaizi_2 == shaizi_3:
        dianshu_guize = 0
        print("点数 {} 开了豹子".format(rst1))
    elif rst1 >= 4 and rst1 <= 10:
        dianshu_guize = -1
        print("点数 {} 开小".format(rst1))
    elif rst1 >= 11 and rst1 <= 17:
        dianshu_guize = 1
        print("点数 {} 开大".format(rst1))
    else:
        print("见鬼了")
    return rst1,dianshu_guize


for i in range(20): # 赌博二十次

    yaodong = guize()



