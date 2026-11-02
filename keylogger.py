import tkinter as tk
from datetime import datetime

def save_text():
    text = box.get("1.0", tk.END).strip()

    with open("key_log.txt", "a") as f:
        f.write(str(datetime.now()) + ": " + text + "\n")

    status.config(text="Input saved!")

root = tk.Tk()
root.title("Keyboard Logger")
root.geometry("400x300")

tk.Label(root, text="Enter text:").pack()

box = tk.Text(root, height=8, width=40)
box.pack()

tk.Button(root, text="Save Input", command=save_text).pack()

status = tk.Label(root, text="")
status.pack()

root.mainloop()