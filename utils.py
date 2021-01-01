import os
from colorama import init, deinit, Fore, Back, Style

def clrscr():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def pintar(color='', fondo='', texto=''):
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
    print(fore+back+text+style)

def welcomeMsg():
    msg = ['¡Bienvenido a CLI Ball Sort,',
    'el juego de ordenar elementos!\n',
    '\x1b[6mInstrucciones',
    '\x1b[1mEnter para iniciar']
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
