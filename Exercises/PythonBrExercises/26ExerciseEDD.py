# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = str(input("Qual tipo de combustivel ? Digite A para álcool e digite G para gasolina \n"))
litros = int(input("Quantos litros foram vendidos \n"))

if combustivel.upper() == "A":
    valor = litros * 1.90
    if litros <= 20:
        Disconto = valor - (3 / 100)
    else:
        Disconto = valor - (5 / 100)


elif combustivel.upper() == "G":
    valor = litros * 2.50
    if litros <= 20:
        Disconto = valor - (4 / 100)
    else:
        Disconto = valor - (6 / 100)

else:
    print("Combustivel nao indetificado")

print(Disconto)
