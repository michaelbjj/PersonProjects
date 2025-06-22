def soma(number1, number2):
    return number1 + number2

def subtrai(number1, number2):
    return number1 - number2

def multiplica(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if b == 0:
        return "Erro: divisão por zero"
    return number1 / number2

print("Calculadora Simples")
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção (1/2/3/4): ")

number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado:", soma(number1, number2))
    print("----------------------------------------")
elif opcao == '2':
    print("Resultado:", subtrai(number1, number2))
    print("----------------------------------------")
elif opcao == '3':
    print("Resultado:", multiplica(number1, number2))
    print("----------------------------------------")
elif opcao == '4':
    print("Resultado:", divide(number1, number2))
    print("----------------------------------------")
else:
    print("Opção inválida")
    print("----------------------------------------")
    
