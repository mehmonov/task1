import json
import threading
import time
import requests
from flask import Flask, request

API_URL = "https://test.icorp.uz/interview.php"
PORT = 5001
NGROK_URL = "https://282b846409b0.ngrok-free.app"

app = Flask(__name__)

part2_storage = {"value": None}

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        data = request.get_json(force=True, silent=True) # https://tedboy.github.io/flask/generated/generated/flask.Request.get_json.html
        
        code_part = list(data.values())[0] if isinstance(data, dict) and data else str(data)
        
        part2_storage["value"] = code_part # type: ignore

        return "OK"
    
    return "Webhook oke"

def main():
    threading.Thread(
        target=lambda: app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False),
        daemon=True
    ).start()
    time.sleep(1)
    
    payload = {"msg": "finally...", "url": NGROK_URL}
    
    res = requests.post(API_URL, json=payload)

    data = json.loads(res.text)

    part1 = data.get("part1")

    print(f"Part 1: {part1}")
    
    while part2_storage["value"] is None:
        time.sleep(0.1) 
    
    part2 = part2_storage["value"]

    print(f"Part 2: {part2}")
    
    combined_code = f"{part1}{part2}" #merged

    print(f"\n combined: {combined_code}")
    
    final_response = requests.get(API_URL, params={"code": combined_code})
    
    print(f"\nfinal message: {final_response.text.strip()}")

if __name__ == "__main__":
    main()