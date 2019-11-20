import psycopg2
import db
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
        try:

            connection = psycopg2.connect(user="postgres",
                                          password="secret",
                                          host="127.0.0.1",
                                          port="5432")

            cursor = connection.cursor()
            # Print PostgreSQL Connection properties
            print(connection.get_dsn_parameters(), "\n")

            # insert record
            insert_user_query = """ INSERT INTO users (username, password) VALUES (%s,%s)"""
            user_to_insert = (username, password)
            cursor.execute(insert_user_query, user_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into users table")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
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
