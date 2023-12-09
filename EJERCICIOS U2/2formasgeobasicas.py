import tkinter as tk

class AplicacionDibujo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación de Dibujo")

        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Botones para seleccionar la forma a dibujar
        self.boton_circulo = tk.Button(ventana, text="Círculo", command=self.dibujar_circulo)
        self.boton_circulo.pack(side=tk.LEFT)

        self.boton_rectangulo = tk.Button(ventana, text="Rectángulo", command=self.dibujar_rectangulo)
        self.boton_rectangulo.pack(side=tk.LEFT)

        self.boton_linea = tk.Button(ventana, text="Línea", command=self.dibujar_linea)
        self.boton_linea.pack(side=tk.LEFT)

    def dibujar_circulo(self):
        self.canvas.create_oval(50, 50, 150, 150, outline="black")

    def dibujar_rectangulo(self):
        self.canvas.create_rectangle(200, 50, 300, 150, outline="black")

    def dibujar_linea(self):
        self.canvas.create_line(50, 200, 150, 300, fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = AplicacionDibujo(root)
    root.mainloop()
