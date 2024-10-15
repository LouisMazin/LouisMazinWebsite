import gradio as gr
import time

def greet(name):
    time.sleep(5)
    return "Hello, " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")