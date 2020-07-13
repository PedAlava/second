import json
from chatterbot import ChatBot
from chatterbot.trainers import  ListTrainer
import requests  
import os
from flask import Flask, request
from chatterbot.response_selection import get_random_response #Para el adaptador lógico de respuesta aleatoria

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
'Hola como estas en que te puedo ayudar'
])
trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Buenos dias',
'Buenos dias como estas en que te puedo ayudar'
])

trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'informacion',
'Sobre que articulo necesita informacion'
])


trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'video',
'No tenemos tarjetas de video por el momento'
])
trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'tarjeta de video',
'No tenemos tarjetas de video por el momento'
])


trainer.train("chatterbot.corpus.spanish") #Comentar este fragmento después de la primera ejecución exitosa del programa
#TOKEN = "1350904905:AAHWuHKc09pz2N_iq7R8Z6s3T0S2x_obM_M"
#URL = "https://api.telegram.org/bot" + TOKEN + "/"


trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Quien es tu creador',
'Mi creador es Pedro Alexander Alava Gil'
])

def aprenderTodo(lista):
  trainer.train([lista[0],lista[1]])

trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'necesito informacion',
'Sobre que articulo necesita informacion tenemos por el momento Laptops y Celulare'
])
trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'Puedes darme informacion por favor',
'Sobre que articulo necesitas informacion tenemos por el momento Laptops y celulares'
])
trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'necesito una tarjeta de video',
'Por el momento no tenemos tarjetas de video solo contamos con laptops, celulares y productos novedosos que te pueden interesar si quiere te puedo redirigir a la pagina de nuestros <a href="{{ url_for("store") }}"> productos </a> '
])

trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'necesito un dashboard',
'Por el momento no tenemos dashboards solo contamos con laptops, celulares y productos novedosos que te pueden interesar si quiere te puedo redirigir a la pagina de nuestros <a href="{{ url_for("store") }}"> productos </a> '
])

trainer.train([ #Comentar este fragmento después de la primera ejecución exitosa del programa
'quiero informacion de una tarjeta de video',
'Por el momento no tenemos tarjetas de video solo contamos con laptops, celulares y productos novedosos que te pueden interesar si quiere te puedo redirigir a la pagina de nuestros <a href="{{ url_for("store") }}"> productos </a> '
])
l = ['una laptop','tenemos laptops de marcas Asus y Dell por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("laps") }}"> laptops </a>']
l1 = ['laptop','tenemos laptops de marcas Asus y Dell por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("laps") }}"> laptops </a>']
l2 = ['laptops','tenemos laptops de marcas Asus y Dell por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("laps") }}"> laptops </a>']
l3 = ['celulares','tenemos celulares de marcas Xiamoi y Huawei por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("cells") }}"> Celulares </a>']
l4 = ['celular','tenemos celulares de marcas Xiamoi y Huawei por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("cells") }}"> Celulares </a>']
l5 = ['un celular','tenemos celulares de marcas Xiamoi y Huawei por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("cells") }}"> Celulares </a>']
l6 = ['productos novedosos','tenemos algunos productos novedosos como reloj con kits medicos, cartera digital, etc por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("cells") }}"> Celulares </a>']
l7 = ['quiero informacion de una laptop','tenemos laptops de marcas Asus y Dell por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("laps") }}"> laptops </a>']
l8 = ['tienen laptops asus','Si tenemos laptops de marca Asus por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("laps") }}"> laptops </a>']
l9 = ['tienen laptops dell','Si tenemos laptops de marca Dell por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("laps") }}"> laptops </a>']
l10 = ['tienen celulares xiamoi','Si tenemos celulares de marca Xiamoi por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("cells") }}"> Celulares </a>']
l11 = ['tienen celulares huawei','Si tenemos celulares de marca Huawei por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("cells") }}"> Celulares </a>']
l12 = ['quiero informacion de un celular','tenemos celulares de marcas Xiamoi y Huawei por el momento si quieres te puedo redirigir a la pagina de <a href="{{ url_for("cells") }}"> Celulares </a>']
l13 = ['que ofertas tienen','tenemos algunos ofertas en laptops y celulares si quieres te puedo redirigir a la pagina de nuestros <a href="{{ url_for("store") }}">productos </a> ']
l14 = ['pago','aceptamos efectivo o tarjeta de credito']
l15 = ['que tipo de pago aceptan','aceptamos efectivo o tarjeta de credito']
l16 = ['metodo de pago','aceptamos efectivo o tarjeta de credito']
l17 = ['que metodo de pago','aceptamos efectivo o tarjeta de credito']

aprenderTodo(l)
aprenderTodo(l1)
aprenderTodo(l2)
aprenderTodo(l3)
aprenderTodo(l4)
aprenderTodo(l5)
aprenderTodo(l6)
aprenderTodo(l7)
aprenderTodo(l8)
aprenderTodo(l9)
aprenderTodo(l10)
aprenderTodo(l11)
aprenderTodo(l12)
aprenderTodo(l13)
aprenderTodo(l14)
aprenderTodo(l15)
aprenderTodo(l16)
aprenderTodo(l17)
#def enviar_mensaje(idchat, texto):
    #Llamar el metodo sendMessage del bot, passando el texto y la id del chat
    #requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))

def respon(message):
  message = message.lower()
  respuesta = chatbot.get_response(message)
  c = float(respuesta.confidence)
  val = 0.5
  if c > val:
    texto_respuesta = str(respuesta)
    c = 0
  else:
    texto_respuesta ="No se la respuesta del mensaje"
    c = 0
  return texto_respuesta


