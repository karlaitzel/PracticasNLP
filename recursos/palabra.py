import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

def tokenzito(ruta):
    # Tokenizador TokTok (palabras)
    toktok = ToktokTokenizer()
    # Tokenizador de oracionesa
    es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
    # Obtener oraciones de un parrafo
    with open (ruta, 'r') as file: #ass fp:
      parrafo=file.read()
      oraciones = es_tokenizador_oraciones.tokenize(parrafo)
      
      # Obtener tokens de cada oración
      var=[]
      for s in oraciones:
        var = var + [t for t in toktok.tokenize(s)]
    file.close()   
    return (var)


def frecuencia(token): #Funcion para la frecuencia
    listaGeneral=[] #Lista inicializada vacía
    listaNumero=[]
    listaPalabra=[]
    longitud=len(token)#Tamaño de la lista de token
    primera=token[0]
    listaPalabra.append(primera)
    listaNumero.append(1) 
    #print(longitud)
    contador = 0

    #Mientras que el contador sea menor al tamaño de la longitud de los tokens
    while(contador < longitud - 1):
        #Si la primera palabra es igual a la segunda, tercera, cuarta, ...
        if(primera == token[contador + 1]):
            #En la posición toma el valor que tiene MAS uno
            listaNumero[0] = listaNumero[0] + 1
        #Si la palabra ya se encuentra en la lista? 
        elif(token[contador + 1] in listaPalabra):
            #Preguntar en que posición se tiene guardada para aumentarle el contador
            indice = listaPalabra.index(token[contador + 1])
            #Agrega el valor en la pcisión que tiene la palabra igual
            listaNumero[indice] = listaNumero[indice] + 1
        else:
            listaPalabra.append(token[contador + 1])
            listaNumero.append(1)
        contador = contador + 1
    #Combinar las dos listas en la listaGeneral
    #El "i" va a ir cambiando desde 0 a la longitud de la listaPalabra
    for i in range(len(listaPalabra)):
        #Se agrega en la listaGeneral la listaNumero en la pocisión "i" y la listaPalabra en la posición "i"
        listaGeneral.append((listaNumero[i], listaPalabra[i]))
    listaGeneral.sort(reverse=True)    
    return listaGeneral

#Quita las Palabras 
def reduccion(token):
    longitud=len(token)
    palabrasFuncionales = stopwords.words("spanish")
    #Lleva el ciclo de la lista
    contador = 0
    #Lleva a los indices
    auxiliar = 0
    #Mientras hay palabras 
    while(contador < longitud -1):
        # IN Regresa verdadero o falso si esta la funcion en la lista palabrasFuncionales
        if(token[auxiliar] in palabrasFuncionales):
            #Quita la palabra 
            token.remove(token[auxiliar])
            auxiliar = auxiliar - 1
        contador = contador + 1
        auxiliar = auxiliar + 1
    return token

#Distribución de Frecuencias con Stemming 
# Stemmer en Espanol  ̃
def stemming(token):
    listaStemming = []
    stemmer = SnowballStemmer("spanish")
    tokens = token # <- aquı va el texto tokenizado
    
    for t in tokens:
        #Obtener la raiz
        #print(stemmer.stem(t))
        listaStemming.append(stemmer.stem(t))
    return listaStemming

#Para probar la función frecuencia
#tokens = tokenzito("practica3.txt")
#print(frecuencia(tokens))

#Para probar la función tokenzito
#token = tokenzito('practica3.txt')
#print(token)

#Para probar la función reduccion 
#tokens = tokenzito("practica3.txt")
#print(reduccion(tokens))

#Para probar la funcion Steamming 
#tokens = tokenzito("practica3.txt")
#print(stemming(tokens))

#Para imprimmir las frecuencias en orden decreciente
tokens = tokenzito("practica3.txt")
reducir = reduccion(tokens)
cortadas = stemming(reducir)
print(frecuencia(cortadas))