
import mysql.connector as mydb


def mysql():
    conn = mydb.connect(
            host="Koba1600.mysql.pythonanywhere-services.com",
            port="3306",
            user="Koba1600",
            password="PWs{Li4{jBgPTg%n",
            database="Koba1600$site"
            )

    
    cur = conn.cursor()

    cur.execute("show tables;")
    result =""
    for x in cur.fetchall():
        if ('RealMadrid',) == x:
            result = "ok"
        else:
            pass

    if result == None:
        print("The table does not exist")
        cur.execute("create table RealMadrid (id int, name varchar(100), position varchar(100));")
    else:
        print("The table exists")

def mysql_insert():

mysql()


