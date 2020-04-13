#shutil

import shutil,os
print(os.getcwd())
# 复制操作
#shutil.copy('C:\\Users\\l1541\\Desktop\\Python\\Jupyter\\web_test\\web_test_1.html','C:\\Users\\l1541\\Desktop\\web_test_1.htm')
# 移动 move

# 删除os.unlink(path) 
# 删除文件夹os.rmdir(path) 文件夹必须为空
# 删除文件夹下所有 shutil.rmtree(path)

# os.walk

for a,b,c in os.walk("C:\\Users\\l1541\\Desktop"):
    print(a)
    print(b)
    print(c)
