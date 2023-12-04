import firebase_admin
import pyrebase
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
import pickle
import os

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


def create_user(name, email, password):
    try:
        user = firebase_auth.create_user(
            email=email,
            password=password,
            display_name=name,
        )
        return user.uid
    except Exception as e:
        return None


def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user['idToken']
    except Exception as e:
        return None


def store_token(token):
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
    with open('token.pickle', 'wb') as f:
        pickle.dump(token, f)


def revoke_token(token):
    firebase_auth.revoke_refresh_tokens(token)
    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
