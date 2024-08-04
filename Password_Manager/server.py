from flask import Flask,request,render_template,session,redirect
from db_manager import DB
from functions_manager import return_form_as_dict

app = Flask(__name__)
app.secret_key = "hkfn3802ndda$jke&lz^%k09"
db_object = DB()

@app.route("/")
def home_page():
    if session.get('user'):
        return render_template("index.html",user=session.get("user"))
    return render_template("login.html")


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
    #Todo inputs validation & DB connection
    params = return_form_as_dict(request.form.items())
    session['user'] = params.get("username")
    return redirect("/")

def clear_session_items():
    session.clear()

@app.route("/logout")
def user_logout():
    clear_session_items()
    return redirect("/")
    




