import tkinter as tk

class DibujarLineas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Dibujar Líneas")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Variables para almacenar los puntos seleccionados
        self.punto1 = None
        self.punto2 = None

        # Enlace de eventos del ratón
        self.canvas.bind("<Button-1>", self.seleccionar_punto)
        self.canvas.bind("<ButtonRelease-1>", self.dibujar_linea)

    def seleccionar_punto(self, evento):
        # Almacenar las coordenadas del punto seleccionado
        x, y = evento.x, evento.y
        if self.punto1 is None:
            self.punto1 = (x, y)
        else:
            self.punto2 = (x, y)

    def dibujar_linea(self, evento):
        # Dibujar la línea entre los dos puntos seleccionados
        if self.punto1 is not None and self.punto2 is not None:
            self.canvas.create_line(self.punto1, self.punto2, fill="black")

            # Reiniciar los puntos para permitir la selección de una nueva línea
            self.punto1 = None
            self.punto2 = None

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = DibujarLineas(root)
    root.mainloop()
