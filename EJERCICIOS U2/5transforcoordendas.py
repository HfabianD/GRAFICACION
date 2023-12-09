import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import math

class AplicacionTransformaciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Transformaciones de Coordenadas")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Crear una imagen en blanco para dibujar
        self.imagen = Image.new("RGB", (400, 400), "white")
        self.dibujo = ImageDraw.Draw(self.imagen)

        # Dibujar un cuadrado en la imagen
        self.dibujo.rectangle([150, 150, 250, 250], outline="black", fill="blue")

        # Convertir la imagen para su visualización en Tkinter
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        # Crear un widget de etiqueta para mostrar la imagen
        self.etiqueta_imagen = tk.Label(ventana, image=self.imagen_tk)
        self.etiqueta_imagen.pack()

        # Botones para aplicar transformaciones
        self.boton_traslacion = tk.Button(ventana, text="Traslación", command=self.aplicar_traslacion)
        self.boton_traslacion.pack(side=tk.LEFT)

        self.boton_rotacion = tk.Button(ventana, text="Rotación", command=self.aplicar_rotacion)
        self.boton_rotacion.pack(side=tk.LEFT)

        self.boton_escala = tk.Button(ventana, text="Escala", command=self.aplicar_escala)
        self.boton_escala.pack(side=tk.LEFT)

    def aplicar_traslacion(self):
        # Trasladar el cuadrado en la imagen
        self.imagen = Image.new("RGB", (400, 400), "white")
        self.dibujo = ImageDraw.Draw(self.imagen)
        self.dibujo.rectangle([150 + 50, 150 + 50, 250 + 50, 250 + 50], outline="black", fill="blue")
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        self.etiqueta_imagen.configure(image=self.imagen_tk)

    def aplicar_rotacion(self):
        # Rotar el cuadrado en la imagen
        self.imagen = Image.new("RGB", (400, 400), "white")
        self.dibujo = ImageDraw.Draw(self.imagen)
        angulo = math.radians(45)  # Ángulo de rotación en radianes
        x_centro, y_centro = 200, 200
        x1, y1 = self.rotar_punto(150, 150, x_centro, y_centro, angulo)
        x2, y2 = self.rotar_punto(250, 150, x_centro, y_centro, angulo)
        x3, y3 = self.rotar_punto(250, 250, x_centro, y_centro, angulo)
        x4, y4 = self.rotar_punto(150, 250, x_centro, y_centro, angulo)
        self.dibujo.polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], outline="black", fill="blue")
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        self.etiqueta_imagen.configure(image=self.imagen_tk)

    def aplicar_escala(self):
        # Escalar el cuadrado en la imagen
        self.imagen = Image.new("RGB", (400, 400), "white")
        self.dibujo = ImageDraw.Draw(self.imagen)
        escala = 1.5  # Factor de escala
        x_centro, y_centro = 200, 200
        x1, y1 = self.escalar_punto(150, 150, x_centro, y_centro, escala)
        x2, y2 = self.escalar_punto(250, 150, x_centro, y_centro, escala)
        x3, y3 = self.escalar_punto(250, 250, x_centro, y_centro, escala)
        x4, y4 = self.escalar_punto(150, 250, x_centro, y_centro, escala)
        self.dibujo.polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], outline="black", fill="blue")
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        self.etiqueta_imagen.configure(image=self.imagen_tk)

    def rotar_punto(self, x, y, x_centro, y_centro, angulo):
        # Rotar un punto alrededor de un centro dado
        x_rotado = (x - x_centro) * math.cos(angulo) - (y - y_centro) * math.sin(angulo) + x_centro
        y_rotado = (x - x_centro) * math.sin(angulo) + (y - y_centro) * math.cos(angulo) + y_centro
        return x_rotado, y_rotado

    def escalar_punto(self, x, y, x_centro, y_centro, escala):
        # Escalar un punto alrededor de un centro dado
        x_escala = (x - x_centro) * escala + x_centro
        y_escala = (y - y_centro) * escala + y_centro
        return x_escala, y_escala

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = AplicacionTransformaciones(root)
    root.mainloop()
