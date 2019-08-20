#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Diana Rocha Botello
"""

class Ahorcado():
	def __init__(self, word, errors):
		# Define the word to guess
		self.p = word
		# Define the number of errors
		self.E = errors
		# user errors
		self.e = 0
		# status game 0= continue, 1= finish 
		self.status = 0
		self.statusP = ''
		# Use for show the word
		for i in range(len(self.p)-1):
			self.statusP += '_ '

	def play(self, c):
		findChar = 0
		for i in range(len(self.p)):
			if(self.p[i] == c):
				pos = i*2
				self.statusP = self.statusP[:pos] + c + ' ' + self.statusP[pos+2:]
				findChar +=1
		if (findChar == 0):
			self.e +=1

	def showStatus(self):
		finishPhrase = ''
		if (self.e == self.E):
			self.status = 1
			finishPhrase = ' (Perdiste)'
		elif (self.statusP.find('_') == -1):
			self.status = 1
			finishPhrase = ' (Ganaste)'
		else:
			finishPhrase = ' ('+str((self.E - self.e))+' errores posibles)'
		print(self.statusP + finishPhrase)
