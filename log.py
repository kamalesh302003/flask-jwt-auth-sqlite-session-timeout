from flask import Flask,request,render_template,redirect,make_response,session
import sqlite3
import jwt,datetime,time,secrets
from werkzeug.security import generate_password_hash,check_password_hash
app=Flask(__name__)
app.secret_key="sessionsecret"
SECRET_KEY = secrets.token_hex(32)
print(SECRET_KEY)
#SECRET_KEY = "this_is_a_very_secure_secret_key_12345"
#SECRET_KEY="jwtsecret"
TIMEOUT=60 
#initialising database sqlite3
def create_db():
    conn=sqlite3.connect('pythonjwt.db')
    cur=conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS reg(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()
create_db()

#function check_timeout
def check_timeout():
    if 'last_activity' in session:
        now=time.time()
        if now - session['last_activity']>TIMEOUT:
            session.clear()
            return True
    session['last_activity']=time.time()
    return False

#home
@app.route('/')
def home():
    return redirect('/login')

#register page
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=generate_password_hash(request.form['password'])
        conn=sqlite3.connect('pythonjwt.db')
        cur=conn.cursor()
        cur.execute("INSERT INTO reg(username,password) VALUES(?,?)",(username,password))
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('register.html')

#login page
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        conn = sqlite3.connect('pythonjwt.db')
        cur=conn.cursor()
        cur.execute("SELECT * FROM reg WHERE username=?",(username,))
        user=cur.fetchone()
        conn.close()
        if user and check_password_hash(user[1],password):
            token=jwt.encode({
                "user_id":user[0],
                "username":user[1],
                "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
            },SECRET_KEY, algorithm="HS256")
            response=make_response(redirect('/dashboard'))
            response.set_cookie("token", token)
            session['last_activity']=time.time() #start session timer
            return response
        return "Invalid Login"
    return render_template('login.html')

#dashboard page
@app.route('/dashboard')
def dashboard():
    if check_timeout():
        return redirect('/login')
    token=request.cookies.get("token")
    if not token:
        return redirect('/login')
    try:
        data=jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        return render_template('dashboard.html',user=data['username'])
    except:
        return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
    response=make_response(redirect('/login'))
    response.delete_cookie("token")
    return response

if __name__=='__main__':
    app.run(debug=True)