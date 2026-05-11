#Crie uma função para informar se um número digitado pelo usuário é par.

w = int(input("um numero: "))

def num():
    if w %2 == 0:
        print("é par")
    else:
        print("é impar")
num()