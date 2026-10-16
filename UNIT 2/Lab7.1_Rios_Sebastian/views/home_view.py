import tkinter as tk
from tkinter import ttk
from model.products_model import Product
import os
from PIL import Image, ImageTk


class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.product_model = Product(None, None, None, None)
        self.root.title("Panel Principal")

        # 📐 Ampliamos el ancho para dar espacio al diseño lado a lado
        self.root.geometry("650x300")

        dir_actual = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(dir_actual, "coca_logo.jpg")

        if os.path.exists(icon_dir):
            try:
                # Carga la imagen usando Pillow para evitar fallos de formato en Tkinter
                img = Image.open(icon_dir)
                # Guardamos en self.icon_img para evitar que el Garbage Collector borre la imagen
                self.icon_img = ImageTk.PhotoImage(img)
                self.root.iconphoto(True, self.icon_img)
            except Exception as e:
                print(f"Error al cargar el icono: {e}")
        else:
            print(f"Advertencia: No se encontró el icono en {icon_dir}")

        lbl_mensaje = tk.Label(
            self.root,
            text=f"¡Bienvenido/a al Sistema! | Usuario: {nombre_usuario}",
            font=("Helvetica", 10, "bold"),
            justify="center",
            pady=5
        )
        lbl_mensaje.pack()

        # 📦 Contenedor principal que alojará las dos secciones lado a lado
        main_container = tk.Frame(self.root)
        main_container.pack(fill="both", expand=True, padx=10, pady=5)

        # Construir ambas secciones pasando el contenedor principal
        self.add_product_frame(main_container)
        self.products_frame(main_container)

        # Cargar los datos automáticamente
        self.refresh_table()

    def add_product_frame(self, parent):
        # 👈 Lado Izquierdo: Formulario en vertical
        left_frame = tk.LabelFrame(parent, text="Agregar Producto", font=(
            "Helvetica", 10, "bold"), padx=10, pady=10)
        left_frame.pack(side="left", fill="y", padx=5, pady=5)

        # Nombre (Fila 0)
        tk.Label(left_frame, text="Nombre:").grid(
            row=0, column=0, sticky="w", pady=2)
        self.input_entry = tk.Entry(left_frame, width=18)
        self.input_entry.grid(row=1, column=0, pady=2)

        # Precio (Fila 2)
        tk.Label(left_frame, text="Precio:").grid(
            row=2, column=0, sticky="w", pady=2)
        self.input_entry2 = tk.Entry(left_frame, width=18)
        self.input_entry2.grid(row=3, column=0, pady=2)

        # Stock (Fila 4)
        tk.Label(left_frame, text="Stock:").grid(
            row=4, column=0, sticky="w", pady=2)
        self.input_entry3 = tk.Entry(left_frame, width=18)
        self.input_entry3.grid(row=5, column=0, pady=2)

        # Botón Agregar al final
        add_button = tk.Button(
            left_frame, text="Agregar", command=self.add_product, width=15, bg="#4CAF50", fg="white", font=("Helvetica", 9, "bold"))
        add_button.grid(row=6, column=0, pady=10)

    def products_frame(self, parent):
        # 👉 Lado Derecho: Tabla expandida
        right_frame = tk.Frame(parent)
        right_frame.pack(side="right", fill="both",
                         expand=True, padx=5, pady=5)

        lbl_tabla = tk.Label(
            right_frame, text="Lista de Productos", font=("Helvetica", 10, "bold"))
        lbl_tabla.pack(anchor="w", pady=2)

        # Scrollbar
        tree_scroll = ttk.Scrollbar(right_frame)
        tree_scroll.pack(side="right", fill="y")

        # Tabla (Treeview)
        self.table = ttk.Treeview(
            right_frame,
            columns=("ID Product", "Name", "Price", "Stock"),
            show="headings",
            yscrollcommand=tree_scroll.set
        )
        self.table.pack(fill="both", expand=True)

        tree_scroll.config(command=self.table.yview)

        # Encabezados
        self.table.heading("ID Product", text="ID")
        self.table.heading("Name", text="Nombre")
        self.table.heading("Price", text="Precio")
        self.table.heading("Stock", text="Stock")

        # Ancho de columnas
        self.table.column("ID Product", width=40, anchor="center")
        self.table.column("Name", width=140)
        self.table.column("Price", width=70, anchor="e")
        self.table.column("Stock", width=60, anchor="center")

    def add_product(self):
        name = self.input_entry.get()
        price = self.input_entry2.get()
        stock = self.input_entry3.get()

        if name and price and stock:
            self.product_model.add_product(name, price, stock)

            # Limpiar entradas
            self.input_entry.delete(0, tk.END)
            self.input_entry2.delete(0, tk.END)
            self.input_entry3.delete(0, tk.END)

            # Refrescar tabla automáticamente
            self.refresh_table()

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        products = self.product_model.refresh_table()

        if products:
            for product in products:
                if isinstance(product, dict):
                    self.table.insert("", "end", values=(
                        product['id_product'], product['nombre'], product['precio'], product['stock']))
                else:
                    self.table.insert("", "end", values=(
                        product[0], product[1], product[2], product[3]))
