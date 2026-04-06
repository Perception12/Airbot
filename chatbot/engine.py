import os
from openai import OpenAI
from dotenv import load_dotenv
from db.db_helper import init_db
from tools.description import tools
from tools.handler import handle_tool_calls

load_dotenv()
init_db()

openai = OpenAI()
MODEL = "gpt-4.1-mini"

system_message = """You are an airline assistant called Airbot. 
You help customers with their flight bookings, cancellations, 
and general inquiries about flights and services. 
Always be polite and helpful.


In order to successfully book a flight, you must:
1. Ask the customer for their full name, desired destination and travel date.
2. Verify the availability of the desired destination.
3. Confirm the booking details with the customer before finalizing.
4. Finalize the booking and return a unique ticket ID to the customer.


Do not make assumptions on destination availability.
Always ask for necessary details before calling a function.
"""

def chat(message, history):
    history = [{"role": h["role"], "content": h["content"]} for h in history]

    messages = [{"role": "system", "content": system_message}] + \
        history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools
    )

    iterations = 0
    max_iterations = 5  # Prevent infinite loops

    while response.choices[0].finish_reason == "tool_calls" and iterations < max_iterations:
        message = response.choices[0].message
        tool_response = handle_tool_calls(message)
        messages.append(message)
        messages.extend(tool_response)

        response = openai.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools
        )
        iterations += 1

    if iterations >= max_iterations:
        return "I'm sorry, but I'm having trouble completing this request. Please try again or contact support."

    return response.choices[0].message.content