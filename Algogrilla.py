import csv
import random

def main():
	
	frase_aleatoria = elegir_frase('frases.csv')
	palabras_aleatorias('palabras.csv', frase_aleatoria)


def palabras_aleatorias(arc_palabras, frase_aleatoria):
	'''recibe un archivo csv con palabras|silabas|definicion, devuelve una lista con palabras al azar'''
	listFrase = partir_frase(frase_aleatoria)
	print(len(listFrase[0]), len(listFrase[1]))
	palabras = abrirArchivo(arc_palabras)

	listaPalabra = []
	listaDePalabras = list(palabras.keys())
	numPosicion = frase_aleatoria[1].split(',') #lista que contiene las columnas
	print(numPosicion)
	'''while len(listaPalabra) <= max(len(listFrase[0],len(listFrase[1]))): 
		palabraAlea = random.choice(listaDePalabras)
		if '''

def partir_frase(frase):
	'''recibe una lista que contiene la frase en la posicion cero, devuelve una lista con la frase partida en dos'''
	print(''.join(frase[0].split()))
	fraseJunta = ''.join(frase[0].split())
	print([fraseJunta[:len(fraseJunta)//2],fraseJunta[(len(fraseJunta)//2):]])
	return [fraseJunta[:len(fraseJunta)//2],fraseJunta[(len(fraseJunta)//2):]]

	
def elegir_frase(arc_frases):
	'''recibe un archivo csv con el formato frases|columas|autor, elige una frase al azar y devuelve una lista
	con el formato que le llega'''
	frases = abrirArchivo(arc_frases)

	listaClaves = list(frases.keys()) #toma las claves del dicc y las guarda en una lista
	claveAlea = random.choice(listaClaves)
	valorClaveAlea = frases.get(claveAlea)
	print([claveAlea.strip('"'), valorClaveAlea[0], valorClaveAlea[1]])
	return [claveAlea.strip('"'), valorClaveAlea[0], valorClaveAlea[1]]

def abrirArchivo(archivo):
	'''recibe un archivo y devuelve el contenido en un diccionario'''
	diccionario = {}
	with open(archivo,encoding= "utf8") as arch:
		for linea in arch:
			try:
				columna1,columna2,columna3 = linea.rstrip('\n').split('|')
			except:
				continue
			if not columna1 in diccionario:
				diccionario[columna1] = [columna2,columna3]
	return diccionario


main()