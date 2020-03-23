#Operadores relacionales 6, son simboloes para comparar valores donde optemdremos true false (boleanos)

variable_uno = 10
variable_dos = 18

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos

comparacion_dos_numeros_enteros = variable_uno is variable_dos

#Operadores logicos 3, and, or, not

resultado = True and True and mayor
resultado2 = False or False or diferente
print(resultado)
print(resultado2)


print("comparar si dos numeros enteros son iguales por medio de is: " + str(comparacion_dos_numeros_enteros))
