import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

#Frecuencia del termimo en 1 documento
def frecuencia(doc, termin):
	documento = doc
	termino = termin
	contador = 0 

	with open (ruta, 'r') as file: #ass fp:
		texto=file.read()
		archivo = texto.split()
		for i in documento:
			if (i == termino):
				contador = contador+1 
		return contador

#Cantidad de documentos donde este el termino
def contarTerminos(termino, Documentos)
	contador = 0

	for i in Documentos:
		#Si el termino esta en toda la lista 
		if(termino in i):
			contador=contador+1
	return contador 


