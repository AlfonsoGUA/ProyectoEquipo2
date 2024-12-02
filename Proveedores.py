import tkinter as tk
from tkinter import ttk
from tkinter import Frame

class ProveedoresView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        

        self.configure(bg="white")
        self.grid(row=0, column=0, sticky="nsew")  
        
        
        tk.Label(self, text="Gestión de proveedores", font=("Arial", 16, "bold"), bg="white", fg="darkblue", anchor="center").grid(row=0, column=0, columnspan=4, pady=10, sticky="w")
        
        
        self.search_label = tk.Label(self, text="Buscar Proveedor:", font=("Arial", 12), bg="white")
        self.search_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.search_entry = tk.Entry(self, font=("Arial", 12))
        self.search_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w", ipadx=5, ipady=5)
        
        self.search_button = tk.Button(self, text="Buscar", command=self.search_user, font=("Arial", 12), bg="lightblue", width=12)
        self.search_button.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        
        
        style = ttk.Style()
        style.configure("Treeview",
                        background="lightblue",  
                        foreground="black",
                        rowheight=25,
                        fieldbackground="lightblue")  
        style.configure("Treeview.Heading",
                        background="lightblue",
                        foreground="black",
                        font=("Arial", 12, "bold"))
        style.map("Treeview", background=[('selected', 'lightgreen')])

       
        style.configure("Treeview", highlightthickness=1, bd=1, relief="solid")
        
       
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        
        self.treeview_frame = Frame(self.canvas, bg="white")
        
       
        self.v_scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.v_scrollbar.grid(row=2, column=4, sticky="ns")
        
       
        self.h_scrollbar = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.h_scrollbar.grid(row=3, column=0, columnspan=4, sticky="ew")
        
       
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        
        
        self.treeview = ttk.Treeview(self.treeview_frame, columns=("Id", "Nombre", "Contacto"), show="headings", height=10)
        self.treeview.heading("Id", text="Id")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Contacto", text="Contacto")
        
      
        self.treeview.column("Id", width=50, anchor="center")
        self.treeview.column("Nombre", width=220, anchor="center")
        self.treeview.column("Contacto", width=220, anchor="center")
        

       
        self.treeview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.canvas.create_window((0, 0), window=self.treeview_frame, anchor="nw")
        
        
        self.treeview_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
       
        button_style = {"font": ("Arial", 12), "width": 12, "relief": "raised", "bd": 3}
        
        tk.Button(self, text="Crear", bg="green", fg="white", command=self.create_user, **button_style).grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        tk.Button(self, text="Modificar", bg="yellow", command=self.modify_user, **button_style).grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        tk.Button(self, text="Eliminar", bg="red", fg="white", command=self.delete_user, **button_style).grid(row=4, column=2, padx=10, pady=10, sticky="ew")
        
    
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        

        self.load_users()

    def load_users(self):
        """Carga los proveedores desde la base de datos en el Treeview"""
        from conexion import DBConnection
        
        db = DBConnection()
        db.connect()
        proveedores = db.fetch_proveedores()
        db.close()
        
      
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
       
        for proveedores in proveedores:
            self.treeview.insert("", "end", values=proveedores)

    def search_user(self):
        """Función para buscar un proveedor basado en el texto del buscador (solo por Nombre e ID)"""
        search_text = self.search_entry.get().lower()

        # Limpiar la vista de la tabla antes de insertar los resultados
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        from conexion import DBConnection

        db = DBConnection()
        db.connect()
        proveedores = db.fetch_proveedores()
        db.close()

        # Insertar en el Treeview solo si el texto de búsqueda se encuentra en el ID o en el Nombre
        for proveedor in proveedores:
         # Asumimos que 'proveedor[0]' es el ID y 'proveedor[1]' es el Nombre
         if (search_text in str(proveedor[0]).lower() or  # Buscar por ID
            search_text in proveedor[1].lower()):  # Buscar por Nombre
            self.treeview.insert("", "end", values=proveedor)


    def create_user(self):
        """Placeholder para crear un proveedor"""
        print("Función de crear proveedor no implementada.")

    def modify_user(self):
        """Placeholder para modificar un proveedor"""
        print("Función de modificar proveedor no implementada.")

    def delete_user(self):
        """Placeholder para eliminar un proveedor"""
        print("Función de eliminar proveedor no implementada.")
