#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""  

# Translate to F language
def translateToF(sentence):
	vowels = ['a', 'e', 'i', 'o', 'u','u', 'A','E', 'I', 'O', 'U', 'y', 'Y']
	specialVowels = ['á', 'é', 'í', 'ó', 'ú', 'ü', 'Á', 'É', 'Í', 'Ó','Ú']
	sentenceLen = len(sentence)
	newSentence = sentence
	j=0
	for i in range(sentenceLen):
		char = sentence[i]
		if (char in vowels or char in specialVowels):
			if j == 0:
				j=i
			if char in specialVowels:
				indexSV = (specialVowels.index(char), specialVowels.index(char)-6)[specialVowels.index(char)>5] 
				newSentence = newSentence[:j+1] + 'f' + vowels[indexSV] + newSentence[j+1:]
			elif (char == 'y' or char == 'Y'):
				if not(sentence[i+1] in vowels):
					newSentence = newSentence[:j+1] + 'f' + vowels[2] + newSentence[j+1:]
				else: 
					j-=2
			else:
				indexV = (vowels.index(char), vowels.index(char)-6)[vowels.index(char)>5] 
				newSentence = newSentence[:j+1] + 'f' + vowels[indexV] + newSentence[j+1:]
			j+=2
		j+=1
	print("Palabra en Lenguaje de la F: "+newSentence)

if __name__ == "__main__":
    sentence = input("Ingrese su texto a traducir: ")
    translateToF(sentence)