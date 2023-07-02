'''
Se solicita crear un script en Python que realice lo siguiente:
● Mida la distancia entre una ciudad de Chile y una ciudad de algún otro país en Latinoamérica en kilómetros (kms).
● Solicitar “Ciudad de Origen” y “Ciudad de Destino”, en español.
 Mostar la duración del viaje en horas, minutos y segundos.
 Mostrar el combustible requerido para el viaje en litros (lts)
 Los valores deben tener solo 1 decimal.
Agregar como salida la letra S.
 Que imprima la narrative del viaje.
El script debe ser subido al repositorio de GitHub con un commit a elección.
'''
import urllib.parse
import requests

import os
#while True:
#    os.system("clear")


while True:
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    os.system("clear")
    print("Ingrese la letra S para Salir")
    orig = input("ingrese ciudad de origen:\n ")
    os.system("clear")
    print("Ingrese la letra S para Salir")
    dest = input("ingrese ciudad de destino:\n")
    os.system("clear")
    key = "tKJdyWn9sR1b4HmByXAiej0rI5ksKmRr"
    locale = "es_ES"
    if orig == "S" or dest == "S":
            break
    
    url = main_api + urllib.parse.urlencode({"key" :key,"locale" :locale, "from" :orig, "to" :dest})

    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    #print(url,"es la url")

    if json_status == 0:
#        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("======================================================================")
        print("Informacion de viaje desde " + (orig) + " hasta " + (dest))
        print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Distancia en Km:      " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        print("======================================================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
            print("======================================================================\n")
        print("gracias por usar el programa")
        break
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Uno de los valores ingresados no son validos")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
