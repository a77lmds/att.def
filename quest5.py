def soma_imposto(taxa_imposto, custo):
    custo = custo + (custo * taxa_imposto / 100)
    return custo

taxa = float(input("Digite a taxa de imposto (%): "))
custo = float(input("Digite o custo do produto: "))
valor_final = soma_imposto(taxa, custo)

print("Valor com imposto:", valor_final)