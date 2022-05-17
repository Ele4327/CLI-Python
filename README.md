![](https://github.com/Ele4327/CLI-Python/blob/main/img/CLI%20Project.png)

👋 Hello Devs
# CLI Python

Hello and Welcome to my CLI project.
This is a project developed by me, for the bootcamp "Introduccón a la Programación" from CodigoFacilito.

## Features

- Developed in  Python.
- Works and affects only to .txt files.
- Dont matter if u include the extension or not, if the file exists, the CLI will work with it.
- CLI app can travel between different folders and directories and affect its .txt files.

## Functions:

- List files in default folder, or another specific folder.
- Read files
- Remove files


## Compilation and Execution
After cloned or downloaded the repository, go to that folder in your console.
Need have installed Python3.

To run the program it is as simple as put in console:
> python3 main.py

### Main Function
> def main():

```
Hola, Bienvenido al CLI
Acá tienes una lista de los archivos txt disponibles en el directorio actual

hola.txt
Test.txt

Directorio actual: /mnt/d/Desktop/Code/Me/Codigo Facilito/BootCamp Introducción a la Programación
Qué deseas hacer?
1. Listar los archivos txt
2. Leer documento.
3. Eliminar documento
4. Trabajar en otro directorio
0. Salir del CLI
```

### Subfunctions

eliminate_file():

> Remove a specific file in the actual directory

def list_files():

> List all txt files in the specified directory or in the actual directory

def list_prncpl():

> List automatically files when opens CLI

def read_files():

> Show content of the specified file
