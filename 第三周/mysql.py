import pymysql


def Connection():
    try:
        db = pymysql.connect(host="localhost", user="root", password="123", database="students")
        print('数据库连接成功!')
    except pymysql.Error as e:
        print('数据库连接失败'+str(e))
    finally:
        db.close()
        
def CreateTable():
    db = pymysql.connect(host="localhost", user="root", password="123", database="students")
    cur = db.cursor()
    try:
        cur.execute('DROP TABLE IF EXISTS student')
        sqlQuery = '''CREATE TABLE student(
                                   id  int  primary key,
                                   name CHAR(20) NOT NULL ,
                                   classroom CHAR(20),
                                   email CHAR(20),
                                   age int )'''
        cur.execute(sqlQuery)
        print("数据表创建完成！")
    except pymysql.Error as error:
        print("数据表创建失败：" + str(error))
        db.rollback()
    finally:
        db.close()

def Insert():
    db = pymysql.connect(host="localhost", user="root", password="123", database="students")
    cur = db.cursor()
    sqlQuery = " INSERT INTO Student (id, name, classroom, email, age) VALUE (%s,%s,%s,%s,%s) "
    value = (1010, "侯超","1班", "123.com", 20)
    try:
        cur.execute(sqlQuery, value)
        db.commit()
        print('数据插入成功！')
    except pymysql.Error as error:
        print("数据插入失败：" + str(error))
        db.rollback()
    finally:
        db.close()

def Update():
    db = pymysql.connect(host="localhost", user="root", password="123", database="students")
    cur = db.cursor()
    sqlQuery = "UPDATE Student SET age= %s WHERE name=%s"
    name = "侯超"
    age = 19
    value = age, name
    try:
        cur.execute(sqlQuery, value)
        db.commit()
        print('数据更新成功！')
    except pymysql.Error as e:
        print("数据更新失败：" + str(e))
        # 发生错误时回滚
        db.rollback()
    finally:
        db.close()

