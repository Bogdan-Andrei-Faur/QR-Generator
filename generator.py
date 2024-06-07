#!/usr/bin/env python3

import qrcode
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, filedialog
import os

def generate_qr():
    # Obtener la URL del campo de entrada
    data = url_entry.get()
    
    if not data:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una URL.")
        return
    
    # Crear un objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Agregar datos al objeto QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Crear una imagen del código QR
    img = qr.make_image(fill='black', back_color='white')

    # Generar un nombre único para el archivo basado en la fecha y hora actuales
    filename = "codigo_qr_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

    # Preguntar al usuario dónde guardar el archivo
    save_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=filename, filetypes=[("PNG files", "*.png")])

    if save_path:
        # Guardar la imagen en el archivo especificado por el usuario
        img.save(save_path)
        messagebox.showinfo("Éxito", f"El código QR ha sido guardado como {save_path}")

# Crear la ventana principal
root = tk.Tk()
root.title("QR Code Generator")

# Cambiar el icono de la ventana
icon_path = os.path.abspath('logo.png')
root.iconbitmap(icon_path)

# Crear y colocar los widgets
tk.Label(root, text="Ingresa la URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generar QR", command=generate_qr)
generate_button.pack(pady=20)

# Agregar la versión del programa en la esquina inferior derecha
version_label = tk.Label(root, text="Versión 1.0", fg="grey")
version_label.place(relx=1.0, rely=1.0, anchor='se')

# Iniciar el bucle principal de Tkinter
root.mainloop()