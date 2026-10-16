import tkinter as tk
import random

root = tk.Tk()
root.title("Тапсырма 8")
root.geometry("500x400")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

def draw_circle(event):
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
    rand_color = random.choice(colors)
    x, y = event.x, event.y
    r = 15 
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=rand_color)

canvas.bind("<Button-1>", draw_circle)

root.mainloop()
