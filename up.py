import json
import tkinter as tk
from tkinter import filedialog, messagebox

def add_entry():
    new_entry = {
        "name": entry_name.get(),
        "choice": entry_choice.get(),
        "website": "none",
        "mediafire": entry_mediafire.get(),
        "wget": "none",
        "link": "none",
        "page": "false"
    }

    # Đọc nội dung hiện tại từ tệp JSON
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Thêm đối tượng mới vào danh sách
        data["data"].append(new_entry)

        # Ghi lại nội dung vào tệp JSON
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=2)

        messagebox.showinfo("Success", "The entry has been added to the JSON file.")


    except FileNotFoundError:
        messagebox.showerror("Error", "Please select a valid JSON file.")

def choose_json_file():
    global json_file_path
    json_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    entry_json_file_path.delete(0, tk.END)
    entry_json_file_path.insert(0, json_file_path)

# Tạo cửa sổ
window = tk.Tk()
window.title("Add Entry")

# Tạo và định vị các thành phần giao diện
tk.Label(window, text="Name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Choice:").pack()
entry_choice = tk.Entry(window)
entry_choice.pack()

tk.Label(window, text="Mediafire Link:").pack()
entry_mediafire = tk.Entry(window)
entry_mediafire.pack()

tk.Label(window, text="JSON File Path:").pack()
entry_json_file_path = tk.Entry(window)
entry_json_file_path.pack()

tk.Button(window, text="Choose JSON File", command=choose_json_file).pack()

tk.Button(window, text="Add Entry", command=add_entry).pack()

window.mainloop()
