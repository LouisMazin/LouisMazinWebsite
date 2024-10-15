import gradio as gr
#list of each 1st elem of ./PalworldBreedingTree/data.csv
palList = []
with open("./PalworldBreedingTree/data.csv") as f:
    for i in f.readlines():
        palList.append(i.split(",")[0])
# Function to update the image based on selected Pokémon
def update_image(pokemon1, pokemon2):
    # Logic to determine the image path based on selected Pokémon
    # For example purposes, we will return a placeholder image path
    return f"images/{pokemon1}_{pokemon2}_breeding_tree.png"

# Function to handle button actions
def button_action(button_id):
    return f"You clicked {button_id}!"

# Create the Gradio interface
def main_interface(pokemon1, pokemon2):
    # Get the updated image based on selections
    image_path = update_image(pokemon1, pokemon2)
    return image_path

def create_dropdown_items():
    return [f'<img smrc="PalworldBreedingTree/Icons/{pokemon.lower()}.png" style="width:20px; height:20px; vertical-align:middle;"/> {pokemon}' for pokemon in palList]
custom_dropdown_items = create_dropdown_items()
# Set up the Gradio Interface with buttons
with gr.Blocks() as interface:
    with gr.Row():
        # ComboBoxes
        pokemon1_input = gr.Dropdown(choices=custom_dropdown_items, label="Select Pokémon 1")
        pokemon2_input = gr.Dropdown(choices=custom_dropdown_items, label="Select Pokémon 2")
    # Dynamic Image
    with gr.Row():
        with gr.Column():
            button1 = gr.Button("Button 1")
            button2 = gr.Button("Button 2")
            button3 = gr.Button("Button 3")
        image_output = gr.Image(label="Breeding Tree", type="filepath")
        with gr.Column():
            button4 = gr.Button("Button 1")
            button5 = gr.Button("Button 2")
            button6 = gr.Button("Button 3")
    # Update image when selections change
    pokemon1_input.change(fn=main_interface, inputs=[pokemon1_input, pokemon2_input], outputs=image_output)
    pokemon2_input.change(fn=main_interface, inputs=[pokemon1_input, pokemon2_input], outputs=image_output)

    # Assign actions to buttons
    button1.click(fn=lambda: button_action("Button 1"))
    button2.click(fn=lambda: button_action("Button 2"))
    button3.click(fn=lambda: button_action("Button 3"))
    button4.click(fn=lambda: button_action("Button 4"))
    button5.click(fn=lambda: button_action("Button 5"))
    button6.click(fn=lambda: button_action("Button 6"))


    
if __name__ == "__main__":
    print("Starting gradio server")
    interface.launch(share=False,server_name="0.0.0.0",server_port=1072,favicon_path="favicon.ico",show_api=False)
    