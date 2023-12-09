import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.animation import FuncAnimation

class AnimacionElipse:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)

        # Parámetros iniciales de la elipse
        self.centro = (0, 0)
        self.semi_ancho_inicial = 1
        self.semi_alto_inicial = 0.5
        self.angulo_inicial = 0

        # Crear la elipse inicial
        self.elipse = Ellipse(self.centro, self.semi_ancho_inicial, self.semi_alto_inicial, angle=self.angulo_inicial, animated=True)
        self.ax.add_patch(self.elipse)

        # Configurar la animación
        self.animacion = FuncAnimation(self.fig, self.actualizar_animacion, frames=100, interval=50, blit=True)

    def actualizar_animacion(self, frame):
        # Actualizar los parámetros de la elipse con el tiempo
        factor_escala = 1 + 0.5 * abs(frame - 50) / 50  # Cambia el tamaño de la elipse con el tiempo
        factor_forma = 1 + 0.5 * abs(frame - 50) / 50   # Cambia la forma de la elipse con el tiempo

        semi_ancho = self.semi_ancho_inicial * factor_escala
        semi_alto = self.semi_alto_inicial * factor_forma
        angulo = self.angulo_inicial + frame  # Rota la elipse con el tiempo

        # Actualizar la elipse
        self.elipse.set_center(self.centro)
        self.elipse.set_width(semi_ancho * 2)
        self.elipse.set_height(semi_alto * 2)
        self.elipse.set_angle(angulo)

        return [self.elipse]

    def mostrar_animacion(self):
        plt.show()

if __name__ == "__main__":
    animacion_elipse = AnimacionElipse()
    animacion_elipse.mostrar_animacion()
