import pyrebase
import os
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials


cred = credentials.Certificate('service_account.json')
firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "AIzaSyDe4-6nyG5Gt3rtW3etfCLjNP_VuaqUobs",
    "authDomain": "automatic-vent-359215.firebaseapp.com",
    "databaseURL": "https://automatic-vent-359215-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "automatic-vent-359215",
    "storageBucket": "automatic-vent-359215.appspot.com",
    "messagingSenderId": "620885103259",
    "appId": "1:620885103259:web:b0ffab2e251758d566ac3e",
    "measurementId": "G-ZHT26YVS4F",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

email = 'email@example.com'
password = '123456'
name = 'Test firebase'

firebase_auth.create_user(
    email=email,
    password=password,
    display_name=name
)
