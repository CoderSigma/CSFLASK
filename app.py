from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "test"

@app.route("/")
def home():
    if request.method == "POST":
        sms = request.form["sms"]
    return render_template("main.html")

@app.route("/about")
def about():
    return render_template("about.html")

    
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    