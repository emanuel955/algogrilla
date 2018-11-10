
import random
import argparse

def main():

	parser = argparse.ArgumentParser(description='Algogrillas')
	parser.add_argument('-s', '--solucion', action='store_true', help='imprimir la solución')
	#parser.add_argument('-n', '--numero', help='número de algogrilla')
	args = parser.parse_args()
	imprimir_solucion = args.solucion # es True si el usuario incluyó la opción -s
	
	dicDeFrases = abrirArchivo('frases.csv')
	dicDePalabras = abrirArchivo('palabras.csv')
	frase_aleatoria = elegir_frase(dicDeFrases)
	FrasePartida = partir_frase(frase_aleatoria)
	palabras_elegidas = elegir_palabras(dicDePalabras, frase_aleatoria[1],FrasePartida)

	while len(palabras_elegidas) < len(FrasePartida[0]):
		frase_aleatoria = elegir_frase(dicDeFrases)
		FrasePartida = partir_frase(frase_aleatoria)
		palabras_elegidas = elegir_palabras(dicDePalabras, frase_aleatoria[1], FrasePartida)

	imprimir(0,'',palabras_elegidas,frase_aleatoria[1], dicDePalabras,[])
	inicioJuego(palabras_elegidas,frase_aleatoria[1],dicDePalabras)
	
#-----------------------------------------------------------------------------
def inicioJuego(palabras_elegidas, frase_aleatoria,dicDePalabras):
	'''interactua con el usuario
	pre: recibe una lista de palabras, frase, diccionario de palabras
	post imprime a medida que el usuario introduzca lo que le pida'''
	numCorrectos = []
	while True:
		numero = input('Ingrese un numero de palabra o 0 para terminar: ')
		if numero == '0':
			return 'Fin del Juego'
		if not numero.isdigit():
			print('No es un numero')
			continue
		palabra = input('ingrese la palabra: ')
		if not palabra.isalpha():
			print('NO ES UNA PALABRA')
			continue

		if comprobar(numero,palabra,palabras_elegidas,numCorrectos):
			numCorrectos.append(int(numero)-1)
			numCorrectos.sort()

		imprimir(numero, palabra, palabras_elegidas, frase_aleatoria, dicDePalabras,numCorrectos)
#-------------------------------------------------------------------------------
def comprobar(numero, palabra, palabras_elegidas,numCorrectos):
	'''compara si el numero de fila y la pabrabra que ingresa el usuario es igual
	a la que esta en la lista de palabras_elegidas'''
		for fila in range(len(palabras_elegidas)):
			palbSinAcent = quitarAcentos(palabras_elegidas[fila])
			if (int(numero) - 1) in numCorrectos:
				print('YA INGRESO ESA PALABRA')
				return False
			if (int(numero) -1)==fila and palabra == palbSinAcent:
				return True
			if (int(numero) -1)==fila and palabra != palbSinAcent:
				print('NO ES LA PALABRA CORRECTA')
			
			
#---------------------------------------------------------------------------------------------
def imprimirSolucion(imprimir_solucion,palb,numpos):
	'''imprime la grilla vacia y a continuacion la grilla resuelta'''	
	pass
#---------------------------------------------------------------------------------------------------------------
def imprimir(numero, palabra, listaPalabras, pos, dicDePalabras,numCorrectos):
	'''pre: recibe el numero de la fila y la palabra, las posiciones donde estaran las letras en mayusculas,
	una lista con las palabras que forman la frase, una lista que contiene los numeros de las filas resueltas 
	y un diccionario que contiene las silabas de las palabras 
	post: imprime la grilla a medida que se va completando'''
	print()
	print('GENERADOR DE ALGOGRILLAS')
	print()
	
	for fila in range(len(listaPalabras)):
		if len(numCorrectos):
			for i in range(len(numCorrectos)):
				if fila not in numCorrectos:
					if fila < 9:
						print('{}.  {}'.format(fila+1, '.'*len(listaPalabras[fila])))
						break
					if fila >= 9:
						print('{}. {}'.format(fila + 1, '.'*len(listaPalabras[fila])))
						break
				if fila == numCorrectos[i]:
					if fila < 9:
						print('{}.  {}'.format(fila+1, listaPalabras[fila][:int(pos[0])]+ listaPalabras[fila][int(pos[0])].upper() + 
						listaPalabras[fila][(int(pos[0])+1):int(pos[1])] + listaPalabras[fila][int(pos[1])].upper() + listaPalabras[fila][int(pos[1])+1:]))
						break
					if fila >= 9:
						if len(listaPalabras[fila]) == int(pos[1]):
							print('{}. {}'.format(fila + 1, listaPalabras[fila][:int(pos[0])]+ listaPalabras[fila][int(pos[0])].upper() + 
							listaPalabras[fila][(int(pos[0])+1):int(pos[1])] + listaPalabras[fila][int(pos[1])].upper()))
							break
						if len(listaPalabras[fila]) < int(pos[1]):
							print('{}. {}'.format(fila + 1, listaPalabras[fila][:int(pos[0])]+ listaPalabras[fila][int(pos[0])].upper() + 
							listaPalabras[fila][(int(pos[0])+1):int(pos[1])]))
							break
						print('{}. {}'.format(fila + 1, listaPalabras[fila][:int(pos[0])]+ listaPalabras[fila][int(pos[0])].upper() + 
						listaPalabras[fila][(int(pos[0])+1):int(pos[1])] + listaPalabras[fila][int(pos[1])].upper() + listaPalabras[fila][int(pos[1])+1:]))
				
		else:
			if fila < 9:
				print('{}.  {}'.format(fila+1, '.'*len(listaPalabras[fila])))
			if fila >= 9:
				print('{}. {}'.format(fila + 1, '.'*len(listaPalabras[fila])))
	print()
	print('DEFINICIONES')
	silabas = []
	for c in range(len(listaPalabras)):
		if c in numCorrectos:
			continue
		valor = dicDePalabras.get(listaPalabras[c])
		#silabas.append(','.join(valor[0].split('-')))
		print('{}. {}'.format(c+1,valor[1]))
	print()
#----------------------------------------------------------------------------------------
def elegir_palabras(dicPalabras, posiciones,FrasePartida):
	'''pre: Recibe un diccionario de palabras que contiene una lista como valor, una lista que contiene la posiciones 
	donde va a ir la frase y la frase partida en dos
	post: devuelve una lista con palabras al azar'''
	listaDePalabra = []
	Palabras = list(dicPalabras.keys())
	numPos1, numPos2 = posiciones #lista que contiene las columnas
	maximo = max(len(FrasePartida[0]),len(FrasePartida[1]))
	for i in range(maximo):
		for o in Palabras:
			c = random.choice(Palabras)
			if c in listaDePalabra:
				continue
			if len(FrasePartida[0]) > len(FrasePartida[1]) and i == (maximo-1):
				if int(numPos1) < len(c) < int(numPos2):
					if len(c) < int(numPos2) and c[int(numPos1)] == FrasePartida[0][i]:
						listaDePalabra.append(c.lower())
						break
				continue
			if len(c) > int(numPos2):
				if c[int(numPos1)] == FrasePartida[0][i] and c[int(numPos2)] == FrasePartida[1][i]:
					listaDePalabra.append(c.lower())
					break
	print(listaDePalabra)
	return listaDePalabra
#--------------------------------------------------------------------------------------------------
def partir_frase(frase):
	'''Recibe una lista que contiene la frase en la posicion cero, devuelve una lista con la frase partida en dos
	si la longitud de la cadena es impar la primera parte sera mas grande que la segunda'''
	fraseJunta = ''
	for i in frase[0]:
		if not i.isalpha():
			if i == '(':
				break
			continue
		fraseJunta += i

	if len(fraseJunta)%2 !=0:
		print([fraseJunta[:(len(fraseJunta)//2)+1],fraseJunta[(len(fraseJunta)//2)+1:]])
		return [fraseJunta[:(len(fraseJunta)//2)+1],fraseJunta[(len(fraseJunta)//2)+1:]]
	print([fraseJunta[:(len(fraseJunta)//2)],fraseJunta[(len(fraseJunta)//2):]])
	return [fraseJunta[:(len(fraseJunta)//2)],fraseJunta[(len(fraseJunta)//2):]]

#------------------------------------------------------------------------------------------	
def elegir_frase(frases):
	'''recibe un diccionario con frases, elige una frase al azar y devuelve una lista
	con la frase elejida, las columnas donde va a ir ubicada y el autor'''

	listaDeClaves = list(frases.keys()) #toma las claves del dic y las guarda en una lista
	claveAleatoria = random.choice(listaDeClaves)
	valorClaveAlea = frases.get(claveAleatoria)
	frase = quitarAcentos(claveAleatoria.lower())
	print(frase)
	return [frase, valorClaveAlea[0].split(','), valorClaveAlea[1]]
#------------------------------------------------------------------------------------------------------
def quitarAcentos(cadena):
	'''pre: recibe una palabra o una oracion y la recorre en busca de letras con acentos
	post: devuelve una nueva cadena sin acento'''
	dic = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}
	palabraSinAcento = ''
	for i in range(len(cadena)):
		if cadena[i] in dic:
			palabraSinAcento += dic[cadena[i]]
			continue
		palabraSinAcento += cadena[i]
	return palabraSinAcento
#--------------------------------------------------------------------------------------------------------
def abrirArchivo(archivo):
	'''pre: recibe un archivo csv con el formato columna1|columa2|columna3
	post: devuelve el contenido en un diccionario'''
	diccionario = {}
	with open(archivo,encoding= "utf8") as arch:
		for linea in arch:
			try:
				clave,valor1,valor2 = linea.rstrip('\n').split('|')
			except:
				continue
			if not clave in diccionario:
				diccionario[clave] = [valor1,valor2]
	return diccionario


main()