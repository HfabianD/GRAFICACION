import tkinter as tk

class DibujarLineasColoresGrosor:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Líneas de Diferentes Colores y Grosor")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Botones para trazar líneas de diferentes colores y grosores
        self.boton_linea_roja = tk.Button(ventana, text="Línea Roja", command=lambda: self.trazar_linea("red"))
        self.boton_linea_roja.pack(side=tk.LEFT)

        self.boton_linea_azul = tk.Button(ventana, text="Línea Azul", command=lambda: self.trazar_linea("blue"))
        self.boton_linea_azul.pack(side=tk.LEFT)

        self.boton_linea_verde = tk.Button(ventana, text="Línea Verde", command=lambda: self.trazar_linea("green"))
        self.boton_linea_verde.pack(side=tk.LEFT)

        self.boton_linea_grosor_delgado = tk.Button(ventana, text="Línea Delgada", command=lambda: self.trazar_linea("black", grosor=1))
        self.boton_linea_grosor_delgado.pack(side=tk.LEFT)

        self.boton_linea_grosor_medio = tk.Button(ventana, text="Línea Mediana", command=lambda: self.trazar_linea("black", grosor=3))
        self.boton_linea_grosor_medio.pack(side=tk.LEFT)

        self.boton_linea_grosor_grueso = tk.Button(ventana, text="Línea Gruesa", command=lambda: self.trazar_linea("black", grosor=6))
        self.boton_linea_grosor_grueso.pack(side=tk.LEFT)

    def trazar_linea(self, color, grosor=2):
        # Dibujar una línea en el lienzo con el color y grosor especificados
        self.canvas.create_line(50, 50, 350, 350, fill=color, width=grosor)

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = DibujarLineasColoresGrosor(root)
    root.mainloop()
