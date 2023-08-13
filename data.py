# gunakan modul json
import json
from flask import Flask

# buka file JSON
file_json = open("data.json")

# prsing data JSON
data = json.loads(file_json.read())

# cetak isi data JSON
# print(data)

app = Flask(__name__)
@app.route('/')
def index():
    # return json.dumps({'name': 'alice',
    #                    'email': 'alice@outlook.com'})
    return json.dumps(data)
app.run()
