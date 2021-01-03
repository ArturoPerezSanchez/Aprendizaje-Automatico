from matplotlib import pyplot as plt
import math

# Función que crea todas las posibles combinaciones 
# de listas binarias con n elementos y devuelve 
# cuantas de ellas son tienen 2 o menos 1's
def counter(n):
	count = 0
	binformat = '0' + str(n) + 'b'
	for i in range(2**n):
		cadena = str(format(i, binformat))
		if(cadena.count('1') <= 2):
			count += 1
	return (count)

def prData(n,estimacion, real):
	print('Para n=' + str(n))
	print('Estimacion:' + str(estimacion))	
	print('Reales: ' + str(real) + '\n')

def main():
	n = 16 #Tamaño máximo de la lista
	printData = True #Mostrar por consola los resultados de cada ejecución
	xvalues = []
	yvalues = []
	for n in range(1,n+1):
		estimacion = int((n**2 + n + 2)/2)
		real = counter(n)
		xvalues.append(n)
		yvalues.append([estimacion, real])
		if(printData):
			prData(n, estimacion, real)
	plt.plot(xvalues, yvalues)
	plt.show()

main()