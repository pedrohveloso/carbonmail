#   É onde fica o código para a Interface Gráfica
# Tudo o que existir de VISUAL vai ficar aqui
# É principalmente aqui que usaremos o PySimpleGUI

from carbonmail.email_sender.view import get_window
import PySimpleGUI as sg
from carbonmail.utils import iner_element_space

lista = ["Administradores", "Alunos"]

def get_layout():
    
    
    frame_list = [
       iner_element_space(600),
        [
           sg.Text("Selecione a lista:"),
           sg.Combo(lista, default_value=lista[1], key="List"),
        ],
        [
           sg.Text("Criar uma lista:"),
           sg.In(key="ListName"),
           sg.Button("Criar", key="Create", size=(10,1)),
        ],
        [
           sg.Button(
              "Deletar a lista",
              key = "Delete",
              size = (15,1),
              pad=(5, (7,7)),
            ),
           sg.Button(
              "Mostrar contatos",
              key = "Delete",
              size = (15,1),
              pad=(5, (7,7)),
            ),
           
        ],
        iner_element_space(600),
    ]


    frame_import = [
       iner_element_space(600),

       [
            sg.Text(
               "Selecione o arquivo (CSV):",
               tooltip="Cabeçalhos: name e e-mail",
            ),
            sg.In(key="CSV"),
            sg.FileBrowse(
               "Selecionar",
               file_types=(("csv", "*.csv"),),
               tooltip="Cabeçalhos: name e e-mail",
            ),
       ],
       [
          sg.Button(
             "Importar Contatos",
             key="Import",
             size=(15,1),
             pad=((0,0), (7,7)),
          )
       ],
       iner_element_space(600),
    ]

    frame_add = [ 
       iner_element_space(600),
       [
          sg.Text("Insira um nome:"),
          sg.In(key="Name")
       ],
       [
          sg.Text("Insira um e-mail:"),
          sg.In(key="e-mail")
       ],
       [
          sg.Button(
             "Adicionar Contato",
            key="Add",
            size=(15,1),
            pad=(0,(7, 7)),
         )
       ],
       iner_element_space(600),
    ]
    
   
    layout = [
       [
          sg.Frame(
             "Configurações da Lista",
            frame_list,
            element_justification="c",
          )
       ],
       [
          sg.Frame(
             "Importar Contatos",
             frame_import,
             element_justification="c",
          )
       ],
       [
          sg.Frame(
             "Adicionar Contato",
             frame_add,
             element_justification="c",
          )
       ],
       [
          sg.Button(
             "Voltar",
             key="Back",
             size=(15,1),
             pad=((0,0), (7,7)),

          )
       ],
       iner_element_space(600),
      ]
    
    return layout

def get_window():
    sg.theme("DarkBlue14")
    return sg.Window("Editor de Lista", get_layout(), element_justification="c")