import warnings
import getpass
import requests
import json
import sys
from siono import si_o_no
from opcionador import selecciona
from importador import importar


r= None
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
headers = {'Content-Type': 'application/json'}
auth_url = None
fmc_url = None
a=None

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

print('***********************************************************')
print('El uso del dispositivo es exclusivo del personal autorizado')
print('Se iniciarán acciones legales en caso de uso no autorizado*')
print('***********************************************************')

print('\n\nEste script importará objetos a la FMC')
if si_o_no('\n¿Desea continuar)?'):
    ()
else:
    quit()

FMC_IP = input('\nProporciona la dirección IP de la FMC: ')

while not FMC_IP:
    FMC_IP = input('\nPor favor proporciona la dirección IP de la FMC: ')

print('\nA continuación proporciona las credenciales de la FMC')

Usuario = input("Usuario: ")
while not Usuario:
    Usuario = input('\nPor favor proporciona un usuario: ')

password = getpass.getpass("\nContraseña: ")
while not password:
    password = input('\nPor favor proporciona la contraseña: ')

auth_url ='https://' + FMC_IP + api_auth_path
fmc_url = 'https://' + FMC_IP

try:
    print('\n\nConectando a la FMC')
    requests.packages.urllib3.disable_warnings()
    r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(Usuario,password), verify=False)
    auth_headers = r.headers
    auth_token = auth_headers.get('X-auth-access-token', default=None)
    #print(auth_token)
    if auth_token == None:
        print("\nToken de autenticación no encontrado. Finalizando...")
        sys.exit()
except Exception as err:
    print ("\nError al generar el token de autenticación --> "+str(err))
    sys.exit()
headers['\nX-auth-access-token'] = auth_token
print('\n\nConectado. Toquen de autenticación obtenido exitosamente:\t\t' + auth_token)

print('\n\n\nA continuación se presenta una lista de opciones\n\n')
print('1.-Importar objetos de servicio (Puertos TCP/UDP)')
print('2.-Importar objetos tipo Host')
print('3.-Importar rangos de IP')
print('4.-Importar objetos de red')
print('5.-Importar objetos de tipo URL')
print('6.-Salir')

importar(fmc_url,selecciona('\nPor favor elija una opción para comenzar'),headers)

#a = (input(selecciona('\nPor favor elija una opción para comenzar')),shell=False)

#if selecciona('\nPor favor elija una opción para comenzar') != None:
#    print(selecciona)

#else :
#    quit()