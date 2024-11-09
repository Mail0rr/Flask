from flask import Flask, request, send_file, url_for, render_template, abort, redirect
import sqlite3

app = Flask(__name__)

try:
    sqlite_connection = sqlite3.connect("sql_python3.db")
    cursor = sqlite_connection.cursor()
    print("Подключение успешно")

    create_table_query = '''CREATE TABLE IF NOT EXISTS db_developers (
        name TEXT NOT NULL UNIQUE,
        description TEXT NOT NULL,
        price REAL NOT NULL
    );
    '''
    cursor.execute(create_table_query)

    insert_query = '''INSERT INTO db_developers (name, description, price)
        VALUES (?, ?, ?);
    '''
    pizzas = [
        ("Пеперони", "Перетертые томаты, моцарелла, салями пикантные пепперони. Аллергены: злаки, лактоза.", 305),
        ("Сырная", "Моцарелла беби, фета, пармезан, горгонзола, проволоне, моцарелла. Аллергены: глютен, лактоза.", 280),
        ("Маргарита", "Перетертые томаты, моцарелла, базилик. Аллергены: злаки, лактоза.", 190)
    ]

    cursor.executemany(insert_query, pizzas)
    sqlite_connection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error connect to DB", error)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQL закрыто")

if __name__ == '__main__':
    app.run(port=5005, debug=True)
