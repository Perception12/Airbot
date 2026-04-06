from tools.pricing_tools import get_ticket_price, check_available_destinations
from tools.booking_tools import create_booking, cancel_booking, check_flight_status
from tools.search_tools import get_todays_date

tools_description = [
    {
        "name": "get_ticket_price",
        "description": "Get the ticket price for a specific location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The DESTINATION location to get the ticket price for."
                }
            },
            "required": ["location"]
        }
    },
    {
        "name": "check_available_destinations",
        "description": "Check the available destinations.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "create_booking",
        "description": "Book a flight for a customer.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the customer."
                },
                "destination": {
                    "type": "string",
                    "description": "The destination for the flight."
                },
                "date": {
                    "type": "string",
                    "description": "The date of the flight (YYYY-MM-DD)."
                }
            },
            "required": ["name", "destination", "date"]
        }
    },
    {
        "name": "cancel_booking",
        "description": "Cancel a flight booking using the ticket ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_id": {
                    "type": "string",
                    "description": "The ticket ID of the flight booking to cancel."
                }
            },
            "required": ["ticket_id"]
        }
    },
    {
        "name": "check_flight_status",
        "description": "Check the status of a flight booking using the ticket ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_id": {
                    "type": "string",
                    "description": "The ticket ID of the flight booking to check."
                }
            },
            "required": ["ticket_id"]
        }
    },
    {
        "name": "get_todays_date",
        "description": "Get today's date.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
]

tools = [
    {"type": "function", "function": fn_descriptor} for fn_descriptor in tools_description
]

tool_dict = {
    "get_ticket_price": get_ticket_price,
    "check_available_destinations": check_available_destinations,
    "create_booking": create_booking,
    "cancel_booking": cancel_booking,
    "check_flight_status": check_flight_status,
    "get_todays_date": get_todays_date
}