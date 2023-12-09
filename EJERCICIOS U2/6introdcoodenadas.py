import matplotlib.pyplot as plt

def mostrar_grafico(coordenadas):
    x = [coordenada[0] for coordenada in coordenadas]
    y = [coordenada[1] for coordenada in coordenadas]

    plt.scatter(x, y, color='red', marker='o')
    plt.title('Gráfico de Coordenadas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(True)
    plt.show()

def obtener_coordenadas():
    coordenadas = []

    while True:
        entrada = input("Introduce las coordenadas (o escribe 'fin' para terminar): ")
        
        if entrada.lower() == 'fin':
            break
        
        try:
            x, y = map(float, entrada.split())
            coordenadas.append((x, y))
        except ValueError:
            print("Error: Ingresa coordenadas válidas (números separados por espacio).")

    return coordenadas

if __name__ == "__main__":
    print("Introduce las coordenadas. Para finalizar, escribe 'fin'.")
    
    puntos = obtener_coordenadas()

    if puntos:
        mostrar_grafico(puntos)
    else:
        print("No se ingresaron coordenadas.")
