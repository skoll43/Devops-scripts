
import requests
import netmiko
import json
from netmiko import ConnectHandler
cisco1 = { "ip": "192.168.56.101",
"device_type": "cisco_ios",
"username": "cisco",
"password": "cisco123!",
}
def operacion(command):
    # Show command that we execute.
    with ConnectHandler(**cisco1) as net_connect:
        output = net_connect.send_command(command)
    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()

menu = ("1: interfaces\n2: show run\n3: show version\ns: Termina el script")

while True:
    print(menu)
    opcion = input("ingrese su opcion:")
    if opcion == "1":
        operacion(command = "show ip int br")
        break
    if opcion == "2":
        operacion(command = "show run")
        break
    if opcion == "3":
        operacion(command = "show version")
        break
    if opcion == "s":
        break
    else:
        print("debe ingresar una opcion valida")


'''
● Obtener información de las IP y estado de las interfaces usando comando show en el script.
● Obtener el running-config usando un comando show en el script.
● Obtener el show version usando un comando en el script.
'''