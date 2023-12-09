import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

class AplicacionDibujo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación de Dibujo")

        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Configuración del pincel
        self.pincel_color = "black"
        self.pincel_tamano = 2

        # Enlace de eventos del ratón
        self.canvas.bind("<B1-Motion>", self.dibujar)

        # Botones
        self.boton_guardar = tk.Button(ventana, text="Guardar", command=self.guardar_dibujo)
        self.boton_guardar.pack(side=tk.RIGHT)

    def dibujar(self, evento):
        x1, y1 = (evento.x - self.pincel_tamano), (evento.y - self.pincel_tamano)
        x2, y2 = (evento.x + self.pincel_tamano), (evento.y + self.pincel_tamano)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.pincel_color, outline=self.pincel_color)

    def guardar_dibujo(self):
        # Obtener la ubicación del archivo para guardar
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png")])

        if file_path:
            # Crear una imagen en blanco del mismo tamaño que el lienzo
            imagen = Image.new("RGB", (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), "white")
            draw = ImageDraw.Draw(imagen)

            # Copiar el contenido del lienzo a la imagen
            imagen.paste(self.canvas, (0, 0))

            # Guardar la imagen
            imagen.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = AplicacionDibujo(root)
    root.mainloop()
