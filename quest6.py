# 6. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

num = int(str(input("DIGITE UM NUMERO: ")))

def r(num):
    reverso = (num)[::-1]
    return reverso
print(r(num))
