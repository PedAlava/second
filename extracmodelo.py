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
