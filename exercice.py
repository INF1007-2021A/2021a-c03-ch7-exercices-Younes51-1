#!/usr/bin/env python
# -*- coding: utf-8 -*-

# modules :

import math
import re
from turtle import *
from exercice_ch6 import frequence

# fonction :

def ellipsoide(a,b,c,mv) :
    volume=4/3*math.pi*a*b*c
    masse=mv*volume
    return masse, volume

def valide(value) :
    for i in range(len(value)):
        if value[i]=='a'or value[i]=='t'or value[i]=='g'or value[i]=='c' :
            return True
        else :
            return False

def saisie(a):
    value=input(f'entrez une {a} d ADN : ')
    if valide(value):
        return value
    else :
        return saisie(a)

def propotion(chaine : str,sequence : str) -> float :
    return chaine.count(sequence)/len(chaine)

def ADN() :
    chaine=saisie('chaine')
    sequence=saisie('sequence')
    print(chaine)
    print(sequence)
    print(f'Il y a {round(propotion(chaine,sequence)*100,2)} % de {sequence}')


def branch(lenght,tick,angle):
    if tick>0 and lenght>0:
        pensize(tick)
        forward(lenght)
        right(angle)
        branch(lenght-10,tick-1,angle-5)
        left(angle*2)
        branch(lenght-10,tick-1,angle-5)
        right(angle)
        backward(lenght)

def arbre() :
    setheading(90)
    color("green")
    branch(70,7,35)
    done()

def tri(phrase):
    return sorted(frequence(phrase).items(), key=lambda item : item[1])[-1]

if __name__ == '__main__':
    # Appel 
    print(ellipsoide(2,5,4,15))
    ADN()
    phrase="hello"
    print(tri(phrase))
    arbre()