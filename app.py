import gradio as gr
import time

def test(x):
    time.sleep(4)
    return x

gr.Interface(test, "textbox", "textbox").queue().launch(server_port=8000)