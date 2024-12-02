import tkinter as tk
from tkinter import ttk
from Usuarios import UsuariosView 
from Proveedores import ProveedoresView 
from Productos import ProductosView

class TiendaMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Menú Principal")
        self.geometry("800x600")
        self.configure(bg="#f7f7f7")
        
        self.columnconfigure(0, weight=0)  
        self.columnconfigure(1, weight=1)  
        self.rowconfigure(0, weight=1)
        
        side_menu = tk.Frame(self, bg="#2c3e50", width=200)
        side_menu.grid(row=0, column=0, sticky="ns")
        side_menu.grid_propagate(False)  
        
        self.main_area = tk.Frame(self, bg="white")
        self.main_area.grid(row=0, column=1, sticky="nsew")
        
        user_label = tk.Label(side_menu, text="Usuario", bg="#2c3e50", fg="white", font=("Arial", 14, "bold"))
        user_label.pack(pady=10)
        
        logout_button = tk.Button(side_menu, text="Cerrar sesión", bg="#e74c3c", fg="white", font=("Arial", 12),
                                   command=self.logout)
        logout_button.pack(fill="x", pady=5, padx=10)
        
        menu_buttons = [
            ("Usuarios", self.show_usuarios),
            ("Productos", self.show_productos),
            ("Proveedores", self.show_proveedores),
            ("Tienda", self.show_tienda)
        ]
        for text, command in menu_buttons:
            btn = tk.Button(side_menu, text=text, bg="#34495e", fg="white", font=("Arial", 12), command=command)
            btn.pack(fill="x", pady=5, padx=10)
        
        cart_button = tk.Button(side_menu, text="Carrito", bg="yellow", font=("Arial", 14, "bold"))
        cart_button.pack(fill="x", pady=10, padx=10)
        
        self.main_area_content = tk.Label(self.main_area, text="Bienvenidos a la ferretería del Equipo 2", font=("Arial", 16), bg="white")
        self.main_area_content.pack(expand=True)
    
    def show_usuarios(self):
        """
        Muestra la vista de gestión de usuarios en el área principal.
        """
        for widget in self.main_area.winfo_children():
            widget.destroy()  
        
        usuarios_view = UsuariosView(self.main_area)  
        usuarios_view.grid(row=0, column=0, sticky="nsew") 
    
    def show_productos(self):
        """
        Muestra la vista de gestión de productos en el área principal.
        """
        for widget in self.main_area.winfo_children():
            widget.destroy()  
    
        productos_view = ProductosView(self.main_area)  
        productos_view.grid(row=0, column=0, sticky="nsew")  
    
    def show_proveedores(self):
        """
        Muestra la vista de gestión de proveedores en el área principal.
        """
        for widget in self.main_area.winfo_children():
            widget.destroy()  
    
        proveedores_view = ProveedoresView(self.main_area)  
        proveedores_view.grid(row=0, column=0, sticky="nsew")  

    
    def show_tienda(self):
        self.update_main_area("Gestión de Tienda")
    
    def update_main_area(self, text):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        label = tk.Label(self.main_area, text=text, font=("Arial", 16), bg="white")
        label.pack(expand=True)
    
    def logout(self):
        self.update_main_area("Cerrando sesión...")

if __name__ == "__main__":
    app = TiendaMenu()
    app.mainloop()
