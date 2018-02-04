#! /usr/bin/env python3

"""
Tato funkce vezme seznam zvířat z funkce genesis. Poté co napíšete, kolik procent zvířat má zemřít, funkce armagedon je odstraní ze seznamu.

"""
import random
from Genesis import seznam_zvirat

umrtnost = int(input("Kolik procent zvířat zahyne? "))
def armagedon(seznam_zvirat,umrtnost):
	pocet_odstraneni = int(len(seznam_zvirat) * (umrtnost/100))
	while pocet_odstraneni != 0:
		seznam_zvirat.remove(random.choice(seznam_zvirat))
		pocet_odstraneni = pocet_odstraneni - 1

	return(seznam_zvirat)
print(armagedon(seznam_zvirat,umrtnost))
