# Operadores comunes

lista = [8.17, 90, 1, 5, 44, 1.32]

#vamos a ordenar la lista
lista.sort(reverse=True)
#si hacemos el ordenamiento lista.sort() -> tenemos un ordenamiento asc-endente
#con (reverse = true) -> tenemos un ordenamiento desc-endente


mayor = lista[0] # Al haver ordenado la lista de una forma desc el numero mayor sera la posicion 0


print(lista)
print(mayor)


#otra forma de obtener el valor maximo y minimo seria

print(".....................................>")

lista2 = [8.17, 90, 1, 5, 44, 1.32]
menor = min(lista2)
mayor = max(lista2)
longitud = len(lista2)

print("min: ", menor)
print("max: ", mayor)
print("tamaño: ", longitud)


#buscar elementos dentro de la lista

resultado = 8.17 in lista2
print("resultado de busqueda: ", resultado)
indice = lista2.index(8.17)
print("indice de la busqueda: ", indice)
contador = lista.count(5)
print("Este elemento aparece : ", contador, " en la lista2")
