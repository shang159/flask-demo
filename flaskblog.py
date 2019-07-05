from flask import Flask

flaskblog=Flask(__name__)



@flaskblog.route("/")
def hello():
    return "hello world"

#两种启动方式：
##利用python-dotenv   flask run
##利用app.run



if __name__ == "__main__":
    flaskblog.run(debug=True)