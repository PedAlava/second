import requests  
import os
from flask import Flask, request
import extracmodelo
#import asistente
#BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable


app = Flask(__name__)


@app.route('/me', methods=['POST'])
def main():  
    data = request.json
    print(data)
    parametro = data['queryResult']['parameters']['modelos']
    print(parametro)
    response = extracmodelo.modelo(parametro)
    nombre ,precio ,url,sitio = extracmodelo.mensaTelegram(parametro)
    subtitulo = "Modelo: " + nombre +" Precio: "+ precio
    if sitio == "store":
        mensaj = "Visualiza algun producto de tu interes"
    else:
        mensaj = "Visualiza tu "+ nombre +" y añadelo al carrito si deseas."
    sitio = "https://tecno-store2.herokuapp.com/" +sitio
    #"fulfillmentText": response,
    if response is not None:
        json_data = {
            
            "fulfillmentMessages": [{
                {
          "imageUri": "https://image.shutterstock.com/image-vector/sad-apologizing-emoticon-emoji-holding-260nw-1398672683.jpg",
          "accessibilityText": "sdfd"
        },"platform": "PLATFORM_UNSPECIFIED"
       },
      {
        "text": {
          "text": [
            response
          ]
        },
        "platform": "PLATFORM_UNSPECIFIED"
      }, {
        ],
            "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "informacion detallada: "
          ]
        },
        "platform": "TELEGRAM"
      },
      {
        "card": {
          "title": nombre,
          "subtitle": subtitulo,
          "imageUri": url,
          "buttons": [
            {
              "text": mensaj,
              "postback": sitio
            },
            {
              "text": "Consulta con nuestro Agente",
              "postback": "https://tecno-store2.herokuapp.com/dialog"
            }
          ]
        },
        "platform": "TELEGRAM"
      }
            ]}
    else:
        json_data = {
            "fulfillmentText": response,"buttons":[ { 
                "text": "debe",
                "postback": "dffdsf"
                    }
                ]
        }
    print(json_data)
    return json_data


if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
