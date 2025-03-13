import os
import pandas
import re
import numpy
from unidecode import unidecode
import tkinter as tk
from tkinter import ttk

def focus_next_window(event):
  event.widget.tk_focusNext().focus()
  return("break")


def check_material_updates(root):
    # Lee todos los entrenamientos registrados
    entrenamientos_registrados = pandas.read_csv('_data/material/entrenamientos.csv')['file'].to_numpy()
    # Lee el archivo libros.yml y extrae los nombres de todos libros (PDF)
    with open('_data/material/libros.yml', 'r') as f:
        libros = f.read()
    libros_registrados = re.findall("  file: \"(.*)\"", libros)
    # Une ambos arrays
    material_registrado = numpy.concatenate((entrenamientos_registrados, libros_registrados))

    # Para cada archivo no registrado
    for file in os.listdir('assets/pdf/Material/'):
        if file not in material_registrado:
            new_material_tab = tk.Toplevel(root)
            new_material_tab.title(file)

            material_filename_label = tk.Label(new_material_tab, text="Nombre del archivo")
            material_filename_label.grid(row=0, column=0)
            material_filename_label = tk.Label(new_material_tab, text=file)
            material_filename_label.grid(row=0, column=1)

            material_title_label = tk.Label(new_material_tab, text="Título")
            material_title_label.grid(row=1, column=0)
            material_title_textbox = tk.Entry(new_material_tab, width=25)
            material_title_textbox.grid(row=1, column=1)

            material_author_label = tk.Label(new_material_tab, text="Autor")
            material_author_label.grid(row=2, column=0)
            material_author_textbox = tk.Entry(new_material_tab, width=25)
            material_author_textbox.grid(row=2, column=1)

            material_topic_label = tk.Label(new_material_tab, text="Tema")
            material_topic_label.grid(row=3, column=0)
            material_topic_listbox = tk.Listbox(new_material_tab, selectmode="single", height=6, exportselection=0)
            material_topic_listbox.insert(tk.END, *["Álgebra", "Combinatoria", "Geometría", "Material introductorio", "Métodos de ataque de problemas", "Teoría de Números"])
            material_topic_listbox.grid(row=3, column=1)

            material_year_label = tk.Label(new_material_tab, text="Año de publicación")
            material_year_label.grid(row=4, column=0)
            material_year_textbox = tk.Entry(new_material_tab, width=25)
            material_year_textbox.grid(row=4, column=1)

            material_level_label = tk.Label(new_material_tab, text="Nivel")
            material_level_label.grid(row=5, column=0)
            material_level_textbox = tk.Entry(new_material_tab, width=25)
            material_level_textbox.grid(row=5, column=1)

            material_alttext_label = tk.Label(new_material_tab, text="Texto secreto")
            material_alttext_label.grid(row=6, column=0)
            material_alttext_textbox = tk.Entry(new_material_tab, width=25)
            material_alttext_textbox.grid(row=6, column=1)

            material_thumbnail_label = tk.Label(new_material_tab, text="Imagen de miniatura")
            material_thumbnail_label.grid(row=7, column=0)
            material_thumbail_combobox = ttk.Combobox(new_material_tab, values=sorted(os.listdir("assets/img/")))
            material_thumbail_combobox.grid(row=7, column=1)
            
            registrar_material_button = tk.Button(new_material_tab, text="Registrar material",
                command= lambda: registrar_material(
                material_title_textbox.get(),
                int(material_year_textbox.get()),
                material_thumbail_combobox.get(),
                material_topic_listbox.get(tk.ANCHOR),
                file,
                material_author_textbox.get(),
                material_level_textbox.get(),
                material_alttext_textbox.get(),
                new_material_tab
                )
            )
            registrar_material_button.grid(row=8, column=2)
            # material_is_book = tk.BooleanVar(new_material_tab, False)
            # content_entries = []
            # content_entries_text = []
                
            # material_is_book_checkbox = tk.Checkbutton(new_material_tab, text="Es un libro o cuadernillo", variable=material_is_book, command=show_contents, onvalue=True, offvalue=False).grid(row=6, column=2)

            # material_contents_label = tk.Label(new_material_tab, text="Contenidos")
            # material_contents_first_entry = tk.Entry(new_material_tab, width=25)
            # material_contents_add_button = tk.Button(material_tab, text="Agregar contenido", command=material_new_content_entry)

            
            root.wait_window(new_material_tab)

def registrar_material(
    title: str,
    year: int,
    thumbnail: str,
    topic: str,
    filename: str,
    author: str,
    level: str,
    alttext: str,
    tab
):
    with open("_data/material/entrenamientos.csv", 'a') as f:
        f.write(f""""{title}","{unidecode(title)}",{year},{thumbnail},{topic},{filename},"{author}",{level},"{alttext}"\n""")
    tab.destroy()
    tab.update()
