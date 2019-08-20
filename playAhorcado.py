#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Diana Rocha Botello
"""
from ahorcado import Ahorcado
import random

def file_length(fileName):
	with open(fileName, 'r', encoding='utf8') as f:
		for i, line in enumerate(f, 1):
			pass
	return i + 1

def getWord(line, fileName):
	f=open(fileName, 'r', encoding='utf8')
	lines=f.readlines()
	word = lines[line]
	return word

def initGame(ahorcado):
	while ahorcado.status == 0:
		ahorcado.showStatus()
		if(ahorcado.status == 0):
			userInput = ''
			while len(userInput) != 1:
				userInput = input('Ingrese una letra: ')
				guessInLower = userInput.lower()
			ahorcado.play(guessInLower)

if __name__ == "__main__":
	fileName = 'listado-general.txt'
	errors = random.randint(3,8)
	wordIndex = random.randint(0, file_length(fileName))
	word = getWord(wordIndex, fileName)
	#print('ERRORES: '+str(errors))
	#print('palabra:'+str(wordIndex))
	#print('palabra:'+str(word))
	ahorcado = Ahorcado(word, errors)
	initGame(ahorcado)