# Introducción MicroPython WebServer

Es un mini web server con soporte para peticiones GET que "escucha" en 
el puerto 80.
Este servidor sirve los archivos de la carpeta web al navegador. La carpeta 
web contiene los archivos de [webrpl](https://github.com/micropython/webrepl) que generan una terminal en el navegador.
Los archivos boot.py y main.py habilitan el uso del deamon webrepl en el
ESP8266, se conecta con la red wifi preestablecida y luego lanzar el
servidor web.

