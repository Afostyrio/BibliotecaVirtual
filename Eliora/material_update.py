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
    libros_registrados = re.findall("  file: (.*)", libros)
    # Une ambos arrays
    material_registrado = numpy.concatenate((entrenamientos_registrados, libros_registrados))

    no_updates = True # Bandera para revisar si hay actualizaciones
    # Para cada archivo no registrado
    for file in os.listdir('assets/pdf/Material/'):
        if file not in material_registrado: # Si hay un archivo no asociado a un entrenamiento o un libro ("no está registrado")
            no_updates = False # Corrige la bandera
            new_material_tab = tk.Toplevel(root) # Crea una ventana donde se va a registrar el material
            new_material_tab.title(file)

            # Mencionamos el nombre del archivo para que abras el archivo y obtengas los datos.
            material_filename_label = tk.Label(new_material_tab, text="Nombre del archivo")
            material_filename_label.grid(row=0, column=0)
            material_filename_label = tk.Label(new_material_tab, text=file)
            material_filename_label.grid(row=0, column=1)

            # Entrada para registrar el título
            material_title_label = tk.Label(new_material_tab, text="Título") 
            material_title_label.grid(row=1, column=0)
            material_title_textbox = tk.Entry(new_material_tab, width=25)
            material_title_textbox.grid(row=1, column=1)

            # Entrada para registrar el autor
            material_author_label = tk.Label(new_material_tab, text="Autor")
            material_author_label.grid(row=2, column=0)
            material_author_textbox = tk.Entry(new_material_tab, width=25)
            material_author_textbox.grid(row=2, column=1)

            # Entrada para registrar el tema
            material_topic_label = tk.Label(new_material_tab, text="Tema")
            material_topic_label.grid(row=3, column=0)
            material_topic_combobox = ttk.Combobox(new_material_tab, values=["Álgebra", "Combinatoria", "Geometría", "Material introductorio", "Métodos de ataque de problemas", "Teoría de Números"])
            material_topic_combobox.grid(row=3, column=1)

            # Entrada para registrar el año de publicación
            material_year_label = tk.Label(new_material_tab, text="Año de publicación")
            material_year_label.grid(row=4, column=0)
            material_year_textbox = tk.Entry(new_material_tab, width=25)
            material_year_textbox.grid(row=4, column=1)

            # Entrada para registrar el nivel
            material_level_label = tk.Label(new_material_tab, text="Nivel")
            material_level_label.grid(row=5, column=0)
            material_level_textbox = tk.Entry(new_material_tab, width=25)
            material_level_textbox.grid(row=5, column=1)

            # Entrada para registrar el texto secreto
            material_alttext_label = tk.Label(new_material_tab, text="Texto secreto")
            material_alttext_label.grid(row=6, column=0)
            material_alttext_textbox = tk.Entry(new_material_tab, width=25)
            material_alttext_textbox.grid(row=6, column=1)

            # Entrada para registrar la miniatura
            material_thumbnail_label = tk.Label(new_material_tab, text="Imagen de miniatura")
            material_thumbnail_label.grid(row=7, column=0)
            material_thumbnail_combobox = ttk.Combobox(new_material_tab, values=sorted(os.listdir("assets/img/")))
            material_thumbnail_combobox.grid(row=7, column=1)
            
            # El siguiente código es para procesar libros
            material_is_book = tk.BooleanVar(new_material_tab, False)
            toc_entries = [] # Lista de contenidos (subtopics)
            material_toc_label = tk.Label(new_material_tab, text="Contenidos")

            def display_toc():
                if material_is_book.get(): # Si el material es un libro, se crea un apartado para agregar los contenidos (subtopics)
                    material_toc_label.grid(row=0, column=3)

                    first_toc_entry = tk.Entry(new_material_tab, width=25)
                    first_toc_entry.grid(row=1, column=3)
                    toc_entries.append(first_toc_entry)

                    material_add_entry_button.grid(row=2, column=3)
                else: # Si no lo es, hay que borrar el apartado
                    material_toc_label.grid_forget()
                    for entry in toc_entries: entry.grid_forget() # Borrar todas las entradas
                    toc_entries.clear() # Limpiar la tabla de contenidos
                    material_add_entry_button.grid_forget()
            
            def add_toc_entry(): # Función para agregar una nueva entrada para registrar contenido
                number_entries = len(toc_entries) + 1
                new_entry = tk.Entry(new_material_tab, width=25)
                new_entry.grid(row=number_entries, column=3)
                toc_entries.append(new_entry)
                material_add_entry_button.grid(row=number_entries+1, column=3)

            # Botón para agregar subtopics a un libro
            material_add_entry_button = tk.Button(new_material_tab, text="Agregar contenido", command= add_toc_entry)
            
            # Checkbox para decir si es un libro o no
            material_is_book_checkbox = tk.Checkbutton(new_material_tab, text="Es un libro o cuadernillo", variable=material_is_book, command= display_toc, onvalue=True, offvalue=False).grid(row=8, column=1)

            # Botón para completar el registro de material
            registrar_material_button = tk.Button(new_material_tab, text="Registrar material",
                command= lambda: registrar_material(
                material_title_textbox.get(),
                int(material_year_textbox.get()),
                material_thumbnail_combobox.get(),
                material_topic_combobox.get(),
                file,
                material_author_textbox.get(),
                material_level_textbox.get(),
                material_alttext_textbox.get(),
                material_is_book,
                toc_entries,
                new_material_tab
                )
            )
            registrar_material_button.grid(row=9, column=1)
            
            # Esperamos hasta acabar el registro de un material para empezar el siguiente
            root.wait_window(new_material_tab)
    if no_updates: # Si no hay actualizaciones,
        no_update_tab = tk.Toplevel(root)
        no_update_tab.title('Todo en orden') # Crea una ventana para indicar que todo está en orden
        no_update_label = tk.Label(no_update_tab, text="Los archivos están completos.\nNada nuevo que registrar.")
        no_update_label.pack()
        close_tab_button = tk.Button(no_update_tab, command= lambda: no_update_tab.destroy(), text="Cerrar esta ventana") # Se cierra con este botón
        close_tab_button.pack()

def registrar_material( # Función para registrar el material
    title: str,
    year: int,
    thumbnail: str,
    topic: str,
    filename: str,
    author: str,
    level: str,
    alttext: str,
    is_book,
    entries,
    tab
):
    if is_book.get():# Si es un libro, se registra en libros.yml
        with(open("_data/material/libros.yml", 'a')) as f:
            f.write(f"""- title: "{title}"\n  title_id: "{unidecode(title)}"\n  year: {year}\n  thumbnail: {thumbnail}\n  topic: {topic}\n  file: {filename}\n  author: "{author}"\n  level: {level}\n  alttext: "{alttext}"\n  content:\n""")
            for entry in entries:
                entry_text = entry.get()
                f.write(f"    - subtopic: {entry_text}\n")
            f.write("\n")
    else: # Si es un entrenamiento, se registra en entrenamientos.csv
        with open("_data/material/entrenamientos.csv", 'a') as f:
            f.write(f""""{title}","{unidecode(title)}",{year},{thumbnail},{topic},{filename},"{author}",{level},"{alttext}"\n""")
    tab.destroy() # Cierra la ventana al terminar el registro del material nuevo.
    tab.update()
