#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
#usuario la nota que ha sacado en cada asignatura, y después las muestre por 
#pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
#es cada una des las asignaturas de la lista y <nota> cada una de las 
#correspondientes notas introducidas por el usuario.
#===========================================================================


subject_List = ['MATEMÁTICAS', 'FÍSICA', 'QUÍMICA', 'HISTORIA', 'LENGUA']
subject_Dict = {}


for x in subject_List:	
	score_Of_Subject = input(f'Enter your score in {x}:')
	subject_Dict[x] = score_Of_Subject

for k, v in subject_Dict.items():
    for w in v:
        print(f'Your score in {k} was {w}')


