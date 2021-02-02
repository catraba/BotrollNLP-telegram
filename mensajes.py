import os
import json
from re import match
from random import choice

from scraping import MonedasV, PelisTMDB
from NLP import processing, mencion

codigos, modelo = processing()


def messageHandler(mensaje):
    
    patron = '(.*)' + os.environ["BOT_NICK"] + '(.*)'
    matcher = match(patron, mensaje)

    if matcher:
        mensaje = mensaje.replace(os.environ["BOT_NICK"], '').strip()
        
        return mencion(mensaje, codigos, modelo)
        
    elif mensaje == '/start' or '/help':
        quehaceres = 'Comandos disponibles:\n\n/btc: Valor del bitcoin actual\n/peli: Te recomiento una película diariamente'

        return quehaceres

    elif mensaje == '/btc':
        scrapper = MonedasV('bitcoin')
        
        return scrapper.extrarPrecio()

    elif mensaje == '/peli':
        eleccion = choice(PelisTMDB.peliDiaria(os.environ["IMDB_TOKEN"]))
        
        return 'Hoy recomendamos: ' + eleccion

    else:
        mensaje = mensaje.lower()
        palabras = mensaje.split(' ')
        
        faltas_ortograficas = ["aki", "alante", "ami", "asin", "aver", "llendo", "haiga", "hoygan", "na", "pa", "pal"]
        
        for palabra in palabras:
            if palabra in faltas_ortograficas:
                return 'Escribe bien que te meto eh'

            else:
                pass
