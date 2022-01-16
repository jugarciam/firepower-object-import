import csv
import requests
import json

from requests import models

def importar(fmc_url,pregunta,headers):
    if pregunta != None and pregunta == "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/protocolportobjects":
        open_csv=input('\n\nColoca la ubicación del archivo incluyendo nombre y extensión, si el archivo se encuentra\nen la misma ubicación que el script sólo coloca\nel nombre del archivo y su extensión:\t\t')
        csvfile = open(open_csv,mode='r')
        objects = csv.DictReader(csvfile)
        #print('\n\n'+fmc_url+pregunta)
        url = fmc_url+pregunta
        if (url[-1] == '/'):
            url = url[:-1]
        for object in objects:
            post_data = {
                "name": object["name"],
                "protocol": object["type"],
                "port": object["data"],
                "description": object["description"],
            }
            print('\n*************************************')
            print('Creating object: ' + object["name"])
            try:
                r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
                status_code = r.status_code
                resp = r.text
                log = open('post_objects.log', 'a')
                print(" Código de estatus: "+str(status_code))
                json_resp = json.loads(resp)
                log.write('\n---------------------------------------------------------------------\n')
                log.write(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
                if status_code == 201 or status_code == 202:
                    print (" Éxito ")
                elif status_code == 400:
                    print (" Mensaje: ")  + resp + ('\n')
                else:
                    r.raise_for_status()
                    print (" Mensaje: ")  + resp + ('\n')
            except requests.exceptions.HTTPError as err:
                print (" Error en la conexión --> "+str(err))
            finally:
                if r: r.close()
    elif pregunta != None and pregunta == "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/urls":
        open_csv=input('\n\nColoca la ubicación del archivo incluyendo nombre y extensión, si el archivo se encuentra\nen la misma ubicación que el script sólo coloca\nel nombre del archivo y su extensión:\t\t')
        csvfile = open(open_csv,mode='r')
        objects = csv.DictReader(csvfile)
        #print('\n\n'+fmc_url+pregunta)
        url = fmc_url+pregunta
        if (url[-1] == '/'):
            url = url[:-1]
        for object in objects:
            post_data = {
                "name": object["name"],
                "type": object["type"],
                "url": object["data"],
                "description": object["description"],
            }
            print('\n*************************************')
            print('Creating object: ' + object["name"])
            try:
                r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
                status_code = r.status_code
                resp = r.text
                log = open('post_objects.log', 'a')
                print(" Código de estatus: "+str(status_code))
                json_resp = json.loads(resp)
                log.write('\n---------------------------------------------------------------------\n')
                log.write(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
                if status_code == 201 or status_code == 202:
                    print (" Éxito ")
                elif status_code == 400:
                    print (" Mensaje: ")  + resp + ('\n')
                else:
                    r.raise_for_status()
                    print (" Mensaje: ")  + resp + ('\n')
            except requests.exceptions.HTTPError as err:
                print (" Error en la conexión --> "+str(err))
            finally:
                if r: r.close()
    elif pregunta != None:
        open_csv=input('\n\nColoca la ubicación del archivo incluyendo nombre y extensión, si el archivo se encuentra\nen la misma ubicación que el script sólo coloca\nel nombre del archivo y su extensión:\t\t')
        csvfile = open(open_csv,mode='r')
        objects = csv.DictReader(csvfile)
        #print('\n\n'+fmc_url+pregunta)
        url = fmc_url+pregunta
        if (url[-1] == '/'):
            url = url[:-1]
        for object in objects:
            post_data = {
                "name": object["name"],
                "type": object["type"],
                "value": object["data"],
                "description": object["description"],
            }
            print('\n*************************************')
            print('Importando objeto: ' + object["name"])
            try:
                r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
                status_code = r.status_code
                resp = r.text
                log = open('post_objects.log', 'a')
                print(" Código de estatus: "+str(status_code))
                json_resp = json.loads(resp)
                log.write('\n---------------------------------------------------------------------\n')
                log.write(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
                if status_code == 201 or status_code == 202:
                    print (" Éxito ")
                elif status_code == 400:
                    print (" Mensaje: ")  + resp + ('\n')
                else:
                    r.raise_for_status()
                    print (" Mensaje: ")  + resp + ('\n')
            except requests.exceptions.HTTPError as err:
                print (" Error en la conexión --> "+str(err))
            finally:
                if r: r.close()
    else:
        quit()