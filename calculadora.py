def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("=== CALCULADORA ===")
    print("Escolha a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    operacao = input("Digite o número da operação (1/2/3/4): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = somar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operacao == '2':
            resultado = subtrair(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operacao == '3':
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operacao == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Operação inválida. Por favor, escolha 1, 2, 3 ou 4.")
    except ValueError:
        print("Erro: você deve digitar números válidos.")

if __name__ == "__main__":
    calculadora()
