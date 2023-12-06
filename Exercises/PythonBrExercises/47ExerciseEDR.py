atleta = input("digite o nome do atleta")
notas = [0, 0, 0, 0, 0, 0, 0]
total = 0
notaMax = 0
notaMin = 10.1

for i in range(7):
    notas[i] = float(input())
    total += notas[i]
    if 0 > notas[i] > 10:
        notas[i] = float(input())
    elif notas[i] > notaMax:
        notaMax = notas[i]
    elif notas[i] < notaMin:
        notaMin = notas[i]

media = (total - notaMax - notaMin) / 5

print("--" * 50)
print(notas)
print(notaMax)
print(notaMin)
print(media)
