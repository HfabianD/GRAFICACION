import tkinter as tk

class RellenarAreas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Rellenar Áreas")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
        self.canvas.pack()

        # Variable para almacenar el color seleccionado
        self.color_seleccionado = "black"

        # Botones para seleccionar el color
        self.boton_color_negro = tk.Button(ventana, text="Negro", command=lambda: self.seleccionar_color("black"))
        self.boton_color_negro.pack(side=tk.LEFT)

        self.boton_color_rojo = tk.Button(ventana, text="Rojo", command=lambda: self.seleccionar_color("red"))
        self.boton_color_rojo.pack(side=tk.LEFT)

        self.boton_color_azul = tk.Button(ventana, text="Azul", command=lambda: self.seleccionar_color("blue"))
        self.boton_color_azul.pack(side=tk.LEFT)

        # Botón para limpiar el lienzo
        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_lienzo)
        self.boton_limpiar.pack(side=tk.RIGHT)

        # Enlace de eventos del ratón
        self.canvas.bind("<B1-Motion>", self.rellenar_area)

    def seleccionar_color(self, color):
        # Función para seleccionar el color
        self.color_seleccionado = color

    def rellenar_area(self, evento):
        # Función para rellenar el área al arrastrar el ratón
        x, y = evento.x, evento.y
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=self.color_seleccionado, outline="")

    def limpiar_lienzo(self):
        # Función para limpiar el lienzo
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = RellenarAreas(root)
    root.mainloop()
