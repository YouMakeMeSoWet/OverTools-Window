import os
import customtkinter as ctk
from tkinter import filedialog
import subprocess
import platform

def apply_modern_style(root):
    if platform.system() == "Windows":
        root.attributes("-alpha", 0.98)

def extract_models():
    overwatch_path = overwatch_folder_entry.get()
    export_path = output_folder_entry.get()
    character_name = character_name_entry.get()
    style_name = style_name_entry.get()
    skin_name = f"{character_name}|skin={style_name}"
    command = ['DataTool.exe', overwatch_path, 'extract-unlocks', export_path, skin_name]
    subprocess.run(command)

def browse_folder(entry_widget):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_widget.delete(0, ctk.END)
        entry_widget.insert(0, folder_path)

def find_overwatch_folder():
    overwatch_path = None
    overwatch_path = ""
    return overwatch_path

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("OverTools Window")
apply_modern_style(root)

window_width = 600
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

header_label = ctk.CTkLabel(root, text="OverTools Window", font=("Helvetica", 44, "bold"))
overwatch_folder_label = ctk.CTkLabel(root, text="Overwatch Game Folder:")
output_folder_label = ctk.CTkLabel(root, text="Output Model Folder:")
character_name_label = ctk.CTkLabel(root, text="Character Name:")
style_name_label = ctk.CTkLabel(root, text="Style Name:")

overwatch_path = find_overwatch_folder()
overwatch_folder_entry = ctk.CTkEntry(root, width=240)
if overwatch_path:
    overwatch_folder_entry.insert(0, overwatch_path)

output_folder_entry = ctk.CTkEntry(root, width=240)
character_name_entry = ctk.CTkEntry(root, width=140)
style_name_entry = ctk.CTkEntry(root, width=140)

export_button = ctk.CTkButton(root, text="Export Skin", command=extract_models, width=570)

header_label.place(x=300, y=45, anchor="center")
overwatch_folder_label.place(x=30, y=100)
overwatch_folder_entry.place(x=180, y=100)
overwatch_browse_button = ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(overwatch_folder_entry))
overwatch_browse_button.place(x=430, y=100)

output_folder_label.place(x=30, y=140)
output_folder_entry.place(x=180, y=140)
output_browse_button = ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(output_folder_entry))
output_browse_button.place(x=430, y=140)

character_name_label.place(x=30, y=180)
character_name_entry.place(x=140, y=180)
style_name_label.place(x=290, y=180)
style_name_entry.place(x=370, y=180)

export_button.place(x=15, y=245)

root.mainloop()
