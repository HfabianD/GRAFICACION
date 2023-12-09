import tkinter as tk

class DibujarCurvas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Dibujar Curvas")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Variable para almacenar el tipo de curva seleccionada
        self.tipo_curva = tk.StringVar()

        # Botones de radio para seleccionar el tipo de curva
        self.radio_elipse = tk.Radiobutton(ventana, text="Elipse", variable=self.tipo_curva, value="elipse")
        self.radio_elipse.pack(side=tk.LEFT)

        self.radio_hiperbola = tk.Radiobutton(ventana, text="Hipérbola", variable=self.tipo_curva, value="hiperbola")
        self.radio_hiperbola.pack(side=tk.LEFT)

        self.radio_parabola = tk.Radiobutton(ventana, text="Parábola", variable=self.tipo_curva, value="parabola")
        self.radio_parabola.pack(side=tk.LEFT)

        # Botón para limpiar el lienzo
        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_lienzo)
        self.boton_limpiar.pack(side=tk.RIGHT)

        # Enlace de eventos del ratón
        self.canvas.bind("<Button-1>", self.dibujar_curva)

    def dibujar_curva(self, evento):
        # Obtener las coordenadas del clic
        x, y = evento.x, evento.y

        # Obtener el tipo de curva seleccionado
        tipo_curva = self.tipo_curva.get()

        # Dibujar la curva según el tipo seleccionado
        if tipo_curva == "elipse":
            self.dibujar_elipse(x, y)
        elif tipo_curva == "hiperbola":
            self.dibujar_hiperbola(x, y)
        elif tipo_curva == "parabola":
            self.dibujar_parabola(x, y)

    def dibujar_elipse(self, x, y):
        # Dibujar una elipse en el lienzo
        radio_x = 50
        radio_y = 30
        self.canvas.create_oval(x - radio_x, y - radio_y, x + radio_x, y + radio_y, outline="black")

    def dibujar_hiperbola(self, x, y):
        # Dibujar una hipérbola en el lienzo
        radio_x = 50
        radio_y = 30
        self.canvas.create_line(x - radio_x, y, x + radio_x, y, fill="black")
        self.canvas.create_line(x, y - radio_y, x, y + radio_y, fill="black")

    def dibujar_parabola(self, x, y):
        # Dibujar una parábola en el lienzo
        radio = 50
        self.canvas.create_line(x - radio, y + radio, x + radio, y + radio, fill="black")

    def limpiar_lienzo(self):
        # Limpiar el lienzo
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = DibujarCurvas(root)
    root.mainloop()
