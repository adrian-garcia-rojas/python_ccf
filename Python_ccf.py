# Tuplas
# las tuplas son inmutables (no se pueden modificar)

tupla0 = ("adrian", 2, 4.5, True)

### Tuplas valores por indices
print("Tuplas con valores por indices")
tupla = (1,2,3,4,5,6,7,8,9,0)
elemento = tupla[4]
print(elemento)


### Comprimir y descomprimir tuplas
print("comprimir y descomprimir tuplas")
tupla1 = (1,2,3,4,5,6)
uno, *dos, cinco, seis = tupla1 # aqui se puede ver como python puede ser lo suficiente inteligente para asignar variables
print(uno)
print(dos)
print(cinco)
print(seis)


### Generando nuevas tuplas a partir de tuplas y listas
print("Generando nuevas tuplas a partir de listas y tuplas")
tupla2 = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]
tupla3 = (100, 200, 300, 400)

resultado = zip(tupla, lista, tupla3) #zip, nos regresara un tupla en el objeto zip
#resultado = tuple(resultado) # asi lo convertimos en una tupla
resultado = list(resultado) # asi lo convertimos en una lista
print(resultado)