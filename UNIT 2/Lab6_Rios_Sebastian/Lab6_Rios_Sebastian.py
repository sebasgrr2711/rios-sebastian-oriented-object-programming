from abc import ABC, abstractmethod
import os
import tkinter as tk
from PIL import Image, ImageTk

# =====================================================================
# CLASES BASE Y DISPOSITIVOS (POLIMORFISMO)
# =====================================================================


class smartdevice(ABC):

    def __init__(self, name: str):
        self.name = name

    # El método abstracto obliga a cada clase hija a implementar su propio turn_on()
    @abstractmethod
    def turn_on(self):
        pass


class smartlight(smartdevice):

    def __init__(self):
        super().__init__("Living room smart light")

    def turn_on(self):
        return f"{self.name}: Set the brightness to 100%"


class smartspeaker(smartdevice):

    def __init__(self):
        super().__init__("Alexa speaker")

    def turn_on(self):
        return f"{self.name}: Playing lofi music at volume 8"


class smartfridge(smartdevice):

    def __init__(self):
        super().__init__("Smart fridge")

    def turn_on(self):
        return f"{self.name}: Set the temperature to 4 degrees Celsius"


# =====================================================================
# INTERFAZ GRÁFICA (GUI)
# =====================================================================


class SmartHomeApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS ---
        self.title("OOP Lab: Polymorphism GUI Template")
        self.geometry("480x360")
        self.resizable(False, False)

        # --- 2. ICONO DE LA APLICACIÓN ---
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(dir_actual, "app_icon.png")

        if os.path.exists(icon_dir):
            try:
                # Carga la imagen usando Pillow para evitar fallos de formato en Tkinter
                img = Image.open(icon_dir)
                # Guardamos en self.icon_img para evitar que el Garbage Collector borre la imagen
                self.icon_img = ImageTk.PhotoImage(img)
                self.iconphoto(True, self.icon_img)
            except Exception as e:
                print(f"Error al cargar el icono: {e}")
        else:
            print(f"Advertencia: No se encontró el icono en {icon_dir}")

        # --- 3. OBJECT REGISTRY ---
        # Asocia las etiquetas con las instancias de cada dispositivo
        self.devices = {
            "Light": smartlight(),
            "Speaker": smartspeaker(),
            "Fridge": smartfridge(),
        }

        # Construir la interfaz gráfica
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="POLYMORPHISM DEMO",
            font=("Arial", 15, "bold"),
            foreground="#2c3e50",
        )
        lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10,
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Seleccionar la primera opción de la lista por defecto
        first_key = list(self.devices.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Generar un Radiobutton dinámicamente por cada dispositivo
        for key in self.devices.keys():
            rb = tk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key,
                font=("Arial", 10),
            )
            rb.pack(anchor="w", pady=3)

        # Trigger Action Button (Compatible con tk.Button)
        btn_action = tk.Button(
            self,
            text="EXECUTE ACTION",
            command=self._handle_action,
            font=("Arial", 10, "bold"),
            bg="#2980b9",
            fg="white",
            activebackground="#3498db",
            activeforeground="white",
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6,
        )
        btn_action.pack(pady=15)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'EXECUTE ACTION'.",
            font=("Arial", 10, "italic"),
            background="#ecf0f1",
            foreground="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center",
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        # 1. Obtiene la clave seleccionada
        chosen_key = self.selected_key.get()

        # 2. Recupera el objeto polimórfico
        active_object: smartdevice = self.devices[chosen_key]

        # 3. EJECUCIÓN POLIMÓRFICA: Llama al método turn_on()
        result_message = active_object.turn_on()

        # 4. Muestra la respuesta en pantalla
        self.lbl_output.config(
            text=result_message, font=("Arial", 10, "bold")
        )


# =====================================================================
# LAUNCHER
# =====================================================================
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
