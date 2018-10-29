
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
	listFraseEnDos = partir_frase(frase_aleatoria)
	palabras_elegidas = elegir_palabras(dicDePalabras, frase_aleatoria[1],listFraseEnDos)

	while len(palabras_elegidas) < (len(listFraseEnDos[0])):
		frase_aleatoria = elegir_frase(dicDeFrases)
		listFraseEnDos = partir_frase(frase_aleatoria)
		palabras_elegidas = elegir_palabras(dicDePalabras, frase_aleatoria[1], listFraseEnDos)


	imprimirs(palabras_elegidas,frase_aleatoria[1],imprimir_solucion, dicDePalabras)

	numCorrectos = []
	while True:
		try:
			numero = int(input('Ingrese un numero de palabra o 0 para terminar: '))
		except ValueError:
			print('No es un numero')
			continue
		if numero == 0:
			return 'Fin del Juego'
		palabra = input('ingrese la palabra: ')
		if not palabra.isalpha():
			print('No es una palabra')
			continue

		for fila in range(len(palabras_elegidas)):
			if (numero -1)==fila and palabra == palabras_elegidas[fila]:
				numCorrectos.append(numero-1)
				numCorrectos.sort()
			if (numero -1)==fila and palabra != palabras_elegidas[fila]:
				print('No es la palabra correcta')
				continue

		imprimir(numero, palabra, palabras_elegidas, frase_aleatoria[1], dicDePalabras,numCorrectos)

def imprimirs(palb,numpos, imprimir_solucion,dicDePalabras):
	print('GENERADOR DE ALGOGRILLAS')
	print()
	
	for fila in range(len(palb)):
			if fila < 9:
				print('{}.  {}'.format(fila+1, '.'*len(palb[fila])))
			if fila >= 9:
				print('{}. {}'.format(fila + 1, '.'*len(palb[fila])))
			print()
	print()
	print('DEFINICIONES')
	for i in range(len(palb)):
		valor = dicDePalabras.get(palb[i])
		print('{}. {}'.format(i+1,valor[1]))
			
	print()
	if imprimir_solucion:
		print('SOLUCION')
		print()
		
		for fila in range(len(palb)):
			if fila < 9:
				print('{}.  {}'.format(fila+1, palb[fila][:int(numpos[0])]+ palb[fila][int(numpos[0])].upper() + 
					palb[fila][(int(numpos[0])+1):int(numpos[1])] + palb[fila][int(numpos[1])].upper() + palb[fila][int(numpos[1])+1:]))
			if fila >= 9:
				if len(palb[fila]) == int(numpos[1]):
					print('{}. {}'.format(fila + 1, palb[fila][:int(numpos[0])]+ palb[fila][int(numpos[0])].upper() + 
					palb[fila][(int(numpos[0])+1):int(numpos[1])] + palb[fila][int(numpos[1])].upper()))
				if len(palb[fila]) < int(numpos[1]):
					print('{}. {}'.format(fila + 1, palb[fila][:int(numpos[0])]+ palb[fila][int(numpos[0])].upper() + 
					palb[fila][(int(numpos[0])+1):int(numpos[1])]))

				print('{}. {}'.format(fila + 1, palb[fila][:int(numpos[0])]+ palb[fila][int(numpos[0])].upper() + 
					palb[fila][(int(numpos[0])+1):int(numpos[1])] + palb[fila][int(numpos[1])].upper() + palb[fila][int(numpos[1])+1:]))
		return None


def imprimir(numero, palabra, palb, pos, dicDePalabras,numCorrectos):
	
	for fila in range(len(palb)):
		if len(numCorrectos):
			for i in numCorrectos:
				if i == fila:
					if fila < 9:
						print('{}.  {}'.format(fila+1, palb[fila][:int(pos[0])]+ palb[fila][int(pos[0])].upper() + 
						palb[fila][(int(pos[0])+1):int(pos[1])] + palb[fila][int(pos[1])].upper() + palb[fila][int(pos[1])+1:]))
						break
					if fila >= 9:
						if len(palb[fila]) == int(pos[1]):
							print('{}. {}'.format(fila + 1, palb[fila][:int(pos[0])]+ palb[fila][int(pos[0])].upper() + 
							palb[fila][(int(pos[0])+1):int(pos[1])] + palb[fila][int(pos[1])].upper()))
							break
						if len(palb[fila]) < int(pos[1]):
							print('{}. {}'.format(fila + 1, palb[fila][:int(pos[0])]+ palb[fila][int(pos[0])].upper() + 
							palb[fila][(int(pos[0])+1):int(pos[1])]))
							break
						print('{}. {}'.format(fila + 1, palb[fila][:int(pos[0])]+ palb[fila][int(pos[0])].upper() + 
						palb[fila][(int(pos[0])+1):int(pos[1])] + palb[fila][int(pos[1])].upper() + palb[fila][int(pos[1])+1:]))
				else:
					if fila < 9:
						print('{}.  {}'.format(fila+1, '.'*len(palb[fila])))
						break
					if fila >= 9:
						print('{}. {}'.format(fila + 1, '.'*len(palb[fila])))
						break
				
			print()
		
	return

def elegir_palabras(dicPalabras, frase_aleatoria,listFrase):
	'''recibe un diccionario de palabras y una lista que contiene una frase,columnas,autor y la frase partida en dos
	y devuelve una lista con palabras al azar'''
	

	listaPalabra = []
	listaDePalabras = list(dicPalabras.keys())
	numPos1, numPos2 = frase_aleatoria #lista que contiene las columnas
	maximo = max(len(listFrase[0]),len(listFrase[1]))
	for i in range(maximo):
		for o in listaDePalabras:
			c = random.choice(listaDePalabras)
			if c in listaPalabra:
				continue
			if len(listFrase[0]) > len(listFrase[1]) and i == (maximo-1):
				if int(numPos1) < len(c) < int(numPos2):
					if len(c) < int(numPos2) and c[int(numPos1)] == listFrase[0][i]:
						listaPalabra.append(c)
						break
				continue
			if len(c) > int(numPos2):
				if c[int(numPos1)] == listFrase[0][i] and c[int(numPos2)] == listFrase[1][i]:
					listaPalabra.append(c)
					break
	print(listaPalabra)
	return listaPalabra
def partir_frase(frase):
	'''recibe una lista que contiene la frase en la posicion cero, devuelve una lista con la frase partida en dos
	si la longitud de la cadena es impar la primera parte sera mas grande que la segunda'''
	fraseJunta = ''
	for i in frase[0]:
		if not i.isalpha():
			continue
		fraseJunta += i

	if len(fraseJunta)%2 !=0:
		return [fraseJunta[:(len(fraseJunta)//2)+1],fraseJunta[(len(fraseJunta)//2)+1:]]
	return [fraseJunta[:(len(fraseJunta)//2)],fraseJunta[(len(fraseJunta)//2):]]

	
def elegir_frase(frases):
	'''recibe un diccionario con frases, elige una frase al azar y devuelve una lista
	con la frase elejida, las columnas donde va a ir ubicada y el autor'''

	listaDeClaves = list(frases.keys()) #toma las claves del dic y las guarda en una lista
	claveAleatoria = random.choice(listaDeClaves)
	valorClaveAlea = frases.get(claveAleatoria)
	return [claveAleatoria.strip('"').lower(), valorClaveAlea[0].split(','), valorClaveAlea[1]]

def abrirArchivo(archivo):
	'''recibe un archivo csv con el formato columna1|columa2|columna3 y devuelve el contenido en un diccionario'''
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