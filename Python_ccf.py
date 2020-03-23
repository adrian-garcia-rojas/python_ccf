#Entrada de datos por teclado

#Comentado
#print("Cual es tu nombre?")
#nombre = input() #la funcion input() -> regresa un valor de tipo string
#print("Cual es tu edad?")
#edad = int(input()) #de esta forma int va a tomar la funcion input() y la convertira en un entero
#print("cual es tu peso?")
#peso = float(input())
#print("Estas autorizado?(si/no)")
#autorizado = input() == "si"


#Optimizando codigo
nombre = input("Cual es tu nombre?\n")
edad = int(input("Cual es tu edad?\n")) #de esta forma int va a tomar la funcion input() y la convertira en un entero
peso = float(input("cual es tu peso?\n"))
print("Estas autorizado?(si/no)")
autorizado = input() == "si"


print("Hola", nombre)
print ("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)