import math

def raiz_biseccion(numero):
    if numero < 0:
        return "Error: no se puede sacar raíz de un número negativo"
    x = numero
    y = (x + 1) / 2
    while abs(y - x) > 0.00001:
        x = y
        y = (x + numero / x) / 2
    return y

def calculadora():
    print("Calculadora con raíz (dos métodos)")
    print("Operaciones: suma, resta, mult, div, potencia, raiz")

    while True:
        operacion = input("\nEscribe una operación (o 'salir'): ").lower()
        if operacion == "salir":
            print("¡Hasta luego!")
            break

        if operacion in ["suma", "resta", "mult", "div", "potencia"]:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))

            if operacion == "suma":
                print("Resultado:", a + b)
            elif operacion == "resta":
                print("Resultado:", a - b)
            elif operacion == "mult":
                print("Resultado:", a * b)
            elif operacion == "div":
                if b != 0:
                    print("Resultado:", a / b)
                else:
                    print("Error: división por cero.")
            elif operacion == "potencia":
                print("Resultado:", a ** b)

        elif operacion == "raiz":
            a = float(input("Número: "))
            metodo = input("¿Usar 'biseccion' o 'math'? ").lower()

            if metodo == "biseccion":
                resultado = raiz_biseccion(a)
                print("Resultado (bisección):", resultado)
            elif metodo == "math":
                if a >= 0:
                    print("Resultado (math.sqrt):", math.sqrt(a))
                else:
                    print("Error: no se puede sacar raíz de un número negativo.")
            else:
                print("Método no válido.")
        else:
            print("Operación no válida.")

calculadora()