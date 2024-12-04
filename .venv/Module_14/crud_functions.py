import sqlite3

def initiate_db(db_shop="initiate_db.db"):
    connection = sqlite3.connect(db_shop)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(id INTEGER PRIMARY KEY, tittle TEXT NOT NULL, description TEXT ,price INTEGER NOT NULL)''')
    for i in range(1, 5):
        cursor.execute(" INSERT INTO Products (tittle , description, price) VALUES (?, ?, ?)", (f"Продукт{i}", f"Описание{i}", i * 100))

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, age INTEGER NOT NULL, balance INTEGER NOT NULL)''')

    connection.commit()
    connection.close()
def add_user(username, email, age):
    connection = sqlite3.connect("initiate_db.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, 1000)", (f"{username}", f"{email}", f"{age}"))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("initiate_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    connection.close()
    if check_user.fetchone() is None:
        return False
    else:
        return True
def get_all_products(db_shop="initiate_db.db"):
    connection = sqlite3.connect(db_shop)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products
