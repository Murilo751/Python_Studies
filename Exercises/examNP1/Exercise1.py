# QUESTÃO 1

matriz = [[0 for _ in range(3)] for _ in range(3)]
maiorN = 0
menorN = 0
soma = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input())

        soma += matriz[i][j]

        if matriz[0][0] > maiorN: menorN = matriz[i][j]

        elif matriz[i][j] < menorN: menorN = matriz[i][j]

        if matriz[i][j] > maiorN: maiorN = matriz[i][j]

media = soma / 9
somaDiagonal = matriz[0][0] + matriz[1][1] + matriz[2][2]

print(soma)
print(maiorN)
print(menorN)
print(media)
print(somaDiagonal)

