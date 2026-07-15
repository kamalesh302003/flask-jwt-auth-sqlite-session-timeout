from flask import Flask ,render_template, url_for,request,redirect
import mysql.connector
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/reg',methods=['POST','GET'])
def reg():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pythonflask"
    )
    mycursor = conn.cursor()
    if request.method=='POST':
        uname=request.form["uname"]
        email=request.form["email"]
        upass=request.form["upass"]
        mycursor.execute("insert into reg(UNAME,EMAIL,UPASS) values(%s,%s,%s)",(uname,email,upass))
        conn.commit()
        mycursor.close()
        return render_template('successful.html')
    


if __name__ == '__main__':
   app.run(debug=True)