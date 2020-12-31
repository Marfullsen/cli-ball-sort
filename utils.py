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

init(autoreset=True)
