def factorial(n):
    # Si n es menor o igual a 1, retorna 1
    if (n <= 1):
        return 1
    else:
        # Llama recursivamente a la función factorial con n-1
        subSolution = factorial(n - 1)
        # Multiplica el resultado de la llamada recursiva por n
        solution = subSolution * n
        # Retorna el resultado final
        return solution

try:
    # Solicita al usuario que ingrese un número y lo convierte a entero
    n = int(input("Ingrese un número para calcular su factorial: "))
    # Imprime el resultado del cálculo del factorial
    print(f"El factorial de {n} es {factorial(n)}")
except ValueError:
    # Maneja el caso en que la entrada no sea un número entero válido
    print("Por favor, ingrese un número entero válido.")
