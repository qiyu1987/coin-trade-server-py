import psycopg2
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
        (id serial PRIMARY KEY,
        username VARCHAR (50) UNIQUE NOT NULL,
        password VARCHAR (50)); 
        CREATE TABLE wallets
        (id serial PRIMARY KEY NOT NULL,
        eur MONEY NOT NULL,
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)); 
        '''
    cursor.execute(drop_existing_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    # insert record
    insert_user_query = """ INSERT INTO users (username, password) VALUES (%s,%s)"""
    insert_wallet_query = """ INSERT INTO wallets (eur, user_id) VALUES (%s,%s)"""
    users_to_insert = [('yuki', 'yuki'), ('xiaodan', 'xiaodan')]
    cursor.executemany(insert_user_query, users_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into users table")
    wallets_to_insert = [(10000, 1), (10000, 2)]
    cursor.executemany(insert_wallet_query, wallets_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into wallets table")

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
