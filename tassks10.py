import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 10")
root.geometry("400x300")

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    result_label.config(text=f"Пайдаланушы мәліметтері:\nАты-жөні: {name}\nЖасы: {age}")

tk.Label(root, text="Аты-жөні:").pack(pady=2)
name_entry = tk.Entry(root, width=25)
name_entry.pack(pady=5)

tk.Label(root, text="Жасы:").pack(pady=2)
age_entry = tk.Entry(root, width=10)
age_entry.pack(pady=5)

btn = tk.Button(root, text="Жіберу", command=submit_form)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
