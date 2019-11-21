from flask import Flask, render_template, request, jsonify
from models import User, app, db, user_schema
import json
db.drop_all()
db.create_all()

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signup", methods=['POST'])
def signup():
    username = request.get_json()['username']
    password = request.get_json()['password']
    if request.method == 'POST':
        if not username or not password:
            return "failure"
        useraccount = User(username=username,password=password)
        db.session.add(useraccount)
        db.session.commit()
        result = User.query.filter_by(username=username).first()
        return user_schema.jsonify(result)

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
