# Faça um programa que imprima a tabuada de soma, subtração, multiplicação e divisão de um número informado pelo usuário.
# O usuário informa o número e a operação e o programa imprime os valores.

num = int(input("Digite um número: "))

def tabuada():
    for i in range(1, 11):
        resultado = num + i
        print(f"{num} + {i} = {resultado}")
    print("")
    for i in range(1, 11):
        resultado = num - i
        print(f"{num} - {i} = {resultado}")
    print("")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")
    print("")

    for i in range(1, 11):
        resultado = num / i
        print(f"{num} : {i} = {resultado}")

    return tabuada
print(tabuada())