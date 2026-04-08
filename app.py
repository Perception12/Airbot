import gradio as gr
from chatbot.engine import chat
from db.db_helper import init_db


if __name__ == "__main__":
    init_db()
    demo = gr.ChatInterface(fn=chat, title="Airbot - Your Airline Assistant")
    demo.launch(theme=gr.themes.Ocean())
