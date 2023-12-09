import tkinter as tk
from PIL import Image, ImageTk  # Asegúrate de tener instalada la biblioteca Pillow (PIL)

def mostrar_imagen():
    # Cargar la imagen
    imagen = Image.open("HF.png")  # Cambia "ejemplo_imagen.jpg" por la ruta de tu imagen

    # Crear una instancia de Tkinter
    ventana = tk.Tk()
    ventana.title("Visor de Imagen")

    # Convertir la imagen para su visualización en Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget de etiqueta para mostrar la imagen
    etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
    etiqueta_imagen.pack()

    # Iniciar el bucle principal de Tkinter
    ventana.mainloop()

# Llamar a la función para mostrar la imagen
mostrar_imagen()
