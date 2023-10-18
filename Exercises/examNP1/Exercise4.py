# QUESTÃO 4

combustive = str(input("A par Alcool e G para Gasolina"))
litros = float(input())

if combustive.upper() == "A":
    valor = litros * 1.90
    if litros <= 20: desconto = litros * (3/100)
    else: desconto = litros * (5/100)

elif combustive.upper() == "G":
    valor = litros * 2.50
    if litros <= 20: desconto = litros * (4/100)
    else: desconto = litros * (6/100)

else: print("tipo de combustivel invalido")

valor -= desconto

print(valor)

