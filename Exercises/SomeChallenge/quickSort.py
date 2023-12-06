def quick(lista, inicio, fim):
    if inicio < fim:
        pivo = dividir(lista, inicio, fim)
        quick(lista, inicio, pivo-1)
        quick(lista,pivo+1, fim)

def dividir(lista, inicio, fim):
    base = lista[inicio]
    i = inicio
    j = i + 1
    while j <= fim:
        if lista[j]<base:
            it = 1
    troca (lista+i,j)
    it = 1