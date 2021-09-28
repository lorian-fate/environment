#ejercicio 6:
# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla si es un número primo o no.
#===========================================================================


number1 = int(input('Enter a number: '))
listNumber1 = []
for a in range(number1, 0, -1):
	x = number1%a
	listNumber1.append(x)

ceroQuantity = listNumber1.count(0)
if quantitiCero == 2:
	print(f'{number1}, es un numero primo')
else:
	print(f'{number1}, no es un numero primo')
