from flask import Flask, request
import requests
from config import URL

app = Flask(__name__)

data = requests.post(url=URL, data={
    'msg': "message",
    "url": "https://89a3c872fe9f.ngrok-free.app"
})

print(data.json)

@app.route("/", methods=['GET', 'POST'])
def get_data():
    query = request.args
    print(query)
    return f'results for: {query}'
