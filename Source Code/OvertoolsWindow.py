import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import platform

def apply_modern_style(root):
    style = ttk.Style()
    style.theme_use("xpnative")
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
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, folder_path)

def find_overwatch_folder():
    overwatch_path = None
    overwatch_path = ""
    return overwatch_path

root = tk.Tk()
root.title("OverTools Extractor")
apply_modern_style(root)

# Set the window icon
icon_path = "Designer.ico"
if os.path.exists(icon_path):
    root.iconbitmap(default=icon_path)

window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

header_label = ttk.Label(root, text="OverTools Extractor", font=("Helvetica", 24, "bold"), padding=10)
overwatch_folder_label = ttk.Label(root, text="Overwatch Game Folder:", padding=(10, 5))
output_folder_label = ttk.Label(root, text="Output Folder:", padding=(10, 5))
character_name_label = ttk.Label(root, text="Character Name:", padding=(10, 5))
style_name_label = ttk.Label(root, text="Style Name:", padding=(10, 5))

overwatch_path = find_overwatch_folder()
overwatch_folder_entry = ttk.Entry(root, width=40)
if overwatch_path:
    overwatch_folder_entry.insert(0, overwatch_path)

output_folder_entry = ttk.Entry(root)
character_name_entry = ttk.Entry(root, width=10)
style_name_entry = ttk.Entry(root, width=10)

export_button = ttk.Button(root, text="Export Skin", command=extract_models)

header_label.grid(row=0, column=0, columnspan=3, padx=10, pady=(20, 10))
overwatch_folder_label.grid(row=1, column=0, sticky="w", padx=(50, 5))
overwatch_folder_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
overwatch_browse_button = ttk.Button(root, text="Browse", command=lambda: browse_folder(overwatch_folder_entry))
overwatch_browse_button.grid(row=1, column=2, padx=(5, 50), pady=5)

output_folder_label.grid(row=2, column=0, sticky="w", padx=(50, 5))
output_folder_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
output_browse_button = ttk.Button(root, text="Browse", command=lambda: browse_folder(output_folder_entry))
output_browse_button.grid(row=2, column=2, padx=(5, 50), pady=5)

character_name_label.place(x=52, y=163, height=30, width=115, anchor="nw")
character_name_entry.place(x=160, y=168, height=20, width=140, anchor="nw")
style_name_entry.place(x=378, y=168, height=20, width=140, anchor="nw")
style_name_label.place(x=297, y=163, height=30, width=140, anchor="nw")

export_button.grid(row=5, column=0, columnspan=4, padx=10, pady=(40, 20), sticky="ew")


root.mainloop()