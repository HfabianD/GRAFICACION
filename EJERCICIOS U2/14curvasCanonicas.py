import matplotlib.pyplot as plt
import numpy as np

class GeneradorCurvasConicas:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal', 'box')
        self.ax.grid(True)

    def generar_elipse(self, foco, excentricidad):
        # Asegurarse de que la excentricidad sea válida
        if excentricidad >= 1:
            raise ValueError("La excentricidad debe ser menor que 1 para una elipse.")

        # Calcular el semieje mayor (a) y menor (b)
        a = foco / excentricidad
        b = foco

        # Parámetro t para el ángulo polar
        t = np.linspace(0, 2 * np.pi, 100)

        # Coordenadas paramétricas de la elipse
        x = a * np.cos(t)
        y = b * np.sin(t)

        return x, y

    def generar_parabola(self, foco):
        # Calcular la distancia focal
        p = foco / 2

        # Parámetro t para el ángulo polar
        t = np.linspace(-np.pi, np.pi, 100)

        # Coordenadas paramétricas de la parábola
        x = p * t
        y = p * t**2

        return x, y

    def generar_hiperbola(self, foco, excentricidad):
        # Asegurarse de que la excentricidad sea válida
        if excentricidad <= 1:
            raise ValueError("La excentricidad debe ser mayor que 1 para una hipérbola.")

        # Calcular el parámetro c y el semieje mayor (a)
        c = foco
        a = c / excentricidad

        # Parámetro t para el ángulo polar
        t = np.linspace(0, 2 * np.pi, 100)

        # Coordenadas paramétricas de la hipérbola
        x = a * np.cosh(t)
        y = c * np.sinh(t)

        return x, y

    def mostrar_curva(self, x, y, titulo):
        self.ax.plot(x, y, label=titulo)
        self.ax.legend()
        plt.title("Generador de Curvas Cónicas")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.show()

if __name__ == "__main__":
    generador = GeneradorCurvasConicas()

    # Generar y mostrar una elipse
    x_elipse, y_elipse = generador.generar_elipse(foco=2, excentricidad=0.8)
    generador.mostrar_curva(x_elipse, y_elipse, "Elipse")

    # Generar y mostrar una parábola
    x_parabola, y_parabola = generador.generar_parabola(foco=2)
    generador.mostrar_curva(x_parabola, y_parabola, "Parábola")

    # Generar y mostrar una hipérbola
    x_hiperbola, y_hiperbola = generador.generar_hiperbola(foco=2, excentricidad=1.2)
    generador.mostrar_curva(x_hiperbola, y_hiperbola, "Hipérbola")
