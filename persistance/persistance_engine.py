import pyrebase
import json
from datetime import datetime
from grandeurs.models import Grandeur ,Mesure
import firebase_admin
from firebase_admin import credentials , firestore

cred= credentials.Certificate(r"C:/Users/hp/firestore_base.json")
firebase_admin.initialize_app(cred)
firebase_config = {
  "apiKey": "AIzaSyDjAEugf6aIbZj32hOcsWgDzRyQ64MGhAs",
  "authDomain": "firestoregestiongrandeurs.firebaseapp.com",
  "databaseURL": "https://firestoregestiongrandeurs-default-rtdb.firebaseio.com",
  "projectId": "firestoregestiongrandeurs",
  "storageBucket": "firestoregestiongrandeurs.firebasestorage.app",
  "messagingSenderId": "122443096800",
  "appId": "1:122443096800:web:050f44e83123539f6ce685",
  "measurementId": "G-QQKY1MP9MH"
}
firebase=pyrebase.initialize_app(firebase_config)
database=firebase.database()

def persist_data(message):
    json_object = json.loads(message)
    json_object['time']= str(datetime.now())
    database.child('temperature').push(json_object)
    doc_ref = db_firestore.collection("temperature").document()
    doc_ref.set(json_object)