# 7

def gratificacao(salario, aumento):
    return(salario * (aumento/100)) + salario

salarios = []
for i in range(5):
    sal = float(input("digite seu salário: "))
    salarios.append(sal)
    if sal <= 1500:
        print("")
        print("aumento com 10%")
    elif sal > 1500:
        print("")
        print("aumento com 8%")