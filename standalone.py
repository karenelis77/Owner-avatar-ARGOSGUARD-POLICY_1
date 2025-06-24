import sqlite3
import tkinter as tk
from tkinter import messagebox, scrolledtext

class PolicyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ArgoSGuardPolicy - Stand-Alone")
        self.root.geometry("600x400")

        # Conexión a la base de datos
        self.conn = sqlite3.connect('policies.db')
        self.cursor = self.conn.cursor()

        # Crear tabla si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS policies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.conn.commit()

        # Interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta
        tk.Label(self.root, text="Gestión de Políticas", font=("Arial", 14, "bold")).pack(pady=10)

        # Campos de entrada
        tk.Label(self.root, text="Nombre:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Descripción:").pack()
        self.desc_entry = tk.Entry(self.root)
        self.desc_entry.pack()

        # Botones
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Crear", command=self.create_policy).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Leer", command=self.read_policies).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Actualizar", command=self.update_policy).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar", command=self.delete_policy).pack(side=tk.LEFT, padx=5)

        # Área de texto para mostrar políticas
        self.text_area = scrolledtext.ScrolledText(self.root, width=70, height=10)
        self.text_area.pack(pady=10)

    def create_policy(self):
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        if name and desc:
            self.cursor.execute('INSERT INTO policies (name, description) VALUES (?, ?)', (name, desc))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Política creada.")
            self.name_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.read_policies()
        else:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")

    def read_policies(self):
        self.text_area.delete(1.0, tk.END)
        self.cursor.execute('SELECT * FROM policies')
        policies = self.cursor.fetchall()
        for policy in policies:
            self.text_area.insert(tk.END, f"ID: {policy[0]}, Nombre: {policy[1]}, Descripción: {policy[2]}\n")

    def update_policy(self):
        name = self.name_entry.get()
        desc = self.desc_entry.get()
        if name and desc:
            self.cursor.execute('UPDATE policies SET description = ? WHERE name = ?', (desc, name))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Política actualizada.")
            self.read_policies()
        else:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")

    def delete_policy(self):
        name = self.name_entry.get()
        if name:
            self.cursor.execute('DELETE FROM policies WHERE name = ?', (name,))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Política eliminada.")
            self.read_policies()
        else:
            messagebox.showwarning("Error", "Por favor, ingresa el nombre de la política a eliminar.")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PolicyApp(root)
    root.mainloop()