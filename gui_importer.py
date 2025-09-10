import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import sqlite3
import os

def charger_fichier():
    path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv"), ("Excel", "*.xlsx;*.xls"), ("Text", "*.txt")])
    if not path:
        return
    
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == ".csv":
            df = pd.read_csv(path)
        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(path)
        elif ext == ".txt":
            df = pd.read_csv(path, delimiter="\t")
        else:
            messagebox.showerror("Erreur", "Format non supporté")
            return
    except Exception as e:
        messagebox.showerror("Erreur de lecture", str(e))
        return

    global data
    data = df
    apercu.delete(*apercu.get_children())
    for col in df.columns:
        apercu.heading(col, text=col)
    for row in df.head(10).values.tolist():
        apercu.insert("", "end", values=row)
    
    if df.isnull().values.any():
        messagebox.showwarning("Attention", "Le fichier contient des valeurs manquantes.")
    else:
        messagebox.showinfo("Info", "Pas de valeurs manquantes.")

def sauvegarder_db():
    if data is None:
        messagebox.showerror("Erreur", "Aucune donnée chargée.")
        return
    conn = sqlite3.connect("fichiers.db")
    data.to_sql("data", conn, if_exists="append", index=False)
    conn.close()
    messagebox.showinfo("Succès", "Données sauvegardées dans SQLite.")

# Interface
root = tk.Tk()
root.title("File Validator & Importer")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_load = tk.Button(frame, text="Charger un fichier", command=charger_fichier)
btn_load.pack(side=tk.LEFT, padx=5)

btn_save = tk.Button(frame, text="Sauvegarder en DB", command=sauvegarder_db)
btn_save.pack(side=tk.LEFT, padx=5)

apercu = ttk.Treeview(root, columns=[], show="headings", height=10)
apercu.pack(fill="both", expand=True, padx=10, pady=10)

data = None
root.mainloop()
