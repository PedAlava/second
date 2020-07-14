import json
from chatterbot import ChatBot
from chatterbot.trainers import  ListTrainer
import requests  
import os
from flask import Flask, request
from chatterbot.response_selection import get_random_response #Para el adaptador lógico de respuesta aleatoria

import aprendizajes

chatbot = ChatBot("Skynet5_bot")


chatbot = ChatBot(
    'Terminal',sqlite3storage_adapter='chatterbot.storage.SQLStorageAdapter',
   
      logic_adapters=[
    'chatterbot.logic.MathematicalEvaluation', #¿Cuánto es 1+(-*/)2?, y el bot responderá al cálculo
    'chatterbot.logic.BestMatch', #Escoge la mejor respuesta
    ],
    preprocessors=[
    'chatterbot.preprocessors.clean_whitespace' #Elimina espacios en blanco
    ],
    response_selection_method=get_random_response #Cuando se encuentren varias respuestas
    #una sentencia de entrada, el bot escogerá aleatoriamente una de estas respuestas para
    #responde, esto hace que no sea monótono y las conversaciones sean más dinámicas
)


trainer = ListTrainer(chatbot) #La variable trainer será el puntero para referenciar a la función "ListTrainer(chatbot)"

trainer.train("chatterbot.corpus.spanish") #Con esta sentencia le enseñamos al Bot un grupo de 
#conversaciones en español prediseñadas que nos brinda ChatterBotCorpus


trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Adios',
'Adios'
])

trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Adios',
'Hasta luego'
])

trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Hola',
'Holis'
])
trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Buenos dias',
'Buenos dias como estas'
])


trainer.train("chatterbot.corpus.spanish") #Comentar este fragmento después de la primera ejecución exitosa del programa
TOKEN = "1376868915:AAGz5em6FJPd4XHNV5RbdmIYElG1e6ftgJs"
URL = "https://api.telegram.org/bot" + TOKEN + "/"


trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Quien es tu creador',
'Mi creador es Pedro Alexander Alava Gil'
])



def aprenderTodo(lista):
  trainer.train([lista[0],lista[1]])

def enviar_mensaje(idchat, texto):
  requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))


def respons(id_chat,message):
  aprendi=[]
  lista = aprendizajes.obtener()
  message_cloud = lista[0]
  id_cloud = lista[1]
  if message_cloud == "no":
    message = message.lower()
    response = chatbot.get_response(message)
    c = float(response.confidence)
    val = 0.5
    if c > val:
      texto_respuesta = str(response)
      c = 0
      n = int(id_cloud)
      n += 1
      aprendizajes.guardar(n,texto_respuesta,"bot","respuesta")
    else:
      texto_respuesta ="nose la respuesta enseñame por favor"
      if response == "nose la respuesta enseñame por favor":
        n = int(id_cloud)
        n += 1
        aprendizajes.guardar(n,texto_respuesta,"bot","respuesta")
        
        c = 0
  elif message_cloud == "aprendido":
    texto_respuesta ="Cambiemos de tema por favor"
  else:
    
    aprendi.append(message_cloud)
    aprendi.append(message)
    aprenderTodo(aprendi)
    n = int(id_cloud)
    n += 1
    aprendizajes.guardar(n,"Gracias por enseñarme","bot","respuesta")
    texto_respuesta = "Gracias por enseñarme"
  
  return texto_respuesta



