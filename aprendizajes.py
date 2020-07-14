import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('asistente-123-firebase-adminsdk-vcael-d2ae64e842.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://asistente-123.firebaseio.com/'
})
def obtener():
    ref = db.reference('conversations')
    lista = ref.get()
    llaves =[]
    for c in lista:
        llaves.append(c)
    v = len(llaves)
    if v > 1:
        ult =llaves[-2:]
        respuesta1 = ult[1]
        respuesta2 = ult[0]
        aprendizaje =[]
        

        for x in lista[respuesta1]['conver']:
            print()
            if lista[respuesta1]['conver'][x] == "nose la respuesta enseñame por favor":

                aprendizaje.append(lista[respuesta2]['conver'][x])
                aprendizaje.append(v)
                #print(lista[respuesta2][x])
            #else:
                #print("pasa")
        for x in lista[respuesta2]['conver']:
            if lista[respuesta2]['conver'][x] == "nose la respuesta enseñame por favor":
                aprendizaje.append("no")
                aprendizaje.append(v)
                #print("no pasa nada")
                #print(lista[respuesta2][x])
        val = len(aprendizaje)
        if val == 0:
            aprendizaje.append("no")
            aprendizaje.append(v)
        return aprendizaje
    else:
        #ref = db.reference('conversations')
        #snapshot = ref.order_by_child('id').get()
        no = ['no',1] 
            
        return no

def guardar(id,message,categoria,tipo):
    ref = db.reference('conversations')
    ref.push({
            'conver': {
                        'id': id,
                        'mesagge': message,
                        'categoria':categoria,
                        'tipo': tipo
                    }
    })




    
