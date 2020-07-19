import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('dialogproyect-firebase-adminsdk-c4bf2-b63b415609.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://dialogproyect.firebaseio.com/'
}) 
def modelo(mode):
    varia = 'chat/' + mode

    try:
        
        ref = db.reference(varia)
        lista = ref.get()
        variable = """Si tenemos el 
                    Modelo:  {} 
                    Precio:  {} 
                """.format(lista['nombre'],lista['precio'])
        #variable = "Modelo: "+ lista['nombre']+"\n "+ "Precio: " + lista['precio']
    except:
        variable = "Por el momento no tenemos el modelo " + mode
    return str(variable)

def mensaTelegram(mode):
    varia =  "chat/" + mode
    try:
        ref = db.reference(varia)
        lista = ref.get()
        nombr = lista['nombre']
        precio = lista['precio']
        url = lista['url']
        sitio = "laps"
    except:
        nombr = "Por el momento no tenemos el modelo " + mode
        precio = "$0.0"
        url = "https://st2.cannypic.com/thumbs/14/141051_632_canny_pic.jpg"
        sitio = "store"
    return nombr,precio,url,sitio
