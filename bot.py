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
            "fulfillmentText": response,"buttons":[ { 
                "text": "Sitio Web",
                "postback": "https://tecno-store2.herokuapp.com/"
                    }
                ]
        }
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
