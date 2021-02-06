import os
import json
from re import match
from random import choice

from scraping import MonedasV, PelisTMDB, Vacunas
#from NLP import processing, mencion

#codigos, modelo = processing()

with open(os.path.join(os.getcwd(), 'conversaciones.json')) as file:
    conversaciones = json.load(file)

def messageHandler(mensaje):
    
    patron = '(.*)' + os.environ["BOT_NICK"] + '(.*)'
    matcher = match(patron, mensaje)

    if matcher:
        #mensaje = mensaje.replace(os.environ["BOT_NICK"], '').strip()
        
        #return mencion(mensaje, codigos, modelo)
        return 'No hablo tu idioma melón'
        
    elif mensaje == '/start':
        quehaceres = 'Comandos disponibles:\n\n/btc: Valor del bitcoin actual. También disponible con eth, xrp y dot\n/peli: Te recomiento una película diariamente\n/vacunas: Estado de la vacunación frente al COVID-19 en España'

        return quehaceres

    elif mensaje == '/btc':
        scrapper = MonedasV('bitcoin')
        
        return scrapper.extrarPrecio()
    
    elif mensaje == '/eth':
        scrapper = MonedasV('ethereum')
        
        return scrapper.extraerPrecio()
    
    elif mensaje == '/xrp':
        scrapper = MonedasV('xrp')
        
        return scrapper.extraerPrecio()
    
    elif mensaje == '/dot':
        scrapper = MonedasV('polkadot-new')
        
        return scrapper.extraerPrecio()

    elif mensaje == '/peli':
        eleccion = choice(PelisTMDB.peliDiaria(os.environ["IMDB_TOKEN"]))
        
        return 'Hoy recomendamos: ' + eleccion

    elif mensaje == '/vacunas':
        return Vacunas.estadoVacunas()

    else:
        mensaje = mensaje.lower()
        palabras = mensaje.split(' ')
        
        faltas_ortograficas = ["aki", "alante", "ami", "asin", "aver", "llendo", "haiga", "hoygan", "na", "pa", "pal"]
        
        for palabra in palabras:
            if palabra in faltas_ortograficas:
                return 'Escribe bien que te meto eh'

            else:
                pass
