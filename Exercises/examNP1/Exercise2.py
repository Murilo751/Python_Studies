# QUESTÃO 2

alturaPai = float(input("Digite a altura de seu pai: "))
alturaMae = float(input("Digite a altura de sua mãe: "))
altura = float(input("Digite a sua altura: "))
sexo = str(input("Digite M par masculino e F para feminino "))

media = alturaPai + alturaMae

if sexo.upper() == "M":
    media += 12.5

elif sexo.upper() == "F":
    media = media - 12.5

else:
    print("sexo invalido")

mediafinal = media / 2

intervalo = mediafinal - altura

print(intervalo)
