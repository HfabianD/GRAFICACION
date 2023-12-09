import matplotlib.pyplot as plt
import numpy as np

def generar_grafico():
    # Crear datos para la ecuación cuadrática y la ecuación senoidal
    x_cuadratico = np.linspace(-10, 10, 100)
    y_cuadratico = x_cuadratico**2

    x_senoidal = np.linspace(0, 4 * np.pi, 100)
    y_senoidal = np.sin(x_senoidal)

    # Graficar los puntos en el plano
    plt.plot(x_cuadratico, y_cuadratico, label='y = x^2', color='blue')
    plt.plot(x_senoidal, y_senoidal, label='y = sin(x)', color='red')

    # Establecer etiquetas y título
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Generador de Gráficos')

    # Agregar leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    generar_grafico()
