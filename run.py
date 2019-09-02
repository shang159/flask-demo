from flaskblog_app import flaskblog

#两种启动方式：
##利用python-dotenv   flask run
##利用app.run

if __name__ == "__main__":
    flaskblog.run(debug=True)