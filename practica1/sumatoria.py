#Sumatoria con lista

def sumatoria(lista):
	resultado=0
	#len para la longitud de la lista 
	for i in range(len(lista)):
		resultado=resultado+lista[i]
	return resultado

	#Segunda forma
	#for i in lista
	#	resultado=resultado.i

	#Tercera forma
	#contador=0
	#while(contador<len(lista)):
	#resultado=resultado+lista[contador]
	#contador=contador+1

var=[1,2,3,4,8]
a=sumatoria(var)
print(a)


