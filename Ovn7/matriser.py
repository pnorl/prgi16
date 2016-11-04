#Skapa en matris i python.
#Det finns inget inbyggt stöd (finns stöd i paket såsom numpy)
#Vi dock konstruera en matris som listor i listor.

def main():
	matrix = createMatrix(5, 4)
	printMatrix(matrix, 5, 4)

def createMatrix(height, width):
	matrix = []#Vi skapar en tom lista som blir matrisen

	#För att skapa matrisen får vi lägga till en lista för varje rad vi vill ha.
	#Sedan får vi lägga till antalet element i varje liten lista för att skapa matrisen.

	for row in range(height):#Yttre loop
		subList = []#Liten lista. För varje varv i yttre loopen fylls matrisen med ett listelement.
		for col in range(width):#Inre loop
			subList.append(row+col)#Här lägger vi til ett faktiskt element
			#I detta exempel läggs summan av index (en int), men detta kan vara strängar, float eller objekt av klasser.

		matrix.append(subList)
	return matrix

def printMatrix(matrix, height, width):
	#För att skriva ut alla element i matrisen vill vi använda två loopar
	#För att ta fram ett element ur matrisen: matrix[index1][index2]
	#Som för att plocka ut element ur lista, men här har vi 2 index. En för rad och en för kolumn.
	
	#Ett sätt att skriva ut matrisen genom att använda matris[index1][index2]
	for row in range(height):
		output = "" #En outputsträng för varje rad
		
		for col in range(width):
			output += str(matrix[row][col]) + " "
		
		print(output)

	print("\n\nAlternativt sätt\n-------------")
	#Alternativt sätt
	#Notera att vi här inte behöver känna till matrisens dimensioner
	for subList in matrix:
		output = ""
		for element in subList:
			output += str(element) + " "
		print(output)

main()
