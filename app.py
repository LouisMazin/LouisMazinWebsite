#little gradio website
import gradio as gr

def greet():
    return "Hello !"

iface = gr.Interface(fn=greet, outputs="text")
iface.launch(share=False,server_name="0.0.0.0",server_port=1072)