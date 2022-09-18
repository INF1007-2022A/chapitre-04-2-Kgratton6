#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	lettre = name.find('-')
	lettre_replace = chr(ord(name[0]) - 32)
	nom_maj = name.replace(name[0], lettre_replace)
	nouveau_nom = nom_maj[0] + nom_maj[1:lettre].lower()

	return nouveau_nom

def get_random_sentence(animals, adjectives, fruits):
	phrase = 'Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s'

	choix_animal = animals[random.randrange(0, (len(animals)))]
	choix_adjectif = adjectives[random.randrange(0, (len(adjectives)))]
	choix_fruit = fruits[random.randrange(0, (len(fruits)))]

	return phrase % (choix_animal, choix_adjectif, choix_fruit)

def encrypt(text, shift):
	nouveau_mot = ''
	for i in text:
		if 96 < (ord(i) + shift) < 123:
			nouveau_mot += chr(ord(i) - 32 + shift)
		elif ord(i) + shift >= 123:
			nouveau_mot += chr(ord(i) - 58 + shift)
		elif 64 < (ord(i) + shift) < 91:
			nouveau_mot += chr(ord(i) + shift)
		elif ord(i) + shift >= 91:
			nouveau_mot += chr(ord(i) - 26 + shift)
		else:
			nouveau_mot += i
	return nouveau_mot

def decrypt(encrypted_text, shift):
	ancien_mot = ''
	for i in encrypted_text:
		if 65 <= ord(i) <= 90:
			if ord(i) - shift <= 64:
				ancien_mot += chr(ord(i) + 26 - shift)
			else:
				ancien_mot += chr(ord(i) - shift)
		else:
			ancien_mot += i
			
	return ancien_mot


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
