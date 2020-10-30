from flask import Flask,render_template,request,redirect,url_for,session,flash,Response
from datetime import timedelta
#from flask_sqlalchemy import SQLAlchemy
import database_management as dm

app=Flask(__name__)
app.secret_key='emiwaybantai'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.permanent_session_lifetime=timedelta(days=5)
lis=[1,2,3,4,5]


###APP AREA

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route("/login_page",methods=["POST","GET"])
def login_page():
    if request.method=="POST":
        session.permanent=True
        username=request.form['username']
        password=request.form['password']
        if dm.check_user_login(username,password)==True:

            session['username']=username
            session['password']=password
            return redirect(url_for('account_home'))
        else:
            flash(f"<h5><center>either account doesnt exists or password is wrong boi</center></h5>")
            return redirect(url_for('login_page')) 
    else:
        if "username" in session:
            return redirect(url_for("account_home"))
        else:        
            return render_template("login.html")

@app.route("/signup_page/<account>",methods=["POST","GET"])
def signup_page(account='student'):
    if account=='student':
        if request.method=="POST":
            username=request.form['username']
            password=request.form['password']
            branch    =request.form['branch']
            semester  =request.form['semester']

            if dm.signup(username,password,branch,semester)==True:
                session['username']=username
                session['password']=password
                return redirect(url_for('account_home'))
        else:
            if "username" in session:
                return redirect(url_for('account_home'))
            else:      
                return render_template("signup.html")
    if account=='teacher':
        if request.method=='POST':
            print(request.form.getlist('branch'))
            return redirect(url_for('signup_page',account="teacher"))
        else:
            return render_template('teachers_signup.html') 

@app.route("/user")
def account_home():
    if "username" in session:
        user=session['username']
        return  render_template('login_home.html',user=user)   
    else:
        return redirect(url_for("login_page"))

@app.route("/logout")
def logout():
    session.pop("username",None)
    session.pop("password",None)
    flash(f"<h5><center>You have been successfully logged out</center></h5>")
    return redirect(url_for('login_page'))       

@app.route('/resources/<int:page_num>',methods=['GET',"POST"])
#@app.route('/resources/',methods=['GET',"POST"])
def resources(page_num=1):
    if request.method=='POST':
        link=request.form['link']
        text=request.form['form']
        db.insert_resource(link,text)
        return redirect(url_for('resources'))
    else:    
        return render_template('resources.html',pn=page_num)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
###################################################################################################################     
if __name__=="__main__":
    #database.create_all()
    app.run(debug=True)    