# from Elioras_handbook import *
from material_update import *
from colaborators import *
from faq import *

root = tk.Tk()
root.title("Eliora, Guardiana de los Tomos Recuperados") # Nombre chido
root.bind_class("Entry", "<Tab>", focus_next_window)

# Botón para abrir el registro de material
check_material_update_button = tk.Button(root, text="Registrar nuevo material", command=lambda: check_material_updates(root=root))
check_material_update_button.pack()
# open_exam_register_button = tk.Button(root, text="Registrar selectivo", command=lambda: open_exam_register(root=root))
# open_exam_register_button.pack()

# Botón para añadir a un colaborador
add_colaborator_button = tk.Button(root, text="Agregar colaborador", command=lambda: add_colaborator(root=root))
add_colaborator_button.pack()
# Botón para añadir FAQ
add_faq_button = tk.Button(root, text="Pregunta frecuente", command=lambda: add_faq(root=root))
add_faq_button.pack()

root.mainloop()

