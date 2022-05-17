
import os
import os.path
from os import path

where_am_i = os.getcwd()
where_i_go = where_am_i

def eliminate_file():

    choose_file = input('¿Cuál es el archivo a eliminar? (Ingrese nombre sin la extensión para efectos de mayor comodidad. Ejemplo: text\n-- PD: No te preocupes, el CLI solo afecta a los archivos con extensión .txt --\n')

    if choose_file.endswith('.txt'):
        all_route = f'{where_i_go}/{choose_file}'
    else:
        all_route = f'{where_i_go}/{choose_file}.txt'

    print(all_route)
    if (path.isfile(all_route)):
        os.remove(all_route)
        print('Archivo eliminado éxitosamente')
    else:
        print('No existe el archivo, intente otra vez')

def list_files():

    print('1. Listar archivos en el directorio actual')
    print('2. Listar archivos en un directorio especifico')
    print('3. Volver al menú principal')
    choose_list = int(input('Ingresa una opción por favor. '))

    if choose_list == 1:
        print('Estos son los archivos txt disponibles en el directorio actual\n')
        for file in os.listdir(where_i_go):
            if file.endswith('.txt'):
                print (file)
    elif choose_list == 2:
        directory_specific = input('Ingresa la ruta del directorio qué quieres listar. Asegúrate de hacerlo de manera absoluta, ejemplo: \n /home/ele/bootcamp \n')
        print('Estos son los archivos txt disponibles en: ' + (directory_specific) + '\n')
        for file in os.listdir(directory_specific):
            if file.endswith('.txt'):
                print (file)
    elif choose_list == 3:
        main()
    else:
        print('No ha seleccionado una opción adecuada')

def list_prncpl():
    for file in os.listdir():
        if file.endswith('.txt'):
            print (file)

def read_files():

    choose_file = input('¿Cuál es el archivo a leer? (Puedes ingresar el nombre sin la extensión para efectos de mayor comodidad.) Ejemplo: text \n -- PD: No te preocupes, el CLI solo afecta a los archivos con extensión .txt --\n')

    if choose_file.endswith('.txt'):
        all_route = f'{where_i_go}/{choose_file}'
    else:
        all_route = f'{where_i_go}/{choose_file}.txt'

    if (path.isfile(all_route)):
        print('Contenido del archivo seleccionado:')
        with open(all_route, 'r') as read_file:
            print('\n' + read_file.read())
        print('\nFin del contenido del archivo seleccionado')
    else:
        print('No existe el archivo, intente otra vez')

def main():

    global where_i_go

    print('Hola, Bienvenido al CLI')
    print('Acá tienes una lista de los archivos txt disponibles en el directorio actual')
    print('')
    list_prncpl()

    while True:

        print('')
        print('Directorio actual: ' + (where_i_go))
        print('Qué deseas hacer?')
        print('1. Listar los archivos txt')
        print('2. Leer documento.')
        print('3. Eliminar documento')
        print('4. Trabajar en otro directorio')
        print('0. Salir del CLI')

        choose = int(input('Ingresa una opción: '))

        if choose == 1:
            list_files()
        elif choose == 2:
            read_files()
        elif choose == 3:
            eliminate_file()
        elif choose == 4:
            where_i_go = input('Ingresa la ruta del directorio al qué quieres viajar: (Hazlo de manera absoluta, por ejemplo: /home/ele/Codigo Facilito) \n')
        elif choose == 0:
            print('Muchas gracias, vuelve pronto, que estés bien!, feliz vida!!')
            break
        else:
            print('Por favor selecciona una opción correcta')


if __name__ == '__main__':

    main()
