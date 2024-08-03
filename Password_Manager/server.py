from flask import Flask,request,render_template,session,redirect

app = Flask(__name__)
app.secret_key = "hkfn3802ndda$jke&lz^%k09"

@app.route("/")
def home_page():
    if session.get('user'):
        return render_template("index.html",user=session.get("user"))
    return render_template("login.html")

@app.route("/verify_login",methods=["POST"])
def verify():
    #Todo inputs validation & DB connection
    items = request.form.items()
    params = {key:value for key,value in items}
    session['user'] = params.get("username")
    return redirect("/")

def clear_session_items():
    session.clear()

@app.route("/logout")
def user_logout():
    clear_session_items()
    return redirect("/")
    




