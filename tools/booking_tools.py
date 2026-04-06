from db.db_helper import run_query
from uuid import uuid4
import datetime

def create_booking(name, destination, date):
    ticket_id = str(uuid4())
    
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    
    run_query("INSERT INTO bookings (ticket_id, name, destination, date) VALUES (?, ?, ?, ?)", (ticket_id, name, destination, date))
    return f"Flight to {destination} on {date} has been booked successfully! Your ticket ID is {ticket_id}."

def cancel_booking(ticket_id):
    run_query("DELETE FROM bookings WHERE ticket_id = ?", (ticket_id,))
    return f"Flight with ticket ID {ticket_id} has been cancelled successfully!"

def check_flight_status(ticket_id):
    result = run_query("SELECT * FROM bookings WHERE ticket_id = ?", (ticket_id,))
    if result:
        return f"Flight with ticket ID {ticket_id} is confirmed and scheduled as planned."
    else:
        return f"No booking found with ticket ID {ticket_id}."