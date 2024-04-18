import eikon as ek
from credentials import apikeys

def connect():
    apikey = apikeys.eikon
    ek.set_app_key(apikey)