from nicegui import ui
import os

# Path to the folder containing the icons
icon_folder = 'icons'

# Sample list of items with paths to the icons and their corresponding text
items = [
    (os.path.join(icon_folder, "apple.png"), "Apple"),
    (os.path.join(icon_folder, "banana.png"), "Banana"),
    (os.path.join(icon_folder, "grapes.png"), "Grapes"),
    (os.path.join(icon_folder, "strawberry.png"), "Strawberry"),
    (os.path.join(icon_folder, "pineapple.png"), "Pineapple")
]

def print_selected_item():
    selected_item = item_selector.value
    selected_label.text = f"You selected: {selected_item[1]}"
    icon_preview.source = selected_item[0]

# Create the main UI components
ui.label("Select an item from the list:")
item_selector = ui.select(items)
select_button = ui.button("Print Selected Item", on_click=print_selected_item)
selected_label = ui.label("")
icon_preview = ui.image("")  # Initialize an empty image




if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host="0.0.0.0", port=1072)