import psycopg2
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    if request.method == 'POST':
        if not username or not password:
            return "failure"
        return "success"

    else:
        return render_template("signup.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form.get("username") or not request.form.get("password"):
            return "failure"
        return "success"
    else:
        return render_template("login.html")


app.debug = True
if __name__ == "__main__":
    app.run()
