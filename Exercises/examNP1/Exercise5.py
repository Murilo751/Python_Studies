# QUESTÃO 5

peso = float(input("Digite o peso do peixe "))
limite = 50

if peso > limite:
    excesso = peso - limite
    valMulta = excesso * 4

print("O peso do peixe inserido foi de: ", peso)
if peso > limite:
 print("O peso exedido foi de:", excesso)
 print("A multa a ser paga tem o valor de: ", valMulta)

else: print("Tudo nos conformes")