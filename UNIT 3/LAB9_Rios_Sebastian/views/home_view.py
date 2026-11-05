import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from model.products_model import ProductModel
from exporters import CSVExporter, TXTExporter, JSONExporter, PDFExporter

class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal - Sistema")
        self.root.geometry("850x660")
        
        self.product_model = ProductModel()

        # Título Superior
        lbl_bienvenida = tk.Label(
            self.root, 
            text=f"Bienvenido/a, {nombre_usuario}", 
            font=("Helvetica", 14, "bold"),
            pady=15
        )
        lbl_bienvenida.pack()

        # Control de Pestañas (Notebook)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=10)

        # Pestaña 1: Inicio
        self.tab_inicio = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_inicio, text="Inicio")
        lbl_inicio = tk.Label(
            self.tab_inicio, 
            text=f"¡Hola {nombre_usuario}! Selecciona una pestaña para comenzar.", 
            font=("Helvetica", 12)
        )
        lbl_inicio.pack(pady=50)

        # Pestaña 2: Inventario de Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Inventario de Productos")
        
        self._crear_vista_productos()
        self.notebook.select(self.tab_productos)

    def _crear_vista_productos(self):
        frame_main = ttk.Frame(self.tab_productos)
        frame_main.pack(fill="both", expand=True, padx=15, pady=15)

        # Panel Izquierdo: Formulario y Exportación
        frame_left = ttk.Frame(frame_main)
        frame_left.pack(side="left", fill="y", padx=(0, 15))

        # 1. Formulario "Registrar Producto"
        frame_form = ttk.LabelFrame(frame_left, text="Registrar Producto", padding=15)
        frame_form.pack(fill="x", pady=(0, 15))

        lbl_nombre = ttk.Label(frame_form, text="Nombre:")
        lbl_nombre.pack(anchor="w", pady=(5, 2))
        self.entry_nombre = ttk.Entry(frame_form, width=22)
        self.entry_nombre.pack(fill="x", pady=(0, 10))

        lbl_precio = ttk.Label(frame_form, text="Precio:")
        lbl_precio.pack(anchor="w", pady=(0, 2))
        self.entry_precio = ttk.Entry(frame_form, width=22)
        self.entry_precio.pack(fill="x", pady=(0, 10))

        lbl_stock = ttk.Label(frame_form, text="Stock:")
        lbl_stock.pack(anchor="w", pady=(0, 2))
        self.entry_stock = ttk.Entry(frame_form, width=22)
        self.entry_stock.pack(fill="x", pady=(0, 15))

        btn_guardar = tk.Button(
            frame_form, 
            text="Guardar Producto", 
            font=("Helvetica", 9, "bold"),
            bg="#ffffff", 
            command=self._guardar_producto
        )
        btn_guardar.pack(fill="x")

        # 2. Panel del Lab 9: "Exportar Reporte"
        frame_export = ttk.LabelFrame(frame_left, text="Exportar Reporte", padding=15)
        frame_export.pack(fill="x")

        lbl_formato = ttk.Label(frame_export, text="Formato del archivo:")
        lbl_formato.pack(anchor="w", pady=(0, 5))

        self.combo_formato = ttk.Combobox(
            frame_export, 
            values=["CSV", "TXT", "JSON", "PDF"], 
            state="readonly",
            width=20
        )
        self.combo_formato.set("PDF")
        self.combo_formato.pack(fill="x", pady=(0, 10))

        btn_exportar = tk.Button(
            frame_export, 
            text="Exportar Reporte", 
            font=("Helvetica", 9, "bold"),
            bg="#2196F3", 
            fg="white", 
            cursor="hand2",
            command=self._exportar_reporte
        )
        btn_exportar.pack(fill="x")

        # Panel Derecho: Tabla de Productos
        frame_tabla = ttk.Frame(frame_main)
        frame_tabla.pack(side="right", fill="both", expand=True)

        columnas = ("ID", "Nombre", "Precio ($)", "Stock")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio ($)", text="Precio ($)")
        self.tabla.heading("Stock", text="Stock")

        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=220, anchor="w")
        self.tabla.column("Precio ($)", width=100, anchor="e")
        self.tabla.column("Stock", width=80, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self._cargar_productos()

    def _cargar_productos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        productos = self.product_model.get_all_products()
        if productos:
            for prod in productos:
                precio_formateado = f"{float(prod['precio']):.2f}"
                self.tabla.insert("", "end", values=(
                    prod['id_product'],
                    prod['nombre'],
                    precio_formateado,
                    prod['stock']
                ))

    def _guardar_producto(self):
        nombre = self.entry_nombre.get().strip()
        precio = self.entry_precio.get().strip()
        stock = self.entry_stock.get().strip()

        if not nombre or not precio or not stock:
            messagebox.showwarning("Campos Vacíos", "Por favor llena todos los campos.")
            return

        try:
            precio_val = float(precio)
            stock_val = int(stock)
        except ValueError:
            messagebox.showerror("Tipo de dato inválido", "Precio debe ser número y Stock un entero.")
            return

        exito = self.product_model.add_product(nombre, precio_val, stock_val)
        if exito:
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            self.entry_stock.delete(0, tk.END)
            self._cargar_productos()
        else:
            messagebox.showerror("Error", "No se pudo guardar el producto.")

    # --- MÉTODO POLIMÓRFICO DE EXPORTACIÓN (LAB 9) ---
    def _exportar_reporte(self):
        formato = self.combo_formato.get()
        productos = self.product_model.get_all_products()

        if not productos:
            messagebox.showwarning("Sin datos", "No hay productos disponibles para exportar.")
            return

        # Diccionario con las clases hijas
        exportadores = {
            "CSV": CSVExporter(),
            "TXT": TXTExporter(),
            "JSON": JSONExporter(),
            "PDF": PDFExporter()
        }

        exportador = exportadores.get(formato)

        if exportador:
            ext = formato.lower()
            ruta = filedialog.asksaveasfilename(
                defaultextension=f".{ext}",
                filetypes=[(f"Archivo {formato}", f"*.{ext}")]
            )

            if ruta:
                # POLIMORFISMO: Invocación genérica de .export()
                exportador.export(productos, ruta)
                messagebox.showinfo("Éxito", f"El archivo {formato} fue generado con éxito.") 