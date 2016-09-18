#Övning 3
#Matbutik skalprogram

def storePrices():
	#Funktionen storePrices läser in varor och priser ifrån textfilen.
	#Samt lagrar datan i ett dictionary och returnerar detta.
	prices = {} #Vi skapar ett tomt dictionary

	file = open("priser.txt", "r", encoding = "UTF-8")
	#vi öppnar filen och anger filnamn, "r" för read, samt på vilket sätt filen är encoded.

	lines = file.readlines()#Ger oss en lista, där varje element är en rad i textfilen
	
	for i in range(len(lines)):#För varje rad hämtar vi ut data och lägger i dictionary
		line = lines[i]
		clearLine = line.rstrip() #rstrip tar bort radbrytstecknet d.v.s. \n
		food, price = clearLine.split("#") #Split delar upp strängen i en lista, delningen sker vid "#"

		prices[food] = price #Vi lägger till i dictionaryn.

	file.close()
	return prices


def main():
	print("Välkommen till matbutiken. \nSkriv in vara för att få pris. \nSkriv avsluta för att avsluta.")
	prices = storePrices() #Vi kallar på funktionen storePrices och lagrar dictionaryn som den returnerar i prices.

	inMenu = True
	while inMenu:
		svar = input("Ange vara eller avsluta: ")

		if svar == "avsluta":
			inMenu = False

		else:
			price = prices[svar]
			#Vi kan här hämta ut datan från vår dictionary genom att använda nyckeln (key), vilket är varans namn
			print("priset är ", price)

main()