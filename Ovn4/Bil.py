
class Bil:
	def __init__(self, marke, topphastighet, farg, vikt):
		#Konstruktorn, denna körs varje gång vi skapar ett objekt av klassen bil.
		self.marke = marke
		self.topphastighet = topphastighet
		self.farg = farg
		self.vikt = vikt
		#instansvariabler

	def repaint(self, newColor):
		#repaint ändrar färgen på bilen. Den ändrar färgen på den bilen som den körs på.
		self.farg = newColor

	def trimma(self):
		#trimma ökar topphastigheten med 5 km/h för den bilen som metoden körs på
		self.topphastighet += 5

	def __str__(self):
		#__str__ körs när vi skriver str(bil1) exempelvis. Eller när vi printar ett bilobjekt.
		#__str__ Ska alltid returnera en STRING
		return self.marke + str(self.topphastighet) + self.farg + str(self.vikt)

def main():
	bil1 = Bil("Volvo", 230, "blå", 1700)
	bil2 = Bil("Tesla", 250, "svart", 1500)
	bil3 = Bil("BMW", 240, "vit", 1750)
	#Vi skapar 3 objekt av klassen bil. Notera att anropsparametrarna stämmer med
	#parametrar i __init__ metoden i bilklassen.

	bilLista = []
	bilLista.append(bil1)
	bilLista.append(bil2)
	bilLista.append(bil3)
	#Vi lägger bilobjekt i en lista.

	for bil in bilLista:#Vi räknar igenom billistan.
		print(bil)#Här kommer python att kalla på __str__, en gång för varje objekt som ska printas.

	bilLista.sort(key = lambda x: x.topphastighet, reverse = True)
	#Vi använder pythons sortmetod som tillhör listklassen.
	#Vi skickar med en "key", inte key som i dictionary, utan key anger m.a.p. vad vi ska sortera.
	#x blir objekten i listan och x.topphastigheten är topphastigheten för varje objekt.
	#Vi sätter reverse = True för att få sorteringen i fallande ordning (högst först).
	
	print()
	for bil in bilLista:
		print(bil)

main()	
		