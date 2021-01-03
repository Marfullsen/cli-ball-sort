#!/usr/bin/env python
#-*- coding: utf-8 -*-

s = {
    0:'ABCDEFGHI',
    1:'♈♉♊♋♌♍♎♏♐♑♒♓',
    2:'♔♕♖♗♘♙♚♛♜♝♞♟',
    3:'♠♡♢♣♤♥♦♧♨♩♪♫♬',
    4:'▐░▓▖▗▘▙▚▛▜▝▞▟',
    5:'◆◇◈◉◌◍◎●◐◑◒◓◔◕◖◗◘',
    6:'◧◨◩◪◫◬◭◰◱◲◳◴◵◶◷',
    7:'⚤⚪⚫⚱⚲⚳⚴⚵⚶⚷⚸⚹',

}
def test():
    for i, item in s.items():
        print(i, '-'.join(item))
    x = input(f'select a set (1-{len(s)}): ')
    x = int(x)
    print('\n')
    print(' '.join(s[x]))
    input('\nEnter to try again\n')
    test()

if __name__ == "__main__":
    test()
