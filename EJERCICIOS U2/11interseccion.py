import tkinter as tk

class InterseccionLineas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Intersección de Líneas")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Variables para almacenar los puntos de las líneas
        self.punto1_linea1 = None
        self.punto2_linea1 = None
        self.punto1_linea2 = None
        self.punto2_linea2 = None

        # Enlace de eventos del ratón
        self.canvas.bind("<Button-1>", self.seleccionar_punto)

        # Botón para encontrar la intersección
        self.boton_interseccion = tk.Button(ventana, text="Encontrar Intersección", command=self.encontrar_interseccion)
        self.boton_interseccion.pack()

    def seleccionar_punto(self, evento):
        # Almacenar las coordenadas del punto seleccionado
        x, y = evento.x, evento.y
        if self.punto1_linea1 is None:
            self.punto1_linea1 = (x, y)
        elif self.punto2_linea1 is None:
            self.punto2_linea1 = (x, y)
        elif self.punto1_linea2 is None:
            self.punto1_linea2 = (x, y)
        elif self.punto2_linea2 is None:
            self.punto2_linea2 = (x, y)

            # Dibujar las líneas
            self.canvas.create_line(self.punto1_linea1, self.punto2_linea1, fill="blue")
            self.canvas.create_line(self.punto1_linea2, self.punto2_linea2, fill="red")

            # Reiniciar los puntos para permitir la selección de nuevas líneas
            self.punto1_linea1 = None
            self.punto2_linea1 = None
            self.punto1_linea2 = None
            self.punto2_linea2 = None

    def encontrar_interseccion(self):
        # Verificar si las líneas están definidas
        if self.punto1_linea1 is not None and self.punto2_linea1 is not None and \
           self.punto1_linea2 is not None and self.punto2_linea2 is not None:
            
            # Obtener las coordenadas de los puntos de las líneas
            x1, y1 = self.punto1_linea1
            x2, y2 = self.punto2_linea1
            x3, y3 = self.punto1_linea2
            x4, y4 = self.punto2_linea2

            # Calcular la intersección de las líneas utilizando la fórmula de intersección de dos líneas
            denominador = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if denominador != 0:
                interseccion_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominador
                interseccion_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominador

                # Mostrar la intersección en el lienzo
                self.canvas.create_oval(interseccion_x - 3, interseccion_y - 3, interseccion_x + 3, interseccion_y + 3, fill="green")
                self.ventana.update()  # Actualizar la ventana para asegurarse de que se muestre la intersección
            else:
                print("Las líneas son paralelas y no se intersectan.")
        else:
            print("Por favor, seleccione dos líneas en el plano.")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = InterseccionLineas(root)
    root.mainloop()
