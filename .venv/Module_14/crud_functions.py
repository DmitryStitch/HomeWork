import sqlite3

def initiate_db(db_shop="initiate_db.db"):
    connection = sqlite3.connect(db_shop)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(id INTEGER PRIMARY KEY,tittle TEXT NOT NULL,description TEXT ,price INTEGER NOT NULL)''')
    # for i in range(1, 5):
    #     cursor.execute(" INSERT INTO Products (tittle , description, price) VALUES (?, ?, ?)", (f"Продукт{i}", f"Описание{i}", i * 100))
    connection.commit()
    connection.close()

def get_all_products(db_shop="initiate_db.db"):
    connection = sqlite3.connect(db_shop)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products
