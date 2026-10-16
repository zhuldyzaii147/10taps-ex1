import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 5")
root.geometry("400x300")

def change_color(selected_color):
    if selected_color == "Сары":
        root.config(bg="yellow")
    elif selected_color == "Сұр":
        root.config(bg="gray")
    elif selected_color == "Қызғылт":
        root.config(bg="pink")
    else:
        root.config(bg="white")

color_var = tk.StringVar(root)
color_var.set("Ақ") 

options = ["Ақ", "Сары", "Сұр", "Қызғылт"]
menu = tk.OptionMenu(root, color_var, *options, command=change_color)
menu.pack(pady=20)

root.mainloop()
