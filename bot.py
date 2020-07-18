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
    if response is not None:
        json_data = {
            "fulfillmentText": response,
            "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "Usted desea Informacion un/unos laptops dell visita nuestra pagina."
          ]
        },
        "platform": "TELEGRAM"
      },
      {
        "card": {
          "title": "Tecnologic Store Ups",
          "subtitle": "Tenemos las mejores ofertas en Laptops y Celulares",
          "imageUri": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Universidad_Polit%C3%A9cnica_Salesiana_%281%29.jpg",
          "buttons": [
            {
              "text": "Visita el Sitio Web",
              "postback": "https://tecno-store2.herokuapp.com/"
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
    return json_data


if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
