#!/usr/bin/env python
#-*- coding: utf-8 -*-

from random import shuffle as revolver
from utils import clrscr, pintar, paint, welcomeMsg
from customizer import s

tubos = list()
totalTubos = 9#int(input('Ingrese cantidad total de tubos (5-12): '))
vacios = 2#int(input('Ingrese de tubos vacíos (1-2): ')) 
if not (totalTubos - vacios > 2): totalTubos = 5; vacios = 2

MAX_ITEMS = 4
setsel = 5 # number of the set of designs selected.

def display():
    char = 48 # Para ver números: 48, para ver letras: 65.
    for num, tubo in enumerate(tubos):
        print(f'{num+1}) |==',end='')
        for i, elemento in enumerate(tubo):
            if i < len(tubo)-1: print(f' {chr(int(elemento)+char)} ',end='-')
            else: print(f' {chr(int(elemento)+char)} ',end='')
        print('')

def displayAsCol():
    '''Mostrar como columnas.'''
    margin = ' ' * 4
    dash = '⎼' # ‐‑‒–—― ⏷⏸⏹⏺⏻⏼⏽⏾ ⎺⎻⎼⎽ ➊➋➌➍➎➏➐➑➒➓
    for i in range(MAX_ITEMS-1,-1,-1):
        for j in range(len(tubos)):
             if len(tubos[j]) < i+1:
                 print(margin+'-', end= '')
             else:
                 #print(margin+chr(int(tubos[j][i])+65), end ='')
                 tubo = int(tubos[j][i])
                 print(margin+s[setsel][tubo], end ='')
        print()

    for tubo in range(len(tubos)):
        print(f'{margin}{dash}',end='')
    print()

    for tubo in range(len(tubos)):
        print(f'{margin}{tubo+1}',end='')
        #print(f'{margin}{s[1][tubo]}',end='')
    print()

def mover(a,b):
    a-=1; b-=1
    if a>len(tubos) or b>len(tubos):
        input('\n¡Out of range!\n')
    elif len(tubos[a]) > 0 and len(tubos[b]) < MAX_ITEMS: # Si no sacas de un tubo vacío ni mueves a un tubo lleno:
        if len(tubos[b]) == 0: # Si mueves a un tubo vacío:
            tubos[b].append(tubos[a].pop())
        elif tubos[a][-1] == tubos[b][-1]: # Si mueves un elemento sobre otro igual:
            tubos[b].append(tubos[a].pop())
        else:
            input('\n¡Can only be moved on empty or on the same ELEMENT!\n')
    else:
        input('\n¡THIS MOVE IS NOT POSSIBLE!\n'
        'You can\'t take an element out of an empty column, '
        'nor move to a full pipe.\n'
        'Try again. '
        f'Max number of elements per tube: {MAX_ITEMS}\n'
              )

def nuevoJuego():
    global tubos
    cuartetosAlAzar = list(''.join([str(i)*MAX_ITEMS for i in range(totalTubos-vacios)]))
    revolver(cuartetosAlAzar)
    tubos = [cuartetosAlAzar[x*MAX_ITEMS:x*MAX_ITEMS+MAX_ITEMS] for x in range(totalTubos)]
    
    while verificar():
        print('\n\nMmmm.... the deck didn\'t shuffle properly... \nShuffling again!\n\n')
        nuevoJuego()

def verificar():
    completado = True
    for tubo in tubos:
        if not (len(set(tubo)) < 2 and len(tubo) in [0, MAX_ITEMS]):
            completado = False
            break
    return completado

welcomeMsg()
clrscr()
nuevoJuego()
displayAsCol()

while True:
    print('-------')
    mover(
        int( input('Select a column to withdraw the top element: ') ),
        int( input('Select a column to put it into the top element: ') )
        )
    clrscr()
    displayAsCol()
    if verificar(): break
input('\x1b[6m¡You win!')
