from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host="0.0.0.0", port=1072)