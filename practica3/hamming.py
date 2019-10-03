#Ejercicio distancia de Hamming 
def hamming(cad1, cad2):
	long1 = len(cad1)
	long2 = len(cad2)
	contador = 0

	if long1 != long2:
		print ("Longitud diferente")
	else: 
		for i in range(long1):
			a=cad1[i]
			b=cad2[i]
			if a!=b:
				contador = contador+1
		return contador

print(hamming("hola","toma"))

