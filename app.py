from nicegui import ui
palList = ["Anubis","Arsox","Astegon"]

def create_dropdown_items():
    return [ui.icon(f"PalworldBreedingTree/Icons/{pokemon}.png") for pokemon in palList]
custom_dropdown_items = create_dropdown_items()

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))
ui.select(custom_dropdown_items)











if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host="0.0.0.0", port=1072)