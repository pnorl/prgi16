def kinetiskEnergi(m, v):
	resultat = m*v*v/2
	return resultat

def potentiellEnergi(m, h):
	return m*9.82*h

svar = input("Ange massan på partikeln: ")
massan = float(svar)

svar = input("Ange höjden för partikeln: ")
hojd = float(svar)

svar = input("Ange hastigheten för partikeln: ")
hastighet = float(svar)

kinetisk = kinetiskEnergi(massan, hastighet)
potentiell = potentiellEnergi(massan, hojd)

print("Potentiell energi: " + str(potentiell))
print("Kinetisk energi: " + str(kinetisk))