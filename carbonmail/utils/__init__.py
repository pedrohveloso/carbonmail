# Arquivo usado para transformar a pasta em pacote
# Ele é sempre executado ao importa este pacote
import PySimpleGUI as sg
def iner_element_space(width=100):
    return [sg.Text(" " * width, font=("Arial", 1))]