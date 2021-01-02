__doc__ = ''' Utilildades de uso común.
- Limpiar pantalla.
- Colorear pantalla.
- Mensaje de bienvenida.
- Testeo de Colorama.
'''

import os
from colorama import init, deinit, Fore, Back, Style

def clrscr():
   ''' Limpiar pantalla, testeado en Windows & Linux '''
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def pintar(color='', fondo='', texto=''):
    '''
    pintar los elementos
    '''
    colores = {'AZUL':Fore.BLUE}
    fondos = {'AZUL':Back.BLUE}
    if color and fondo:
        print(colores[color] + fondos[fondo] + texto)
    elif color and not fondo:
        print(colores[color] + texto)
    elif not color and fondo:
        print(fondos[fondo] + texto)
    else:
        print(texto)

def paint(fore='', back='', text='', style=''):
    ''' Esto nunca se usó '''
    print(fore+back+text+style)

def welcomeMsg():
    ''' Mensaje de bienvenida y explicación del juego '''
    clrscr()
    msg = ['¡Welcome to \x1b[31m\x1b[40mCLI Ball Sort\x1b[0m,',
    'the game of sorting items!\n',
    '    ◆    ◇    -\n'*3+
    '    ⎼    ⎼    ⎼',
    '    1°   2°   3°\n',
    '\x1b[21mHow to play\x1b[0m',
    'You must move the elements at the top of the columns over other matching elements or over empty columns.',
    'Note that columns have a maximum number of elements.',
    '\x1b[6m    •- - ↴     \x1b[0m',
    '    ◇    .    .',
    '    ◆    ◇    .',
    '    ◆    ◇    .',
    '    ⎼    ⎼    ⎼',
    '    1°   2°   3°',
    'Sort each column with a unique element to win.',
    'That\'s all so let\'s start!\n',
    '\x1b[6mPress ENTER to start.\x1b[0m\n'
    ]
    input('\n'.join(msg))

def coloramatest():
    for i in range(120):
        if i%10:
            text = f'{i}) \x1b[{i}mtext '
            text = text.rjust(10)
            print(text, end='')
        else:
            print(f'{i}) \x1b[{i}mtext '.rjust(10))

init(autoreset=True)
