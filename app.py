import db
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


app.debug = True
if __name__ == "__main__":
    app.run()
