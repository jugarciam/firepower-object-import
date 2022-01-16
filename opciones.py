import shlex
import subprocess


def selecciona(pregunta):
    respuesta = None
    respuesta = input(pregunta + " (1, 2, 3, 4, 5 ó 6):\t\t").lower().strip()
    print("")
    while not(respuesta == "1" or respuesta == "2" or respuesta == "3" or respuesta == "4" or respuesta == "5" or respuesta == "6"):
        respuesta = input(pregunta + " 1, 2, 3, 4, 5 ó 6:\t\t").lower().strip()
        print("")
    if respuesta[0] == "1":
        print('El archivo que contiene los objetos a importar deberá estar en formato .csv.')
        print('Deberá contener las siguientes columnas: name,type,port,description.')
        print('En la columna type se deberá colocar si los objetos son tcp o udp.')
        print('No es necesario colocar valores en la columna description')
        return "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/protocolportobjects"
    elif respuesta[0] == "2":
        print('El archivo que contiene los objetos a importar deberá estar en formato .csv.')
        print('Deberá contener las siguientes columnas: name,type,port,description.')
        print('En la columna type se deberá colocar la palabra host.')
        print('No es necesario colocar valores en la columna description')
        return "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/hosts"
    elif respuesta[0] == "3":
        print('El archivo que contiene los objetos a importar deberá estar en formato .csv.')
        print('Deberá contener las siguientes columnas: name,type,port,description.')
        print('En la columna type se deberá colocar la palabra range.')
        print('No es necesario colocar valores en la columna description')
        return "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/ranges"
    elif respuesta[0] == "4":
        print('El archivo que contiene los objetos a importar deberá estar en formato .csv.')
        print('Deberá contener las siguientes columnas: name,type,port,description.')
        print('En la columna type se deberá colocar la palabra network.')
        print('No es necesario colocar valores en la columna description')
        return "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"
    elif respuesta[0] == "5":
        print('El archivo que contiene los objetos a importar deberá estar en formato .csv.')
        print('Deberá contener las siguientes columnas: name,type,port,description.')
        print('En la columna type se deberá colocar la palabra url.')
        print('No es necesario colocar valores en la columna description')
        return "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/urls"
    else:
        respuesta = "6"
        