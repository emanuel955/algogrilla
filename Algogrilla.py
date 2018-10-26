import csv
import random

def main():
	
	frase_aleatoria = elegir_frase('frases.csv')
	frases_elegidas = elegir_palabras('palabras.csv', frase_aleatoria)


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