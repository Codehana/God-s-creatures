#! /usr/bin/env python3

"""
Funkce polovnik náhodně vybere zvířata s určitými vlastnostmi a ty pak odstraní. Loví je s danou úspěšností.
"""

from Genesis import seznam_zvirat

def polovnik(seznam_zvirat):
	Nohy = int(input("Má mít lovené zvíře 2, 3 nebo 4 nohy? "))

	Kozich = str(input("Má mít lovené zvíře kožich?(answer True/False, please) "))

	Potrava = str(input("Má jíst lovené zvíře maso, vegie nebo oboje? "))

	Uspesnost = int(input("Na kolik procent má být lov úspěšný? "))
	
	seznam_zvirat2 = []
	y = {"pocet_nohou":Nohy, "kozisek":Kozich, "potrava":Potrava}
	for x in seznam_zvirat:
		if x == y:
			seznam_zvirat2.append(y)
			seznam_zvirat.remove(y)

	pocet_mrtvych = (len(seznam_zvirat2) * (Uspesnost/100))
	
	while pocet_mrtvych > 0:
		pocet_mrtvych = pocet_mrtvych - 1
		seznam_zvirat2.remove(y)

	seznam_zvirat = seznam_zvirat2 + seznam_zvirat

	return(seznam_zvirat)
seznam_zvirat = polovnik(seznam_zvirat)
print("Zvířata, co přežila lov: ",seznam_zvirat)

