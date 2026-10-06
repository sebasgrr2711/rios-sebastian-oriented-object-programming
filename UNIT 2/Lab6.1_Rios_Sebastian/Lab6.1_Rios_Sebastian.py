from abc import ABC, abstractmethod
from datetime import datetime
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# =====================================================================
# CLASES BASE Y DISPOSITIVOS (POLIMORFISMO)
# =====================================================================


class smartdevice(ABC):

    def __init__(self, name: str):
        self.name = name

    # Métodos abstractos obligatorios para las clases hijas
    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass


class smartlight(smartdevice):

    def __init__(self):
        super().__init__("Living room smart light")

    def turn_on(self) -> str:
        return f"{self.name}: Set brightness to 100%"

    def turn_off(self) -> str:
        return f"{self.name}: Light turned OFF"


class smartspeaker(smartdevice):

    def __init__(self):
        super().__init__("Alexa speaker")

    def turn_on(self) -> str:
        return f"{self.name}: Playing lofi music at volume 8"

    def turn_off(self) -> str:
        return f"{self.name}: Stopped playback and muted"


class smartfridge(smartdevice):

    def __init__(self):
        super().__init__("Smart fridge")

    def turn_on(self) -> str:
        return f"{self.name}: Eco-mode activated at 4°C"

    def turn_off(self) -> str:
        return f"{self.name}: Power saving mode engaged"


# Nuevo dispositivo para demostrar la escalabilidad
class smarttv(smartdevice):

    def __init__(self):
        super().__init__("4K Living Room TV")

    def turn_on(self) -> str:
        return f"{self.name}: Powered ON (Input: HDMI 1 - Streaming)"

    def turn_off(self) -> str:
        return f"{self.name}: Standby mode (Screen turned OFF)"


# =====================================================================
# INTERFAZ GRÁFICA (GUI)
# =====================================================================


class SmartHomeApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS ---
        self.title("OOP Lab: Polymorphism & Log GUI")
        self.geometry("520x480")
        self.resizable(False, False)

        # --- 2. ICONO DE LA APLICACIÓN ---
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(dir_actual, "app_icon.png")

        if os.path.exists(icon_dir):
            try:
                img = Image.open(icon_dir)
                self.icon_img = ImageTk.PhotoImage(img)
                self.iconphoto(True, self.icon_img)
            except Exception as e:
                print(f"Error al cargar el icono: {e}")
        else:
            print(f"Advertencia: No se encontró el icono en {icon_dir}")

        # --- 3. OBJECT REGISTRY (ESCALABILIDAD) ---
        self.devices = {
            "Light": smartlight(),
            "Speaker": smartspeaker(),
            "Fridge": smartfridge(),
            "TV": smarttv(),  # Nuevo dispositivo agregado
        }

        # Construir la interfaz gráfica
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="SMART HOME CONTROL PANEL",
            font=("Arial", 14, "bold"),
            foreground="#2c3e50",
        )
        lbl_header.pack(pady=10)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5,
        )
        group_box.pack(fill="x", padx=20, pady=5)

        first_key = list(self.devices.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.devices.keys():
            rb = tk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key,
                font=("Arial", 10),
            )
            rb.pack(anchor="w", pady=2)

        # --- ACTION BUTTONS (ON / OFF) ---
        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=10)

        btn_on = tk.Button(
            frame_buttons,
            text="TURN ON",
            command=lambda: self._handle_action("on"),
            font=("Arial", 9, "bold"),
            bg="#27ae60",
            fg="white",
            activebackground="#2ecc71",
            activeforeground="white",
            width=12,
            cursor="hand2",
        )
        btn_on.pack(side="left", padx=10)

        btn_off = tk.Button(
            frame_buttons,
            text="TURN OFF",
            command=lambda: self._handle_action("off"),
            font=("Arial", 9, "bold"),
            bg="#c0392b",
            fg="white",
            activebackground="#e74c3c",
            activeforeground="white",
            width=12,
            cursor="hand2",
        )
        btn_off.pack(side="left", padx=10)

        # --- ACTIVITY LOG (LISTBOX + SCROLLBAR) ---
        log_frame = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.scrollbar = tk.Scrollbar(log_frame, orient="vertical")
        self.log_listbox = tk.Listbox(
            log_frame,
            yscrollcommand=self.scrollbar.set,
            font=("Consolas", 9),
            selectmode="single",
            bg="#f8f9fa",
        )
        self.scrollbar.config(command=self.log_listbox.yview)

        self.scrollbar.pack(side="right", fill="y")
        self.log_listbox.pack(side="left", fill="both", expand=True)

    def _handle_action(self, action_type: str):
        chosen_key = self.selected_key.get()
        active_object: smartdevice = self.devices[chosen_key]

        # EJECUCIÓN POLIMÓRFICA según el botón presionado
        if action_type == "on":
            result_message = active_object.turn_on()
        else:
            result_message = active_object.turn_off()

        # Registro en el Activity Log con Marca de Tiempo
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        log_entry = f"{timestamp} {result_message}"

        self.log_listbox.insert(tk.END, log_entry)
        # Auto-scroll hacia el último elemento insertado
        self.log_listbox.see(tk.END)


# =====================================================================
# LAUNCHER
# =====================================================================
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
