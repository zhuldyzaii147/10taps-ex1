import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 6")
root.geometry("400x200")

def add_numbers():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        result_label.config(text=f"Қосындысы: {a + b}", fg="black")
    except ValueError:
        result_label.config(text="Қате: Бүтін сан енгізіңіз!", fg="red")

entry1 = tk.Entry(root, width=10)
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=10)
entry2.pack(pady=5)

btn = tk.Button(root, text="Қосу", command=add_numbers)
btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
