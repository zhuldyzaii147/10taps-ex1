import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 7")
root.geometry("400x200")

seconds = 0
running = False

def count():
    global seconds
    if running:
        seconds += 1
        label.config(text=f"Уақыт: {seconds} сек")
        root.after(1000, count)

def start_timer():
    global running
    if not running:
        running = True
        count()

def stop_timer():
    global running
    running = False

btn_start = tk.Button(root, text="Бастау", command=start_timer)
btn_start.pack(side="left", padx=50)

btn_stop = tk.Button(root, text="Тоқтату", command=stop_timer)
btn_stop.pack(side="right", padx=50)

label = tk.Label(root, text="Уақыт: 0 сек", font=("Arial", 14))
label.pack(pady=50)

root.mainloop()
