import os
from unidecode import unidecode
import tkinter as tk
from tkinter import ttk

def add_colaborator(root):
    new_colaborator_tab = tk.Toplevel(root) # Ventana para registrar al colaborador
    new_colaborator_tab.title("Nuevo colaborador")

    # Entrada para registrar el nombre del colaborador
    new_colaborator_name_label = tk.Label(new_colaborator_tab, text="Nombre del colaborador")
    new_colaborator_name_label.grid(row=0, column=0)
    new_colaborator_name_entry = tk.Entry(new_colaborator_tab, width=25)
    new_colaborator_name_entry.grid(row=0, column=1)

    # Entrada para registrar el enlace a la página del colaborador
    new_colaborator_link_label = tk.Label(new_colaborator_tab, text="Enlace a su página")
    new_colaborator_link_label.grid(row=1, column=0)
    new_colaborator_link_entry = tk.Entry(new_colaborator_tab, width=25)
    new_colaborator_link_entry.grid(row=1, column=1)

    # Entrada para registrar la imagen de miniatura asociada
    new_colaborator_thumbnail_label = tk.Label(new_colaborator_tab, text="Imagen que se mostrará")
    new_colaborator_thumbnail_label.grid(row=2, column=0)
    new_colaborator_thumbnail_combobox = ttk.Combobox(new_colaborator_tab, values=sorted(os.listdir("assets/img/")))
    new_colaborator_thumbnail_combobox.grid(row=2, column=1)

    # Entrada para registrar la contribución
    new_colaborator_contribution_label = tk.Label(new_colaborator_tab, text="Contribución")
    new_colaborator_contribution_label.grid(row=3, column=0)
    new_colaborator_contribution_text = tk.Text(new_colaborator_tab, width=25, height=10)
    new_colaborator_contribution_text.grid(row=3, column=1)

    # Botón para finalizar el registro
    add_new_colaborator_button = tk.Button(new_colaborator_tab, text="Agregar colaborador", command=lambda: add_new_colaborator(
        new_colaborator_name_entry.get(),
        new_colaborator_link_entry.get(),
        new_colaborator_thumbnail_combobox.get(),
        new_colaborator_contribution_entry.get(),
        new_colaborator_tab
    ))
    add_new_colaborator_button.grid(row=4, column=1)

def add_new_colaborator( # Función para registrar el colaborador
    name: str,
    link: str,
    thumbnail: str,
    contribution: str,
    tab
):
    with open("_data/colaboradores.yml", 'a') as f:
        f.write(f"""- name: {name}\n  link: {link}\n  thumbnail: {thumbnail}\n  contribution:{contribution}\n\n""")
    tab.destroy()
    tab.update()
