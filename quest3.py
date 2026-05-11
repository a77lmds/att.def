# 3. Crie uma função para informar se um número digitado pelo usuário é múltiplo de 3.

w = int(input("um numero: "))

def num():
    if w % 3 == 0:
        print("é multiplo de 3")
    else:
        print("não é multiplo de 3")
num()