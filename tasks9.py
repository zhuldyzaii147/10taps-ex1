import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 9")
root.geometry("400x200")

def show_text():
    user_text = entry.get()
    output_label.config(text=f"Енгізілген мәтін: {user_text}")

entry = tk.Entry(root, width=25)
entry.pack(pady=20)

btn = tk.Button(root, text="Көрсету", command=show_text)
btn.pack(pady=5)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=20)

root.mainloop()
