import psycopg2
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

try:
    connection = psycopg2.connect(user="postgres",
                                  password="secret",
                                  host="127.0.0.1",
                                  port="5432")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")
    drop_existing_table_query = '''DROP TABLE IF EXISTS users CASCADE;
        DROP TABLE IF EXISTS wallets CASCADE;'''
    create_table_query = '''CREATE TABLE users
        (ID INT PRIMARY KEY     NOT NULL,
        username           TEXT    NOT NULL,
        password         TEXT); 
        CREATE TABLE wallets
        (ID INT PRIMARY KEY     NOT NULL,
        eur           MONEY    NOT NULL); 
        '''

    cursor.execute(drop_existing_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
