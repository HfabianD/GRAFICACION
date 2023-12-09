import tkinter as tk
import random

class GeneradorPatronesAleatorios:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Generador de Patrones Aleatorios")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Botón para generar patrones aleatorios
        self.boton_generar = tk.Button(ventana, text="Generar Patrón", command=self.generar_patron)
        self.boton_generar.pack()

    def generar_patron(self):
        # Limpiar el lienzo
        self.canvas.delete("all")

        # Generar patrón de puntos aleatorios
        for _ in range(50):  # Cambia el número para ajustar la cantidad de puntos
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            radio = random.randint(5, 20)  # Cambia el rango para ajustar el tamaño de los puntos
            self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = GeneradorPatronesAleatorios(root)
    root.mainloop()
