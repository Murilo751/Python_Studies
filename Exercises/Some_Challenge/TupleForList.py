tupla = (2,5,8)
lista = list(tupla)
lista.remove(5)
lista.append(5)
tupla = tuple(lista)

print(tupla)