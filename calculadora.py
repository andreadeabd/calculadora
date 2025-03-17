class Calculadora:
    @staticmethod
    def multiplicar(a, b):
        return a * b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        resultado = Calculadora.multiplicar(num1, num2)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Ingresa solo números válidos.")
        sys.exit(1)
