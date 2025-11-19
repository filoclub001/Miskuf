import tkinter as tk
from tkinter import messagebox
import random

def vypocitaj():
    try:
        N = int(entry_N.get())
        if N % 2 != 0 or N < 2:
            messagebox.showerror("Chyba", "Zadajte párne N väčšie než 1.")
            return
        cisla = [random.randint(50, 500) for _ in range(N)]
        cisla.sort()
        polovica = N // 2
        prva = cisla[:polovica]
        druha = cisla[polovica:]
        priemer1 = round(sum(prva)/len(prva), 2)
        priemer2 = round(sum(druha)/len(druha), 2)
        text_prva.delete(1.0, tk.END)
        text_druha.delete(1.0, tk.END)
        text_prva.insert(tk.END, f"{prva}\nPriemer: {priemer1}")
        text_druha.insert(tk.END, f"{druha}\nPriemer: {priemer2}")
    except ValueError:
        messagebox.showerror("Chyba", "Zadajte platné celé číslo N.")

# Hlavné okno
root = tk.Tk()
root.title("Generovanie čísel")

# Vstup N
label_N = tk.Label(root, text="Zadajte párne N:")
label_N.grid(row=0, column=0, padx=5, pady=5)
entry_N = tk.Entry(root)
entry_N.grid(row=0, column=1, padx=5, pady=5)

button_vypocitat = tk.Button(root, text="Vypočítať", command=vypocitaj)
button_vypocitat.grid(row=0, column=2, padx=5, pady=5)

# Výstup 1. polovica
label_prva = tk.Label(root, text="1. polovica:")
label_prva.grid(row=1, column=0, padx=5, pady=5)
text_prva = tk.Text(root, height=6, width=40)
text_prva.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Výstup 2. polovica
label_druha = tk.Label(root, text="2. polovica:")
label_druha.grid(row=1, column=2, padx=5, pady=5)
text_druha = tk.Text(root, height=6, width=40)
text_druha.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()

