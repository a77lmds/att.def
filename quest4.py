# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
 
w = int(input("digite um número: "))
x = int(input("digite outro número: "))
y = int(input("mais outro: "))

def num(w, x, y):
    soma = w+x+y
    return soma
print(num(w, x, y))