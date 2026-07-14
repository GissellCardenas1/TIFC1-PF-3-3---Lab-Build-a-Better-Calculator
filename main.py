def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    resultado = 1
    for i in numbers:
        resultado = resultado * i
    return resultado

def isiteven(num):
    return isitaninteger(num) and num % 2 == 0

def isitaninteger(num):
    return isinstance(num, int)

def main():
    print("Hello learners!")
    print("1. Sumar una lista de números")
    print("2. Multiplicar una lista de números")
    print("3. Verificar si un número es entero y par")
    print("4. Verificar si un número es un entero")
    print("5. Salir")

    opcion = input("\nElige una opcion (1-5)")
    if opcion == "1":
        # Pedimos los números separados por espacios y los convertimos a float
        entrada = input("Introduce los números separados por espacios (ej: 2 4.5 6): ")
        numeros = [float(x) for x in entrada.split()]
        resultado = addmultiplenumbers(numeros)
        print(f"La suma es: {resultado}")
        
    elif opcion == "2":
        entrada = input("Introduce los números separados por espacios (ej: 2 3 4): ")
        numeros = [float(x) for x in entrada.split()]
        resultado = multiplymultiplenumbers(numeros)
        print(f"El producto es: {resultado}")
        
    elif opcion == "3":
        # Evaluamos la entrada. Intentamos convertir a entero o flotante
        entrada = input("Introduce un número: ")
        try:
            # Si tiene un punto decimal, lo evaluamos como flotante
            num = float(entrada)
            # Si el flotante es equivalente a un entero (ej: 4.0), lo convertimos a int para que pase tu validador
            if num.is_integer():
                num = int(num)
        except ValueError:
            print("Eso no es un número válido.")
            return
            
        if isiteven(num):
            print(f"¡El número {num} es entero y PAR!")
        else:
            print(f"El número {num} NO es entero y par.")
            
    elif opcion == "4":
        entrada = input("Introduce un número: ")
        try:
            num = float(entrada)
            if num.is_integer():
                num = int(num)
        except ValueError:
            print("Eso no es un número válido.")
            return
            
        if isitaninteger(num):
            print(f"¡El número {num} es un ENTERO!")
        else:
            print(f"El número {num} NO es un entero.")
            
    elif opcion == "5":
        print("¡Gracias por usar la calculadora!")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()