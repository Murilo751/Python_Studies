# Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando for informado
# um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

numeroDValores = int(input("Quantos valores você quer ler? "))

vetor = [0 for _ in range(numeroDValores)]
soma = 0
NAdM = 0
NA7 = 0

for i in range(numeroDValores):
    vetor[i] = float(input("Digite uma nota: "))
    if -1 >= vetor[i]:
        vetor[i] = 0
        numeroDValores = numeroDValores - 1
    soma += vetor[i]

media = soma / numeroDValores

for i in range(numeroDValores):
    if vetor[i] > media:
        NAdM += 1
    if vetor[i] < 7:
        NA7 += 1

print(vetor)
print(vetor.reverse())
print("A soma dos valores é: ", soma)
print("A media dos valores é: ", media)
print("A quantidade de numeros acima da media são: ", NAdM)
print("A quantidade de numeros abaixo de 7 são: ", NA7)
