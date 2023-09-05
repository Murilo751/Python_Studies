# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Digite seu salário "))

if salario < 280.00:
    percent = 20
elif 280.00 <= salario <= 700.00:
    percent = 15
elif 700.00 <= salario <= 1500.00:
    percent = 10
elif salario > 1500.00:
    percent = 5

aumento = salario + (percent/100)
newSalario = salario + aumento

print("seu salario anterior era", salario)
print("o percentual do aumento aplicado foi de", percent)
print("o valor do almento é de", aumento)
print("seu salario como o reajuste é", newSalario)