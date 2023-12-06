# Supondo que a população de um país A seja da ordem de 80000
# habitantes com uma taxa anual de crescimento de 3% e que
# a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva
# o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

PopA = 80000
PopB = 200000

taxA = 3 / 100
taxB = 1.5 / 100

years = 0

while PopA < PopB:
    PopA += PopA * taxA
    PopB += PopB * taxB

    years += 1

print(years)