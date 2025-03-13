# from Elioras_handbook import *
from material_update import *


root = tk.Tk()
root.title("Eliora, la última bibliotecaria")
root.bind_class("Entry", "<Tab>", focus_next_window)

check_material_update_button = tk.Button(root, text="Registrar nuevo material", command=lambda: check_material_updates(root=root))
check_material_update_button.pack()

# open_exam_register_button = tk.Button(root, text="Registrar selectivo", command=lambda: open_exam_register(root=root))
# open_exam_register_button.pack()

root.mainloop()

