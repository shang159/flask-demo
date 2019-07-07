from flaskblog_app import flaskblog
from flask import render_template,url_for,flash,redirect
from .forms import RegistrationForm,LoginForm
from .models import User,Post


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
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!',"success")
        return redirect(url_for('home'))
    return render_template("register.html",title="Register",form=form)

@flaskblog.route("/login",methods=["GET","POST"])

def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@blog.com" and form.passwd.data=="passwd":
            flash("You have been logged in!","success")
            return redirect(url_for("home"))
        else:
            flash("Login unsucessful.Please check username and password","danger")

    return render_template("login.html",title="Login",form=form)




