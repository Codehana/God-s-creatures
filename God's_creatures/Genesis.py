#! /usr/bin/env python3

"""
Funkce genesis náhodně vygeneruje zvířata s určitými vlastnostmi, poté co zadáte počet zvířat.
"""

import random

pocet_zvirat = int(input("Kolik bude zvířátek? "))
seznam_zvirat = []
def genesis(pocet_zvirat):
	while pocet_zvirat != 0:
		pocet_zvirat = pocet_zvirat - 1
		casti = {"nohy" : [2,3,4], "kozich" : ["True","False"], "jidlo" : ["maso","oboje","vegie"]}
		z = {"pocet_nohou" : random.choice(casti["nohy"]), "kozisek" : random.choice(casti["kozich"]), "potrava" : random.choice(casti["jidlo"])}
		seznam_zvirat.append(z)
	
	return(seznam_zvirat)
seznam_zvirat = genesis(pocet_zvirat)
print(seznam_zvirat)
