
import random
import argparse

def main():

	parser = argparse.ArgumentParser(description='Algogrillas')
	parser.add_argument('-s', '--solucion', action='store_true', help='imprimir la solución')
	#parser.add_argument('-n', '--numero', help='número de algogrilla')
	args = parser.parse_args()
	imprimir_solucion = args.solucion # es True si el usuario incluyó la opción -s
	
	frase_aleatoria = elegir_frase('frases.csv')
	palabras_elegidas = elegir_palabras('palabras.csv', frase_aleatoria)

	numpos = frase_aleatoria[1].split(',')

	imprimirs(palabras_elegidas,numpos,imprimir_solucion)

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

		numPos = frase_aleatoria[1].split(',')

		imprimir(numero, palabra, palabras_elegidas, numPos )

def imprimirs(palb,numpos, imprimir_solucion):
	print('GENERADOR DE ALGOGRILLAS')
	print()

	for fila in range(len(palb)):
			if fila < 9:
				print('{}.  {}'.format(fila+1, '.'*len(palb[fila])))
			if fila >= 10:
				print('{}. {}'.format(fila + 1, '.'*len(palb[fila])))
			print()
			print(DEFINICIONES)

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


'''def imprimir(num, pal, palb, pos):
	numCorrectos = []
	for fila in range(len(palb)):
		for columnas in fila:
			if (num -1)==fila and pal == palb[fila]:
				numCorrectos.append(num)'''




def elegir_palabras(arc_palabras, frase_aleatoria):
	'''recibe un archivo csv con palabras|silabas|definicion y una lista que contiene una frase,columnas,autor
	y devuelve una lista con palabras al azar'''
	listFrase = partir_frase(frase_aleatoria)
	palabras = abrirArchivo(arc_palabras)

	listaPalabra = []
	listaDePalabras = list(palabras.keys())
	numPos = frase_aleatoria[1].split(',') #lista que contiene las columnas
	maximo = max(len(listFrase[0]),len(listFrase[1]))
	for i in range(maximo):
		for o in listaDePalabras:
			c = random.choice(listaDePalabras)
			if c in listaPalabra:
				continue
			if len(listFrase[0]) > len(listFrase[1]) and i == (maximo-1):
				if int(numPos[0]) < len(c) < int(numPos[1]):
					if len(c) < int(numPos[1]) and c[int(numPos[0])] == listFrase[0][i]:
						listaPalabra.append(c)
						break
				continue
			if len(c) > int(numPos[1]):
				if c[int(numPos[0])] == listFrase[0][i] and c[int(numPos[1])] == listFrase[1][i]:
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
	print(fraseJunta, len(fraseJunta))
	if len(fraseJunta)%2 !=0:
		return [fraseJunta[:(len(fraseJunta)//2)+1],fraseJunta[(len(fraseJunta)//2)+1:]]

	print([fraseJunta[:(len(fraseJunta)//2)],fraseJunta[(len(fraseJunta)//2):]])
	return [fraseJunta[:(len(fraseJunta)//2)],fraseJunta[(len(fraseJunta)//2):]]

	
def elegir_frase(arc_frases):
	'''recibe un archivo csv con el formato frases|columas|autor, elige una frase al azar y devuelve una lista
	con el formato que le llega'''
	frases = abrirArchivo(arc_frases)

	listaClaves = list(frases.keys()) #toma las claves del dicc y las guarda en una lista
	claveAlea = random.choice(listaClaves)
	valorClaveAlea = frases.get(claveAlea)
	print([claveAlea.strip('"').lower(), valorClaveAlea[0], valorClaveAlea[1]])
	return [claveAlea.strip('"').lower(), valorClaveAlea[0], valorClaveAlea[1]]

def abrirArchivo(archivo):
	'''recibe un archivo y devuelve el contenido en un diccionario'''
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