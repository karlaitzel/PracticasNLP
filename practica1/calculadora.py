#Ejemplo Calculadora
class Calculadora: 
	numero1=0
	numero2=0

	#Constructor
	def __init__ (self, num1, num2):
		self.numero1=num1
		self.numero2=num2

	#Funciones
	def suma(self):
		resultado = self.numero1 + self.numero2
		return resultado

	def resta(self):
		resultado = self.numero1 - self.numero2
		return resultado

	def multiplicacion(self):
		#resultado = self.numero1 * self.numero2
		#return resultado
		contador=self.numero2
		resultado=0
		while (contador > 0):
			resultado = resultado+self.numero1
			contador = contador-1
		return resultado

		for  in (>0)
			if 

	#Ejemplo con un If 
	def division(self):
		#resultado = self.numero1 / self.numero2
		#return resultado
		if self.numero2 == 0:
			print ("Error")
		else:	
			resultado = self.numero1 / self.numero2
			return resultado		

	def entrada(self):
		n1=int(input("Ingresa el primer numero:"))
		n2=int(input("Ingresa el segundo numero:"))
		self.numero1=n1 
		self.numero2=n2


ObjCalc=Calculadora(1,5)
resultadoEntrada=ObjCalc.entrada()
resultadoSuma=ObjCalc.suma()
resultadoResta=ObjCalc.resta()
resultadoMulti=ObjCalc.multiplicacion()
resultadoDiv=ObjCalc.division()



print(resultadoDiv)
print(resultadoMulti)
print(resultadoResta)
print(resultadoSuma)


