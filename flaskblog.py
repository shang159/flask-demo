from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy

flaskblog=Flask(__name__)
flaskblog.config['SECRET_KEY']="bad021b759edb72292003fafbe02264e"
flaskblog.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
db=SQLAlchemy(flaskblog)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default="default.jpg")
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


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
    return render_template("about.html")


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

    return render_template("login.html",title="login",form=form)





#两种启动方式：
##利用python-dotenv   flask run
##利用app.run

if __name__ == "__main__":
    flaskblog.run(debug=True)