import os
from unidecode import unidecode
import tkinter as tk
from tkinter import ttk

def add_faq(root):
    new_faq_tab = tk.Toplevel(root) # Ventana para registrar al colaborador
    new_faq_tab.title("Nueva pregunta frecuente")

    # Entrada para registrar la pregunta frecuente
    new_faq_question_label = tk.Label(new_faq_tab, text="Pregunta")
    new_faq_question_label.grid(row=0, column=0)
    new_faq_question_entry = tk.Text(new_faq_tab, width=25, height=10)
    new_faq_question_entry.grid(row=0, column=1)

    # Entrada para registrar su respuesta
    new_faq_answer_label = tk.Label(new_faq_tab, text="Respuesta")
    new_faq_answer_label.grid(row=1, column=0)
    new_faq_answer_entry = tk.Text(new_faq_tab, width=25, height=10)
    new_faq_answer_entry.grid(row=1, column=1)

    # Botón para finalizar el registro
    add_new_faq_button = tk.Button(new_faq_tab, text="Agregar pregunta frecuente", command=lambda: add_new_faq(
        new_faq_question_entry.get("1.0",tk.END),
        new_faq_answer_entry.get("1.0",tk.END),
        new_faq_tab
    ))
    add_new_faq_button.grid(row=2, column=1)

def add_new_faq( # Función para registrar la pregunta frecuente
    question: str,
    answer: str,
    tab
):
    with open("_data/faqs.yml", 'a') as f:
        f.write(f"""- question: {question}\n  answer: {answer}\n\n""")
    tab.destroy()
    tab.update()
