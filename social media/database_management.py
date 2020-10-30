#from runner import account_credentials
import sqlite3
connection=sqlite3.connect('social media/temp.db',check_same_thread=False)


def signup(name,password,branch,semester):
    cur=connection.cursor()
    cur.execute("SELECT * FROM student_details WHERE username=(?);",(name,))
    result=cur.fetchone()
    if result is None:
        cur.execute('INSERT INTO student_details VALUES(?,?,?,?);',(name,password,branch,semester))
        connection.commit()
        cur.close()
        return True
    else:
        cur.close()
        return False    

           
def check_user_login(name,password):
    cur=connection.cursor()
    result = cur.execute('SELECT username FROM student_details WHERE username=(?) AND password=(?);',(name,password))
    if result:
        cur.close()
        return True
    else:
        cur.close()
        return False    
#def teacher_signup(name,):

def insert_resource(link,des):
    cur=connection.cursor()
    cur.execute("INSERT INTO resources VALUES(?,?)",(link,des))
    cur.close()
    connection.commit()

def get_db_len(name):
    sql='SELECT MAX(rowid) FROM '+name
    cur=connection.cursor()
    cur.execute(sql)
    result=cur.fetchone()[0]
    return result 

    
