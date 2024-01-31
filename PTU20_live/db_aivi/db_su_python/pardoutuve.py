import sqlite3

connector = sqlite3.connect('product.db')
cursor = connector.cursor()

def create_table(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = '''
CREATE TABLE IF NOT EXISTS product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
quantity INTEGER,
price INTEGER
);
'''
    cursor.execute(query)
    connector.commit()

def insert_product(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print("Inserting a product...")
    name = input("Name: ")
    quantity = input("Quantity: ")
    price = input("Price: ")
    with connector:
        cursor.execute("INSERT INTO product (name, quantity, price)"
                       "VALUES (?, ?, ?)", (name, quantity, price))
    print("Done.")

def print_products(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print("Products List:")
    with connector:
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        for product in products:
            print(f"{product[0]} {product[1]}, {product[2]}, {product[3]}")

def find_by(connector: sqlite3.Connection, cursor: sqlite3.Cursor, find_by: str):
    query = f'SELECT * FROM product WHERE {find_by} = ?'
    search_argument = input(f"Find products by {find_by.replace('_', ' ')}: ")
    with connector:
        cursor.execute(query, (search_argument, ))
        products = cursor.fetchall()
        if len(products) > 0:
            for product in products:
                print(f"{product[0]} {product[1]}, {product[2]}, {product[3]}")
        else:
            print("No products found.")

if __name__ == "__main__":
    create_table(connector, cursor)
    while True:
        choice = input("Enter Command (h or help for help): ")
        if choice == 'h' or choice == 'help':
            print("Commands:")
            print("h or help - show this help")
            print("i or insert - insert a product")
            print("p or print - print all products")
            print("f or find - find product by name, quantity, or price")
            print("q or quit - quit the program")
        elif choice == 'i' or choice == 'insert':
            insert_product(connector, cursor)
        elif choice == 'p' or choice == 'print':
            print_products(connector, cursor)
        elif choice == 'f' or choice == 'find':
            find_by(connector, cursor, 'name')
            find_by(connector, cursor, 'quantity')
            find_by(connector, cursor, 'price')
        elif choice == 'q' or choice == 'quit':
            break
        else:
            print("Invalid command. Type h or help for help.")

    connector.close()
