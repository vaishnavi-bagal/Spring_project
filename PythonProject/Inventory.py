import pymysql

# Connect to MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='pass@word1',
    database='inventory'
)

cursor = conn.cursor()

def menu():
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

def add_item():
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    sql = "INSERT INTO items (name, quantity, price) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, qty, price))
    conn.commit()
    print("Item added successfully.")

def view_items():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    if items:
        for item in items:
            print(item)
    else:
        print("No items found.")

def update_item():
    id = int(input("Enter item ID to update: "))
    qty = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))
    sql = "UPDATE items SET quantity=%s, price=%s WHERE id=%s"
    cursor.execute(sql, (qty, price, id))
    conn.commit()
    print("Item updated successfully.")

def delete_item():
    id = int(input("Enter item ID to delete: "))
    sql = "DELETE FROM items WHERE id=%s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Item deleted successfully.")

while True:
    menu()
    choice = input("Enter choice: ")
    if choice == '1':
        add_item()
    elif choice == '2':
        view_items()
    elif choice == '3':
        update_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        print("Exiting...")
        break;

    else:
        print("Invalid choice.")

# Close connection when done
cursor.close()
conn.close()
