import os
import os.path
from os import path

where_am_i = os.getcwd()
where_i_go = where_am_i



""" def current_place():
    return os.getcwd() """

""" def start_file():
        if (path.isfile(choose_file)):
            print('Perfecto. ¿Qué deseas hacer con el archivo?, selecciona una opción.')
        else:
            print('El archivo no existe, ó no es un archivo de texto válido') """

def eliminate_file():

    choose_file = input('Cuál es el archivo a eliminar (Ingrese nombre sin la extensión para efectos de mayor comodidad. Ejemplo: text - \nEn serio, sin extensión, de eso depende el funcionamiento XD\n')

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

    choose_file = input('Cuál es el archivo a leer (Ingrese nombre sin la extensión para efectos de mayor comodidad.) Ejemplo: text -\n -- En serio, sin extensión, de eso depende el funcionamiento XD --\n')

    if choose_file.endswith('.txt'):
        all_route = f'{where_i_go}/{choose_file}'
    else:
        all_route = f'{where_i_go}/{choose_file}.txt'

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

        choose = int(input('Ingresa una opción '))

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

    # Vamos a listar los documentos con extensión txt.
    # Esto no funciona si no se le indica en dónde debe listar los archivos??.
    # Si, sí que funciona, era que no tenías archivos txt. Por ende, funciona en el folder qué contiene el main

    # -------for file in os.listdir():
        # ---------if file.endswith('.txt'):
            # ----------- print (file)
    # Mero rato viendo porque la aplicación no funciona... y pues claro, le estás diciendo que busque archivos con extensión txt, y vas y no tienes archivos... /_.
    #Ah bueno, encuentra los txt, más no los otros archivos, 2x1

    # Ahora a leer el archivo.
    #Open() pide especificación de qué archivo abrir, y pues, funciona, si ya listé ya sé que archivo abrir:

    ## f = open('hola.txt', 'r')
    ## print (f.read())

    #Ya me abre el archivo, pero tengo qué indicar el nombre del archivo en el main.py, eso no me sirve, so, asignemos un valor en memoria
    # al nombre del archivo.

    ## choose_file = input('¿Qué archivo desea leer?')

    # Y ahora abrirlo solo con indicar qué archivo es:
    ## if (path.isfile(choose_file)):
        ## with open(choose_file, 'r') as read_file:
            ## print(read_file.read())
    ## else:
        ## print('No existe el archivo, intente otra vez')

    # Y ahora a eliminar el archivo. Puedo aprovechar qué ya tengo la capacidad de elegir el archivo, de qué puedo indicar a cual quiero 
    # acceder.

    # ----------- os.remove('test.txt')

    #FUNCIONAAAAA!!!!... pues claro qué funciona, bueno, vamos a hacer el ensayo de nuevo.

    # def eliminate_file:
    #    os.remove(choose_file)
    # Pere, claro, es una función, va por fuera, no, los paréntesis, fuck.

    # def eliminate_file():
    #    os.remove(choose_file) """

    # No, si, las funciones van por fuera, se llama solo la función a la hora de ejecutarla.

    # ------ eliminate_file()

    # Claro, toy eliminando dos veces, por eso no encuentra el archivo, ya fue eliminado.

    # Bien, ya funca.
    # El problema es... no me gusta como se ve.

    # Acá usé el archivo que quise leer, lo qué me lleva a pensar: Es mejor primero seleccionar el archivo y luego qué hacer con él.
    # Ó primero decidir qué hacer, y luego el archivo?

    # Es qué, a ver, yo sé que quiero hacer con un archivo que voy a buscar en mí PC, lo que me induce a pensar que es que quiero hacer con él
    # PERO, de manera ímplicita, si lo piensas bien, lo primero qué haces es ir a buscar el archivo, para poder hacer algo.

    # Y si, primero digo qué quiero hacer, luego tengo qué escoger el archivo. Entonces tendría que recibir el archivo en cada 
    # cosa que vaya a hacer, preguntar por cada acción, aunque... bueno, si eso está dentro de la función, no hay problema, 
    # solo es repetir la pregunta y el choose_file. Pero no me gusta.

    # Se me ocurre qué de entrada liste, luego pregunte qué archivo quiere afectar, y luego que escoja qué hacer.
    # Es, ó entra, pregunta qué hacer, y luego selecciona el archivo.
    # Ó, entra, lista, que archivo selecciona, y luego la acción.
    # En ambos son dos pasos. Pero es qué en la primera... ah bueno, da igual, lo importante es qué liste de entrada.
    # Seguiré el concepto como lo hace un PC actual, cojo archivo, elimino.

    """     print('Hola, Bienvenido al CLI')
    print('Acá tienes una lista de los archivos txt disponibles en el directorio actual')
    print('')
    list_files()
    print('')
    print('Qué deses hacer?')

    print('1. Listar los archivos txt en un directorio específico.')
    print('2. Leer documento.')
    print('3. Eliminar documento')
    print('0. Salir del CLI')

    choose = int(input('Ingresa una opción '))

    if choose == 1:
        list_files()
    elif choose == 2:
        read_files()
    elif choose == 3:
        eliminate_file()
    else:
        print('Por favor selecciona una opción correcta') """

    # Bueno, pues bitácora del capitán, no podíamos tener el choose file dentro del start_file()
    # Al parecer llamar a la función como lo hice dentro de las funciones del menú, me tira esto:

    ## Traceback (most recent call last):
    ##    File "/mnt/c/Users/L/Desktop/Code/Me/Codigo Facilito/BootCamp Introducción a la Programación/main.py", line 122, in <module>
    ##    eliminate_file()
    ##    File "/mnt/c/Users/L/Desktop/Code/Me/Codigo Facilito/BootCamp Introducción a la Programación/main.py", line 18, in eliminate_file
    ##    os.remove(start_file)
    ## TypeError: remove: path should be string, bytes or os.PathLike, not function

    # Igual si lo pensamos bien, el choosefile debe sobrescribirse cada que se quiera usar un archivo distinto.

    # Ahora... como hacemos qué el programa se cierre cuando se le indique...
    # Pues, que esté siempre en un ciclo, y cuando se le indique, rompa.


    """     while True:
        choose1 = int(input('Ingrese una opción'))
        if int(choose1) == 1:
            print('Hola, estoy siendo un programa cíclico éxitosamente')
        elif int(choose1 == 2):
            print('Muchas gracias, vuelve pronto, que estés bien!')
            break
        else:
            print('Selecciona la opción correcta por favor.') """

    # Perfecto.
    # Ahora a implementarlo:

    """     print('Hola, Bienvenido al CLI')
    print('Acá tienes una lista de los archivos txt disponibles en el directorio actual')
    print('')
    list_files()

    while True:

        print('')
        print('Qué deseas hacer?')
        print('1. Listar los archivos txt en un directorio específico.')
        print('2. Leer documento.')
        print('3. Eliminar documento')
        print('0. Salir del CLI')

        choose = int(input('Ingresa una opción '))

        if choose == 1:
            list_files()
        elif choose == 2:
            read_files()
        elif choose == 3:
            eliminate_file()
        elif choose == 0:
            print('Muchas gracias, vuelve pronto, que estés bien!')
            break
        else:
            print('Por favor selecciona una opción correcta') """

    main()

    # Error localbound porque la variable no ha sido declarada antes de usarla, se arregló metiendo la variable al main.

    # Sé que parece redundante que el cli pueda viajar a otro directorio, y en ése otro directorio pregunte si quiere listar 
    # los archivos de otro otro directorio, pero es que quería dejarle ésa facultad en todas las situaciones, como lo indica los
    # requerimientos del proyecto.


# Nota, si las funciones globales están luego del if, como carajo lo va a ejecutar en el if!?, primero le pasas las herramientas, para que luego las pueda usar.
# Paso 1: Crear las funciones: Listar, leer, eliminar.
# Empecé por hacer el menú y me perdí, entonces a lo funcional.
# Paso 2: Ya las tengo por separado, todo en el mismo programa, ahora, irónicamente, no las hice funciones!. Paso 2: Separar las funciones 
# y organizarlas.
# Paso 3: Listar de entrada y luego preguntar qué se necesita hacer.
# Paso 4: Recibir la opción adecuada e implementar las funciones.
# Paso 5: Una vez todo queda funcionando bien... hacer qué el programa cierre cuando el usuario lo indique
# Paso 6: Colocar todo en una sola función main.
# Paso 7: Qué todo tenga simetría y cohesión en sí mismo, si entra a un menú que pueda volver al menú principal, escoger opciones, ó 
# en su defecto que el programa retorne a un mismo punto.
# Paso 8: Poder aceptar un directorio distinto al que se está para poder listar.
# Paso 9: Entró la avaricia y ahora quiero que liste, elimine y lea no solo desde el directorio actual.
# Paso 10: Que no sea necesario poner la extensión txt para leer, ó eliminar el archivo.


#Nota PD: Las líneas de Python se explican casi que ímplicitamente, es la lógica con lo que lidio.