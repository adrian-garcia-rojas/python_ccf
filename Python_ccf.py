#Indices y sublistas

cursos = ["python", "django", "flask", "c", "c++", "c#", "java", "php"]
print(cursos[0])

#sublista
sub = cursos[0:3]
sub1 = cursos[1:7:2] #quiero la lista desde la posicion 1 a la 7 con saltos de 2 en dos
sub2 = cursos[:5] #le indica a python que requerimos los valores desde la posicion 0 a la 5
sub3 = cursos[2:] #le indica a python que queremos los valores desde la posicion 2 a la ultima
sub4 = cursos[:] #python copiara toda la lista tal cual esta
sub5 = cursos[::-1] #regresara el inverso de nuestra lista (inverso)
print(sub3)