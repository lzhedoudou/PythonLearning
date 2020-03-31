# 测试一下数据库
import pymysql

db = pymysql.connect(host = '192.168.151.251',user='root',password='root',port=3306,db='spyder_test') # 创建数据库连接

# 数据库查询
def select():
    cursor = db.cursor() # 获得游标
    cursor.execute('select * from person;') # 利用游标执行sql
    #rst = cursor.fetchone() # 获得第一条数据
    rst = cursor.fetchall() 
    print(rst)
    db.close()

    # 注意如果执行添加、修改等操作需要commit() 如果写了异常，需要roolback()
#select()

# 数据库添加

def insert():
    # 定义要插入的数据
    
    id = 4
    name = '安生'
    age = '15'
    sex = '女'

    cursor = db.cursor()
    sql = 'insert into person(id,name,age,sex) values(%s,%s,%s,%s)'
    
    # 上面方法效率不高，可以采用字典的方式

    try:
        cursor.execute(sql,(id,name,age,sex))
        db.commit()
    except:
        db.rollback()
    else:
        cursor.execute('select * from person;')
        rst = cursor.fetchall() 
        print(rst)
    finally:
        db.close()
#insert()
        
# 数据库修改



