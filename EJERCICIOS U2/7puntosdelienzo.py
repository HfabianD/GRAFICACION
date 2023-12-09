import tkinter as tk
from math import sqrt

class AplicacionDibujoDistancia:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Distancia")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Lista para almacenar las coordenadas de los puntos
        self.puntos = []

        # Enlace de eventos del ratón
        self.canvas.bind("<Button-1>", self.dibujar_punto)

        # Botón para calcular la distancia
        self.boton_calcular = tk.Button(ventana, text="Calcular Distancia", command=self.calcular_distancia)
        self.boton_calcular.pack()

    def dibujar_punto(self, evento):
        # Obtener las coordenadas del clic
        x, y = evento.x, evento.y

        # Dibujar un punto en el lienzo
        radio = 3
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="black")

        # Agregar las coordenadas a la lista
        self.puntos.append((x, y))

    def calcular_distancia(self):
        # Verificar que hay al menos dos puntos
        if len(self.puntos) < 2:
            print("Se necesitan al menos dos puntos para calcular la distancia.")
            return

        # Obtener las coordenadas de los dos últimos puntos agregados
        x1, y1 = self.puntos[-2]
        x2, y2 = self.puntos[-1]

        # Calcular la distancia euclidiana
        distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Mostrar la distancia en la consola
        print(f"Distancia entre los puntos: {distancia}")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = AplicacionDibujoDistancia(root)
    root.mainloop()
