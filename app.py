import gradio as gr
from chatbot.engine import chat


if __name__ == "__main__":
    demo = gr.ChatInterface(fn=chat, title="Airbot - Your Airline Assistant", description="Ask me anything about flight bookings, cancellations, and general inquiries about flights and services!")
    demo.launch()
