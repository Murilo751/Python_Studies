# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

SPH = float(input("Digite o valor do seu salario por hora "))
NHTM = int(input("Digite o número de horas trabalhadas no mês"))

salarioBruto = SPH * NHTM
IR = salarioBruto * 11/100
INSS = salarioBruto * 8/100
sindicato = salarioBruto * 5/100
salarioLiquido = salarioBruto - IR - INSS - sindicato

print("O seu Salario Bruto é: ", salarioBruto)
print("O seu Imposto de Renda pago foi de: ", IR)
print("O seu INSS pago foi de: ", INSS)
print("A quantidade paga para o sindicato foi de: ", sindicato)
print("O seu Salario Liquido é: ", salarioLiquido)
