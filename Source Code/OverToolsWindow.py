import customtkinter as ctk
from tkinter import filedialog, messagebox
import subprocess
import platform
import os

header_label = None
overwatch_folder_label = None
output_folder_label = None
character_name_label = None
style_name_label = None
map_name_label = None


def apply_modern_style(root):
    if platform.system() == "Windows":
        root.attributes("-alpha", 0.98)


def extract_models(extract_type):
    overwatch_path = overwatch_folder_entry.get()
    export_path = output_folder_entry.get()
    character_name = character_name_entry.get()

    if not os.path.exists(overwatch_path):
        messagebox.showerror("Error", "Overwatch folder path is invalid.")
        return

    if not os.path.exists(export_path):
        messagebox.showerror("Error", "Output folder path is invalid.")
        return

    if not character_name:
        messagebox.showerror("Error", "Character name is required.")
        return

    if extract_type == "highlight_intros":
        highlight_intro_name = f"{character_name}|highlightintro={style_name_entry.get()}"
        command = ['DataTool.exe', overwatch_path, 'extract-unlocks', export_path, highlight_intro_name]
    elif extract_type == "victory_poses":
        victory_pose_name = f"{character_name}|victorypose={style_name_entry.get()}"
        command = ['DataTool.exe', overwatch_path, 'extract-unlocks', export_path, victory_pose_name]
    elif extract_type == "maps":
        map_name = map_name_entry.get()
        if not map_name:
            messagebox.showerror("Error", "Map name is required.")
            return
        command = ['DataTool.exe', overwatch_path, 'extract-maps', export_path, map_name]
    else:
        skin_name = f"{character_name}|skin={style_name_entry.get()}"
        command = ['DataTool.exe', overwatch_path, 'extract-unlocks', export_path, skin_name]

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Extraction completed successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error",
                             "DataTool.exe not found. Ensure it is in the same directory as this script or provide the full path.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred during extraction: {e}")


def browse_folder(entry_widget):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_widget.delete(0, ctk.END)
        entry_widget.insert(0, folder_path)


def hide_common_elements():
    global header_label, overwatch_folder_label, output_folder_label, character_name_label, style_name_label, map_name_label
    header_label.place_forget()
    overwatch_folder_label.place_forget()
    output_folder_label.place_forget()
    character_name_label.place_forget()
    style_name_label.place_forget()
    map_name_label.place_forget()
    overwatch_folder_entry.place_forget()
    output_folder_entry.place_forget()
    character_name_entry.place_forget()
    style_name_entry.place_forget()
    map_name_entry.place_forget()
    overwatch_browse_button.place_forget()
    output_browse_button.place_forget()
    export_button.place_forget()


def show_skins_tab():
    global header_label, overwatch_folder_label, output_folder_label, character_name_label, style_name_label
    hide_common_elements()

    header_label.configure(text="OverTools Skins")
    header_label.place(x=300, y=45, anchor="center")

    overwatch_folder_label.place(x=30, y=100)
    overwatch_folder_entry.place(x=180, y=100)
    overwatch_browse_button.place(x=430, y=100)

    output_folder_label.place(x=30, y=140)
    output_folder_entry.place(x=180, y=140)
    output_browse_button.place(x=430, y=140)

    character_name_label.place(x=30, y=180)
    character_name_entry.place(x=140, y=180)

    style_name_label.configure(text="Skin Name:")
    style_name_label.place(x=295, y=180)
    style_name_entry.place(x=370, y=180)

    export_button.configure(command=lambda: extract_models("skins"))
    export_button.place(x=15, y=245)


def show_highlight_intros_tab():
    global header_label, overwatch_folder_label, output_folder_label, character_name_label, style_name_label, style_name_entry
    hide_common_elements()

    header_label.configure(text="OverTools Highlight Intros")
    header_label.place(x=300, y=45, anchor="center")

    overwatch_folder_label.place(x=30, y=100)
    overwatch_folder_entry.place(x=180, y=100)
    overwatch_browse_button.place(x=430, y=100)

    output_folder_label.place(x=30, y=140)
    output_folder_entry.place(x=180, y=140)
    output_browse_button.place(x=430, y=140)

    character_name_label.place(x=30, y=180)
    character_name_entry.place(x=140, y=180)

    style_name_label.configure(text="HL Name:")
    style_name_label.place(x=302, y=180)
    style_name_entry.place(x=370, y=180)

    export_button.configure(command=lambda: extract_models("highlight_intros"))
    export_button.place(x=15, y=245)


def show_victory_pose_tab():
    global header_label, overwatch_folder_label, output_folder_label, character_name_label, style_name_label
    hide_common_elements()

    header_label.configure(text="OverTools Victory Pose")
    header_label.place(x=300, y=45, anchor="center")

    overwatch_folder_label.place(x=30, y=100)
    overwatch_folder_entry.place(x=180, y=100)
    overwatch_browse_button.place(x=430, y=100)

    output_folder_label.place(x=30, y=140)
    output_folder_entry.place(x=180, y=140)
    output_browse_button.place(x=430, y=140)

    character_name_label.place(x=30, y=180)
    character_name_entry.place(x=140, y=180)

    style_name_label.configure(text="VP Name:")
    style_name_label.place(x=302, y=180)
    style_name_entry.place(x=370, y=180)

    export_button.configure(command=lambda: extract_models("victory_poses"))
    export_button.place(x=15, y=245)


def show_maps_tab():
    global header_label, overwatch_folder_label, output_folder_label, map_name_label
    hide_common_elements()

    header_label.configure(text="OverTools Maps")
    header_label.place(x=300, y=45, anchor="center")

    overwatch_folder_label.place(x=30, y=100)
    overwatch_folder_entry.place(x=180, y=100)
    overwatch_browse_button.place(x=430, y=100)

    output_folder_label.place(x=30, y=140)
    output_folder_entry.place(x=180, y=140)
    output_browse_button.place(x=430, y=140)

    map_name_label.place(x=180, y=180)
    map_name_entry.place(x=260, y=180)

    export_button.configure(command=lambda: extract_models("maps"))
    export_button.place(x=15, y=245)


def create_maps_tab(root):
    switch_tab1 = ctk.CTkButton(root, text="Skins", width=50, command=show_skins_tab)
    switch_tab1.place(x=150, y=305)

    switch_tab2 = ctk.CTkButton(root, text="Highlight Intros", width=50, command=show_highlight_intros_tab)
    switch_tab2.place(x=205, y=305)

    switch_tab3 = ctk.CTkButton(root, text="Victory Pose", width=50, command=show_victory_pose_tab)
    switch_tab3.place(x=309, y=305)

    switch_tab4 = ctk.CTkButton(root, text="Maps", width=50, command=show_maps_tab)
    switch_tab4.place(x=397, y=305)


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("OverTools Window")
apply_modern_style(root)

window_width, window_height = 600, 330
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

header_label = ctk.CTkLabel(root, text="OverTools Window", font=("Helvetica", 44, "bold"))
overwatch_folder_label = ctk.CTkLabel(root, text="Overwatch Game Folder:")
output_folder_label = ctk.CTkLabel(root, text="Output Model Folder:")
character_name_label = ctk.CTkLabel(root, text="Character Name:")
style_name_label = ctk.CTkLabel(root, text="Style Name:")
map_name_label = ctk.CTkLabel(root, text="Map Name:")

overwatch_folder_entry = ctk.CTkEntry(root, width=240)
output_folder_entry = ctk.CTkEntry(root, width=240)
character_name_entry = ctk.CTkEntry(root, width=140)
style_name_entry = ctk.CTkEntry(root, width=140)
map_name_entry = ctk.CTkEntry(root, width=140)

export_button = ctk.CTkButton(root, text="Export", width=570)
overwatch_browse_button = ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(overwatch_folder_entry))
output_browse_button = ctk.CTkButton(root, text="Browse", command=lambda: browse_folder(output_folder_entry))

show_skins_tab()
create_maps_tab(root)
root.mainloop()
