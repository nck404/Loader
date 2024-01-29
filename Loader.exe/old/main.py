import tkinter as tk
from tkinter import ttk
import json
from tkinter import filedialog

json_file_path = None  # Biến lưu trữ đường dẫn file JSON đã chọn

def add_entry_to_json(new_entry):
    global json_file_path
    try:
        if json_file_path is None:
            json_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            if not json_file_path:
                return False

        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            if "data" not in data:
                data["data"] = []
            data["data"].append(new_entry)

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

        return True
    except Exception as e:
        print(f"Error adding entry to JSON: {e}")
        return False

def on_add_entry_click():
    new_entry = {
        "name": name_entry.get(),
        "choice": choice_entry.get(),
        "website": website_entry.get(),
        "mediafire": mediafire_entry.get(),
        "wget": wget_entry.get(),
        "link": link_entry.get(),
        "page": page_entry.get()
    }

    if add_entry_to_json(new_entry):
        result_label.config(text=f"Entry added successfully {name_entry.get()}")
    else:
        result_label.config(text="Failed to add entry.")
window = tk.Tk()
window.title("Add Entry to JSON Tool")

# Tạo và định vị các widget
name_label = ttk.Label(window, text="Name:")
name_entry = ttk.Entry(window)

choice_label = ttk.Label(window, text="Choice:")
choice_entry = ttk.Entry(window)

website_label = ttk.Label(window, text="Website:")
website_entry = ttk.Entry(window)

mediafire_label = ttk.Label(window, text="Mediafire:")
mediafire_entry = ttk.Entry(window)

wget_label = ttk.Label(window, text="Wget:")
wget_entry = ttk.Entry(window)

link_label = ttk.Label(window, text="Link:")
link_entry = ttk.Entry(window)

page_label = ttk.Label(window, text="Page:")
page_entry = ttk.Entry(window)

add_button = ttk.Button(window, text="Add Entry", command=on_add_entry_click)

result_label = ttk.Label(window, text="")

# Định vị các widget trên cửa sổ
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

choice_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
choice_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

website_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
website_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

mediafire_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
mediafire_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

wget_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
wget_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

link_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
link_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

page_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
page_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

add_button.grid(row=7, column=0, columnspan=2, pady=10)

result_label.grid(row=8, column=0, columnspan=2)

# Hiển thị cửa sổ
window.mainloop()
