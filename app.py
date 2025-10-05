import gradio as gr
import os

def greet(name):
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    gr.Markdown("## Enter your name to get greeted")
    with gr.Row():
        name = gr.Textbox(label="Name")
        greet_btn = gr.Button("Greet")
    output = gr.Textbox(label="Greeting")
    greet_btn.click(fn=greet, inputs=[name], outputs=[output])

# Важно: Render передаёт порт через переменную окружения PORT
demo.launch(server_port=int(os.environ.get("PORT", 10000)))
