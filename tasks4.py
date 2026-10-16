import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 4")
root.geometry("500x300")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

# Қызыл шеңбер, жасыл тікбұрыш, көк үшбұрыш
canvas.create_oval(50, 50, 150, 150, fill="red")
canvas.create_rectangle(200, 50, 350, 150, fill="green")
canvas.create_polygon(420, 50, 370, 150, 470, 150, fill="blue")

root.mainloop()
