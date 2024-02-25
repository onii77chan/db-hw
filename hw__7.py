import sqlite3


def create_connection(db_connect):
    try:
        db_connect = sqlite3.connect(db_connect)
        return db_connect
    except sqlite3.Error as db_error:
        print(db_error)
        return None


def create_products_table(db_connect):
    create_table_sql = """CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR(200) NOT NULL,
        price REAL(10, 2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(create_table_sql)
        db_connect.commit()
    except sqlite3.Error as db_error:
        print(db_error)


def insert_product(db_connect, product):
    sql = """INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(sql, product)
        db_connect.commit()
    except sqlite3.Error as db_error:
        print(db_error)


def add_multiple_products(db_connect):
    product_data = [
        ("Товар 1", 10.99, 50),
        ("Товар 2", 5.49, 30),
    ]
    for product in product_data:
        insert_product(db_connect, product)


def update_quantity_by_id(db_connect, product_id, new_quantity):
    sql = """UPDATE products SET quantity = ? WHERE id = ?"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(sql, (new_quantity, product_id))
        db_connect.commit()
    except sqlite3.Error as db_error:
        print(db_error)


def update_price_by_id(db_connect, product_id, new_price):
    sql = """UPDATE products SET price = ? WHERE id = ?"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(sql, (new_price, product_id))
        db_connect.commit()
    except sqlite3.Error as db_error:
        print(db_error)


def delete_product_by_id(db_connect, product_id):
    sql = """DELETE FROM products WHERE id = ?"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(sql, (product_id,))
        db_connect.commit()
    except sqlite3.Error as db_error:
        print(db_error)


def print_all_products(db_connect):
    sql = """SELECT * FROM products"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as db_error:
        print(db_error)


def print_filtered_products(db_connect, price_limit, quantity_limit):
    sql = """SELECT * FROM products WHERE price < ? AND quantity > ?"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as db_error:
        print(db_error)


def search_products_by_title(db_connect, search_term):
    sql = """SELECT * FROM products WHERE product_title LIKE ?"""
    try:
        cursor = db_connect.cursor()
        cursor.execute(sql, ('%' + search_term + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as db_error:
        print(db_error)


connect = create_connection("hw.db")

create_products_table(connect)

add_multiple_products(connect)

update_quantity_by_id(connect, 1, 100)
update_price_by_id(connect, 2, 7.99)
delete_product_by_id(connect, 3)
print_all_products(connect)
print_filtered_products(connect, 100, 10)
search_products_by_title(connect, "мыло")

connect.close()
