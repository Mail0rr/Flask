from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("main.html")

def save_to_db(name, description, price):
    sqlite_connection = sqlite3.connect("sql_python3.db")
    cursor = sqlite_connection.cursor()
    sqlite_insert_with_param = '''
    INSERT INTO db_developers (name, description, price)
    VALUES (?, ?, ?);
    '''
    data_tuple = (name, description, price)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()
    print("Запись добавлена.")

@app.get("/join/")
def get_join():
    return render_template("join.html")

@app.post("/join/")
def post_join():
    name = request.form["name"]
    description = request.form["description"]
    price = float(request.form["price"])
    save_to_db(name, description, price)
    return render_template("main.html")

@app.get("/participants/")
def participants():
    sqlite_connection = sqlite3.connect("sql_python3.db")
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT * FROM db_developers")
    data = cursor.fetchall()
    cursor.close()
    sqlite_connection.close()
    return render_template("participants.html", data=data)

if __name__ == '__main__':
    app.run(port=5005, debug=True)
