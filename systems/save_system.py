
import json, os

DEFAULT={
'cash':5000,
'rep':0,
'cars':['Civic EG']
}

def load_save(path='saves/profile.json'):
    if not os.path.exists(path):
        return DEFAULT.copy()
    with open(path) as f:
        return json.load(f)
