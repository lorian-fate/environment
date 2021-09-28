#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña hasta que introduzca la 
#contraseña correcta.
#===========================================================================


password = 'd35t1ny'
password1 = ''
while password1 != password:
	print('=============================================')
	password1 = input('Enter your password: ')
	if password1 != password:
		print('Access denied')
	else:
		print('Access granted')
		break

