import csv
import random

def palabras_aleatorias(arc_palabras):
	'''recibe un archivo csv con palabras|silabas|definicion, devuelve palabras al azar'''
	
def fraseEnDos(frase):
	'''recibe una lista que contiene la frase, devuelve una lista con la frase partida en dos'''
	print(''.join(frase[0].split()))
	fraseJunta = ''.join(frase[0].split())
	return fraseJunta // 2
	
def elegir_frase(arc_frases):
	'''recibe un archivo csv con el formato frases|columas|autor, elige una frase al azar y devuelve una lista
	con el formato que le llega'''
	frases = {}
	with open(arc_frases,encoding= "utf8") as archivoFrases:
		for linea in archivoFrases:
			frase,columnas,autor = linea.rstrip('\n').split('|')
			if not frase in frases:
				frases[frase] = [columnas,autor]

	listaClaves = list(frases.keys())
	claveAlea = random.choice(listaClaves)
	valorClaveAlea = frases.get(claveAlea)
	print([claveAlea.strip('"'), valorClaveAlea[0], valorClaveAlea[1]])
	return [claveAlea, valorClaveAlea[0], valorClaveAlea[1]]

def main():
	
	frase_aleatoria = elegir_frase('frases.csv')
	numFilas = fraseEnDos(frase_aleatoria)
	palabras_aleatorias('palabras.csv', numFilas)

main()