#   É onde fica o código para a Interface Gráfica
# Tudo o que existir de VISUAL vai ficar aqui
# É principalmente aqui que usaremos o PySimpleGUI

import PySimpleGUI as sg
from carbonmail.utils import iner_element_space

# Window => Janela
# Layout => O que vai mostrar na janela
#        => Lista de Listas
#           cada sublista é uma "linha da janela"
#           cada elemento é um componente visual
lista = ["Administradores", "Alunos"]


def get_layout():



    frame_campaing = [
         iner_element_space(500),
         [ 
             sg.Text("Selecione o Código"),
             sg.In(key ="Code", size = (30,1)),
             sg.FileBrowse("Selecionar",
             file_types = (("Códigos Python", "*.py"),),
             size = (15,1),
             ),
         ],
         [ 
             sg.Text("Selecione a lista de destinatários"),
             sg.Combo(lista, lista[1], key = "Lists",),
         ],
         iner_element_space(500),

    ]


    frame_email = [ 
        iner_element_space(500),
        [sg.Text("Insira o título", font = ("Helvetica 15"))],
        [sg.In(key = "Title", size = (62,1))],
        [sg.Text("Insira o Conteúdo", font = ("Helvetica 15"))],
        [sg.MLine(key = "Content", size = (60,10))],
        iner_element_space(500),
    ]
    
    layout = [ 
        iner_element_space(500), 
        [
            sg.Frame(
                "Configurações da Campanha",
                frame_campaing,
                element_justification = "c",
            )
        ],
        [ 
            sg.Frame(
                "Configurações do E-mail",
                frame_email,
                element_justification = "c",
            )
        ],
        [ 
            sg.Button(
                "Enviar E-mail",
                key = "Send",
                size = (15,1),
                pad = (10,(10,0)),
            ),
                sg.Button(
                "Gerenciar Listas",
                key = "ListEditor",
                size = (15,1),
                pad = (10,(10,0)),
            ),
        ],
        iner_element_space(500),

    ]

    return layout


def get_window():
    sg.theme("DarkBlue14")
    return sg.Window("Enviador de E-mail", get_layout(), element_justification="c")