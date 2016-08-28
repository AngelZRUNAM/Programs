"""	Nombre del Programa	: Cifrado Cesar
	Fecha de creacion 	: 24/08/2016
	Autor(s)		: Garcia Xoconostle Ivan Rafael
				: Zuñiga Reyes Miguel Angel
"""


"""	Metodo para cifrar o descifrar texto dependiendo del desplazamiento recorriendo letra por letra
	de la cadena validando que sea solo una cadena compuesta de letras.
	Parametros:
		wordToCipher -- Texto a cifrar o decifrar
		numericKey   -- Cantidad de desplazamientos 
		cipherType   -- Modo del algoritmo 
				1   para cifrar
			       -1   para decifrar
	        Return:
		newWord      -- Texto cifrado o decifrado 
	                     Si la cadena no pudo ser procesada el valor es None				   
""" 
def cipherWord(wordToCipher,numericKey,cipherType):
	wordToCipher = formatCipherString(wordToCipher)
	newWord = ""
	#El sentido de desplazamiento inicial para cifrar es derecha y para descifrar es izquierda
	numericKey = numericKey * cipherType
	#Contador para ayudar a llevar el sentido del desplazamiento
	#i par desplaza a la derecha, i impar desplaza a la izquierda
	i = 0
	for charctr in wordToCipher:
		#Revisamos que todo sea una letra mayúscula
		if not (ord(charctr)>=65 and ord(charctr)<=90):
			print("Error en la cadena")
			return(None)
		charctr = getLetter(charctr,numericKey,i)
		i += 1
		#Concatenamos las letras ya desplazadas
		newWord = newWord + str(charctr)	
	return(newWord)


"""Metodo para obtener la letra indicada por el desplazamiento, la direccion y la letra base """
def getLetter(charctr,numericKey,cont):
	#Revisamos si el contador es par para encontrar la dirección del desplazamiento
	if(cont%2 != 0): numericKey *= -1;
	#Sumamos el desplazamiento al valor numerico del carácter
	aux = ord(charctr) + numericKey
	#Realizamos la validación para reajustar si se salió del límite de valores ASCII para 
	#las letras mayúsculas (65,90)
	if(aux<65): aux += 26
	if(aux>90): aux -= 26
	return chr(aux)

"""Realiza un pequeño formato a la cadena para que pueda ser procesada por el algoritmo"""
def formatCipherString(stringToFormat):
	#Se cambian todas las letras a mayúsculas
	stringToFormat = stringToFormat.upper()
	#Se eliminan los espacios en blanco
	stringToFormat = stringToFormat.replace(' ', '')
	return(stringToFormat)	


def test():
	wordToCipher = "LA CRIPTOGRAFIA ES ROMANTICA"
	print("Texto a cifrar : " + wordToCipher)
	numericKey = 5
	print("Desplazamiento : " + str(numericKey))
	chiperedWord = cipherWord(wordToCipher,numericKey,1)
	print("Texto cifrado : " + chiperedWord)
	newWord = cipherWord(chiperedWord,numericKey,-1)
	print("Text decifrado: " + newWord)
	return(1)




