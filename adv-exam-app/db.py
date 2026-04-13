import json
import os

DATA_FILE = "/tmp/data.json"

def initialize():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def get_data():
    initialize()
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def add_data(entry):
    initialize()
    data = get_data()
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)