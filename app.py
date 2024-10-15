import gradio as gr

def tts_fn(text):
    # Placeholder function for text-to-speech
    return "Generated message", None

app = gr.Blocks()
with app:
    with gr.Tab("T"):
        with gr.Row():
            with gr.Column():
                textbox = gr.TextArea(label="Text",
                                        placeholder="Type your sentence here",
                                        value="", elem_id=f"input")
            with gr.Column():
                text_output = gr.Textbox(label="Message")
                audio_output = gr.Audio(label="Output Audio", elem_id="audio")
                btn = gr.Button("Generate!")
                btn.click(tts_fn,
                            inputs=[textbox],
                            outputs=[text_output, audio_output])