#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Diana Rocha Botello
"""  

# add numbers from 1 to n
def addNumbers(n):
    result = 0
    for i in range(0, n+1):
        result += i
    print("El resultado de la suma es "+ str(result))

if __name__ == "__main__":
    n = int(input("Ingrese un número: "))
    # Add numbers
    addNumbers(n)