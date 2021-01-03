from matplotlib import pyplot as plt
import math

# Función que crea todas las posibles combinaciones 
# de listas binarias con n elementos y devuelve 
# cuantas de ellas son palindromos
def counter(n):
	count = 0
	binformat = '0' + str(n) + 'b'
	for i in range(2**n):
		cadena = str(format(i, binformat))
		cadenainv = cadena[::-1]
		if(cadena==cadenainv):
			count += 1
	return (count)

def prData(n,estimacion, real):
	print('Para n=' + str(n) + ':')
	print('estimamos que habrán ' + str(estimacion) + ' palindromos')	
	print('y realmente hay ' + str(real) + ' palindromos \n')

def main():
	n = 16 #Tamaño máximo de la lista
	printData = True #Mostrar por consola los resultados de cada ejecución
	a = []
	b = []
	for n in range(1,n+1):
		estimacion = 2**(math.ceil(n/2)) 
		real = counter(n)
		a.append(n)
		b.append([estimacion,real])
		if(printData):
			prData(n, estimacion, real)
	plt.plot(a,b)
	plt.show()

main()