# app.py
import pymysql 
import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

host_name = "127.0.0.1"
user_name = "root"
user_password = "darshan253"
db_name = "eduschema"

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection(host_name, user_name, user_password, db_name)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/retrieve', methods=['POST'])
def retrieve():
    try:
        if request.method == 'POST':
            cursor = connection.cursor()
            table = str(request.form['input'])
            query = f"SELECT * FROM {table} WHERE isDeleted = FALSE"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return render_template('index.html', result=results)
    except pymysql.MySQLError as e:
        error_msg = f"Database error: {e}"
        print(error_msg)
        return render_template('index.html', results=error_msg)
    except Exception as e:
        error_msg = f"An error occurred: {e}"
        print(error_msg)
        return render_template('index.html', results=error_msg)


if __name__ == '__main__':
    app.run(debug=True)
