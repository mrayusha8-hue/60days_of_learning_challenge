import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="expense_tracker"
    )
    
def add_expense():
    # Get user input
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    payment_method = input("Enter payment method: ")

    # Connect to DB
    conn = connect_db()
    cursor = conn.cursor()   # pointer to the database

    # Insert query
    sql = """
    INSERT INTO expenses (date, category, amount, description, payment_method)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (date, category, amount, description, payment_method)

    # Execute and commit
    cursor.execute(sql, values) 
    conn.commit()

    print("Expense added successfully!")

    cursor.close()
    conn.close()

# Run the function
if __name__ == "__main__":  # python convention (makes code reusable, if later import main, the func wont run only get access)
    add_expense()

