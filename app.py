import gradio as gr

def generate(prompt):
    return f"Ты ввела: {prompt}"

with gr.Blocks() as demo:
    gr.Markdown("## Пример WebUI на Render (без Hugging Face)")
    prompt = gr.Textbox(label="Промпт")
    output = gr.Textbox(label="Результат")
    btn = gr.Button("Сгенерировать")
    btn.click(fn=generate, inputs=prompt, outputs=output)

demo.launch()
