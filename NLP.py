from constantes import conversaciones

from spacy import load
nlp = load('es_core_news_md-3.0.0/es_core_news_md/es_core_news_md-3.0.0')

from numpy import array, asarray, reshape, argmax
from sklearn.linear_model import LogisticRegression

from random import choice


def lemmatizer(mensaje, frase=''):

    with nlp.disable_pipes():
        for palabra in nlp(mensaje):
            frase = frase + palabra.lemma_ + ' '

        frase = frase[:-1]

    return frase
    

def processing():

    etiquetas = []
    codigos = {}
    docs = []

    for i, intencion in enumerate(conversaciones['intenciones']):
        codigos[i] = intencion['etiqueta']

        with nlp.disable_pipes():
            for patron in intencion['patrones']:
                frase = ''
                for p in nlp(patron):
                    frase = frase + p.lemma_ + ' '

                frase = frase[:-1]
                docs.append(frase)

                etiquetas.append(i)


            vectores = array([nlp(d).vector for d in docs])
            labels = asarray(etiquetas)


    LR = LogisticRegression() #solver="liblinear", max_iter=10000
    modelo = LR.fit(vectores, labels)

    return codigos, modelo


def mencion(mensaje, codigos, modelo):

    patron = nlp(lemmatizer(mensaje)).vector
    patron = patron.reshape(1, -1)

    y_prob = modelo.predict_proba(patron)
    
    maximo = y_prob.max().astype(float)
    indice = argmax(y_prob)

    respuestas = []

    if maximo > 0.85:
        opcion = codigos.get(indice)

        for intencion in conversaciones['intenciones']:
            for respuesta in intencion['respuestas']:
                respuestas.append(respuesta)

        return choice(respuestas)




