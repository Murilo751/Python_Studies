# QUESTÃO 3

nome = str(input())

saltos = [0,0,0,0,0]
soma = 0

for i in range(5):
    saltos[i] = float(input())
    soma += saltos[i]

media = soma/5

print("Atleta:", nome)
print("Saltos:", saltos)
print("Média dos saltos:", media)
