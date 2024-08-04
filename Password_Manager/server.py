from flask import Flask,request,render_template,session,redirect
from db_manager import DB
from functions_manager import return_form_as_dict
import hashlib

app = Flask(__name__)
app.secret_key = "hkfn3802ndda$jke&lz^%k09"
db_object = DB()

@app.route("/")
def home_page():
    msg = ''
    if session.get('user'):
        return render_template("index.html",user=session.get("user"))
    if session.get('message'):
        msg = session.get('message','')
        session.pop('message')
    return render_template("login.html",message=msg)


@app.route("/signup")
def registerpage():
    return render_template('register.html')

@app.route("/register",methods=["POST"])
def register():
    data = return_form_as_dict(request.form.items())
    db_object.save_login_details(data)
    return redirect("/")



@app.route("/verify_login",methods=["POST"])
def verify():
    verified = False
    #Todo inputs validation
    params = return_form_as_dict(request.form.items())

    email = params['email']
    pwd = hashlib.sha256(params['password'].encode()).hexdigest()
    phone = params['phoneno']
    username = params['username']

    db_data = db_object.get_one_document("_id",email)

    if not db_data:
        return render_template("login.html",message="Invalid Credentials !!")
    else:
        if not ((db_data['_id']==email) 
           and (db_data['userName']==username) 
           and (db_data['secret'] == pwd)
           and (db_data['phone'] == phone)):
            session['message'] = "Invalid Credentials !!"
        else:
            verified = True

    if verified:        
        session['user'] = params.get("username")
    return redirect("/")

def clear_session_items():
    session.clear()

@app.route("/logout")
def user_logout():
    clear_session_items()
    return redirect("/")
    




