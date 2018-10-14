import csv
import random

def palabras_aleatorias(arc_palabras):
	'''recibe un archivo csv con palabras|silabas|definicion, devuelve palabras al azar'''
	
def numFilas(frase):
	'''recibe una lista que contiene la frase, la divide en dos y devuelve el valor de la mas larga'''
	
def elegir_frase(arc_frases):
	'''recibe un archivo csv con el formato frases|columas|autor, elige una frase al azar y devuelve una lista
	con el formato que le llega'''
	frases = {}
	with open(arc_frases,encoding= "utf8") as archivoFrases:
		for linea in archivoFrases:
			frase,columnas,autor = linea.rstrip('\n').split('|')
			if not frase in frases:
				frases[frase] = [columnas,autor]

	clavesDic = list(frases.keys())
	claveDicAlea = random.choice(keys)
	valorClaveAlea = frases.get(claveDicAlea)
	return [valorDic, valorClaveAlea[0], valorClaveAlea[1]]

def main(arc_frases,arc_palabras):
	
	frase_aleatoria = elegir_frase(arc_frases)
	numFilas = filaMasLarga(frase_aleatoria)
	palabras_aleatorias(arc_palabras, numFilas)