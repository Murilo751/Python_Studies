def soma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

list = [1,2,3,4,5]
resultado = soma_lista(list)
print(resultado)