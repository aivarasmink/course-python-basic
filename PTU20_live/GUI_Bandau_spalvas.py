import sys  
import PySimpleGUI as sg

layout = [
    sg.Text("Koks tavo vardas?", font="Verdana 15"),
    [sg.Input(key="-NAME-", font="Terminal 15")],
    [sg.Button("Pasisveikinti", key="-HELLO-")],
    [sg.Button("Atsisveikinti", key="-BYE-")],