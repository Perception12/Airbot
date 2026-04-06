import sqlite3

def run_query(query, params=()):
    db = sqlite3.connect("airline_data.db")
    cursor = db.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results

def init_db():
    db = sqlite3.connect("airline_data.db")
    cursor = db.cursor()

    # Create bookings table if it doesn't exist
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS bookings (ticket_id TEXT PRIMARY KEY, name TEXT, destination TEXT, date DATE)")

    
    # Create ticket_prices table if it doesn't exist
    cursor.execute("""CREATE TABLE IF NOT EXISTS ticket_prices (
                        location TEXT PRIMARY KEY,
                        price NUMERIC
                    )""")

    # Check if the ticket_prices table is empty
    cursor.execute("SELECT COUNT(*) FROM ticket_prices")
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert initial ticket prices
        prices = [
            ("new york", 300),
            ("los angeles", 250),
            ("chicago", 200),
            ("miami", 350),
            ("dallas", 280),
            ("berlin", 400),
            ("paris", 450),
            ("tokyo", 500),
            ("london", 420),
        ]
        cursor.executemany(
            "INSERT INTO ticket_prices (location, price) VALUES (?, ?)", prices)
        
    db.commit()
    db.close()