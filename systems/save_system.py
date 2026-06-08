import json
import os

DEFAULT = {
    "cash": 5000,
    "rep": 0,
    "fuel": 100,
    "cars": ["Civic EG"],
    "current_car": "Civic EG"
}

def load_save(path="saves/profile.json"):
    if not os.path.exists(path):
        return DEFAULT.copy()

    with open(path, "r") as f:
        return json.load(f)

def save_game(data, path="saves/profile.json"):
    os.makedirs("saves", exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
