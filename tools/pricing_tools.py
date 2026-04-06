from db.db_helper import run_query

def set_ticket_price(location, price):
    run_query("INSERT INTO ticket_prices (location, price) VALUES (?, ?) ON CONFLICT(location) DO UPDATE SET price = ?", (location.lower(), price, price))

    return f"Ticket price for {location} has been set to {price}."

def get_ticket_price(location):
    result = run_query("SELECT price FROM ticket_prices WHERE location = ?", (location.lower(),))
    if result:
        return f"The ticket price for {location} is ${result[0][0]}."
    else:
        return f"Price not available for {location}."
    
def check_available_destinations():
    results = run_query("SELECT location FROM ticket_prices")
    destinations = [row[0].title() for row in results]
    return f"Available destinations: {', '.join(destinations)}."