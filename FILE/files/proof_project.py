

#Ejercicio 3
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
#de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
#mensaje informando de ello.

#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	0.85
#Naranja	0.70

#platano : {'precio':19, 'peso':36}
#===========================================================================


exit_number = 0
dictionary_fruits = {'sandia':{'WEIGHT':'12', 'PRICE':'$42'}, 'payaya':{'WEIGHT':'19', 'PRICE':'$14'}}
while exit_number != 1:
	only_fruit_dictionary = {}
	list_fruits = ['WEIGHT', 'PRICE']
	print('============================================================================')
	enter_number = int(input("1._Press '2'  to add a new fruit: \n2._Press '3' to look for a fruit: \n4._Press '4' to see our stock: \n3._Press '1' to go out: \nSelect a option: "))
	print('============================================================================')

	if enter_number == 2:
		fruin_name = input('Enter the fruit name: ')
		for i in list_fruits:			
			fruit_data = input(F'Enter the {i}: ')
			only_fruit_dictionary[i] = fruit_data
		dictionary_fruits[fruin_name] = only_fruit_dictionary
		for key, value in dictionary_fruits.items():
			print(key, value)
		print(only_fruit_dictionary)


	elif enter_number == 3:
		sedated_fruit = input('Enter the fruit name: ')		
		if sedated_fruit in dictionary_fruits.keys():
			print(f'{list(dictionary_fruits.keys())[list(dictionary_fruits.values()).index(dictionary_fruits[sedated_fruit])]}: {dictionary_fruits[sedated_fruit]}')
		else:
			print(f'We doesnt have the fruit requested: {sedated_fruit}')

	elif enter_number == 4:
		for key, value in dictionary_fruits.items():
			print(key, value)
	
	elif enter_number == 1:
		break

print('============================================================================')
print('===========================  PROGRAM SHUTDOWN  =============================')
print('============================================================================')


