from flaskblog_app import flaskblog,db,bcrypt
from flask import render_template,url_for,flash,redirect,request
from flaskblog_app.forms import RegistrationForm,LoginForm
from flaskblog_app.models import  User,Post
from flask_login import login_user,current_user,logout_user,login_required



posts=[
    {'author':'skeep588','title':'Blog Post 1',
        'content':'First post conte','date_posted':"April 20,2018"},
    {'author': 'skeep1','title': 'Blog Post 2',
        'content': 'First post conte1','date_posted': "April 20,2018"},
    {'author': 'skeep2','title': 'Blog Post 3',
        'content': 'First post conte3','date_posted': "April 20,2018"},
    {'author': 'skeep3','title': 'Blog Post 4',
     'content': 'First post conte2','date_posted': "April 20,2018"}
]


@flaskblog.route("/")
@flaskblog.route("/home")
def home():
    return render_template('home.html',posts=posts,title="Home")

@flaskblog.route("/about")
def about():
    return render_template("about.html",title="About")

@flaskblog.route("/register",methods=['GET',"POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=RegistrationForm()
    if form.validate_on_submit():
        hasded_password=bcrypt.generate_password_hash(form.passwd.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=hasded_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!',"success")
        return redirect(url_for('login'))
    return render_template("register.html",title="Register",form=form)

@flaskblog.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.passwd.data):
            login_user(user,remember=form.rember.data)
            flash("You have been logged in!","success")
            next_page = request.args.get("get")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login unsucessful.Please check email and password","danger")
    return render_template("login.html",title="Login",form=form)

@flaskblog.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@flaskblog.route("/account")
@login_required
def account():
    return render_template("account.html",title="Account")


