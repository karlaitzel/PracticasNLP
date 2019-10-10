import nltk
import math
#Frecuencia del termino en 1 documento
def frecuencia (doc, term):
	with open(doc, 'r') as file:
		texto = file.read()
		documento = texto.split()
		termino = term
		contador = 0
		for i in documento:
			if (i == termino):
				contador = contador+1
		return contador
#Cantidad de documentos donde esté el documento
def contarTerminos(term, Documentos):#documentos es muchas listas dentro de una lista
	contador = 0
	for i in Documentos:
		if (term in i):
			contador = contador+1
	return contador


def tfidf(term, doc, Documentos):
	with open (doc, "r") as file:
		documento = file.read()
		documento = documento.split()
	#print(len(doc))
	#print(frecuencia(doc,term))
	longitud = len(documento)
	#longitud = longitud * 1.0
	tf = frecuencia(doc, term) / (longitud*1.0)
	#print(tf)
	idf = math.log(len(Documentos) / contarTerminos(term, Documentos))
	resultado = tf * idf
	return resultado

def hacerMatriz(terminos,Documentos):
	documentos = []
	fila = []
	columna = [] 
	for i in Documentos:
		with open(i, 'r') as file:
			doc = file.read()
			doc = doc.split()
		documentos.append(doc)
	for i in range(len(Documentos)):
		for j in terminos:
			fila.append(tfidf(j, Documentos[i],documentos))
		columna.append(fila)
		fila=[]
	return columna  		

def coseno(vectorA, vectorB):
	for i in range(len(vectorA)):
		suma = (vectorA[i]*vectorB[i])+suma
		sumaA =(vectorA[i]*vectorA[i])+suma
		sumaB =   	

#Para probar la frecuencia 
#Documentos=[["hola","como"], ["hola"],["como"]]
#algo=tfidf("hola","prueba.txt", documentos)
#print(algo)

#Para probar la matrix
terminos=["hola","como"]
Documentos=["prueba.txt","prueba2.txt"]
matriz=hacerMatriz(terminos, Documentos)
print(matriz)

