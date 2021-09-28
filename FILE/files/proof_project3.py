#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
#usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
#asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
#asignaturas que el usuario tiene que repetir.
#===========================================================================



subject_List = ['MATH', 'PHYSIC', 'CHEMISTRY', 'HISTORY', 'LANGUAGUE']
subject_Dict = {}


for x in subject_List:	
	score_Of_Subject = input(f'Enter your score in {x}:')
	subject_Dict[x] = score_Of_Subject

recovery_List = []
for x, y in subject_Dict.items():
	if int(y) < 6:
		recovery_List.append(x)

print(f'{recovery_List}: This is a subject you must to recover')

