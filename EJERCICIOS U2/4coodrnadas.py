import tkinter as tk

class AplicacionCoordenadas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Coordenadas")

        # Crear el lienzo con un sistema de coordenadas
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Configurar el sistema de coordenadas
        self.canvas.create_line(200, 0, 200, 400, fill="black", arrow=tk.LAST)
        self.canvas.create_line(0, 200, 400, 200, fill="black", arrow=tk.LAST)

        # Enlace de eventos del ratón
        self.canvas.bind("<Button-1>", self.obtener_coordenadas)

    def obtener_coordenadas(self, evento):
        # Obtener las coordenadas del clic
        x = evento.x - 200  # Ajustar según el centro del sistema de coordenadas
        y = 200 - evento.y  # Invertir y para que sea consistente con el sistema de coordenadas

        # Mostrar las coordenadas en la consola
        print(f"Coordenadas: ({x}, {y})")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = AplicacionCoordenadas(root)
    root.mainloop()
