import math
from fractions import Fraction

# Función para resolver proporciones (a/b = c/x)
def solve_proportion(a, b, c):
    if a == 0: 
        return "Error: División por cero no permitida."
    return (b * c) / a

# Función para resolver ecuaciones simples de la forma ax = b
def solve_for_x(a, b):
    if a == 0: 
        return "Error: División por cero no permitida."
    return b / a

# Función para factorizar raíces cuadradas
def factor_square_root(n):
    if n < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(n)

# Función para convertir decimales a fracciones
def decimal_to_fraction(decimal):
    try:
        return str(Fraction(decimal).limit_denominator())
    except:
        return "Error: Entrada no válida."

# Función para convertir decimales a porcentajes
def decimal_to_percentage(decimal):
    try:
        return f"{decimal * 100}%"
    except:
        return "Error: Entrada no válida."

# Función para convertir fracciones a decimales
def fraction_to_decimal(fraction_str):
    try:
        return float(Fraction(fraction_str))
    except:
        return "Error: Entrada no válida."

# Función para convertir fracciones a porcentajes
def fraction_to_percentage(fraction_str):
    try:
        decimal = float(Fraction(fraction_str))
        return f"{decimal * 100}%"
    except:
        return "Error: Entrada no válida."

# Función para convertir porcentajes a decimales
def percentage_to_decimal(percentage):
    try:
        return float(percentage.replace("%", "")) / 100
    except:
        return "Error: Entrada no válida."

# Función para convertir porcentajes a fracciones
def percentage_to_fraction(percentage):
    try:
        decimal = percentage_to_decimal(percentage)
        return decimal_to_fraction(decimal)
    except:
        return "Error: Entrada no válida."

# Menú de interacción con el usuario
def main():
    while True:
        print("\nCalculadora Multifuncional")
        print("1. Resolver proporciones")
        print("2. Resolver para x en ecuaciones")
        print("3. Factorizar raíces cuadradas")
        print("4. Convertir decimales a fracciones y porcentajes")
        print("5. Convertir fracciones a decimales y porcentajes")
        print("6. Convertir porcentajes a decimales y fracciones")
        print("0. Salir")
        
        choice = input("Seleccione una opción: ")

        if choice == '1':
            a = float(input("Ingrese el valor de 'a': "))
            b = float(input("Ingrese el valor de 'b': "))
            c = float(input("Ingrese el valor de 'c': "))
            print(f"Resultado: {solve_proportion(a, b, c)}")
        
        elif choice == '2':
            a = float(input("Ingrese el valor de 'a': "))
            b = float(input("Ingrese el valor de 'b': "))
            print(f"Resultado: {solve_for_x(a, b)}")
        
        elif choice == '3':
            n = float(input("Ingrese el valor de 'n': "))
            print(f"Raíz cuadrada: {factor_square_root(n)}")
        
        elif choice == '4':
            decimal = float(input("Ingrese el valor decimal: "))
            print(f"Fracción: {decimal_to_fraction(decimal)}")
            print(f"Porcentaje: {decimal_to_percentage(decimal)}")
        
        elif choice == '5':
            fraction_str = input("Ingrese la fracción (como 'numerador/denominador'): ")
            print(f"Decimal: {fraction_to_decimal(fraction_str)}")
            print(f"Porcentaje: {fraction_to_percentage(fraction_str)}")
        
        elif choice == '6':
            percentage = input("Ingrese el porcentaje (como '75%'): ")
            print(f"Decimal: {percentage_to_decimal(percentage)}")
            print(f"Fracción: {percentage_to_fraction(percentage)}")
        
        elif choice == '0':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar la calculadora
if __name__ == "__main__":
    main()


