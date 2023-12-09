import tkinter as tk

class DibujarPalabras:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Dibujar Palabras")

        # Crear el lienzo
        self.canvas = tk.Canvas(ventana, width=400, height=200, bg="white")
        self.canvas.pack()

        # Entrada de texto para ingresar palabras o frases
        self.entrada_palabra = tk.Entry(ventana)
        self.entrada_palabra.pack()

        # Botón para dibujar la palabra o frase
        self.boton_dibujar = tk.Button(ventana, text="Dibujar", command=self.dibujar_palabra)
        self.boton_dibujar.pack()

    def dibujar_palabra(self):
        # Obtener la palabra o frase ingresada
        palabra = self.entrada_palabra.get()

        # Limpiar el lienzo
        self.canvas.delete("all")

        # Coordenadas iniciales para dibujar las letras
        x, y = 50, 100

        # Dibujar cada letra de la palabra o frase
        for letra in palabra:
            self.canvas.create_text(x, y, text=letra, font=("Arial", 14, "bold"))
            x += 20  # Ajustar la separación entre letras

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = DibujarPalabras(root)
    root.mainloop()
