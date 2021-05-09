import os
import json
from re import match
from random import choice

from scraping import MonedasV, Vacunas
from NLP import org

#codigos, modelo = processing()

#with open(os.path.join(os.getcwd(), 'conversaciones.json')) as file:
    #conversaciones = json.load(file)

def messageHandler(mensaje):
    
    patron = '(.*)' + os.environ["BOT_NICK"] + '(.*)'
    matcher = match(patron, mensaje)

    if matcher:
        #mensaje = mensaje.replace(os.environ["BOT_NICK"], '').strip()
        
        return 'No tengo suficiente memoria RAM, a ver si @cryptofono hace algo al respecto' #mencion(lemmatizer(mensaje), codigos, modelo)
        
    elif mensaje == '/start':
        quehaceres = 'Comandos disponibles:\n\n/btc: Valor del bitcoin actual. También disponible con eth y dot\n/vacunas: Estado de la vacunación COVID-19 en España'

        return quehaceres

    elif mensaje == '/btc':
        scrapper = MonedasV('bitcoin')
        
        return scrapper.extrarPrecio()

    elif mensaje == '/eth':
        scrapper = MonedasV('ethereum')
        
        return scrapper.extrarPrecio()

    elif mensaje == '/dot':
        scrapper = MonedasV('polkadot-new')
        
        return scrapper.extrarPrecio()

    elif mensaje == '/vacunas':
        return Vacunas.estadoVacunas()

    else:
        return org(mensaje)
    
        '''
        mensaje = mensaje.lower()
        palabras = mensaje.split(' ')
        
        faltas_ortograficas = ["aki", "alante", "ami", "asin", "aver", "llendo", "haiga", "hoygan", "na", "pa", "pal"]
        
        for palabra in palabras:
            if palabra in faltas_ortograficas:
                return 'Mis hogos'

            else:
                pass
        '''
