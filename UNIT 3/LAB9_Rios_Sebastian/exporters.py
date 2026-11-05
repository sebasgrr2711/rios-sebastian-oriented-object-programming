import csv
import json
from fpdf import FPDF

# Clase Base Abstracta (Estrategia / Interfaz)
class Exporter:
    def export(self, data, file_path):
        """Método base a ser sobrescrito por las subclases"""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

# 1. Exportador TXT
class TXTExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE INVENTARIO DE PRODUCTOS ---\n\n")
            for prod in data:
                file.write(f"ID: {prod['id_product']} | Nombre: {prod['nombre']} | Precio: ${float(prod['precio']):.2f} | Stock: {prod['stock']}\n")
        print(f"Archivo TXT generado en: {file_path}")

# 2. Exportador CSV
class CSVExporter(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Precio ($)", "Stock"])
            for prod in data:
                writer.writerow([prod['id_product'], prod['nombre'], float(prod['precio']), prod['stock']])
        print(f"Archivo CSV generado en: {file_path}")

# 3. Exportador JSON
class JSONExporter(Exporter):
    def export(self, data, file_path):
        lista_productos = []
        for prod in data:
            lista_productos.append({
                "id_product": prod['id_product'],
                "nombre": prod['nombre'],
                "precio": float(prod['precio']),
                "stock": prod['stock']
            })
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(lista_productos, file, indent=4, ensure_ascii=False)
        print(f"Archivo JSON generado en: {file_path}")

# 4. Exportador PDF
class PDFExporter(Exporter):
    def export(self, data, file_path):
        pdf = FPDF()
        pdf.add_page()
        
        # Título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(190, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')
        pdf.ln(10)
        
        # Registros
        pdf.set_font("Arial", size=12)
        for prod in data:
            texto_linea = f"ID: {prod['id_product']} - Producto: {prod['nombre']} - Precio: ${float(prod['precio']):.2f} - Stock: {prod['stock']}"
            pdf.cell(190, 10, txt=texto_linea, ln=True)
            
        pdf.output(file_path)
        print(f"Archivo PDF generado en: {file_path}")
   