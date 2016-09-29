import random #Vi importerar biblioteket random för att kunna blanda kortleken.

class Kort:
	def __init__(self, färg, värde):
		#Varje kort har två instansvariabler, färg och värde.
		self.färg = färg
		self.värde = värde

	def __str__(self):
		return self.färg + " " + self.värde
		#Pythons str-metod måste returnera en string.
		#Vi returnerar hur vi vill att objektet ska representeras som en string.

class Kortlek:
	def __init__(self):
		self.korten = [] #Lista med alla korten

		värden = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Kn", "D", "K", "E")
		färger = ("Hj", "Kl", "Ru", "Sp")
		#Två tuplar som innehåller alla värden och alla färger
		#En tuple fungerar som en lista, men vi kan inte lägga till/ta bort data.

		#Nästlad forloop som räknar igenom färger samt värden
		for färg in färger:
			for värde in värden:
				kortobjekt = Kort(färg, värde)
				#Vi skapar ett kort för varje kombination av färg och värde
				self.korten.append(kortobjekt)
				#Kortet (objekt av klassen Kort) som skapats läggs till i listan.

	def __str__(self):
		#Vi bygger ihop en string med alla korten och returnerar denna.
		resultat = "Kortlek: \n"
		for kort in self.korten:
			resultat += str(kort) + "\n"
			#För varje kort lägger vi till str-representationen av kortet. (Vi kallar på str i kortklassen)
		return resultat

	def blanda(self):
		random.shuffle(self.korten)
		#Blandar listan med objekten.

def main():
	k = Kortlek()#Vi skapar här ett objekt av klassen Kortlek (Konstruktorn påkallas)
	print(k)#Vi skriver ut objektet vi skapar (__str__ i Kortlek påkallas)
	k.blanda()#Vi kallar på metoden blanda i Kortlekklassen.
	print(k)#Vi skriver ut objektet igen (denna gång är korleken blandad.)

main()




