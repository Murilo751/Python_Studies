# Número por extenso.
# Escreva um programa que solicite ao usuário a digitação de um número até 99
# e imprima-o na tela por extenso.
unidades = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove"]
dezenas = ["vinte", "trinta", "quarenta", "cinquanta", "sessenta", "setenta", "oitenta", "noventa"]
i = 0
j = 0

N = int(input("Digite um número até 99 "))

if N > 99 or N < 0: print("Numero invalido")

if N == 0: print("Zero")

elif N <= 9:
    for i in range(9):
        if N == i + 1: print(unidades[i])

elif 10 <= N < 20:
    for i in range(9):
        if N == i + 10: print(especiais[i])

elif N >= 20:
    if N == 20: print(dezenas[0])

    for i in range(9):
        if N == i + 21:
            print(dezenas[0] + " e " + unidades[i])

    if N == 30: print(dezenas[1])

    for i in range(9):
        if N == i + 31:
            print(dezenas[1] + " e " + unidades[i])

    if N == 40: print(dezenas[2])

    for i in range(9):
        if N == i + 41:
            print(dezenas[2] + " e " + unidades[i])

    if N == 50: print(dezenas[3])

    for i in range(9):
        if N == i + 51:
            print(dezenas[3] + " e " + unidades[i])

    if N == 60: print(dezenas[4])

    for i in range(9):
        if N == i + 61:
            print(dezenas[4] + " e " + unidades[i])

    if N == 70: print(dezenas[5])

    for i in range(9):
        if N == i + 71:
            print(dezenas[5] + " e " + unidades[i])

    if N == 80: print(dezenas[6])

    for i in range(9):
        if N == i + 81:
            print(dezenas[6] + " e " + unidades[i])

    if N == 90: print(dezenas[7])

    for i in range(9):
        if N == i + 91:
            print(dezenas[7] + " e " + unidades[i])


