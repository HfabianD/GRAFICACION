import tkinter as tk
from PIL import Image, ImageTk

class AplicarEfectos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Efectos Gráficos")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Botones para aplicar efectos
        self.boton_sombreado = tk.Button(ventana, text="Aplicar Sombreado", command=self.aplicar_sombreado)
        self.boton_sombreado.pack(side=tk.LEFT)

        self.boton_textura = tk.Button(ventana, text="Aplicar Textura", command=self.aplicar_textura)
        self.boton_textura.pack(side=tk.LEFT)

        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_lienzo)
        self.boton_limpiar.pack(side=tk.RIGHT)

    def aplicar_sombreado(self):
        # Crear un rectángulo en el lienzo
        rectangulo = self.canvas.create_rectangle(50, 50, 150, 150, fill="blue")

        # Aplicar sombreado al rectángulo
        self.canvas.itemconfig(rectangulo, outline="black", width=3)

    def aplicar_textura(self):
        # Crear un rectángulo en el lienzo
        rectangulo = self.canvas.create_rectangle(200, 50, 300, 150, fill="green")

        # Aplicar textura al rectángulo
        imagen = Image.open("textura.jpg")  # Reemplaza "textura.jpg" con la ruta de tu propia imagen
        textura = ImageTk.PhotoImage(imagen)
        self.canvas.itemconfig(rectangulo, fill="", stipple=textura)

    def limpiar_lienzo(self):
        # Limpiar el lienzo
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = AplicarEfectos(root)
    root.mainloop()
