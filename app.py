from flask import Flask, render_template,request, url_for, redirect
import sqlalchemy as db
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
import mysql.connector
import json

app = Flask(__name__)
'''
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'cc'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)
con = mysql.connect()
with open("init.sql", 'r') as file1:
    sql_cmds = file1.read()

sql_cmds1 = sql_cmds.split(";")

for i in range(0, len(sql_cmds1)-1):
    query = sql_cmds1[i] + ';'
    cursor = con.cursor()
    cursor.execute(query)
con.commit()
cursor.close()

'''
config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'port': 3306,
    'database': 'cc'
}

con = mysql.connector.connect(**config)
with open("init.sql",'r') as file1:
    sql_cmds = file1.read()

sql_cmds1 = sql_cmds.split(";")

for i in range(0,len(sql_cmds1)-1):
    query = sql_cmds1[i] + ';'
    cursor = con.cursor()
    cursor.execute(query)
con.commit()


@app.route("/",methods=['GET'])
def index():
    '''
    config = {
    'user':'root',
    'password':'root',
    'host':'db',
    'database':'cc',
    'port' : '3306'
    }
    con = mysql.connector.connect(**config)
    '''
    cursor = con.cursor()
    cursor.execute('SELECT * FROM sessions')
    sessions = cursor.fetchall()
    cursor.close()

    return render_template('index.html',sessions=sessions)


@app.route("/insert",methods=['GET'])
def insert():
    '''
    config = {
    'user':'root',
    'password':'root',
    'host':'db',
    'database':'cc',
    'port' : '3306'
    }
    con = mysql.connector.connect(**config)
    '''
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sessions")
    sessions = cursor.fetchall()
    cursor.close()

    return render_template("insert.html", sessions=sessions)

@app.route("/view", methods=['POST', 'GET'])
def view():
    #cursor = mysql.connection.cursor()
    '''
    config = {
    'user':'root',
    'password':'root',
    'host':'db',
    'database':'cc',
    'port' : '3306'
    }
    con = mysql.connector.connect(**config)
    '''
    cursor = con.cursor()
    if request.method == "POST":
        #name = request.form.get("name")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        roll_no = request.form.get("roll_no")
        contact = request.form.get("contact")
        session = request.form.get("session")
        total_fee = request.form.get("total_fee")
        sub_fee = request.form.get("sub_fee")
        rem_fee = int(total_fee) - int(sub_fee)
        #roll_no = str(session) + "-" + str(roll_no2)
        
        cursor.execute("INSERT into students (fname,lname,contact,roll_no,session) VALUES (%s, %s, %s, %s, %s)",(fname,lname,contact,roll_no,session))

        cursor.execute("INSERT into fee (total_fee, sub_fee, rem_fee, roll_no) VALUES (%s, %s, %s, %s)",(total_fee,sub_fee,rem_fee,roll_no))
        #mysql.connection.commit()
        con.commit()

        # Get all records again
        cursor.execute("SELECT * from students INNER JOIN fee ON students.roll_no = fee.roll_no")
        students = cursor.fetchall()
        cursor.close()

        return render_template("view.html", students=students)
    
    else:
        cursor.execute("SELECT * from students INNER JOIN fee ON students.roll_no = fee.roll_no")
        students = cursor.fetchall()
        cursor.close()
        
        return render_template("view.html", students=students)


@app.route("/all_session", methods=['POST', 'GET'])
def all_session():
    '''
    config = {
    'user':'root',
    'password':'root',
    'host':'db',
    'database':'cc',
    'port' : '3306'
    }
    con = mysql.connector.connect(**config)
    '''
    cursor = con.cursor()
    if request.method == "POST":
        session = request.form.get("session")
        cursor.execute("INSERT into sessions (title) VALUES (%s)",(session,))
        #mysql.connection.commit()
        con.commit()
        cursor.execute("SELECT sessions.title, COUNT(students.roll_no), sum(fee.total_fee), sum(fee.sub_fee), sum(fee.rem_fee) FROM students INNER JOIN fee on students.roll_no = fee.roll_no RIGHT JOIN sessions ON students.session = sessions.title GROUP BY sessions.title")
        sessions = cursor.fetchall()
        cursor.close()
        
        return render_template("all_session.html", sessions=sessions)
    
    else:
        cursor.execute("SELECT sessions.title, COUNT(students.roll_no), sum(fee.total_fee), sum(fee.sub_fee), sum(fee.rem_fee) FROM students INNER JOIN fee on students.roll_no = fee.roll_no RIGHT JOIN sessions ON students.session = sessions.title GROUP BY sessions.title")
        sessions = cursor.fetchall()
        cursor.close()
        
        return render_template("all_session.html", sessions=sessions)

@app.route("/search", methods=['POST','GET'])
def search():
    '''
    config = {
    'user':'root',
    'password':'root',
    'host':'db',
    'database':'cc',
    'port' : '3306'
    }
    con = mysql.connector.connect(**config)
    '''
    cursor = con.cursor()    

    if request.method == "POST":       
        session = request.form.get("session")
        cursor.execute("SELECT * from students INNER JOIN fee ON students.roll_no = fee.roll_no where students.session = %s", (session,))
        students = cursor.fetchall()
        cursor.close()
        
        return render_template("view.html", students=students)

    else:
        return "Please search from Home Tab"

@app.route("/update/<roll_no>/", methods=['POST','GET'])
def update(roll_no):
    '''
    config = {
    'user':'root',
    'password':'root',
    'host':'db',
    'database':'cc',
    'port' : '3306'
    }
    con = mysql.connector.connect(**config)
    '''
    cursor = con.cursor()

    if request.method=="POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        roll_no2 = request.form.get("roll_no")
        contact = request.form.get("contact")
        session = request.form.get("session")
        total_fee = request.form.get("total_fee")
        sub_fee = request.form.get("sub_fee")
        rem_fee = int(total_fee) - int(sub_fee)
        a = str(roll_no)
     

        cursor.execute("Update students SET  fname =%s, lname =%s, contact =%s, roll_no = %s where roll_no=%s",(fname,lname,contact,roll_no2,roll_no))
        cursor.execute("Update fee SET total_fee = %s, sub_fee =%s, rem_fee =%s, roll_no = %s where roll_no=%s",(total_fee,sub_fee,rem_fee,roll_no2,roll_no))
        #mysql.connection.commit()
        con.commit()
        cursor.close()
        return redirect(url_for('view'))

    else:
        cursor.execute("SELECT * from students INNER JOIN fee ON students.roll_no = fee.roll_no WHERE students.roll_no = %s", (roll_no,))
        stud = cursor.fetchone()
        cursor.close()

        return render_template("update.html", stud=stud, roll_no=roll_no)

@app.route("/delete/<roll_no>/")
def delete(roll_no):
    '''
    config = {
    'user':'root',
    'password':'root',
    'host':'db',
    'database':'cc',
    'port' : '3306'
    }
    con = mysql.connector.connect(**config)
    '''
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
    stud = cursor.fetchone()
    if stud is None:
        return "No record found by Roll No = " + str(roll_no) +". Kindly go back to <a href='/view'> View All Students </a>"
    else:
        cursor.execute("DELETE FROM students WHERE roll_no =%s ",(roll_no,))
        cursor.execute("DELETE FROM fee WHERE roll_no =%s ",(roll_no,))
        #mysql.connection.commit()
        con.commit()
        cursor.close()

        return redirect(url_for('view'))

if __name__ == "__main__":
    app.run(debug=True)