import PySimpleGUI as sg
import pyperclip
import string
import random

def create_window():
    sg.theme("Default1")
    sg.set_options(font=("Arial", 12))

    layout = [
        [sg.Text("Generate a random password", font=("Arial", 18, "bold"), expand_x=True, pad=20)],

        [sg.Input("", key="-PASSWORD-", disabled=True, font=("Consolas", 20), size=(25, 1)),
         sg.Button("Copy", key="-COPY-"), 
         sg.Button("Generate", key="-GENERATE-", button_color="#66c2ff")],

        [sg.Sizer(0, 25)],

        [sg.Text("Customize your password: ", font=("Arial", 12, "bold"))],

        [sg.HorizontalSeparator()],

        [sg.Text("Length: 12", key="-LENGTH_VALUE-", size=(10, 1), justification="left"),
         sg.Slider(key="-LENGTH-", range=(1, 50), default_value=12, orientation="horizontal", 
                   enable_events=True, disable_number_display=True, expand_x=True)],

        [sg.Checkbox("Uppercase", key="-UPPERCASE-", default=True, expand_x=True), 
         sg.Checkbox("Lowercase", key="-LOWERCASE-", default=True, expand_x=True), 
         sg.Checkbox("Numbers", key="-NUMBERS-", default=True, expand_x=True), 
         sg.Checkbox("Symbols", key="-SYMBOLS-", default=True, expand_x=True)]
    ]
    return sg.Window("Password Generator", layout, finalize=True, text_justification="center")


def generate_password(length, uppercase, lowercase, numbers, symbols):
    chars = ""
    if uppercase: chars += string.ascii_uppercase
    if lowercase: chars += string.ascii_lowercase
    if numbers: chars += string.digits
    if symbols: chars += string.punctuation
    if chars == "": return

    return "".join(random.choice(chars) for i in range(length))


window = create_window()
password = generate_password(12, True, True, True, True)
window["-PASSWORD-"].update(password)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == "-GENERATE-":
        length = int(values["-LENGTH-"])
        uppercase = values["-UPPERCASE-"]
        lowercase = values["-LOWERCASE-"]
        numbers = values["-NUMBERS-"]
        symbols = values["-SYMBOLS-"]
        
        password = generate_password(length, uppercase, lowercase, numbers, symbols)
        window["-PASSWORD-"].update(password)
    
    elif event == "-COPY-":
        password = values["-PASSWORD-"]
        if password != "":
            pyperclip.copy(password)

    window["-LENGTH_VALUE-"].update(f"Length: {int(values['-LENGTH-'])}")

window.close()
