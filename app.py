"""in case using a temp dir for *.html
compile this file use
pyinstaller --onefile -w --add-data "templates;templates" --add-data "static;static" app.py
temporarily use debugging"""
from flask_debug import Debug
from flask import Flask
from flask import request, send_file
from flask import render_template, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from common import projectdir

use_temp_dir = True
templates_dir = projectdir("templates", use_temp_dir)
static_dir = projectdir("static", use_temp_dir)

app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
app.config["SECRET_KEY"] = "681019bb3369b102e337f59b50dd5a6ca527947ac87152e362e9b0e45405bb11"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storage.db"

# web pages
@app.route("/")
def home_page():
    return render_template("home.html", title="JSC ECM")

@app.route("/register", methods=["get", "post"])
def register():
    from regform import RegistrationForm
    from flask import flash
    from flask import redirect

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        flash(f'Account successfully created for {reg_form.username.data} ({reg_form.email.data})', 'success')
        return redirect(url_for('home_page'))
    return render_template("register.html", title="Sign up", form=reg_form)

@app.route("/login", methods=["get", "post"])
def login():
    from regform import LoginForm
    from flask import flash
    from flask import redirect

    log_form = LoginForm()
    if log_form.validate_on_submit():
        if "admin" in log_form.email.data:
            flash("You have been logged in!", "success")
            return redirect(url_for('home_page'))
        else:
            flash("Login unseccessful. Please check username and password!", "danger m-auto w-25")
    return render_template("login.html", title="Log in", form=log_form)

# rest api functions
auth = HTTPBasicAuth()
"""must be a database"""
users_websrv = {
    "admin": generate_password_hash("123")
}

@auth.verify_password
def verify_password(user, password):
    if user in users_websrv:
        return check_password_hash(users_websrv.get(user), password)

@app.route("/api/reports/contracts", methods=["get", "post"])
@auth.login_required
def getreport():
    from reports.contracts.contract import get_contract_report
    binary_report = get_contract_report()
    return send_file(binary_report, attachment_filename="*.xlsx")

if __name__ == "__main__":
    Debug(app)
    app.run(debug=True, port=8181)
