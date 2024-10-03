def rana(n):
    # Si n es 0, retorna 0
    if n == 0:
        return 0
    # Si n es 1, retorna 1
    elif n == 1:
        return 1
    else:
        # Llama recursivamente a la función rana con n-1 y n-2 y suma los resultados
        return rana(n-1) + rana(n-2)

def main():
    try:
        # Solicita al usuario que ingrese un número y lo convierte a entero
        n = int(input("Ingrese un número para calcular el enésimo número de Fibonacci: "))
        if n < 0:
            # Verifica si el número es negativo y muestra un mensaje de error
            print("Por favor, ingrese un número entero no negativo.")
        else:
            # Imprime el resultado del cálculo del enésimo número de Fibonacci
            print(f"El enésimo número de Fibonacci para n={n} es {rana(n)}")
    except ValueError:
        # Maneja el caso en que la entrada no sea un número entero válido
        print("Por favor, ingrese un número entero válido.")

# Verifica si el script se está ejecutando directamente y llama a la función main
if __name__ == "__main__":
    main()
